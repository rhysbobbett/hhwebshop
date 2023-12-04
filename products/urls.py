from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.all_products, name='all_products'),
    # URL pattern for products filtered by category and subcategory
    path('products/<str:category>/', views.all_products, name='category_products'),
    path('products/<str:category>/<str:sub_category>/', views.all_products, name='subcategory_products'),
    path('products/<str:special_offer>/', views.all_products, name='special_offer_products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'), # noqa 
]