from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

# Resources para Import/Export
class StatusCodeResource(resources.ModelResource):
    class Meta:
        model = StatusCode
        import_id_fields = ["status_code_id"]


class DocumentTypeResource(resources.ModelResource):
    class Meta:
        model = DocumentType
        import_id_fields = ["document_type_id"]


class GenderResource(resources.ModelResource):
    class Meta:
        model = Gender
        import_id_fields = ["gender_id"]


class BloodTypeResource(resources.ModelResource):
    class Meta:
        model = BloodType
        import_id_fields = ["blood_type_id"]


class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department
        import_id_fields = ["department_id"]


class CityResource(resources.ModelResource):
    class Meta:
        model = City
        import_id_fields = ["city_id"]


class PopulatedPlaceResource(resources.ModelResource):
    class Meta:
        model = PopulatedPlace
        import_id_fields = ["populated_place_id"]


class NeighborhoodResource(resources.ModelResource):
    class Meta:
        model = Neighborhood
        import_id_fields = ["neighborhood_id"]


class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer
        import_id_fields = ["customer_id"]


class CommercialPremiseCategoryResource(resources.ModelResource):
    class Meta:
        model = CommercialPremiseCategory
        import_id_fields = ["commercial_category_id"]


class CommercialPremiseResource(resources.ModelResource):
    class Meta:
        model = CommercialPremise
        import_id_fields = ["commercial_premise_id"]


class InvoiceResource(resources.ModelResource):
    class Meta:
        model = Invoice
        import_id_fields = ["invoice_id"]


# Admin classes con Import/Export
class StatusCodeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = [
        "status_code_code",
        "status_code_name",
        "status_code_spanish_name",
    ]

    list_display = (
        "status_code_id",
        "status_code_user",
        "status_code_registration_date",
        "status_code_update_date",
        "status_code_code",
        "status_code_name",
        "status_code_spanish_name",
        "status_code_status",
    )

    resource_class = StatusCodeResource


class CustomSettingsAdmin(admin.ModelAdmin):
    search_fields = [
        "custom_settings_shopping_center_name",
        "custom_settings_company_name",
        "custom_settings_nit",
    ]

    list_display = (
        "custom_settings_id",
        "custom_settings_shopping_center_name",
        "custom_settings_company_name",
        "custom_settings_nit",
        "custom_settings_mailing_enabled",
        "custom_settings_wacom",
        "custom_settings_status",
    )

    fieldsets = (
        ("Información Básica", {
            "fields": (
                "custom_settings_shopping_center_name",
                "custom_settings_company_name",
                "custom_settings_nit",
                "custom_settings_domain",
                "custom_settings_status_code",
            )
        }),
        ("APIs y Claves", {
            "fields": (
                "custom_settings_crab_api_key",
            )
        }),
        ("Configuraciones de Funcionalidades", {
            "fields": (
                "custom_settings_mailing_enabled",
                "custom_settings_wacom",
            )
        }),
        ("Campos Requeridos para Clientes", {
            "fields": (
                "custom_settings_blood_type_required",
                "custom_settings_landline_number_required",
                "custom_settings_residence_address_required",
                "custom_settings_neighborhood_required",
                "custom_settings_social_class_required",
                "custom_settings_marital_status_required",
                "custom_settings_occupation_required",
                "custom_settings_health_plan_required",
                "custom_settings_emergency_contact_required",
            )
        }),
        ("Imágenes Corporativas", {
            "fields": (
                "custom_settings_vertical_imagotypical_image",
                "custom_settings_horizontal_imagotypical_image",
                "custom_settings_isotypical_image",
            )
        }),
        ("Autorización de Datos", {
            "fields": (
                "custom_settings_data_processing_authorization",
            )
        }),
        ("Estado", {
            "fields": (
                "custom_settings_status",
            )
        }),
    )


class DocumentTypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = [
        "document_type_name",
    ]

    list_display = (
        "document_type_id",
        "document_type_name",
        "document_type_status",
    )

    resource_class = DocumentTypeResource


class GenderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = [
        "gender_name",
    ]

    list_display = (
        "gender_id",
        "gender_acronym",
        "gender_name",
        "gender_status",
    )

    resource_class = GenderResource


class BloodTypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = [
        "blood_type_name",
    ]

    list_display = (
        "blood_type_id",
        "blood_type_name",
        "blood_type_status",
    )

    resource_class = BloodTypeResource


class DepartmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = [
        "department_name",
    ]

    list_display = (
        "department_id",
        "department_name",
        "department_status",
    )

    resource_class = DepartmentResource


class CityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = [
        "city_name",
    ]

    list_display = (
        "city_id",
        "city_name",
        "city_department",
        "city_status",
    )

    list_filter = ("city_department", "city_status")
    resource_class = CityResource


class PopulatedPlaceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = [
        "populated_place_name",
    ]

    list_display = (
        "populated_place_id",
        "populated_place_name",
        "populated_place_city",
        "populated_place_status",
    )

    list_filter = ("populated_place_city", "populated_place_status")
    resource_class = PopulatedPlaceResource


class NeighborhoodAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = [
        "neighborhood_name",
    ]

    list_display = (
        "neighborhood_id",
        "neighborhood_name",
        "neighborhood_populated_place",
        "neighborhood_status",
    )

    list_filter = ("neighborhood_populated_place", "neighborhood_status")
    resource_class = NeighborhoodResource


# Administración principal para Customer (CRM)
class CustomerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = [
        "customer_first_name",
        "customer_first_surname",
        "customer_email",
        "customer_document_number",
        "customer_cell_number",
    ]

    list_display = (
        "customer_id",
        "customer_document_number",
        "customer_first_name",
        "customer_first_surname",
        "customer_email",
        "customer_cell_number",
        "customer_points",
        "customer_status",
    )

    list_filter = (
        "customer_gender",
        "customer_document_type",
        "customer_blood_type",
        "customer_marital_status",
        "customer_health_plan",
        "customer_neighborhood",
        "customer_internal",
        "customer_status",
    )

    readonly_fields = (
        "customer_registration_date",
        "customer_date_update",
        "customer_user",
        "customer_points",
        "customer_invoices",
        "customer_purchases",
    )

    fieldsets = (
        ("Información Básica del Cliente", {
            "fields": (
                "customer_document_type",
                "customer_document_number",
                "customer_first_name",
                "customer_middle_name",
                "customer_first_surname",
                "customer_second_surname",
                "customer_gender",
                "customer_date_birth",
                "customer_blood_type",
            )
        }),
        ("Información de Contacto", {
            "fields": (
                "customer_cell_number",
                "customer_landline_number",
                "customer_email",
            )
        }),
        ("Información de Ubicación", {
            "fields": (
                "customer_neighborhood",
                "customer_residence_address_select",
                "customer_residence_address_part_one",
                "customer_residence_address_part_two",
                "customer_residence_address_part_three",
                "customer_residence_address_supplementary_part",
            )
        }),
        ("Información Adicional", {
            "fields": (
                "customer_social_class",
                "customer_marital_status",
                "customer_occupation",
                "customer_health_plan",
            )
        }),
        ("Redes Sociales", {
            "fields": (
                "customer_facebook",
                "customer_instagram", 
                "customer_twitter",
                "customer_whatsapp",
            )
        }),
        ("Autorizaciones y Notificaciones", {
            "fields": (
                "customer_notifications_email",
                "customer_notifications_cell",
                "customer_notifications_residence_address",
            )
        }),
        ("Información Familiar y Personal", {
            "fields": (
                "customer_children_sw",
                "customer_children_number",
                "customer_vehicles_sw",
                "customer_pets_sw",
            )
        }),
        ("Contacto de Emergencia", {
            "fields": (
                "customer_emergency_contact_names",
                "customer_emergency_contact_surnames",
                "customer_emergency_contact_number",
            )
        }),
        ("Firma Digital", {
            "fields": (
                "customer_signature_option",
                "customer_signature_desc",
            )
        }),
        ("Configuración del Sistema", {
            "fields": (
                "customer_covenant",
                "customer_internal",
                "customer_status",
            )
        }),
        ("Estadísticas del Sistema (Solo lectura)", {
            "fields": (
                "customer_user",
                "customer_points",
                "customer_invoices",
                "customer_purchases",
                "customer_registration_date",
                "customer_date_update",
            ),
            "classes": ("collapse",),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        
        # Configurar el usuario que crea/modifica el registro
        if hasattr(form.base_fields, 'customer_user'):
            form.base_fields['customer_user'].initial = request.user.username
            
        return form

    def save_model(self, request, obj, form, change):
        if not change:  # Si es un nuevo objeto
            obj.customer_user = request.user.username
        else:  # Si es una modificación
            obj.customer_user = request.user.username
        super().save_model(request, obj, form, change)

    resource_class = CustomerResource


# Registrar todos los modelos con sus respectivos admins
admin.site.register(StatusCode, StatusCodeAdmin)
admin.site.register(CustomSettings, CustomSettingsAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(BloodType, BloodTypeAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(PopulatedPlace, PopulatedPlaceAdmin)
admin.site.register(Neighborhood, NeighborhoodAdmin)
admin.site.register(Customer, CustomerAdmin)

# Registros simples para el resto de modelos
admin.site.register(TypeOfVehicle)
admin.site.register(MeansOfTransport)
admin.site.register(TypeOfPets)
admin.site.register(Kinship)
admin.site.register(HealthPlan)
admin.site.register(MaritalStatus)
admin.site.register(Address)
admin.site.register(Generation)
admin.site.register(SignatureOption)
admin.site.register(Group)
admin.site.register(Contact)
admin.site.register(Directory)


# Resources para Campaigns
class CampaignTypeResource(resources.ModelResource):
    class Meta:
        model = CampaignType
        import_id_fields = ["campaign_type_id"]


class CampaignResource(resources.ModelResource):
    class Meta:
        model = Campaign
        import_id_fields = ["campaign_id"]


# Admin classes para Campaigns
@admin.register(CampaignType)
class CampaignTypeAdmin(ImportExportModelAdmin):
    resource_class = CampaignTypeResource
    list_display = ['campaign_type_spanish_name', 'campaign_type_name', 'campaign_type_code', 'campaign_type_status']
    list_filter = ['campaign_type_status', 'campaign_type_registration_date']
    search_fields = ['campaign_type_spanish_name', 'campaign_type_name']
    ordering = ['campaign_type_spanish_name']


@admin.register(Campaign)
class CampaignAdmin(ImportExportModelAdmin):
    resource_class = CampaignResource
    list_display = ['campaign_name', 'campaign_type', 'campaign_start_date', 'campaign_end_date', 'campaign_status', 'campaign_registration_date']
    list_filter = ['campaign_status', 'campaign_type', 'campaign_start_date', 'campaign_end_date']
    search_fields = ['campaign_name', 'campaign_award_title']
    ordering = ['-campaign_registration_date']
    date_hierarchy = 'campaign_start_date'
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('campaign_name', 'campaign_type', 'campaign_status')
        }),
        ('Premio', {
            'fields': ('campaign_award_title', 'campaign_award_description', 'campaign_image'),
            'classes': ('collapse',)
        }),
        ('Fechas y Horarios', {
            'fields': (
                ('campaign_start_date', 'campaign_end_date'),
                ('campaign_start_time_window', 'campaign_end_time_window')
            )
        }),
        ('Días de la Semana', {
            'fields': (
                ('campaign_monday', 'campaign_tuesday', 'campaign_wednesday'),
                ('campaign_thursday', 'campaign_friday'),
                ('campaign_saturday', 'campaign_sunday')
            ),
            'classes': ('collapse',)
        }),
        ('Configuración de Participación', {
            'fields': (
                'campaign_minimum_purchase_value',
                'campaign_ticket_multiplier',
                ('campaign_maximum_tickets_per_campaign', 'campaign_maximum_tickets_per_customer'),
                'campaign_maximum_tickets_per_invoice'
            )
        }),
        ('Configuración de Tickets', {
            'fields': (
                'campaign_print_ticket',
                ('campaign_ticket_title', 'campaign_ticket_award'),
                ('campaign_ticket_award_description', 'campaign_ticket_validity_date'),
                ('campaign_ticket_document_number', 'campaign_ticket_names'),
                ('campaign_ticket_birth_day', 'campaign_ticket_cell_number'),
                ('campaign_ticket_email', 'campaign_ticket_regulatory_agency')
            ),
            'classes': ('collapse',)
        }),
        ('Información del Sistema', {
            'fields': ('campaign_invoices_number',),
            'classes': ('collapse',)
        })
    )


class InvoiceForEachCampaignResource(resources.ModelResource):
    class Meta:
        model = InvoiceForEachCampaign
        fields = (
            'invoice_campaign_id', 'invoice_campaign_campaign', 'invoice_campaign_customer',
            'invoice_campaign_invoice_number', 'invoice_campaign_invoice_date',
            'invoice_campaign_total_value', 'invoice_campaign_discount_value', 'invoice_campaign_final_value',
            'invoice_campaign_tickets_generated', 'invoice_campaign_is_valid', 'invoice_campaign_validation_notes',
            'invoice_campaign_status', 'invoice_campaign_registration_date', 'invoice_campaign_update_date'
        )


class TicketResource(resources.ModelResource):
    class Meta:
        model = Ticket
        fields = (
            'ticket_id', 'ticket_customer', 'ticket_campaign',
            'ticket_value', 'ticket_anchor_value', 'ticket_campaign_value',
            'ticket_total', 'ticket_opening', 'ticket_closing', 'ticket_status',
            'ticket_registration_date'
        )


@admin.register(Ticket)
class TicketAdmin(ImportExportModelAdmin):
    resource_class = TicketResource
    list_display = ('ticket_id', 'ticket_customer', 'ticket_campaign', 'ticket_value', 'ticket_total', 'ticket_status')
    list_filter = ('ticket_status', 'ticket_campaign', 'ticket_registration_date')
    search_fields = ('ticket_customer__customer_first_name', 'ticket_customer__customer_first_surname', 'ticket_campaign__campaign_name')
    readonly_fields = ('ticket_value', 'ticket_anchor_value', 'ticket_campaign_value', 'ticket_total', 'ticket_opening', 'ticket_closing', 'ticket_registration_date')
    
    fieldsets = (
        ('Relaciones', {
            'fields': ('ticket_customer', 'ticket_campaign', 'ticket_status')
        }),
        ('Valores', {
            'fields': ('ticket_value', 'ticket_anchor_value', 'ticket_campaign_value', 'ticket_total')
        }),
        ('Tickets', {
            'fields': ('ticket_opening', 'ticket_closing')
        }),
        ('Información del Sistema', {
            'fields': ('ticket_registration_date',),
            'classes': ('collapse',)
        })
    )


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = (
        'payment_method_id',
        'payment_method_name',
        'payment_method_code',
        'payment_method_status',
    )
    
    list_filter = (
        'payment_method_status',
    )
    
    search_fields = (
        'payment_method_name',
        'payment_method_code',
    )
    
    ordering = ('payment_method_name',)
    
    readonly_fields = (
        'payment_method_code',
        'payment_method_user',
        'payment_method_registration_date',
        'payment_method_update_date',
    )
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('payment_method_name', 'payment_method_code')
        }),
        ('Estado', {
            'fields': ('payment_method_status',)
        }),
        ('Información del Sistema', {
            'fields': (
                'payment_method_user',
                'payment_method_registration_date',
                'payment_method_update_date',
            ),
            'classes': ('collapse',)
        })
    )


