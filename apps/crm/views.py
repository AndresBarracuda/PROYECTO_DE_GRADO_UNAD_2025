from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q, F, Count
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def get_campaign_data(request, campaign_id):
    """Obtener datos de una campaña para cálculos en el frontend"""
    try:
        campaign = Campaign.objects.get(campaign_id=campaign_id, campaign_status=True)
        data = {
            'campaign_id': campaign.campaign_id,
            'campaign_name': campaign.campaign_name,
            'minimum_purchase_value': campaign.campaign_minimum_purchase_value,
            'ticket_multiplier': campaign.campaign_ticket_multiplier,
            'is_active': campaign.is_active,
        }
        return JsonResponse(data)
    except Campaign.DoesNotExist:
        return JsonResponse({'error': 'Campaña no encontrada'}, status=404)
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import Group, User
from django.conf import settings
import time
import json
import os
from .models import (
    Customer, Campaign, CampaignType, Ticket, 
    Invoice, PaymentMethod, CommercialPremise, InvoiceForEachCampaign
)
from .forms import CustomerForm, CampaignForm, CustomerSearchForm, InvoiceForm, InvoiceForEachCampaignForm
from .decorators import login_required, staff_required, admin_group_required, admin_or_operator_required

# Create your views here.

def index(request):
    """Vista principal del CRM - Acceso público para mostrar información básica"""
    context = {
        'page_title': 'Inicio',
    }
    return render(request, 'crm/index.html', context)


@login_required
def dashboard(request):
    """Dashboard con estadísticas del CRM - Requiere autenticación"""
    total_customers = Customer.objects.count()
    
    context = {
        'page_title': 'Dashboard',
        'total_customers': total_customers,
    }
    return render(request, 'crm/dashboard.html', context)


@login_required
def customer_list(request):
    """Lista de clientes con búsqueda y paginación - Requiere autenticación"""
    search_query = request.GET.get('search', '')
    customers = Customer.objects.all()
    
    if search_query:
        customers = customers.filter(
            Q(customer_first_name__icontains=search_query) |
            Q(customer_first_surname__icontains=search_query) |
            Q(customer_email__icontains=search_query) |
            Q(customer_document_number__icontains=search_query)
        )
    
    # Paginación
    paginator = Paginator(customers, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_title': 'Lista de Clientes',
        'customers': page_obj,
        'search_query': search_query,
    }
    return render(request, 'crm/customer_list.html', context)


@login_required
def customer_detail(request, customer_id):
    """Detalle de un cliente específico - Requiere autenticación"""
    customer = get_object_or_404(Customer, customer_id=customer_id)
    
    context = {
        'page_title': f'Cliente: {customer.customer_first_name} {customer.customer_first_surname}',
        'customer': customer,
    }
    return render(request, 'crm/customer_detail.html', context)


@admin_or_operator_required
def customer_add(request):
    """Agregar nuevo cliente - Requiere permisos de Admin o Operator"""
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            
            # Procesar datos de firma electrónica
            signature_data = request.POST.get('signature_data', '')
            if signature_data:
                try:
                    import json
                    import os
                    import time
                    from django.conf import settings
                    
                    # Crear directorio para firmas si no existe
                    signatures_dir = os.path.join(settings.MEDIA_ROOT, 'signatures')
                    os.makedirs(signatures_dir, exist_ok=True)
                    
                    # Generar nombre único para el archivo de firma
                    signature_filename = f"signature_{customer.customer_document_number}_{int(time.time())}.json"
                    signature_path = os.path.join(signatures_dir, signature_filename)
                    
                    # Guardar datos de firma en archivo JSON
                    with open(signature_path, 'w', encoding='utf-8') as f:
                        json.dump(json.loads(signature_data), f, ensure_ascii=False, indent=2)
                    
                    # Guardar referencia en el campo signature_desc
                    customer.customer_signature_desc = f"Firma electrónica guardada: {signature_filename}"
                    
                    messages.success(request, 'Firma electrónica guardada exitosamente.')
                    
                except Exception as e:
                    messages.warning(request, f'Error al guardar la firma electrónica: {str(e)}')
            
            # Asignar usuario actual como creador
            if hasattr(customer, 'created_by'):
                customer.created_by = request.user
            
            customer.save()
            
            messages.success(request, f'Cliente {customer.customer_first_name} {customer.customer_first_surname} agregado exitosamente.')
            return redirect('crm:customer_detail', customer_id=customer.customer_id)
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = CustomerForm()
    
    context = {
        'page_title': 'Agregar Cliente',
        'form': form,
        'is_edit': False,
    }
    return render(request, 'crm/customer_form.html', context)


