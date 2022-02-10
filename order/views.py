from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import JsonResponse
from django.shortcuts import redirect, render
from order.models import *
from product.models import *
from order.forms import *
from .utils import *
from utils import *
import json
import datetime


def validateCopoun(request, copoun):
    # check if that user has already applied for token

    try:
        CouponCode.objects.get(code=copoun)
        print('1')
    except:
        print('2')
        return JsonResponse({'message': 'Item added to cart successfully not'}, status=400)
        return redirect('cart-list')


def validateOrder(request):
    try:
        return Order.objects.get(user=request.user, ordered=False)
    except:
        messages.info(request, 'Order Not Found')
        return redirect('cart-list')


@login_required
def addToCart(request):
    print("Talha ADDTO CARTTTTTTT")
    product_id = request.GET.get('product_id')
    count = CartItem.objects.filter(user=request.user).count()
    product = Product.objects.get(id=product_id)
    user = request.user
    order_obj = Order.objects.filter(user=request.user, ordered=False)
    sub_array = []
    sub_values = request.GET.get('values_array')
    print("All Sub attributes here",sub_values)
    try:
        if sub_values != '':
            sub_array = sub_values.split('-')
            print(sub_values,sub_array,"----------------------")
    except:
        pass

    if not CartItem.objects.filter(user=user, product=product).exists():

        try:
            quantity = request.GET.get('quantity')

            cart = CartItem.objects.create(
                user=user,
                product=product,
                quantity=quantity
            )
            if len(sub_array) > 0:
                for i in sub_array:
                    if i != '':
                        sub = SAttribute.objects.get(id=int(i))
                        cart.sub_attributes.add(sub)
                        cart.save()
            cart.save()
            print('quantity found')

        except:
            print('no quanity found')
            cart = CartItem.objects.create(
                user=user,
                product=product,
            )
            if len(sub_array) > 0:
                for i in sub_array:
                    if i != '':
                        sub = SAttribute.objects.get(id=int(i))
                        cart.sub_attributes.add(sub)
                        cart.save()
            cart.save()

        order_obj = Order.objects.filter(user=request.user, ordered=False)
        print(order_obj)
        if not order_obj.exists():
            print('here in exist')
            order = Order.objects.create(user=request.user, ordered=False)
            order.items.add(cart)
            order.save()

        else:
            for ord in Order.objects.filter(user=request.user, ordered=False):
                ord.items.add(cart)
                ord.save()
        count = CartItem.objects.filter(user=request.user).count()
        return JsonResponse(
            {'status': '200', 'message': 'Item added to cart successfully', 'cartItemCount': count}
        )

    else:
        return JsonResponse({'status': '200', 'message': 'Item is already added','cartItemCount': count})


@login_required
def changeQuantity(request):
    product_id = request.GET.get('product_id')
    quantity = request.GET.get('quantity')
    product = Product.objects.get(id=product_id)
    user = request.user
    obj = CartItem.objects.get(
        user=user,
        product=product)

    obj.quantity = quantity
    obj.save()

    order = Order.objects.get(user=request.user, ordered=False)
    cart_list = CartItem.objects.filter(user=request.user)
    product_sum = sum([i.get_price for i in cart_list])
    tax = float("{0:.2f}".format(float(product_sum) * 0.05))
    shipment = float(20)

    total = product_sum + tax + shipment

    return JsonResponse(
        {'status': '200',
         'quantity': obj.quantity,
         'price': obj.get_price,
         'total': order.total_price_w_tax,
         'product_sum': order.total_price_wo_tax,
         'coupon_discount': order.coupon_discount,
         'tax': order.tax,
         'message': 'Quantity updated successfully'
         })


@login_required
def removeToCart(request):
    product_id = request.GET.get('product_id')
    product = Product.objects.get(id=product_id)
    user = request.user

    obj = CartItem.objects.get(
        user=user,
        product=product)

    order_obj = Order.objects.filter(user=request.user, ordered=False)

    for ord in order_obj:
        ord.items.remove(obj)
        ord.save()

        if ord.items.all().count() < 1:
            ord.coupon_code = None
            ord.shipping = False
            ord.save()

    obj.delete()
    cart_list = CartItem.objects.filter(user=request.user)

    product_sum = sum([i.get_price for i in cart_list])
    tax = float("{0:.2f}".format(float(product_sum) * 0.05))
    shipment = float(20)
    total = product_sum + tax + shipment

    count = CartItem.objects.filter(user=request.user).count()

    print(count)
    return JsonResponse(
        {'status': '200',
         'quantity': obj.quantity,
         'price': obj.get_price,
         'total': total,
         'product_sum': product_sum,
         'tax': tax,
         'message': 'Item removed successully',
         'cartItemCount': count
         })


