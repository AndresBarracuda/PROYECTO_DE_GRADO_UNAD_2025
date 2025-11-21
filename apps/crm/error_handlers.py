from django.shortcuts import render
from django.http import HttpResponseForbidden

def permission_denied_view(request, exception):
    """
    Vista personalizada para errores 403 (Forbidden)
    """
    context = {
        'exception': exception,
        'request_path': request.path,
    }
    
    response = render(request, 'registration/access_denied.html', context)
    response.status_code = 403
    return response