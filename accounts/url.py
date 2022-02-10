from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from accounts.views import *

urlpatterns = [
    path('login/',LoginView,name='login'),
    path('register/',register,name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('logout/',logoutView,name='logout')
] 