@admin_or_operator_required
def customer_edit(request, customer_id):
    """Editar cliente existente - Requiere permisos de Admin o Operator"""
    customer = get_object_or_404(Customer, customer_id=customer_id)
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, f'Cliente {customer.customer_first_name} {customer.customer_first_surname} actualizado exitosamente.')
            return redirect('crm:customer_detail', customer_id=customer_id)
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = CustomerForm(instance=customer)
    
    context = {
        'page_title': f'Editar Cliente: {customer.customer_first_name} {customer.customer_first_surname}',
        'form': form,
        'customer': customer,
        'is_edit': True,
    }
    return render(request, 'crm/customer_form.html', context)
    
    context = {
        'page_title': f'Editar Cliente: {customer.customer_first_name} {customer.customer_first_surname}',
        'customer': customer,
    }
    return render(request, 'crm/customer_form.html', context)


@require_http_methods(["GET"])
def check_authentication(request):
    """Vista para verificar si el usuario está autenticado - para prevenir acceso con botón atrás"""
    return JsonResponse({
        'authenticated': request.user.is_authenticated
    })


def user_has_admin_group(user):
    """Función auxiliar para verificar si el usuario pertenece al grupo Admin"""
    if not user.is_authenticated:
        return False
    try:
        admin_group = Group.objects.get(name='Admin')
        return admin_group in user.groups.all()
    except Group.DoesNotExist:
        return False


def user_has_operator_permissions(user):
    """Función auxiliar para verificar si el usuario tiene permisos de Admin u Operator"""
    if not user.is_authenticated:
        return False
    user_groups = user.groups.values_list('name', flat=True)
    return any(group in user_groups for group in ['Admin', 'Operators'])


@admin_group_required
def admin_dashboard(request):
    """Dashboard exclusivo para usuarios del grupo Admin"""
    total_users = User.objects.count()
    total_customers = Customer.objects.count()
    admin_users = User.objects.filter(groups__name='Admin').count()
    
    context = {
        'page_title': 'Panel de Administración',
        'total_users': total_users,
        'total_customers': total_customers,
        'admin_users': admin_users,
    }
    return render(request, 'crm/admin_dashboard.html', context)


def get_stats(request):
    """Vista para obtener estadísticas en JSON"""
    from django.db.models import Count
    from datetime import datetime, timedelta
    
    # Total de clientes
    total_customers = Customer.objects.count()
    
    # Clientes activos
    active_customers = Customer.objects.filter(customer_status=True).count()
    
    # Nuevos clientes este mes
    current_month = datetime.now().month
    current_year = datetime.now().year
    new_customers = Customer.objects.filter(
        customer_registration_date__month=current_month,
        customer_registration_date__year=current_year
    ).count()
    
    # Calcular crecimiento (comparar con el mes anterior)
    last_month = current_month - 1 if current_month > 1 else 12
    last_month_year = current_year if current_month > 1 else current_year - 1
    
    last_month_customers = Customer.objects.filter(
        customer_registration_date__month=last_month,
        customer_registration_date__year=last_month_year
    ).count()
    
    if last_month_customers > 0:
        growth_rate = round(((new_customers - last_month_customers) / last_month_customers) * 100, 1)
    else:
        growth_rate = 100 if new_customers > 0 else 0
    
    stats = {
        'total_customers': total_customers,
        'active_customers': active_customers,
        'new_customers': new_customers,
        'growth_rate': f'{growth_rate}%'
    }
    
    return JsonResponse(stats)


