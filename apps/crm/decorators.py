from functools import wraps
from django.contrib.auth.decorators import login_required as django_login_required
from django.contrib.auth.mixins import LoginRequiredMixin as DjangoLoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

def add_no_cache_headers(response):
    """Agregar headers para prevenir cache"""
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate, private'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    response['Last-Modified'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
    return response

def login_required(function=None, login_url=None, redirect_field_name='next'):
    """
    Decorador personalizado para requerir login con mensajes mejorados y headers de seguridad
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.warning(request, 'Debes iniciar sesión para acceder a esta página.')
                response = redirect(login_url or '/login/')
                return add_no_cache_headers(response)
            
            response = view_func(request, *args, **kwargs)
            return add_no_cache_headers(response)
        return _wrapped_view
    
    if function:
        return decorator(function)
    return decorator


def staff_required(function=None, login_url=None):
    """
    Decorador que requiere que el usuario sea staff
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.warning(request, 'Debes iniciar sesión para acceder a esta página.')
                response = redirect(login_url or '/login/')
                return add_no_cache_headers(response)
            
            if not request.user.is_staff:
                messages.error(request, 'No tienes permisos para acceder a esta página.')
                raise PermissionDenied("Acceso denegado - Se requieren permisos de staff")
            
            response = view_func(request, *args, **kwargs)
            return add_no_cache_headers(response)
        return _wrapped_view
    
    if function:
        return decorator(function)
    return decorator


def superuser_required(function=None, login_url=None):
    """
    Decorador que requiere que el usuario sea superusuario
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.warning(request, 'Debes iniciar sesión para acceder a esta página.')
                response = redirect(login_url or '/login/')
                return add_no_cache_headers(response)
            
            if not request.user.is_superuser:
                messages.error(request, 'No tienes permisos de administrador para acceder a esta página.')
                raise PermissionDenied("Acceso denegado - Se requieren permisos de superusuario")
            
            response = view_func(request, *args, **kwargs)
            return add_no_cache_headers(response)
        return _wrapped_view
    
    if function:
        return decorator(function)
    return decorator


class LoginRequiredMixin(DjangoLoginRequiredMixin):
    """
    Mixin personalizado para vistas basadas en clases que requieren login
    """
    login_url = '/login/'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'Debes iniciar sesión para acceder a esta página.')
        return super().dispatch(request, *args, **kwargs)


class StaffRequiredMixin(LoginRequiredMixin):
    """
    Mixin que requiere que el usuario sea staff
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'Debes iniciar sesión para acceder a esta página.')
            return redirect(self.login_url)
        
        if not request.user.is_staff:
            messages.error(request, 'No tienes permisos para acceder a esta página.')
            raise PermissionDenied("Acceso denegado - Se requieren permisos de staff")
        
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class SuperuserRequiredMixin(LoginRequiredMixin):
    """
    Mixin que requiere que el usuario sea superusuario
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'Debes iniciar sesión para acceder a esta página.')
            return redirect(self.login_url)
        
        if not request.user.is_superuser:
            messages.error(request, 'No tienes permisos de administrador para acceder a esta página.')
            raise PermissionDenied("Acceso denegado - Se requieren permisos de superusuario")
        
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


def permission_required_custom(permission, login_url=None, raise_exception=False):
    """
    Decorador personalizado para verificar permisos específicos
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.warning(request, 'Debes iniciar sesión para acceder a esta página.')
                return redirect(login_url or '/login/')
            
            if not request.user.has_perm(permission):
                message = f'No tienes el permiso "{permission}" para acceder a esta página.'
                if raise_exception:
                    raise PermissionDenied(message)
                else:
                    messages.error(request, message)
                    return redirect('crm:index')
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    
    return decorator


def admin_group_required(view_func):
    """
    Decorador para requerir pertenencia al grupo 'Admin'
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'Debes iniciar sesión para acceder a esta página.')
            response = redirect('/login/')
            return add_no_cache_headers(response)
        
        try:
            admin_group = Group.objects.get(name='Admin')
            if admin_group not in request.user.groups.all():
                messages.error(request, 'No tienes permisos de administrador para acceder a esta página.')
                response = redirect('crm:index')
                return add_no_cache_headers(response)
        except Group.DoesNotExist:
            messages.error(request, 'El grupo Admin no existe en el sistema.')
            response = redirect('crm:index')
            return add_no_cache_headers(response)
        
        response = view_func(request, *args, **kwargs)
        return add_no_cache_headers(response)
    return _wrapped_view


def admin_or_operator_required(view_func):
    """
    Decorador para requerir pertenencia al grupo 'Admin' o 'operator'
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'Debes iniciar sesión para acceder a esta página.')
            response = redirect('/login/')
            return add_no_cache_headers(response)
        
        user_groups = request.user.groups.values_list('name', flat=True)
        allowed_groups = ['Admin', 'operator']
        
        if not any(group in user_groups for group in allowed_groups):
            messages.error(request, 'No tienes permisos para acceder a esta página. Se requiere ser Admin o Operator.')
            response = redirect('crm:index')
            return add_no_cache_headers(response)
        
        response = view_func(request, *args, **kwargs)
        return add_no_cache_headers(response)
    return _wrapped_view