from django.core.paginator import Paginator
from django.core.mail import message
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import render
from product.filters import *
from product.models import *
from order.models import *
from home.models import *
from product.forms import *
from utils import *


def product_list(request,slug):



    grand_parent_object = GrandCategory.objects.filter(slug=slug)
    categories = ParentCategory.objects.filter(
        grand_category=grand_parent_object[0]
        )
    boxes = Box.objects.all()
    products = Product.objects.filter(grand_category=grand_parent_object[0])

    context = {}

    page = request.GET.get('page', 1)
    paginator = Paginator(products, 12)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)


    context['parent_categories'] = categories
    context['objects'] = products
    context['boxes'] = boxes
    context['grand_category'] = grand_parent_object[0]

    return render(request,'product_list.html',context)

def product_detail(request,slug,g_c):
    product = Product.objects.get(slug=slug)
    product_sliders = ProductSliderImage.objects.filter(product=product)
    context = {}
    try:
        order_item_flag = CartItem.objects.filter(product=product,user=request.user).exists()
    except:
        order_item_flag = False
    if order_item_flag:
        order_item = CartItem.objects.get(product=product,user=request.user)
    else:
        order_item = ''

    attributes = product.get_attributes
    slider_image = ProductSliderImage.objects.filter(product=product).values('sub_attribute')
    slider_image_id_list = list(set([i['sub_attribute'] for i in slider_image]))
    sub_attributes = SAttribute.objects.filter(id__in=slider_image_id_list)


    attr_links = {}
    for att in attributes:
        single_attibute = Attribute.objects.filter(id=att.id).values('sattribute')
        single_attribute_list =[ SAttribute.objects.get(id=j) for j in list(set([i['sattribute'] for i in single_attibute] )) if SAttribute.objects.get(id=j) in sub_attributes]
        single_attribute_list_id = [i.id for i in single_attribute_list ]
        attr_links[att] = SAttribute.objects.filter(id__in=single_attribute_list_id)


    context['product'] = product
    context['attr_links'] = attr_links
    context['order_item'] = order_item
    context['product_sliders'] = product_sliders
    context['order_item_flag'] = order_item_flag
    context['sub_attributes'] = sub_attributes

    return render(request,'product_detail.html',context)

def addAttributeToCart(request,product_id,attribute_id,super_attr):
    print("addAttributeToCart ............................")
    count = CartItem.objects.filter(user=request.user,product__id =product_id).count()
    if count > 0:

        sattr_obj  = SAttribute.objects.get(id=attribute_id)
        cart_obj  = CartItem.objects.filter(user=request.user,product__id =product_id).first()

        #first deleting all attributes of a specifc Super-Attribute to make sure only 1 child attr exist

        if sattr_obj in cart_obj.sub_attributes.all():
            cart_obj.sub_attributes.remove(sattr_obj)
            cart_obj.save()
            print("print saved 1st")

        #now adding the attribute
        cart_obj.sub_attributes.add(sattr_obj)
        cart_obj.save()
        print("print saved 1st")
        return JsonResponse(
            {'status':'200',
            'message':'Attribute Saved Successfully!'
            })

def getAttributesFromCategory(request):
    id = request.GET.get('id')
    objects = GrandCategory.objects.filter(id=id)
    attributes = Attribute.objects.filter(grand_category=objects[0]).values()
    data = {}
    counter = 0
    for i in attributes:
        data[counter] = i
        counter += 1
    print(data)
    return JsonResponse(data)


def productAdminCreate(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.errors)
    context = {}
    g_c = GrandCategory.objects.all()
    context['form'] = ProductForm()
    context['g_c'] = g_c

    return render(request,'product_admin.html',context)

def productAdminUpdate(request,id):

    g_c = GrandCategory.objects.all()
    product = Product.objects.get(id=id)
    sliders = ProductSliderImage.objects.filter(product=product)



    context = {}
    context['g_c'] = g_c
    context['slider_images'] = sliders
    context['sa_attributes'] = SAttribute.objects.all()
    context['product'] = product


    users = [{
      'id': 0,
      'name': "Select"
    }, ];

    counter = 1
    for gc in g_c:

        for attr in gc.get_attributes :
            for sub_attr in  context['sa_attributes']:
                if  sub_attr.product.id == product.id and sub_attr.attribute == attr:
                    counter += 1
                    users.append(
                        {
                            "id":counter,
                            "name":sub_attr.name
                         }
                        )
    context['users'] = users

    return render(request,'product_admin_update.html',context)

def productUsersGET(request,id):
    g_c = GrandCategory.objects.all()
    product = Product.objects.get(id=id)

    context = {}
    context['sa_attributes'] = SAttribute.objects.all()
    context['product'] = product
    users = [{
      'id': 0,
      'name': "Select"
    }, ];

    counter = 1
    for gc in g_c:

        for attr in gc.get_attributes :
            for sub_attr in  context['sa_attributes']:
                if  sub_attr.product.id == product.id and sub_attr.attribute == attr:
                    counter += 1
                    users.append(
                        {
                            "id":sub_attr.id,
                            "name":sub_attr.name
                         }
                        )
    context['users'] = users
    return JsonResponse({'data':context['users']})

###################################################################
#                       Sub Product CRUD                         #
###################################################################

