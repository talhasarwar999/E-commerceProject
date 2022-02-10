from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.url')),
    path('',include('accounts.url')),
    path('',include('blog.url')),
    path('',include('product.url')),
    path('',include('order.url')),
    path('',include('contact.url')),
    path('',include('shop.url')),
    url(r'^chaining/', include('smart_selects.urls')),

]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

