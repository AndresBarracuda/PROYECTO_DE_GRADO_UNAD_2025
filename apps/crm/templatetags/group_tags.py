from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter
def has_group(user, group_name):
    """
    Verifica si un usuario pertenece a un grupo específico
    Uso en template: {% if user|has_group:"Admin" %}
    """
    if not user.is_authenticated:
        return False
    
    try:
        group = Group.objects.get(name=group_name)
        return group in user.groups.all()
    except Group.DoesNotExist:
        return False

@register.filter
def has_any_group(user, group_names):
    """
    Verifica si un usuario pertenece a cualquiera de los grupos especificados
    Uso en template: {% if user|has_any_group:"Admin,Operators" %}
    """
    if not user.is_authenticated:
        return False
    
    group_list = [name.strip() for name in group_names.split(',')]
    user_groups = user.groups.values_list('name', flat=True)
    
    return any(group_name in user_groups for group_name in group_list)

@register.simple_tag
def user_in_group(user, group_name):
    """
    Tag simple para verificar pertenencia a grupo
    Uso en template: {% user_in_group user "Admin" as is_admin %}
    """
    if not user.is_authenticated:
        return False
    
    try:
        group = Group.objects.get(name=group_name)
        return group in user.groups.all()
    except Group.DoesNotExist:
        return False

@register.simple_tag
def user_in_any_group(user, *group_names):
    """
    Tag simple para verificar pertenencia a cualquier grupo
    Uso en template: {% user_in_any_group user "Admin" "Operators" as has_permissions %}
    """
    if not user.is_authenticated:
        return False
    
    user_groups = user.groups.values_list('name', flat=True)
    return any(group_name in user_groups for group_name in group_names)