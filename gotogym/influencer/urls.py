from django.urls import path
from . import views

urlpatterns = [
    path('suscribete/', views.suscribete, name='influencer_suscribete'),
    path('dashboard/', views.dashboard, name='influencer_dashboard'),
   
    path('solicitar-retiro/', views.solicitar_retiro, name='influencer_solicitar_retiro'),
    path('quitar-suscripcion/', views.quitar_suscripcion, name='influencer_quitar_suscripcion'),
    path('admin/list/', views.influencer_admin_list, name='influencer_admin_list'),
    path('admin/<int:pk>/delete/', views.influencer_admin_delete, name='influencer_admin_delete'),
    path('admin/<int:pk>/edit/', views.influencer_admin_edit, name='influencer_admin_edit'),
]
