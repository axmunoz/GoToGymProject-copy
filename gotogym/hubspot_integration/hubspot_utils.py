# Obtener todos los contactos de HubSpot
def get_all_hubspot_contacts():
    contacts = []
    try:
        api_response = client.crm.contacts.basic_api.get_page(limit=100)
        for obj in api_response.results:
            properties = obj.properties
            contacts.append({
                'email': properties.get('email', ''),
                'firstname': properties.get('firstname', ''),
                'lastname': properties.get('lastname', ''),
            })
    except Exception as e:
        pass
    return contacts
import hubspot
from hubspot.crm.contacts import BasicApi, SimplePublicObjectInput
from django.conf import settings

# cliente de HubSpot usando el access token de settings.py
client = hubspot.Client.create(access_token=settings.HUBSPOT_ACCESS_TOKEN)

#  crear un contacto en HubSpot
def create_hubspot_contact(email, firstname=None, lastname=None):
    properties = {
        "email": email,
        "firstname": firstname or "",
        "lastname": lastname or ""
    }
    simple_public_object_input = SimplePublicObjectInput(properties=properties)
    api_response = client.crm.contacts.basic_api.create(simple_public_object_input_for_create=simple_public_object_input)
    return api_response
