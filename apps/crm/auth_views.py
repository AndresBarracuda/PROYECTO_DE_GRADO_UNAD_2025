from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomLoginView(TemplateView):
    """Vista personalizada para el login"""
    template_name = 'registration/login.html'
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('crm:index')
        
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido de nuevo, {user.first_name or user.username}!')
                
                # Redirigir a la página solicitada o al dashboard
                next_page = request.GET.get('next', 'crm:index')
                return redirect(next_page)
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
        
        return render(request, self.template_name, {'form': form})


def custom_login_view(request):
    """Vista de función para login - para compatibilidad con URLs"""
    view = CustomLoginView.as_view()
    return view(request)


def custom_logout_view(request):
    """Vista personalizada para el logout"""
    if request.user.is_authenticated:
        username = request.user.username
        
        # Limpiar la sesión completamente
        request.session.flush()
        
        # Logout del usuario
        logout(request)
        
        messages.success(request, f'Has cerrado sesión exitosamente. ¡Hasta pronto, {username}!')
    
    # Crear respuesta con headers para prevenir cache
    response = redirect('login')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate, private'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    
    return response


class AccessDeniedView(TemplateView):
    """Vista para mostrar cuando el acceso es denegado"""
    template_name = 'registration/access_denied.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Acceso Denegado'
        return context