##########################
##   CAMPAIGN VIEWS     ##
##########################

@login_required
def campaign_list(request):
    """Lista de campañas con búsqueda y paginación - Requiere autenticación"""
    search_query = request.GET.get('search', '')
    campaigns = Campaign.objects.all()
    
    if search_query:
        campaigns = campaigns.filter(
            Q(campaign_name__icontains=search_query) |
            Q(campaign_award_title__icontains=search_query) |
            Q(campaign_type__campaign_type_spanish_name__icontains=search_query)
        )
    
    # Paginación
    paginator = Paginator(campaigns, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_title': 'Lista de Campañas',
        'campaigns': page_obj,
        'search_query': search_query,
        'total_campaigns': campaigns.count(),
    }
    return render(request, 'crm/campaign_list.html', context)


@login_required
def campaign_detail(request, campaign_id):
    """Detalle de una campaña específica - Requiere autenticación"""
    campaign = get_object_or_404(Campaign, campaign_id=campaign_id)
    
    context = {
        'page_title': f'Campaña: {campaign.campaign_name}',
        'campaign': campaign,
    }
    return render(request, 'crm/campaign_detail.html', context)


@admin_or_operator_required
def campaign_add(request):
    """Agregar nueva campaña - Requiere permisos de Admin o Operator"""
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)
        if form.is_valid():
            campaign = form.save()
            
            messages.success(request, f'Campaña "{campaign.campaign_name}" creada exitosamente.')
            return redirect('crm:campaign_detail', campaign_id=campaign.campaign_id)
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = CampaignForm()
    
    context = {
        'page_title': 'Crear Campaña',
        'form': form,
        'is_edit': False,
    }
    return render(request, 'crm/campaign_form.html', context)


@admin_or_operator_required
def campaign_edit(request, campaign_id):
    """Editar campaña existente - Requiere permisos de Admin o Operator"""
    campaign = get_object_or_404(Campaign, campaign_id=campaign_id)
    
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES, instance=campaign)
        if form.is_valid():
            form.save()
            messages.success(request, f'Campaña "{campaign.campaign_name}" actualizada exitosamente.')
            return redirect('crm:campaign_detail', campaign_id=campaign_id)
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = CampaignForm(instance=campaign)
    
    context = {
        'page_title': f'Editar Campaña: {campaign.campaign_name}',
        'form': form,
        'campaign': campaign,
        'is_edit': True,
    }
    return render(request, 'crm/campaign_form.html', context)


# Vistas para Tickets
@admin_or_operator_required
def ticket_list(request):
    """Lista de tickets con filtros y búsqueda"""
    tickets = Ticket.objects.filter(ticket_status=True).select_related(
        'ticket_customer', 'ticket_campaign'
    )
    
    # Filtros
    search = request.GET.get('search', '')
    campaign_filter = request.GET.get('campaign', '')
    status_filter = request.GET.get('status', '')
    
    if search:
        tickets = tickets.filter(
            Q(ticket_number__icontains=search) |
            Q(ticket_customer__customer_first_name__icontains=search) |
            Q(ticket_customer__customer_first_surname__icontains=search) |
            Q(ticket_validation_code__icontains=search)
        )
    
    if campaign_filter:
        tickets = tickets.filter(ticket_campaign_id=campaign_filter)
    
    if status_filter == 'printed':
        tickets = tickets.filter(ticket_is_printed=True)
    elif status_filter == 'unprinted':
        tickets = tickets.filter(ticket_is_printed=False)
    elif status_filter == 'winner':
        tickets = tickets.filter(ticket_is_winner=True)
    
    # Paginación
    paginator = Paginator(tickets, 20)
    page_number = request.GET.get('page')
    tickets = paginator.get_page(page_number)
    
    # Campañas para el filtro
    campaigns = Campaign.objects.filter(campaign_status=True)
    
    context = {
        'tickets': tickets,
        'campaigns': campaigns,
        'search': search,
        'campaign_filter': campaign_filter,
        'status_filter': status_filter,
        'page_title': 'Lista de Tickets',
    }
    return render(request, 'crm/ticket_list.html', context)


