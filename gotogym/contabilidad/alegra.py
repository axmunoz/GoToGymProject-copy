import os
import base64
import requests

class AlegraAPI:
    def get_bills(self):
        """Obtiene las facturas de proveedor (egresos) desde Alegra."""
        return self.get('bills')
    BASE_URL = 'https://api.alegra.com/api/v1/'

    def __init__(self, email=None, api_token=None):
        # Permitir pasar email y token o usar variables de entorno
        self.email = email or os.environ.get('ALEGRA_EMAIL')
        self.api_token = api_token or os.environ.get('ALEGRA_API_TOKEN')
        if not self.email or not self.api_token:
            raise ValueError('Debes configurar ALEGRA_EMAIL y ALEGRA_API_TOKEN en variables de entorno o pasarlos al inicializar AlegraAPI.')
        # Alegra usa Basic Auth: base64(email:token)
        credentials = f'{self.email}:{self.api_token}'.encode('utf-8')
        b64_credentials = base64.b64encode(credentials).decode('utf-8')
        self.headers = {
            'Authorization': f'Basic {b64_credentials}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

    def get(self, endpoint, params=None):
        url = self.BASE_URL + endpoint
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    # clientes
    def get_clients(self):
        return self.get('contacts')
    
    def create_client(self, data):
        """
        Crea un cliente en Alegra.
        data: dict con los datos del cliente (name, email, phonePrimary, etc)
        """
        url = self.BASE_URL + 'contacts'
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    #  facturas
    def get_invoices(self):
        return self.get('invoices')


