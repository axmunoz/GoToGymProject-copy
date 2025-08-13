from django.urls import path
from . import views
from . import views_checkout

app_name = 'carrito'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:product_id>/', views.update_cart, name='update_cart'),
    path('checkout/', views_checkout.checkout, name='checkout'),
    path('payment-status/', views_checkout.payment_status, name='payment_status'),
    
    path('remove-coupon/', views.remove_coupon, name='remove_coupon'),  # This line remains unchanged
    path('apply-coupon/', views.apply_coupon, name='apply_coupon'),  # New line added
    path('resumen/<int:historial_id>/', views.resumen_compra, name='resumen_compra'),
    path('historial/', views.historial_compras, name='historial_compras'),
]
