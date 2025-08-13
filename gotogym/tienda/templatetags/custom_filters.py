from django import template
register = template.Library()

@register.filter
def get_stock(stocks, talla):
    """Devuelve el objeto stock para la talla dada o None."""
    return next((s for s in stocks if s.talla == talla), None)
