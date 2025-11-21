"""
Utilidades para el manejo de tickets en el sistema CRM
"""
from django.db import transaction
from .models import Ticket, TicketAccumulation, InvoiceForEachCampaign, TicketConfiguration


def generate_tickets_for_invoice(invoice):
    """
    Genera tickets automáticamente para una factura válida
    """
    if not invoice.is_eligible_for_tickets:
        return []
    
    tickets_generated = []
    campaign = invoice.invoice_campaign_campaign
    customer = invoice.invoice_campaign_customer
    
    # Calcular cuántos tickets se deben generar
    tickets_to_generate = invoice.invoice_campaign_tickets_generated
    
    if tickets_to_generate <= 0:
        return []
    
    with transaction.atomic():
        # Crear los tickets individuales
        for i in range(tickets_to_generate):
            ticket = Ticket.objects.create(
                ticket_customer=customer,
                ticket_campaign=campaign,
                ticket_invoice=invoice,
                ticket_value=campaign.campaign_minimum_purchase_value,
            )
            tickets_generated.append(ticket)
        
        # Actualizar o crear la acumulación de tickets
        accumulation, created = TicketAccumulation.objects.get_or_create(
            ticket_accum_customer=customer,
            ticket_accum_campaign=campaign,
            defaults={
                'ticket_accum_total_tickets': 0,
                'ticket_accum_used_tickets': 0,
                'ticket_accum_available_tickets': 0,
            }
        )
        
        # Actualizar la acumulación
        accumulation.ticket_accum_total_tickets += tickets_to_generate
        accumulation.ticket_accum_last_invoice_date = invoice.invoice_campaign_invoice_date
        accumulation.save()  # El save() calculará automáticamente los tickets disponibles
    
    return tickets_generated


def print_ticket(ticket):
    """
    Marca un ticket como impreso
    """
    from django.utils import timezone
    
    if not ticket.ticket_campaign.campaign_print_ticket:
        raise ValueError("Esta campaña no permite la impresión de tickets")
    
    if ticket.ticket_is_printed:
        raise ValueError("Este ticket ya ha sido impreso")
    
    ticket.ticket_is_printed = True
    ticket.ticket_print_date = timezone.now()
    ticket.save()
    
    return ticket


def validate_ticket(ticket_number, validation_code):
    """
    Valida un ticket usando su número y código de validación
    """
    try:
        ticket = Ticket.objects.get(
            ticket_number=ticket_number,
            ticket_validation_code=validation_code,
            ticket_status=True
        )
        return ticket
    except Ticket.DoesNotExist:
        return None


def get_customer_tickets(customer, campaign=None, status=None):
    """
    Obtiene los tickets de un cliente para una campaña específica
    """
    queryset = Ticket.objects.filter(
        ticket_customer=customer,
        ticket_status=True
    )
    
    if campaign:
        queryset = queryset.filter(ticket_campaign=campaign)
    
    if status == 'printed':
        queryset = queryset.filter(ticket_is_printed=True)
    elif status == 'unprinted':
        queryset = queryset.filter(ticket_is_printed=False)
    elif status == 'winner':
        queryset = queryset.filter(ticket_is_winner=True)
    
    return queryset.order_by('-ticket_registration_date')


def get_ticket_statistics(campaign=None):
    """
    Obtiene estadísticas de tickets para una campaña
    """
    queryset = Ticket.objects.filter(ticket_status=True)
    
    if campaign:
        queryset = queryset.filter(ticket_campaign=campaign)
    
    stats = {
        'total_tickets': queryset.count(),
        'printed_tickets': queryset.filter(ticket_is_printed=True).count(),
        'unprinted_tickets': queryset.filter(ticket_is_printed=False).count(),
        'winner_tickets': queryset.filter(ticket_is_winner=True).count(),
        'total_customers': queryset.values('ticket_customer').distinct().count(),
        'total_campaigns': queryset.values('ticket_campaign').distinct().count() if not campaign else 1,
    }
    
    return stats


def mark_ticket_as_winner(ticket):
    """
    Marca un ticket como ganador
    """
    if not ticket.ticket_status:
        raise ValueError("No se puede marcar un ticket inactivo como ganador")
    
    ticket.ticket_is_winner = True
    ticket.save()
    
    return ticket


def get_campaign_ticket_config(campaign):
    """
    Obtiene la configuración de tickets para una campaña específica
    """
    return {
        'print_enabled': campaign.campaign_print_ticket,
        'show_title': campaign.campaign_ticket_title,
        'show_award': campaign.campaign_ticket_award,
        'show_award_description': campaign.campaign_ticket_award_description,
        'show_validity_date': campaign.campaign_ticket_validity_date,
        'show_document_number': campaign.campaign_ticket_document_number,
        'show_names': campaign.campaign_ticket_names,
        'show_birth_day': campaign.campaign_ticket_birth_day,
        'show_cell_number': campaign.campaign_ticket_cell_number,
        'show_email': campaign.campaign_ticket_email,
        'show_regulatory_agency': campaign.campaign_ticket_regulatory_agency,
    }