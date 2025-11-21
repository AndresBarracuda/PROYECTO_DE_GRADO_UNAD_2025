from django.urls import path
from . import views
from .auth_views import custom_login_view, custom_logout_view
from .signature_views import get_customer_signature, view_signature_image

app_name = 'crm'

urlpatterns = [
    # Vistas principales
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Autenticación
    path('login/', custom_login_view, name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path('check-auth/', views.check_authentication, name='check_auth'),
    
    # Panel de administración (solo grupo Admin)
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # Gestión de clientes
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.customer_add, name='customer_add'),
    path('customers/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('customers/<int:customer_id>/edit/', views.customer_edit, name='customer_edit'),
    path('customers/<int:customer_id>/signature/', views.customer_signature, name='customer_signature'),
    path('customers/<int:customer_id>/signature/image/', views.customer_signature_image, name='customer_signature_image'),
    
    # Gestión de campañas
    path('campaigns/', views.campaign_list, name='campaign_list'),
    path('campaigns/add/', views.campaign_add, name='campaign_add'),
    path('campaigns/<int:campaign_id>/', views.campaign_detail, name='campaign_detail'),
    path('campaigns/<int:campaign_id>/edit/', views.campaign_edit, name='campaign_edit'),
    
    # Gestión de tickets
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('tickets/<int:ticket_id>/print/', views.ticket_print, name='ticket_print'),
    path('tickets/<int:ticket_id>/print-preview/', views.ticket_print_preview, name='ticket_print_preview'),
    path('tickets/<int:ticket_id>/mark-winner/', views.ticket_mark_winner, name='ticket_mark_winner'),
    path('tickets/statistics/', views.ticket_statistics, name='ticket_statistics'),
    path('customers/<int:customer_id>/tickets/', views.customer_tickets, name='customer_tickets'),
    
    # Gestión de facturas
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/search-customer/', views.invoice_search_customer, name='invoice_search_customer'),
    path('invoices/add/<int:customer_id>/', views.invoice_add, name='invoice_add'),
    path('invoices/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('invoices/<int:invoice_id>/edit/', views.invoice_edit, name='invoice_edit'),
    path('api/campaigns/<int:campaign_id>/data/', views.get_campaign_data, name='get_campaign_data'),
    path('customers/add-from-invoice/<str:document_number>/', views.customer_add_from_invoice, name='customer_add_from_invoice'),
    
    # API endpoints
    path('api/stats/', views.get_stats, name='get_stats'),
    
    # Firmas electrónicas
    path('customers/<int:customer_id>/signature/', get_customer_signature, name='get_customer_signature'),
    path('customers/<int:customer_id>/signature/image/', view_signature_image, name='view_signature_image'),
]