@admin_or_operator_required
def ticket_detail(request, ticket_id):
    """Detalle de un ticket específico"""
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)
    
    context = {
        'ticket': ticket,
        'page_title': f'Ticket {ticket.ticket_number}',
    }
    return render(request, 'crm/ticket_detail.html', context)


@admin_or_operator_required
def ticket_print(request, ticket_id):
    """Marcar un ticket como impreso"""
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)
    
    try:
        from .ticket_utils import print_ticket
        print_ticket(ticket)
        messages.success(request, f'Ticket {ticket.ticket_number} marcado como impreso.')
    except ValueError as e:
        messages.error(request, str(e))
    
    return redirect('crm:ticket_detail', ticket_id=ticket_id)


@admin_or_operator_required
def ticket_mark_winner(request, ticket_id):
    """Marcar un ticket como ganador"""
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)
    
    try:
        from .ticket_utils import mark_ticket_as_winner
        mark_ticket_as_winner(ticket)
        messages.success(request, f'Ticket {ticket.ticket_number} marcado como ganador.')
    except ValueError as e:
        messages.error(request, str(e))
    
    return redirect('crm:ticket_detail', ticket_id=ticket_id)


@admin_or_operator_required
def ticket_statistics(request):
    """Estadísticas de tickets"""
    from .ticket_utils import get_ticket_statistics
    
    campaign_id = request.GET.get('campaign', '')
    campaign = None
    
    if campaign_id:
        campaign = get_object_or_404(Campaign, campaign_id=campaign_id)
    
    stats = get_ticket_statistics(campaign)
    campaigns = Campaign.objects.filter(campaign_status=True)
    
    context = {
        'stats': stats,
        'campaigns': campaigns,
        'selected_campaign': campaign,
        'page_title': 'Estadísticas de Tickets',
    }
    return render(request, 'crm/ticket_statistics.html', context)


@admin_or_operator_required
def customer_tickets(request, customer_id):
    """Tickets de un cliente específico"""
    customer = get_object_or_404(Customer, customer_id=customer_id)
    
    from .ticket_utils import get_customer_tickets
    tickets = get_customer_tickets(customer)
    
    # Paginación
    paginator = Paginator(tickets, 10)
    page_number = request.GET.get('page')
    tickets = paginator.get_page(page_number)
    
    context = {
        'customer': customer,
        'tickets': tickets,
        'page_title': f'Tickets de {customer.customer_first_name} {customer.customer_first_surname}',
    }
    return render(request, 'crm/customer_tickets.html', context)


@admin_or_operator_required
def ticket_print_preview(request, ticket_id):
    """Vista previa del ticket para impresión"""
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)
    
    context = {
        'ticket': ticket,
        'page_title': f'Vista Previa - Ticket {ticket.ticket_number}',
    }
    return render(request, 'crm/ticket_print_preview.html', context)


# ==================== MÓDULO DE FACTURAS ====================

@admin_or_operator_required
def invoice_search_customer(request):
    """Buscar cliente para registro de factura"""
    if request.method == 'POST':
        form = CustomerSearchForm(request.POST)
        if form.is_valid():
            document_number = form.cleaned_data['customer_document_number']
            
            try:
                customer = Customer.objects.get(
                    customer_document_number=document_number,
                    customer_status=True
                )
                # Cliente encontrado, redirigir al registro de factura
                return redirect('crm:invoice_add', customer_id=customer.customer_id)
                
            except Customer.DoesNotExist:
                # Cliente no encontrado, redirigir al registro de cliente
                messages.warning(
                    request, 
                    f'Cliente con documento {document_number} no encontrado. Por favor registre el cliente primero.'
                )
                return redirect('crm:customer_add_from_invoice', document_number=document_number)
    else:
        form = CustomerSearchForm()
    
    context = {
        'form': form,
        'page_title': 'Buscar Cliente para Factura',
    }
    return render(request, 'crm/invoice_search_customer.html', context)


