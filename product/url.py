
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from product.views import *

urlpatterns = [

    path('products/<slug:slug>/',product_list,name='product-list'), 
    path('proudcts/<slug:g_c>/<slug:slug>/',product_detail,name='product-detail'), 
    path('createProduct/',createProduct,name='product-create'), 
    path('updateProduct/<id>/',updateProduct,name='product-update'), 
    
    path('addAttributeToCart/<product_id>/<attribute_id>/<super_attr>/',addAttributeToCart,name='add-attribute'), 
    path('getAttributesFromCategory/',getAttributesFromCategory,name='get-att-from-cate'),


    #admin page for products #
    path('product/admin/',productAdminCreate,name='product-admin-create'),
    path('product/admin/<id>/',productAdminUpdate,name='product-admin-update'),
    path('createSAttribute/',createSubAttribute,name='create-sa-attribute'),
    path('deleteAllSubAttribute/',deleteAllSubAttributeByProductID,name='delete-all-sa-attribute'),
    path('updateSAttribute/',updateSubAttribute,name='update-sa-attribute'),
    path('deleteSAAttribute/',deleteSubAttribute,name='delete-sa-attribute'),
    path('getSAttribute/',getSAttribute,name='get-sa-attribute'),
    path('productUsersGET/<id>/',productUsersGET,name='product-users-get'),
    path('product-users-get-slider/',DeleteProductSlider,name='product-users-get-slider'),

    #admin page for slider images 
    path('getProductSliderSubAndRelatedAttr/',getProductSliderSubAndRelatedAttr,name='get-slider-attr-related-attribute'),
    path('createProductSliderImage/',createProductSliderImage,name='create-slider-image'),
    path('getAttibutesFromProduct/',getAttibutesFromProduct,name='get-attribute-product'),
    
    
]      
