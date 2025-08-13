
from django import template

register = template.Library()

def get_stock(stocks, talla):
    """Devuelve la cantidad de stock para la talla dada o 0."""
    stock_obj = next((s for s in stocks if getattr(s, 'talla', None) == talla), None)
    if stock_obj is not None:
        return getattr(stock_obj, 'cantidad', 0)
    return 0
register.filter('get_stock', get_stock)

def intcomma_custom(value):
    try:
        # Si viene como string, separar parte entera y decimal correctamente
        if isinstance(value, str):
            # Si tiene coma, es decimal (3.500,25)
            if ',' in value:
                ent, dec = value.rsplit(',', 1)
                ent = ent.replace('.', '')
                value = float(ent + '.' + dec)
            else:
                value = float(value.replace('.', ''))
        # Si es Decimal, convertir a float
        from decimal import Decimal
        if isinstance(value, Decimal):
            value = float(value)
        # Formato: 450.000,00
        formatted = '{:,.2f}'.format(value)
        # Cambia separador miles a punto y decimal a coma
        formatted = formatted.replace(',', 'X').replace('.', ',').replace('X', '.')
        return formatted
    except (ValueError, TypeError):
        return value

register.filter('intcomma_custom', intcomma_custom)
