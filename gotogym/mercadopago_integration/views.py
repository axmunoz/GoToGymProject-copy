import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import mercadopago

@csrf_exempt
def crear_preferencia(request):
    if request.method == 'POST':
        access_token = getattr(settings, 'MP_ACCESS_TOKEN', None)
        if not access_token:
            return HttpResponseBadRequest('Access token not configured')
        sdk = mercadopago.SDK(access_token)
        title = request.POST.get('title', 'Pago carrito')
        quantity = int(request.POST.get('quantity', 1))
        unit_price_str = request.POST.get('unit_price', '0')
        unit_price = float(unit_price_str.replace(',', '.'))
        # Construir back_urls para redirigir después del pago
        # MercadoPago requiere que back_urls.success sea una URL pública (no localhost)
        # Puedes usar temporalmente ngrok o una URL de prueba pública
        # Ejemplo: "https://tusitio.com/carrito/?collection_status=approved"
        # Para pruebas locales, MercadoPago puede rechazar localhost
        public_base_url = "https://d4ed65101df0.ngrok-free.app/es/carrito/"  # Cambia esto por tu dominio real en producción
        back_urls = {
            "success": public_base_url + "/carrito/?collection_status=approved",
            "pending": public_base_url + "/carrito/?collection_status=pending",
            "failure": public_base_url + "/carrito/?collection_status=rejected",
        }
        preference_data = {
            "items": [
                {
                    "title": title,
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "currency_id": "COP"
                }
            ],
            "auto_return": "approved",
            "back_urls": back_urls,
            "payment_methods": {
                "excluded_payment_types": [],
                "installments": 1
            }
        }
        # Solo agregar 'payer' si el email no está vacío
        payer_email = request.POST.get('payer_email', '').strip()
        if payer_email:
            preference_data["payer"] = {"email": payer_email}
        preference_response = sdk.preference().create(preference_data)
        if preference_response["status"] == 201:
            return JsonResponse({"id": preference_response["response"]["id"]})
        else:
            # Devuelve el error real de MercadoPago para depuración
            error_message = preference_response.get("response", {}).get("message", "No se pudo crear la preferencia")
            return JsonResponse({
                "error": error_message,
                "mp_response": preference_response.get("response", {})
            }, status=400)
    return HttpResponseBadRequest('Método no permitido')
