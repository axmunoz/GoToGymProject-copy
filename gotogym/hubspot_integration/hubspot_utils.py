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