@admin_or_operator_required
def customer_add_from_invoice(request, document_number):
    """Registrar cliente desde el proceso de facturación"""
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            messages.success(request, f'Cliente {customer.customer_first_name} {customer.customer_first_surname} registrado exitosamente.')
            return redirect('crm:invoice_add', customer_id=customer.customer_id)
    else:
        # Pre-cargar el número de documento
        initial_data = {'customer_document_number': document_number}
        form = CustomerForm(initial=initial_data)
    
    context = {
        'form': form,
        'document_number': document_number,
        'page_title': 'Registrar Cliente',
        'from_invoice': True,
    }
    return render(request, 'crm/customer_form.html', context)


@admin_or_operator_required
def invoice_add(request, customer_id):
    """Registrar nueva factura para un cliente específico"""
    customer = get_object_or_404(Customer, customer_id=customer_id)
    
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            campaign = form.cleaned_data['campaign']
            invoice = form.save(commit=False)
            invoice.invoice_customer = customer
            
            # Asignar el usuario que crea la factura
            if hasattr(request.user, 'username'):
                invoice.invoice_user = request.user.username
            
            invoice.save()
            
            # Crear la relación con la campaña
            relation = InvoiceForEachCampaign.objects.create(
                invoice_for_each_campaign_invoice=invoice,
                invoice_for_each_campaign_campaign=campaign,
            )
            
            # Generar tickets si la campaña está activa y el valor cumple con el mínimo
            tickets_generated = 0
            if campaign.is_active and invoice.invoice_purchase_value >= campaign.campaign_minimum_purchase_value:
                # Calcular número de tickets
                tickets_count = int(invoice.invoice_purchase_value / campaign.campaign_minimum_purchase_value) * campaign.campaign_ticket_multiplier
                
                # Crear tickets
                for i in range(tickets_count):
                    Ticket.objects.create(
                        ticket_customer=customer,
                        ticket_campaign=campaign,
                        ticket_value=invoice.invoice_purchase_value,
                        ticket_total=tickets_count,
                        ticket_opening=i + 1,
                        ticket_closing=i + 1,
                    )
                tickets_generated = tickets_count
            
            messages.success(
                request, 
                f'Factura {invoice.invoice_number} registrada exitosamente para la campaña {campaign.campaign_name}. Se generaron {tickets_generated} tickets.'
            )
            return redirect('crm:invoice_detail', invoice_id=relation.invoice_for_each_campaign_id)
    else:
        form = InvoiceForm(initial={'invoice_customer': customer})
    
    context = {
        'form': form,
        'customer': customer,
        'page_title': 'Registrar Factura',
    }
    return render(request, 'crm/invoice_form.html', context)


