from django.core.management.base import BaseCommand
from apps.crm.models import PaymentMethod, CommercialStore, City


class Command(BaseCommand):
    help = 'Crea datos de ejemplo para métodos de pago y locales comerciales'

    def handle(self, *args, **options):
        self.stdout.write('Creando datos de ejemplo...')
        
        # Crear métodos de pago
        payment_methods = [
            {
                'payment_method_name': 'Efectivo',
                'payment_method_description': 'Pago en efectivo'
            },
            {
                'payment_method_name': 'Tarjeta de Crédito',
                'payment_method_description': 'Pago con tarjeta de crédito'
            },
            {
                'payment_method_name': 'Tarjeta de Débito',
                'payment_method_description': 'Pago con tarjeta de débito'
            },
            {
                'payment_method_name': 'Transferencia Bancaria',
                'payment_method_description': 'Transferencia electrónica'
            },
            {
                'payment_method_name': 'PSE',
                'payment_method_description': 'Pago Seguro en Línea'
            },
            {
                'payment_method_name': 'Nequi',
                'payment_method_description': 'Pago con billetera digital Nequi'
            },
            {
                'payment_method_name': 'Daviplata',
                'payment_method_description': 'Pago con billetera digital Daviplata'
            }
        ]
        
        for method_data in payment_methods:
            payment_method, created = PaymentMethod.objects.get_or_create(
                payment_method_name=method_data['payment_method_name'],
                defaults=method_data
            )
            if created:
                self.stdout.write(f'✓ Método de pago creado: {payment_method.payment_method_name}')
            else:
                self.stdout.write(f'- Método de pago ya existe: {payment_method.payment_method_name}')
        
        # Obtener alguna ciudad para los locales
        try:
            city = City.objects.first()
        except:
            city = None
            self.stdout.write(self.style.WARNING('No hay ciudades disponibles para asignar a los locales'))
        
        # Crear locales comerciales
        stores = [
            {
                'store_code': 'CC001',
                'store_name': 'Centro Comercial Santafé',
                'store_address': 'Calle 185 # 45-03',
                'store_city': city,
                'store_phone': '+57 1 123 4567',
                'store_manager': 'Ana García'
            },
            {
                'store_code': 'CC002',
                'store_name': 'Centro Comercial Andino',
                'store_address': 'Carrera 11 # 82-71',
                'store_city': city,
                'store_phone': '+57 1 234 5678',
                'store_manager': 'Carlos Rodríguez'
            },
            {
                'store_code': 'CC003',
                'store_name': 'Centro Comercial Unicentro',
                'store_address': 'Carrera 15 # 123-30',
                'store_city': city,
                'store_phone': '+57 1 345 6789',
                'store_manager': 'María López'
            },
            {
                'store_code': 'LOC001',
                'store_name': 'Local Zona Rosa',
                'store_address': 'Carrera 13 # 85-32',
                'store_city': city,
                'store_phone': '+57 1 456 7890',
                'store_manager': 'Pedro Martínez'
            },
            {
                'store_code': 'LOC002',
                'store_name': 'Local Centro Histórico',
                'store_address': 'Calle 11 # 4-21',
                'store_city': city,
                'store_phone': '+57 1 567 8901',
                'store_manager': 'Laura Sánchez'
            }
        ]
        
        for store_data in stores:
            store, created = CommercialStore.objects.get_or_create(
                store_code=store_data['store_code'],
                defaults=store_data
            )
            if created:
                self.stdout.write(f'✓ Local comercial creado: {store.store_name}')
            else:
                self.stdout.write(f'- Local comercial ya existe: {store.store_name}')
        
        self.stdout.write(self.style.SUCCESS('¡Datos de ejemplo creados exitosamente!'))
        self.stdout.write(f'Métodos de pago: {PaymentMethod.objects.count()}')
        self.stdout.write(f'Locales comerciales: {CommercialStore.objects.count()}')