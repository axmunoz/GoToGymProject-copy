from django.shortcuts import render, redirect
from .alegra import AlegraAPI
from django.conf import settings

def clientes(request):
    api = AlegraAPI(
        email=getattr(settings, 'ALEGRA_EMAIL', None),
        api_token=getattr(settings, 'ALEGRA_API_TOKEN', None)
    )
    clientes = []
    error = None
    filtro = request.GET.get('filtro', '').lower()
    try:
        clientes = api.get_clients()
        if filtro:
            clientes = [c for c in clientes if filtro in c.get('name', '').lower() or filtro in c.get('email', '').lower()]
        # Calcular totales
        total_clientes = len(clientes)
        # Activos: email no vacío y no 'inactivo'
        total_activos = sum(1 for c in clientes if c.get('email') and (c.get('estado', '').lower() != 'inactivo'))
        from datetime import datetime, timedelta
        total_nuevos = 0
        if clientes and 'fecha_registro' in clientes[0]:
            hace_15 = datetime.now() - timedelta(days=15)
            total_nuevos = sum(1 for c in clientes if c.get('fecha_registro') and datetime.strptime(c['fecha_registro'], '%Y-%m-%d') >= hace_15)
        # Ingresos: suma de facturas de venta
        total_ingresos = 0
        try:
            facturas = api.get_invoices()
            total_ingresos = sum(float(f.get('total', 0) or 0) for f in facturas if f.get('total'))
            total_ingresos = f"€{total_ingresos:,.0f}" if total_ingresos else "-"
        except Exception:
            total_ingresos = "-"
        # Egresos: suma de facturas de proveedor
        total_egresos = 0
        try:
            bills = api.get_bills()
            total_egresos = sum(float(b.get('total', 0) or 0) for b in bills if b.get('total'))
            total_egresos = f"€{total_egresos:,.0f}" if total_egresos else "-"
        except Exception:
            total_egresos = "-"
    except Exception as e:
        error = str(e)
        total_clientes = total_activos = total_nuevos = 0
        total_ingresos = "-"
    return render(request, 'contabilidad/clientes.html', {
        'clientes': clientes,
        'error': error,
        'filtro': filtro,
        'total_clientes': total_clientes,
        'total_activos': total_activos,
        'total_nuevos': total_nuevos,
        'total_ingresos': total_ingresos,
        'total_egresos': total_egresos,
    })

def facturas_cliente(request, cliente_id):
    api = AlegraAPI(
        email=getattr(settings, 'ALEGRA_EMAIL', None),
        api_token=getattr(settings, 'ALEGRA_API_TOKEN', None)
    )
    cliente = None
    facturas = []
    error = None
    filtro_factura = request.GET.get('filtro_factura', '').lower()
    try:
        clientes = api.get_clients()
        cliente = next((c for c in clientes if str(c['id']) == str(cliente_id)), None)
        facturas = [f for f in api.get_invoices() if f.get('client', {}).get('id') == str(cliente_id)]
        if filtro_factura:
            facturas = [f for f in facturas if filtro_factura in str(f.get('number', '')).lower() or filtro_factura in str(f.get('status', '')).lower()]
    except Exception as e:
        error = str(e)
    return render(request, 'contabilidad/facturas_cliente.html', {
        'cliente': cliente,
        'facturas': facturas,
        'error': error
    })


# Vista para crear un nuevo cliente y enviarlo a Alegra
from django import forms

class ClienteForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Teléfono', max_length=20, required=False)

def nuevo_cliente(request):
    error = None
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            api = AlegraAPI(
                email=getattr(settings, 'ALEGRA_EMAIL', None),
                api_token=getattr(settings, 'ALEGRA_API_TOKEN', None)
            )
            data = {
                'name': form.cleaned_data['name'],
                'type': 'client',
                'identification': '',
                'email': form.cleaned_data['email'],
                'phonePrimary': {'number': form.cleaned_data['phone']} if form.cleaned_data['phone'] else None,
            }
            try:
                api.create_client(data)
                return redirect('contabilidad:clientes')
            except Exception as e:
                error = str(e)
    else:
        form = ClienteForm()
    return render(request, 'contabilidad/nuevo_cliente.html', {
        'form': form,
        'error': error
    })

# Vista para ver el detalle de un cliente
def ver_cliente(request, cliente_id):
    api = AlegraAPI(
        email=getattr(settings, 'ALEGRA_EMAIL', None),
        api_token=getattr(settings, 'ALEGRA_API_TOKEN', None)
    )
    cliente = None
    error = None
    try:
        clientes = api.get_clients()
        cliente = next((c for c in clientes if str(c['id']) == str(cliente_id)), None)
        if not cliente:
            error = 'Cliente no encontrado.'
    except Exception as e:
        error = str(e)
    return render(request, 'contabilidad/ver_cliente.html', {
        'cliente': cliente,
        'error': error
    })

# Vista para editar un cliente
def editar_cliente(request, cliente_id):
    api = AlegraAPI(
        email=getattr(settings, 'ALEGRA_EMAIL', None),
        api_token=getattr(settings, 'ALEGRA_API_TOKEN', None)
    )
    error = None
    cliente = None
    try:
        clientes = api.get_clients()
        cliente = next((c for c in clientes if str(c['id']) == str(cliente_id)), None)
        if not cliente:
            error = 'Cliente no encontrado.'
    except Exception as e:
        error = str(e)
    if request.method == 'POST' and cliente:
        form = ClienteForm(request.POST)
        if form.is_valid():
            data = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'phonePrimary': form.cleaned_data['phone'],
            }
            try:
                api.update_client(cliente_id, data)
                return redirect('contabilidad:ver_cliente', cliente_id=cliente_id)
            except Exception as e:
                error = str(e)
    else:
        initial = {
            'name': cliente['name'] if cliente else '',
            'email': cliente['email'] if cliente else '',
            'phone': cliente.get('phonePrimary', '') if cliente else '',
        }
        form = ClienteForm(initial=initial)
    return render(request, 'contabilidad/editar_cliente.html', {
        'form': form,
        'cliente': cliente,
        'error': error
    })

# Vista para eliminar un cliente
def eliminar_cliente(request, cliente_id):
    api = AlegraAPI(
        email=getattr(settings, 'ALEGRA_EMAIL', None),
        api_token=getattr(settings, 'ALEGRA_API_TOKEN', None)
    )
    error = None
    cliente = None
    try:
        clientes = api.get_clients()
        cliente = next((c for c in clientes if str(c['id']) == str(cliente_id)), None)
        if not cliente:
            error = 'Cliente no encontrado.'
    except Exception as e:
        error = str(e)
    if request.method == 'POST' and cliente:
        try:
            api.delete_client(cliente_id)
            return redirect('contabilidad:clientes')
        except Exception as e:
            error = str(e)
    return render(request, 'contabilidad/eliminar_cliente.html', {
        'cliente': cliente,
        'error': error
    })