@admin_or_operator_required
def invoice_list(request):
    """Lista de facturas con filtros y búsqueda"""
    invoices = InvoiceForEachCampaign.objects.select_related(
        'invoice_for_each_campaign_invoice',
        'invoice_for_each_campaign_campaign',
        'invoice_for_each_campaign_invoice__invoice_customer',
        'invoice_for_each_campaign_invoice__invoice_payment_method',
        'invoice_for_each_campaign_invoice__invoice_commercial_premise'
    ).filter(invoice_status=True).annotate(
        tickets_count=Count(
            'invoice_for_each_campaign_invoice__invoice_customer__ticket',
            filter=Q(invoice_for_each_campaign_invoice__invoice_customer__ticket__ticket_campaign=F('invoice_for_each_campaign_campaign'))
        )
    )
    
    # Filtros
    search_query = request.GET.get('search', '')
    campaign_id = request.GET.get('campaign', '')
    payment_method_id = request.GET.get('payment_method', '')
    store_id = request.GET.get('store', '')
    date_from = request.GET.get('date_from', '')
    date_to = request.GET.get('date_to', '')
    
    if search_query:
        invoices = invoices.filter(
            Q(invoice_for_each_campaign_invoice__invoice_number__icontains=search_query) |
            Q(invoice_for_each_campaign_invoice__invoice_customer__customer_first_name__icontains=search_query) |
            Q(invoice_for_each_campaign_invoice__invoice_customer__customer_first_surname__icontains=search_query) |
            Q(invoice_for_each_campaign_invoice__invoice_customer__customer_document_number__icontains=search_query)
        )
    
    if campaign_id:
        invoices = invoices.filter(invoice_for_each_campaign_campaign_id=campaign_id)
    
    if payment_method_id:
        invoices = invoices.filter(invoice_for_each_campaign_invoice__invoice_payment_method_id=payment_method_id)
    
    if store_id:
        invoices = invoices.filter(invoice_for_each_campaign_invoice__invoice_commercial_premise_id=store_id)
    
    if date_from:
        invoices = invoices.filter(invoice_for_each_campaign_invoice__invoice_purchase_date__gte=date_from)
    
    if date_to:
        invoices = invoices.filter(invoice_for_each_campaign_invoice__invoice_purchase_date__lte=date_to)
    
    # Ordenamiento
    order = request.GET.get('order', '-invoice_for_each_campaign_invoice__invoice_purchase_date')
    invoices = invoices.order_by(order)
    
    # Paginación
    paginator = Paginator(invoices, 25)
    page_number = request.GET.get('page')
    invoices = paginator.get_page(page_number)
    
    # Datos para filtros
    campaigns = Campaign.objects.filter(campaign_status=True).order_by('campaign_name')
    payment_methods = PaymentMethod.objects.filter(payment_method_status=True).order_by('payment_method_name')
    # stores = CommercialStore.objects.filter(store_status=True).order_by('store_name')  # Modelo no existe aún
    
    context = {
        'invoices': invoices,
        'campaigns': campaigns,
        'payment_methods': payment_methods,
        # 'stores': stores,  # Comentado hasta crear el modelo CommercialStore
        'search_query': search_query,
        'page_title': 'Lista de Facturas',
    }
    return render(request, 'crm/invoice_list.html', context)


@admin_or_operator_required
def invoice_detail(request, invoice_id):
    """Detalle de una factura específica"""
    invoice_relation = get_object_or_404(
        InvoiceForEachCampaign.objects.select_related(
            'invoice_for_each_campaign_invoice__invoice_customer',
            'invoice_for_each_campaign_campaign',
            'invoice_for_each_campaign_invoice__invoice_payment_method',
            'invoice_for_each_campaign_invoice__invoice_commercial_premise'
        ),
        invoice_for_each_campaign_id=invoice_id
    )
    
    # Obtener tickets generados por esta factura (tickets del cliente para esta campaña, ordenados por fecha reciente)
    tickets = Ticket.objects.filter(
        ticket_customer=invoice_relation.invoice_for_each_campaign_invoice.invoice_customer,
        ticket_campaign=invoice_relation.invoice_for_each_campaign_campaign
    ).order_by('-ticket_registration_date')
    
    context = {
        'invoice': invoice_relation,
        'tickets': tickets,
        'page_title': f'Factura {invoice_relation.invoice_for_each_campaign_invoice.invoice_number}',
    }
    return render(request, 'crm/invoice_detail.html', context)


@admin_or_operator_required
def invoice_edit(request, invoice_id):
    """Editar factura existente"""
    invoice_relation = get_object_or_404(InvoiceForEachCampaign, invoice_for_each_campaign_id=invoice_id)
    invoice = invoice_relation.invoice_for_each_campaign_invoice
    
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            updated_invoice = form.save(commit=False)
            
            # Asignar el usuario que modifica la factura
            if hasattr(request.user, 'username'):
                updated_invoice.invoice_user = request.user.username
            
            updated_invoice.save()
            
            messages.success(request, f'Factura {updated_invoice.invoice_number} actualizada exitosamente.')
            return redirect('crm:invoice_detail', invoice_id=invoice_relation.invoice_for_each_campaign_id)
    else:
        form = InvoiceForm(instance=invoice)
    
    context = {
        'form': form,
        'invoice': invoice_relation,
        'customer': invoice.invoice_customer,
        'page_title': f'Editar Factura {invoice.invoice_number}',
        'is_edit': True,
    }
    return render(request, 'crm/invoice_form.html', context)


