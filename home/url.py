from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from home.views import *

urlpatterns = [
    path('',home,name='home'),
    path('faq/',FAQView.as_view(),name='faq'), 
    path('privacy_policy/',PrivacyPolicyView.as_view(),name='privacy-policy'),
    path('terms_condition/',TermsConditionView.as_view(),name='terms-codition'),
] 
