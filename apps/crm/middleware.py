from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect

class NoCacheMiddleware(MiddlewareMixin):
    """
    Middleware para prevenir el cache de páginas que requieren autenticación
    """
    
    def process_response(self, request, response):
        # Lista de URLs que requieren no-cache
        protected_urls = [
            '/dashboard/',
            '/customers/',
            '/admin/',
        ]
        
        # Verificar si la URL actual requiere protección
        path = request.path
        is_protected = any(path.startswith(url) for url in protected_urls)
        
        # También proteger si el usuario está autenticado
        if request.user.is_authenticated or is_protected:
            # Headers para prevenir cache
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate, private'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
            response['Last-Modified'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
            
            # Headers adicionales de seguridad
            response['X-Content-Type-Options'] = 'nosniff'
            response['X-Frame-Options'] = 'DENY'
            response['X-XSS-Protection'] = '1; mode=block'
        
        return response


class AuthenticationCheckMiddleware(MiddlewareMixin):
    """
    Middleware para verificar autenticación en cada request
    """
    
    def process_request(self, request):
        # URLs que no requieren autenticación
        public_urls = [
            '/',
            '/login/',
            '/logout/',
            '/password_reset/',
            '/static/',
            '/media/',
            '/admin/login/',
        ]
        
        # Verificar si la URL es pública
        path = request.path
        is_public = any(path.startswith(url) for url in public_urls)
        
        # Si no es pública y el usuario no está autenticado
        if not is_public and not request.user.is_authenticated:
            # Si es una petición AJAX, devolver respuesta JSON
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return HttpResponse(
                    '{"error": "Authentication required", "redirect": "/login/"}', 
                    content_type='application/json',
                    status=401
                )
            
            # Para requests normales, redirigir al login
            return redirect('login')
        
        return None