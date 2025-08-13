def cart_count(request):
    cart = request.session.get('cart', {})
    num_items = sum(cart.values())
    return {'num_items': num_items, 'cart_count': num_items}


from django.conf import settings
def mercadopago_public_key(request):
    public_key = getattr(settings, 'MP_PUBLIC_KEY', '')
    if not public_key:
        pass
    return {
        'mp_public_key': public_key
    }