# Actualizar el admin de InvoiceForEachCampaign para incluir los nuevos campos
@admin.register(InvoiceForEachCampaign)
class InvoiceForEachCampaignAdmin(admin.ModelAdmin):
    list_display = (
        'invoice_for_each_campaign_id',
        'invoice_for_each_campaign_invoice',
        'invoice_for_each_campaign_campaign',
        'invoice_status',
    )
    
    list_filter = (
        'invoice_status',
        'invoice_for_each_campaign_campaign',
    )
    
    search_fields = (
        'invoice_for_each_campaign_invoice__invoice_number',
        'invoice_for_each_campaign_campaign__campaign_name',
    )
    
    ordering = ('-invoice_for_each_campaign_id',)
    
    fieldsets = (
        ('Información Básica', {
            'fields': (
                'invoice_for_each_campaign_invoice',
                'invoice_for_each_campaign_campaign',
            )
        }),
        ('Estado', {
            'fields': ('invoice_status',)
        })
    )


@admin.register(Invoice)
class InvoiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('invoice_number', 'invoice_customer', 'invoice_commercial_premise', 'invoice_purchase_date', 'invoice_purchase_value', 'invoice_status')
    list_filter = ('invoice_status', 'invoice_purchase_date', 'invoice_commercial_premise', 'invoice_payment_method')
    search_fields = ('invoice_number', 'invoice_customer__customer_first_name', 'invoice_customer__customer_first_surname', 'invoice_commercial_premise__commercial_premise_name')
    ordering = ('-invoice_purchase_date',)
    resource_class = InvoiceResource

    fieldsets = (
        ('Información Básica', {
            'fields': (
                'invoice_customer',
                'invoice_commercial_premise',
                'invoice_purchase_date',
                'invoice_number',
                'invoice_purchase_value',
                'invoice_time_of_stay',
            )
        }),
        ('Pago y Método', {
            'fields': (
                'invoice_payment_method',
                'invoice_parking',
            )
        }),
        ('Estado', {
            'fields': ('invoice_status',)
        })
    )


@admin.register(CommercialPremiseCategory)
class CommercialPremiseCategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('commercial_category_name', 'commercial_category_status')
    list_filter = ('commercial_category_status',)
    search_fields = ('commercial_category_name',)
    ordering = ('commercial_category_name',)
    resource_class = CommercialPremiseCategoryResource


@admin.register(CommercialPremise)
class CommercialPremiseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('commercial_premise_name', 'commercial_premise_nomenclature', 'commercial_premise_category', 'commercial_premise_status')
    list_filter = ('commercial_premise_status', 'commercial_premise_category', 'commercial_premise_anchor')
    search_fields = ('commercial_premise_name', 'commercial_premise_nomenclature')
    ordering = ('commercial_premise_name',)
    resource_class = CommercialPremiseResource
