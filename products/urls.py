from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.all_products, name='all_products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/<str:category>/', views.all_products, name='category_products'),  # noqa
    path('products/<str:category>/<str:sub_category>/', views.all_products, name='subcategory_products'),  # noqa
    path('special_offers/', views.all_products, name='specials'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),  # noqa
]