def createProduct(request):
    if request.method == 'POST':

        print(request)
        print(request.POST)
        print('file',request.FILES)
        form = ProductForm(request.POST,request.FILES)
        grand_category = GrandCategory.objects.get(name=request.POST.get('grand_category'))

        if  Product.objects.filter(
                title=request.POST.get('title'),
                code=request.POST.get('code'),
                sub_title=request.POST.get('sub_title'),
                price=request.POST.get('price'),
                sold_times=request.POST.get('sold_times'),
                grand_category=grand_category.id,
            ).exists():
          return JsonResponse({'status':'200','message':'Product Already Exist'})

        if form.is_valid():
            obj = form.save(commit=False)
            obj.grand_category = grand_category
            obj.save()

            return JsonResponse({
                'status':'200',
                'message':'Product Created',
                'attributes': list(obj.grand_category.get_attributes.values('id','name')),
                'id':obj.id
                })
        return JsonResponse({'status':'200','message':'form not valid'})

def updateProduct(request,id):
    if request.method == 'POST':

        product =  Product.objects.get(id=id)
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            obj = form.save()
            obj.save()
            return JsonResponse({'status':'200','message':'Product Update','id':obj.id})
        return JsonResponse({'status':'200','message':'form not valid'})


###################################################################
#                       Sub Attribute CRUD                        #
###################################################################

def getSAttribute(request):
    product_id = request.POST.get('product_id')
    attribute_id = request.POST.get('attribute_id')
    objects = SAttribute.objects.filter(attribute_id=attribute_id,product_id=product_id).values('id','name','attribute')
    return JsonResponse(status=200,data={'objects':list(objects)})

def createSubAttribute(request):
    product_id = request.POST.get('product_id')
    attribute_id = request.POST.get('attribute')
    name = request.POST.get('name')
    print('------------------')
    print(product_id)

    if not product_id and not attribute_id:
        return JsonResponse({'status':'200','message':'product_id or attribute_id not found'})
    product = Product.objects.get(id=product_id)
    attribute = Attribute.objects.get(id=attribute_id)
    if not SAttribute.objects.filter(
        product=product,
        attribute=attribute,
        name = name
        ).exists():

        obj = SAttribute.objects.create(
            product=product,
            attribute=attribute,
            name = name
        )
        obj.save()
        return JsonResponse({'status':'200','message':'Sub Attribute Created','id':obj.id,'name':obj.name})
    else:
        return JsonResponse(status=400,data={'message':'Sub Attribute Already Created'})

def updateSubAttribute(request):
    id = request.POST.get('id')
    name = request.POST.get('name')

    print(id,name)
    if not name and not id:
        return JsonResponse({'status':'200','message':'name or id not found'})
    SAttribute.objects.filter(id=id).update(
        name = name
    )
    obj = SAttribute.objects.get(id=id)
    print(obj.id,obj.name)
    return JsonResponse({'status':'200','message':'Sub Attribute Updated','id':obj.id,'name':obj.name})

def deleteSubAttribute(request):
    id = request.POST.get('id')
    print('------------------------------------------')
    print(id)
    if not id:
        return JsonResponse({'status':'200','message':'id not found'})
    SAttribute.objects.filter(id=id).delete()
    return JsonResponse({'status':'200','message':'Sub Attribute Deleted'})

def deleteAllSubAttributeByProductID(request):
    product_id = request.POST.get('product_id')
    product = Product.objects.get(id=product_id)
    delete_count = SAttribute.objects.filter(product=product).delete()
    return JsonResponse({'status':'200','message':'Sub Attribute Deleted','counts':delete_count})


###################################################################
#                       Slider Image CRUD                         #
###################################################################

def createProductSliderImage(request):
    if request.method == 'POST':
        form = ProductSliderImageForm(request.POST,request.FILES)
        print(form.errors)
        print(request.POST)

        sub_attribute = SAttribute.objects.get(id=request.POST['sub_attribute'])
        attribute = Attribute.objects.get(id=request.POST['atttibute'])
        product = Product.objects.get(id=request.POST['product'])

        print(sub_attribute,attribute,product)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.product  = product
            obj.sub_attribute = sub_attribute
            if SAttribute.objects.filter(id=request.POST['related_sub_attribute']).exists():
                obj.related_sub_attribute =SAttribute.objects.get(id=request.POST['related_sub_attribute'])
            obj.save()
            obj.attribute = attribute
            obj.save()
            print("SAveddddd",obj.id)
            data= {
                'id': obj.id
            }

            return JsonResponse(data)
        else:
            return JsonResponse({'status':'200','message':'Slider Image values missing'})

def updateProductSliderImage(request,id):
    if request.method == 'POST':
        if not id:
            return JsonResponse({'status':'200','message':'ID not Found!'})

        form = ProductSliderImageForm(request.POST)
        print(form.errors)

        if form.is_valid():
            form.save()
            return JsonResponse({'status':'200','message':'Slider Image created succesfully'})
        else:
            return JsonResponse({'status':'200','message':'Slider Image values missing'})

def getProductSliderSubAndRelatedAttr(request):
    product_id = request.GET.get('product_id')
    attribute_id = request.GET.get('attribute_id')
    sub_attributes = SAttribute.objects.filter(
        Q(product = Product.objects.get(id=product_id)),
        attribute = Attribute.objects.get(id=attribute_id)
    ).values('id','name')
    related_attributes = SAttribute.objects.filter(
        Q(product = Product.objects.get(id=product_id)),
        ~Q(attribute = Attribute.objects.get(id=attribute_id))
    ).values('id','name')
    return JsonResponse({'status':'200','sub_attributes':list(sub_attributes),'related_attributes':list(related_attributes)})

def getAttibutesFromProduct(request):
    product_id = request.GET.get('id')
    attributes = Product.objects.get(id=product_id).grand_category.get_attributes.values('id','name')
    return JsonResponse({'status':'200','attributes':list(attributes)})



def DeleteProductSlider(request):
    id = request.GET.get('id', None)
    print(request.GET)
    delete_count = ProductSliderImage.objects.get(id=id).delete()
    print("Deleted Successfully", id)
    data = {
        'deleted': True
    }
    return JsonResponse(data)