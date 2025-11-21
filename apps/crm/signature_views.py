from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Customer
import json
import os
from django.conf import settings

@login_required
def get_customer_signature(request, customer_id):
    """Obtener la firma de un cliente específico"""
    try:
        customer = Customer.objects.get(customer_id=customer_id)
        
        # Buscar archivo de firma
        signatures_dir = os.path.join(settings.MEDIA_ROOT, 'signatures')
        
        for filename in os.listdir(signatures_dir):
            if filename.startswith(f"signature_{customer.customer_document_number}_"):
                signature_path = os.path.join(signatures_dir, filename)
                
                with open(signature_path, 'r', encoding='utf-8') as f:
                    signature_data = json.load(f)
                
                return JsonResponse({
                    'success': True,
                    'signature': signature_data,
                    'filename': filename
                })
        
        return JsonResponse({
            'success': False,
            'message': 'No se encontró firma para este cliente'
        })
        
    except Customer.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Cliente no encontrado'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error al obtener la firma: {str(e)}'
        })

@login_required 
def view_signature_image(request, customer_id):
    """Ver la imagen de la firma de un cliente"""
    try:
        customer = Customer.objects.get(customer_id=customer_id)
        
        # Buscar archivo de firma
        signatures_dir = os.path.join(settings.MEDIA_ROOT, 'signatures')
        
        for filename in os.listdir(signatures_dir):
            if filename.startswith(f"signature_{customer.customer_document_number}_"):
                signature_path = os.path.join(signatures_dir, filename)
                
                with open(signature_path, 'r', encoding='utf-8') as f:
                    signature_data = json.load(f)
                
                if 'imageData' in signature_data:
                    # Extraer los datos de la imagen base64
                    image_data = signature_data['imageData']
                    
                    # Remover el prefijo 'data:image/png;base64,'
                    if image_data.startswith('data:image/png;base64,'):
                        image_data = image_data.replace('data:image/png;base64,', '')
                    
                    import base64
                    image_bytes = base64.b64decode(image_data)
                    
                    response = HttpResponse(image_bytes, content_type='image/png')
                    response['Content-Disposition'] = f'inline; filename="firma_{customer.customer_document_number}.png"'
                    return response
        
        raise Http404("Firma no encontrada")
        
    except Customer.DoesNotExist:
        raise Http404("Cliente no encontrado")
    except Exception as e:
        raise Http404(f"Error al cargar la firma: {str(e)}")