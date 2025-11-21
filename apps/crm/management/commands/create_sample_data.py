from django.core.management.base import BaseCommand
from apps.crm.models import PaymentMethod, CommercialPremise


class Command(BaseCommand):
    help = 'Crea datos de prueba para el sistema'

    def handle(self, *args, **options):
        # Crear métodos de pago de prueba
        payment_methods = [
            {'name': 'Efectivo'},
            {'name': 'Tarjeta de Crédito'},
            {'name': 'Tarjeta de Débito'},
            {'name': 'Transferencia Bancaria'},
            {'name': 'PayPal'},
        ]
        
        for pm_data in payment_methods:
            payment_method, created = PaymentMethod.objects.get_or_create(
                payment_method_name=pm_data['name'],
                defaults={
                    'payment_method_status': True,
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Método de pago creado: {payment_method.payment_method_name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Método de pago ya existe: {payment_method.payment_method_name}')
                )
        
        # Crear locales comerciales de prueba si el modelo existe
        try:
            commercial_premises = [
                {
                    'name': 'Local Centro',
                    'address': 'Calle 10 # 15-20',
                    'manager': 'Ana García'
                },
                {
                    'name': 'Local Norte',
                    'address': 'Carrera 20 # 45-30',
                    'manager': 'Carlos Pérez'
                },
                {
                    'name': 'Local Sur',
                    'address': 'Avenida 30 # 25-15',
                    'manager': 'María López'
                },
            ]
            
            for cp_data in commercial_premises:
                commercial_premise, created = CommercialPremise.objects.get_or_create(
                    commercial_premise_name=cp_data['name'],
                    defaults={
                        'commercial_premise_address': cp_data['address'],
                        'commercial_premise_manager': cp_data['manager'],
                        'commercial_premise_status': True,
                    }
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f'Local comercial creado: {commercial_premise.commercial_premise_name}')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'Local comercial ya existe: {commercial_premise.commercial_premise_name}')
                    )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creando locales comerciales: {str(e)}')
            )

        self.stdout.write(
            self.style.SUCCESS('Datos de prueba creados exitosamente!')
        )