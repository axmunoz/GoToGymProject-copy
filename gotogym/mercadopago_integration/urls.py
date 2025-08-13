from django.urls import path
from . import views

urlpatterns = [
	path('crear-preferencia/', views.crear_preferencia, name='crear_preferencia'),
	path('webhook/', views.webhook_pago, name='webhook_pago'),
	path('checkout/', views.mercadopago_checkout, name='mercadopago_checkout'),
]
