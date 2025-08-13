from django.shortcuts import render

def mercadopago_checkout(request):
    return render(request, 'mercadopago_integration/checkout.html', {
        'mercadopago_public_key': settings.MERCADOPAGO_PUBLIC_KEY
    })
import mercadopago
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def crear_preferencia(request):
    if request.method == 'POST':
        sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)
        preference_data = {
            "items": [
                {
                    "title": "Pago carrito",
                    "quantity": 1,
                    "unit_price": float(request.POST.get('unit_price', 100.0)),
                }
            ],
            "back_urls": {
                "success": f"{settings.SITE_URL}/mercadopago/success/",
                "failure": f"{settings.SITE_URL}/mercadopago/failure/",
                "pending": f"{settings.SITE_URL}/mercadopago/pending/"
            },
            "auto_return": "approved",
        }
        try:
            preference_response = sdk.preference().create(preference_data)
            if 'response' in preference_response and 'id' in preference_response['response']:
                return JsonResponse({
                    'id': preference_response['response']['id']
                })
            else:
                return JsonResponse({
                    'error': preference_response.get('message', 'Error desconocido'),
                    'response': preference_response
                }, status=400)
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            }, status=500)
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def webhook_pago(request):
    # Aquí puedes procesar la notificación de MercadoPago
    return HttpResponse('Webhook recibido', status=200)