@login_required
def customer_signature(request, customer_id):
    """Obtener firma del cliente en formato JSON"""
    try:
        customer = get_object_or_404(Customer, customer_id=customer_id)
        print(f"DEBUG: customer_signature_desc = '{customer.customer_signature_desc}'")
        
        # Verificar si existe descripción de firma
        if not customer.customer_signature_desc:
            print("DEBUG: No hay customer_signature_desc")
            return JsonResponse({
                'success': False,
                'message': 'No hay firma registrada'
            })
        
        # Extraer nombre del archivo desde la descripción
        import re
        match = re.search(r'(signature_\d+_\d+\.json)', customer.customer_signature_desc)
        print(f"DEBUG: regex match = {match}")
        if not match:
            print("DEBUG: Regex no coincide")
            return JsonResponse({
                'success': False,
                'message': 'Referencia de firma no válida'
            })
        
        filename = match.group(1)
        signature_path = os.path.join(settings.MEDIA_ROOT, 'signatures', filename)
        print(f"DEBUG: signature_path = {signature_path}")
        print(f"DEBUG: archivo existe = {os.path.exists(signature_path)}")
        
        # Verificar si el archivo existe
        if not os.path.exists(signature_path):
            return JsonResponse({
                'success': False,
                'message': 'Archivo de firma no encontrado'
            })
        
        # Leer el archivo JSON
        with open(signature_path, 'r', encoding='utf-8') as f:
            signature_data = json.load(f)
        
        return JsonResponse({
            'success': True,
            'signature': signature_data
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error al cargar firma: {str(e)}'
        })


@login_required
def customer_signature_image(request, customer_id):
    """Servir imagen de firma del cliente"""
    try:
        customer = get_object_or_404(Customer, customer_id=customer_id)
        
        if not customer.customer_signature_desc:
            return JsonResponse({'error': 'No hay firma registrada'}, status=404)
        
        # Extraer nombre del archivo desde la descripción
        import re
        match = re.search(r'(signature_\d+_\d+\.json)', customer.customer_signature_desc)
        if not match:
            return JsonResponse({'error': 'Referencia de firma no válida'}, status=404)
        
        filename = match.group(1)
        signature_path = os.path.join(settings.MEDIA_ROOT, 'signatures', filename)
        
        if not os.path.exists(signature_path):
            return JsonResponse({'error': 'Archivo de firma no encontrado'}, status=404)
        
        # Leer el archivo JSON y extraer imageData
        with open(signature_path, 'r', encoding='utf-8') as f:
            signature_data = json.load(f)
        
        if 'imageData' not in signature_data:
            return JsonResponse({'error': 'Datos de imagen no encontrados'}, status=404)
        
        # Decodificar imagen base64
        import base64
        from django.http import HttpResponse
        
        image_data = signature_data['imageData']
        if image_data.startswith('data:image/png;base64,'):
            image_data = image_data.replace('data:image/png;base64,', '')
        
        image_binary = base64.b64decode(image_data)
        
        response = HttpResponse(image_binary, content_type='image/png')
        response['Content-Disposition'] = f'inline; filename="firma_{customer.customer_document_number}.png"'
        return response
        
    except Exception as e:
        return JsonResponse({'error': f'Error: {str(e)}'}, status=500)


@login_required
def campaign_data(request, campaign_id):
    """Obtener datos de campaña para cálculos en JavaScript"""
    try:
        campaign = get_object_or_404(Campaign, campaign_id=campaign_id)
        data = {
            'campaign_id': campaign.campaign_id,
            'campaign_name': campaign.campaign_name,
            'minimum_purchase_value': campaign.campaign_minimum_purchase_value,
            'minimum_purchase_value_anchor': campaign.campaign_minimum_purchase_value_anchor,
            'ticket_multiplier': campaign.campaign_ticket_multiplier,
            'campaign_bonus': campaign.campaign_bonus,
            'campaign_bonus_ticket_multiplier': campaign.campaign_bonus_ticket_multiplier if campaign.campaign_bonus else 1,
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