def cart_list(request):
    context = {}

    try:
        cart_list = CartItem.objects.filter(user=request.user)
        order = Order.objects.get_or_create(user=request.user, ordered=False)
    except:
        if not request.user.is_authenticated:
            order = ''
            cart_list = []
            objects = {}
            order_object = {}

            # i = product_id, k = quantity
            print(request.COOKIES)
            for i, k in request.COOKIES.items():
                if i != "csrftoken":
                    order = Order.objects.get(ordered=False)
                    context['is_guest'] = True
                    product = Product.objects.get(slug=i).__dict__
                    product_obj = Product.objects.get(slug=i)
                    objects[product['id']] = product
                    objects[product['id']]['quantity'] = k
                    objects[product['id']]['get_price'] = float(k) * float(product['price'])
                    objects[product['id']][
                        'thumbnail_url'] = product_obj.thumbnail.url if product_obj.thumbnail else None
                    context['objects'] = objects

            order_object['tax'] = tax(objects)
            order_object['total_price_w_tax'] = total_price_w_tax(objects)
            order_object['total_price_wo_tax'] = total_price_wo_tax(objects)

            context['order'] = order_object
            context['order_flag'] = True
            return render(request, 'cart_list.html', context)

    context['objects'] = cart_list
    context['order'] = order[0]
    return render(request, 'cart_list.html', context)


def orderView(request):
    if request.method == 'POST':
        shipping_form = ShippingAddressForm(request.POST, prefix='shipping_form')
        billing_form = BillingAddressForm(request.POST, prefix='billing_form')
        order = Order.objects.get(user=request.user, ordered=False)
        email = request.POST.get('payment_form-email')
        delivery_method = request.POST.get('payment_form-delivery_methods')
        Order.objects.filter(id=order.id).update(email=email, delivery_methods=delivery_method)

        if shipping_form.is_valid():
            shipping_obj = shipping_form.save()
            shipping_obj.order = order
            shipping_obj.save()
        if billing_form.is_valid():
            billing_obj = billing_form.save()
            billing_obj.order = order
            billing_obj.save()
            return redirect('thank-you')

    shipping_form = ShippingAddressForm(prefix="shipping_form")
    billing_form = BillingAddressForm(prefix="billing_form")
    context = {}
    context['billing_form'] = billing_form
    context['shipping_form'] = shipping_form

    cart_list = CartItem.objects.filter(user=request.user)

    context['objects'] = cart_list
    context['order'] = Order.objects.get(user=request.user, ordered=False)

    return render(request, 'payment.html', context)


def applyCoupon(request):
    copoun = request.GET.get('coupon')
    print("Our Coupon", copoun)
    # validating order and coupon
    validateOrder(request)
    validateCopoun(request, copoun)

    try:
        copoun_obj = CouponCode.objects.get(code=copoun)
        print("Applicable")
    except:
        return JsonResponse(
            {'message': 'Coupon is not Applicable'}, status=400
        )
        print("Not Applicable")
        return redirect('cart-list')
    copoun_obj = CouponCode.objects.get(code=copoun)
    order = Order.objects.get(user=request.user, ordered=False)
    order.coupon_code = copoun_obj
    order.save()
    return JsonResponse({'message': 'Coupon is applicable'}, status=200)
    return redirect('cart-list')


@check_order_confirmation
def thankYou(request):
    context = {}
    order = Order.objects.all()[0]
    product_sum = sum([i.get_price for i in order.items.all()])
    tax = float("{0:.2f}".format(float(product_sum) * 0.05))
    shipment = float(20)

    total = product_sum + tax + shipment
    context['order'] = order.items.all()
    context['total'] = total
    context['now'] = datetime.datetime.now()

    return render(request, 'order_confirm.html', context)




