from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.product_details, name='product-details'), 
    path('add-product/', views.add_product, name='add-product'), 
    path('update-product/', views.update_product, name='update-product'), 
    path('checkout/<int:pk>/', views.check_out, name='checkout'), 
    path('order-history/', views.order_history, name='order-history')
]