from django.urls import path
from . import views

app_name = 'contabilidad'

urlpatterns = [
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/nuevo/', views.nuevo_cliente, name='nuevo_cliente'),
    path('clientes/<int:cliente_id>/', views.ver_cliente, name='ver_cliente'),
    path('clientes/<int:cliente_id>/editar/', views.editar_cliente, name='editar_cliente'),
    path('clientes/<int:cliente_id>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),
    path('clientes/<int:cliente_id>/facturas/', views.facturas_cliente, name='facturas_cliente'),
]
