from django import template
register = template.Library()

@register.filter(name='sum_attr')
def sum_attr(values, attr=None):
    """
    Suma una lista de diccionarios por el atributo dado, o una lista de números.
    Uso: {{ list|sum_attr:'subtotal' }}
    """
    if not values:
        return 0
    if attr:
        total = 0
        for v in values:
            if v is None:
                continue
            # Soporta tanto objetos como dicts
            if hasattr(v, attr):
                total += getattr(v, attr)
            elif isinstance(v, dict) and attr in v:
                total += v[attr]
        return total
    return sum(v for v in values if v is not None)
