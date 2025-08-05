def cart_count(request):
    cart = request.session.get('cart', {})
    num_items = sum(cart.values())
    return {'cart_count': num_items}


from django.conf import settings
def mercadopago_public_key(request):
    # Siempre retorna la public key de MercadoPago para el template
    public_key = getattr(settings, 'MP_PUBLIC_KEY', '')
    if not public_key:
        # Opcional: puedes lanzar un error o loggear si falta la key
        pass
    return {
        'mp_public_key': public_key
    }
