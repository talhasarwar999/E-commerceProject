from django.contrib.auth import authenticate, login, logout

from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.forms import ValidationError
from django.http import JsonResponse
from django.contrib import messages
from accounts.forms import *
from utils import *

User = get_user_model()



def LoginView(request):
    logout(request)
    form = LoginForm(request.POST)

    if (request.method == 'POST'):
        email = request.POST.get('email')  
        password = request.POST.get('password') 
        user = authenticate(request, email=email, password=password)
        if User.objects.filter(email=email).count() < 1:
            return JsonResponse({'status':'400','message':'No User Found with the Credentials','field':'email'},status=400)
          
        if user is not None:
            login(request, user)
            return JsonResponse({'status':'200','message':'Login Successfull','field':'login'},status=200)

        else:
            form.add_error("email",error= ValidationError("Password Missmatch!"))
            return JsonResponse({'status':'400','message':'Password Missmatch!','field':'password'},status=400)



def register(request):

    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        username  = request.POST.get('username')
        email     = request.POST.get('email')
        password  = request.POST.get('password1')
        check     = User.objects.filter(username=username).exists()

        form = RegisterForm(request.POST)
        if form.is_valid():
            if not check:
                user = User.objects.create(fullname=fullname,
                    username=username,
                    email=email)
                user.set_password(password)
                user.is_superuser = False
                user.is_staff = False
                user.save()
                data = {'message': "Account for '{}' Created Successfully.".format(username)}            
                return JsonResponse(data)
            else:
                data = {'message': "Account already exist with '{}' username.".format(username)}            
                return JsonResponse(data)
        else:
            return JsonResponse(form.errors,status=400)
def logoutView(request):
    """
        This function will handle user logout from kompetez
        website. User will not be able to use main of kompetez 
        functionality.
    """
    logout(request)
    return redirect('home')