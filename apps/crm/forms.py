from django import forms
from datetime import date
from .models import (
    Customer, DocumentType, Neighborhood, Gender, Campaign, CampaignType,
    InvoiceForEachCampaign, PaymentMethod, Invoice, CommercialPremise,
    BloodType, MaritalStatus, HealthPlan, Address, SignatureOption
)


class CustomerForm(forms.ModelForm):
    """Formulario para crear y editar clientes"""
    
    class Meta:
        model = Customer
        fields = [
            # Información básica
            'customer_document_type',
            'customer_document_number',
            'customer_first_name',
            'customer_middle_name', 
            'customer_first_surname',
            'customer_second_surname',
            'customer_gender',
            'customer_date_birth',
            'customer_blood_type',
            
            # Información de contacto
            'customer_cell_number',
            'customer_landline_number',
            'customer_email',
            
            # Información de ubicación
            'customer_neighborhood',
            'customer_residence_address_select',
            'customer_residence_address_part_one',
            'customer_residence_address_part_two',
            'customer_residence_address_part_three',
            'customer_residence_address_supplementary_part',
            
            # Información adicional
            'customer_social_class',
            'customer_marital_status',
            'customer_occupation',
            'customer_health_plan',
            
            # Redes sociales
            'customer_facebook',
            'customer_instagram',
            'customer_twitter',
            'customer_whatsapp',
            
            # Notificaciones
            'customer_notifications_email',
            'customer_notifications_cell',
            'customer_notifications_residence_address',
            
            # Información familiar
            'customer_children_sw',
            'customer_children_number',
            'customer_vehicles_sw',
            'customer_pets_sw',
            
            # Contacto de emergencia
            'customer_emergency_contact_names',
            'customer_emergency_contact_surnames',
            'customer_emergency_contact_number',
            
            # Firma digital
            'customer_signature_option',
            'customer_signature_desc',
            
            # Sistema
            'customer_covenant',
            'customer_internal',
            'customer_status',
        ]
        
        widgets = {
            # Información básica
            'customer_document_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'customer_document_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de documento'
            }),
            'customer_first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Primer nombre'
            }),
            'customer_middle_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Segundo nombre (opcional)'
            }),
            'customer_first_surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Primer apellido'
            }),
            'customer_second_surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Segundo apellido (opcional)'
            }),
            'customer_gender': forms.Select(attrs={
                'class': 'form-select'
            }),
            'customer_date_birth': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'customer_blood_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            
            # Información de contacto
            'customer_cell_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de celular'
            }),
            'customer_landline_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de teléfono fijo'
            }),
            'customer_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            
            # Información de ubicación
            'customer_neighborhood': forms.Select(attrs={
                'class': 'form-select'
            }),
            'customer_residence_address_select': forms.Select(attrs={
                'class': 'form-select'
            }),
            'customer_residence_address_part_one': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 123'
            }),
            'customer_residence_address_part_two': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 45'
            }),
            'customer_residence_address_part_three': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 67'
            }),
            'customer_residence_address_supplementary_part': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apto 101, Bloque A, etc.'
            }),
            
            # Información adicional
            'customer_social_class': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '6',
                'placeholder': '1-6'
            }),
            'customer_marital_status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'customer_occupation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ocupación del cliente'
            }),
            'customer_health_plan': forms.Select(attrs={
                'class': 'form-select'
            }),
            
            # Redes sociales
            'customer_facebook': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'customer_instagram': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'customer_twitter': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'customer_whatsapp': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            
            # Notificaciones
            'customer_notifications_email': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'customer_notifications_cell': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'customer_notifications_residence_address': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            
            # Información familiar
            'customer_children_sw': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'customer_children_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'placeholder': 'Número de hijos'
            }),
            'customer_vehicles_sw': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'customer_pets_sw': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            
            # Contacto de emergencia
            'customer_emergency_contact_names': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombres del contacto de emergencia'
            }),
            'customer_emergency_contact_surnames': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellidos del contacto de emergencia'
            }),
            'customer_emergency_contact_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número del contacto de emergencia'
            }),
            
            # Firma digital
            'customer_signature_option': forms.Select(attrs={
                'class': 'form-select'
            }),
            'customer_signature_desc': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción de la firma'
            }),
            
            # Sistema
            'customer_covenant': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Convenio deportivo'
            }),
            'customer_internal': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'customer_status': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        
        labels = {
            # Información básica
            'customer_document_type': 'Tipo de Documento *',
            'customer_document_number': 'Número de Documento *',
            'customer_first_name': 'Primer Nombre *',
            'customer_middle_name': 'Segundo Nombre',
            'customer_first_surname': 'Primer Apellido *',
            'customer_second_surname': 'Segundo Apellido',
            'customer_gender': 'Género *',
            'customer_date_birth': 'Fecha de Nacimiento *',
            'customer_blood_type': 'Tipo de Sangre (RH) *',
            
            # Información de contacto
            'customer_cell_number': 'Número de Celular *',
            'customer_landline_number': 'Teléfono Fijo',
            'customer_email': 'Correo Electrónico',
            
            # Información de ubicación
            'customer_neighborhood': 'Barrio *',
            'customer_residence_address_select': 'Tipo de Dirección',
            'customer_residence_address_part_one': 'Dirección Parte 1',
            'customer_residence_address_part_two': 'Dirección Parte 2',
            'customer_residence_address_part_three': 'Dirección Parte 3',
            'customer_residence_address_supplementary_part': 'Información Adicional',
            
            # Información adicional
            'customer_social_class': 'Clase Social (1-6)',
            'customer_marital_status': 'Estado Civil',
            'customer_occupation': 'Ocupación',
            'customer_health_plan': 'Plan de Salud',
            
            # Redes sociales
            'customer_facebook': 'Facebook',
            'customer_instagram': 'Instagram',
            'customer_twitter': 'Twitter',
            'customer_whatsapp': 'WhatsApp',
            
            # Notificaciones
            'customer_notifications_email': 'Notificaciones por Email',
            'customer_notifications_cell': 'Notificaciones por SMS',
            'customer_notifications_residence_address': 'Notificaciones por Correo',
            
            # Información familiar
            'customer_children_sw': '¿Tiene Hijos?',
            'customer_children_number': 'Número de Hijos',
            'customer_vehicles_sw': '¿Tiene Vehículos?',
            'customer_pets_sw': '¿Tiene Mascotas?',
            
            # Contacto de emergencia
            'customer_emergency_contact_names': 'Nombres Contacto de Emergencia',
            'customer_emergency_contact_surnames': 'Apellidos Contacto de Emergencia',
            'customer_emergency_contact_number': 'Teléfono Contacto de Emergencia',
            
            # Firma digital
            'customer_signature_option': 'Opción de Firma',
            'customer_signature_desc': 'Descripción de Firma',
            
            # Sistema
            'customer_covenant': 'Convenio',
            'customer_internal': 'Cliente Interno',
            'customer_status': 'Cliente Activo',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Configurar querysets para campos ForeignKey
        self.fields['customer_document_type'].queryset = DocumentType.objects.filter(document_type_status=True)
        self.fields['customer_gender'].queryset = Gender.objects.filter(gender_status=True)
        self.fields['customer_blood_type'].queryset = BloodType.objects.filter(blood_type_status=True)
        self.fields['customer_neighborhood'].queryset = Neighborhood.objects.filter(neighborhood_status=True)
        self.fields['customer_residence_address_select'].queryset = Address.objects.filter(address_status=True)
        self.fields['customer_marital_status'].queryset = MaritalStatus.objects.filter(marital_status_status=True)
        self.fields['customer_health_plan'].queryset = HealthPlan.objects.filter(health_plan_status=True)
        self.fields['customer_signature_option'].queryset = SignatureOption.objects.filter(sign_opt_status=True)
        
        # Configurar empty_label
        self.fields['customer_document_type'].empty_label = "Selecciona tipo de documento"
        self.fields['customer_gender'].empty_label = "Selecciona género"
        self.fields['customer_blood_type'].empty_label = "Selecciona tipo de sangre"
        self.fields['customer_neighborhood'].empty_label = "Selecciona un barrio"
        self.fields['customer_residence_address_select'].empty_label = "Selecciona tipo de dirección"
        self.fields['customer_marital_status'].empty_label = "Selecciona estado civil"
        self.fields['customer_health_plan'].empty_label = "Selecciona plan de salud"
        self.fields['customer_signature_option'].empty_label = "Selecciona opción de firma"
        
        # Campos requeridos
        required_fields = [
            'customer_document_type', 'customer_document_number',
            'customer_first_name', 'customer_first_surname',
            'customer_gender', 'customer_date_birth', 'customer_blood_type',
            'customer_cell_number', 'customer_neighborhood'
        ]
        
        for field_name in required_fields:
            self.fields[field_name].required = True
        
        # Campos opcionales
        optional_fields = [
            'customer_middle_name', 'customer_second_surname', 'customer_landline_number',
            'customer_email', 'customer_residence_address_select',
            'customer_residence_address_part_one', 'customer_residence_address_part_two',
            'customer_residence_address_part_three', 'customer_residence_address_supplementary_part',
            'customer_social_class', 'customer_marital_status', 'customer_occupation',
            'customer_health_plan', 'customer_children_number',
            'customer_emergency_contact_names', 'customer_emergency_contact_surnames',
            'customer_emergency_contact_number', 'customer_signature_option',
            'customer_signature_desc', 'customer_covenant'
        ]
        
        for field_name in optional_fields:
            self.fields[field_name].required = False

    def clean_customer_document_number(self):
        """Validar que el número de documento sea único"""
        document_number = self.cleaned_data.get('customer_document_number')
        
        if document_number:
            # Verificar si ya existe otro cliente con el mismo documento
            existing_customer = Customer.objects.filter(
                customer_document_number=document_number
            ).exclude(pk=self.instance.pk if self.instance else None)
            
            if existing_customer.exists():
                raise forms.ValidationError(
                    'Ya existe un cliente con este número de documento.'
                )
        
        return document_number

    def clean_customer_email(self):
        """Validar email si se proporciona"""
        email = self.cleaned_data.get('customer_email')
        
        if email:
            # Verificar si ya existe otro cliente con el mismo email
            existing_customer = Customer.objects.filter(
                customer_email=email
            ).exclude(pk=self.instance.pk if self.instance else None)
            
            if existing_customer.exists():
                raise forms.ValidationError(
                    'Ya existe un cliente con este correo electrónico.'
                )
        
        return email
    
    def save(self, commit=True):
        """Personalizar el guardado"""
        customer = super().save(commit=False)
        
        # Si customer_status no está marcado, establecerlo como True por defecto
        if customer.customer_status is None:
            customer.customer_status = True
            
        if commit:
            customer.save()
        return customer


class CampaignForm(forms.ModelForm):
    """Formulario para crear y editar campañas"""
    
    class Meta:
        model = Campaign
        fields = [
            'campaign_name',
            'campaign_type',
            'campaign_award_title',
            'campaign_award_description',
            'campaign_image',
            'campaign_start_date',
            'campaign_end_date',
            'campaign_start_time_window',
            'campaign_end_time_window',
            'campaign_monday',
            'campaign_tuesday',
            'campaign_wednesday',
            'campaign_thursday',
            'campaign_friday',
            'campaign_saturday',
            'campaign_sunday',
            'campaign_minimum_purchase_value',
            'campaign_ticket_multiplier',
            'campaign_maximum_tickets_bingo_cards_campaign',
            'campaign_maximum_tickets_bingo_cards_customer',
            'campaign_maximum_tickets_bingo_cards_invoice',
            'campaign_print_ticket',
            'campaign_ticket_title',
            'campaign_ticket_award',
            'campaign_ticket_award_description',
            'campaign_ticket_validity_date',
            'campaign_ticket_document_number',
            'campaign_ticket_names',
            'campaign_ticket_birth_day',
            'campaign_ticket_cell_number',
            'campaign_ticket_email',
            'campaign_ticket_regulatory_agency',
            'campaign_status',
        ]
        
        widgets = {
            'campaign_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la campaña'
            }),
            'campaign_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'campaign_award_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del premio'
            }),
            'campaign_award_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción detallada del premio',
                'rows': 3
            }),
            'campaign_image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'campaign_start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'campaign_end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'campaign_start_time_window': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),
            'campaign_end_time_window': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),
            'campaign_monday': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'campaign_tuesday': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'campaign_wednesday': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'campaign_thursday': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'campaign_friday': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'campaign_saturday': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'campaign_sunday': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'campaign_minimum_purchase_value': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '50000',
                'min': '0'
            }),
            'campaign_ticket_multiplier': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '1',
                'min': '1'
            }),
            'campaign_maximum_tickets_per_campaign': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sin límite (opcional)',
                'min': '1'
            }),
            'campaign_maximum_tickets_per_customer': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sin límite (opcional)',
                'min': '1'
            }),
            'campaign_maximum_tickets_per_invoice': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sin límite (opcional)',
                'min': '1'
            }),
            'campaign_print_ticket': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'campaign_ticket_title': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'campaign_ticket_award': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'campaign_ticket_award_description': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'campaign_ticket_validity_date': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'campaign_ticket_document_number': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'campaign_ticket_names': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'campaign_ticket_birth_day': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'campaign_ticket_cell_number': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'campaign_ticket_email': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'campaign_ticket_regulatory_agency': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'campaign_status': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        
        labels = {
            'campaign_name': 'Nombre de la Campaña *',
            'campaign_type': 'Tipo de Campaña',
            'campaign_award_title': 'Título del Premio',
            'campaign_award_description': 'Descripción del Premio',
            'campaign_image': 'Imagen de la Campaña',
            'campaign_start_date': 'Fecha de Inicio *',
            'campaign_end_date': 'Fecha de Fin *',
            'campaign_start_time_window': 'Hora de Inicio *',
            'campaign_end_time_window': 'Hora de Fin *',
            'campaign_monday': 'Lunes',
            'campaign_tuesday': 'Martes',
            'campaign_wednesday': 'Miércoles',
            'campaign_thursday': 'Jueves',
            'campaign_friday': 'Viernes',
            'campaign_saturday': 'Sábado',
            'campaign_sunday': 'Domingo',
            'campaign_minimum_purchase_value': 'Valor Mínimo de Compra *',
            'campaign_ticket_multiplier': 'Multiplicador de Tickets *',
            'campaign_maximum_tickets_per_campaign': 'Máximo Tickets por Campaña',
            'campaign_maximum_tickets_per_customer': 'Máximo Tickets por Cliente',
            'campaign_maximum_tickets_per_invoice': 'Máximo Tickets por Factura',
            'campaign_print_ticket': 'Permitir Impresión de Tickets',
            'campaign_ticket_title': 'Mostrar Título en Ticket',
            'campaign_ticket_award': 'Mostrar Premio en Ticket',
            'campaign_ticket_award_description': 'Mostrar Descripción del Premio',
            'campaign_ticket_validity_date': 'Mostrar Fecha de Validez',
            'campaign_ticket_document_number': 'Mostrar Número de Documento',
            'campaign_ticket_names': 'Mostrar Nombres',
            'campaign_ticket_birth_day': 'Mostrar Fecha de Nacimiento',
            'campaign_ticket_cell_number': 'Mostrar Número de Celular',
            'campaign_ticket_email': 'Mostrar Email',
            'campaign_ticket_regulatory_agency': 'Mostrar Ente Regulador',
            'campaign_status': 'Campaña Activa',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Configurar querysets
        self.fields['campaign_type'].queryset = CampaignType.objects.filter(campaign_type_status=True)
        
        # Configurar empty_label
        self.fields['campaign_type'].empty_label = "Selecciona tipo de campaña"
            
        # Campos requeridos
        self.fields['campaign_name'].required = True
        self.fields['campaign_start_date'].required = True
        self.fields['campaign_end_date'].required = True
        self.fields['campaign_start_time_window'].required = True
        self.fields['campaign_end_time_window'].required = True
        self.fields['campaign_minimum_purchase_value'].required = True
        self.fields['campaign_ticket_multiplier'].required = True
        
        # campaign_status no es requerido pero por defecto será True (activo)
        self.fields['campaign_status'].required = False

    def clean(self):
        """Validaciones personalizadas del formulario"""
        cleaned_data = super().clean()
        start_date = cleaned_data.get('campaign_start_date')
        end_date = cleaned_data.get('campaign_end_date')
        start_time = cleaned_data.get('campaign_start_time_window')
        end_time = cleaned_data.get('campaign_end_time_window')
        
        # Validar que la fecha de fin sea posterior a la de inicio
        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError(
                    'La fecha de fin debe ser posterior a la fecha de inicio.'
                )
        
        # Validar que al menos un día de la semana esté seleccionado
        days_selected = any([
            cleaned_data.get('campaign_monday'),
            cleaned_data.get('campaign_tuesday'),
            cleaned_data.get('campaign_wednesday'),
            cleaned_data.get('campaign_thursday'),
            cleaned_data.get('campaign_friday'),
            cleaned_data.get('campaign_saturday'),
            cleaned_data.get('campaign_sunday'),
        ])
        
        if not days_selected:
            raise forms.ValidationError(
                'Debe seleccionar al menos un día de la semana para la campaña.'
            )
        
        # Validar horarios
        if start_time and end_time:
            if end_time <= start_time:
                raise forms.ValidationError(
                    'La hora de fin debe ser posterior a la hora de inicio.'
                )
        
        return cleaned_data
    
    def save(self, commit=True):
        """Personalizar el guardado"""
        campaign = super().save(commit=False)
        
        # Si campaign_status no está marcado, establecerlo como True por defecto
        if campaign.campaign_status is None:
            campaign.campaign_status = True
            
        if commit:
            campaign.save()
        return campaign


class CustomerSearchForm(forms.Form):
    """Formulario para buscar cliente por cédula"""
    customer_document_number = forms.CharField(
        label='Número de Documento',
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el número de documento',
            'autofocus': True,
        }),
        help_text='Ingrese el número de documento del cliente para verificar si está registrado'
    )


