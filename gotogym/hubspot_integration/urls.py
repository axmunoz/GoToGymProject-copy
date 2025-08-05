from django.urls import path
from .views import crm_hubspot_view, list_hubspot_contacts

urlpatterns = [
    path('crm/', crm_hubspot_view, name='crm_hubspot'),
    path('contactos/', list_hubspot_contacts, name='list_contacts'),
]
