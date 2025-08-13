
from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from hubspot_integration.hubspot_utils import get_all_hubspot_contacts, create_hubspot_contact

def list_hubspot_contacts(request):
    contacts = get_all_hubspot_contacts()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(contacts, 10)  # 10 contactos por página
    page_obj = paginator.get_page(page_number)
    return render(request, 'hubspot_integration/list_contacts.html', {'contacts': page_obj.object_list, 'page_obj': page_obj})

def crm_hubspot_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        try:
            response = create_hubspot_contact(email, firstname, lastname)
            messages.success(request, 'Contacto creado en HubSpot correctamente.')
        except Exception as e:
            messages.error(request, f'Error al crear contacto: {e}')
    return render(request, 'hubspot_integration/crm_hubspot.html')