class InvoiceForm(forms.ModelForm):
    """Formulario para registrar facturas"""
    
    campaign = forms.ModelChoiceField(
        queryset=Campaign.objects.filter(campaign_status=True, campaign_end_date__gte=date.today()),
        empty_label="Selecciona una campaña",
        widget=forms.Select(attrs={
            'class': 'form-select',
            'required': True,
        }),
        label="Campaña",
        help_text="Campaña a la que pertenece la factura",
    )
    
    class Meta:
        model = Invoice
        fields = [
            'invoice_number',
            'invoice_purchase_date',
            'invoice_customer',
            'invoice_purchase_value',
            'invoice_payment_method',
            'invoice_commercial_premise',
        ]
        
        widgets = {
            'invoice_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de factura',
                'required': True,
            }),
            'invoice_purchase_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True,
            }),
            'invoice_customer': forms.HiddenInput(),
            'invoice_purchase_value': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
                'min': '1',
                'step': '1',
                'required': True,
            }),
            'invoice_payment_method': forms.Select(attrs={
                'class': 'form-select',
            }),
            'invoice_commercial_premise': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
        
        labels = {
            'invoice_number': 'Número de Factura',
            'invoice_purchase_date': 'Fecha de Compra',
            'invoice_customer': 'Cliente',
            'invoice_purchase_value': 'Valor de Compra',
            'invoice_payment_method': 'Método de Pago',
            'invoice_commercial_premise': 'Local Comercial',
        }
        
        help_texts = {
            'invoice_number': 'Número único de la factura',
            'invoice_purchase_value': 'Valor total de la compra',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Filtrar solo métodos de pago activos
        self.fields['invoice_payment_method'].queryset = PaymentMethod.objects.filter(
            payment_method_status=True
        ).order_by('payment_method_name')
        
        # Filtrar solo locales comerciales activos
        self.fields['invoice_commercial_premise'].queryset = CommercialPremise.objects.filter(
            commercial_premise_status=True
        ).order_by('commercial_premise_name')

    def clean(self):
        cleaned_data = super().clean()
        purchase_value = cleaned_data.get('invoice_purchase_value', 0)
        
        # Validar que el valor de compra sea positivo
        if purchase_value <= 0:
            raise forms.ValidationError(
                'El valor de la compra debe ser mayor a cero.'
            )
        
        return cleaned_data


class InvoiceForEachCampaignForm(forms.ModelForm):
    """Formulario para registrar facturas por campaña"""
    
    class Meta:
        model = InvoiceForEachCampaign
        fields = [
            'invoice_for_each_campaign_campaign',
            'invoice_for_each_campaign_invoice',
        ]
        
        widgets = {
            'invoice_for_each_campaign_campaign': forms.Select(attrs={
                'class': 'form-select',
                'required': True,
            }),
            'invoice_for_each_campaign_invoice': forms.HiddenInput(),
        }
        
        labels = {
            'invoice_for_each_campaign_campaign': 'Campaña',
            'invoice_for_each_campaign_invoice': 'Factura',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Filtrar solo campañas activas
        self.fields['invoice_for_each_campaign_campaign'].queryset = Campaign.objects.filter(
            campaign_status=True
        ).order_by('campaign_name')