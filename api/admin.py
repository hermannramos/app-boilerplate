import os
from django.contrib import admin
from .models import User  # Ajusta este import a los modelos que tengas en tu proyecto

# Personalización del sitio de administración
admin.site.site_header = "Backend Boilerplate Admin"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Bienvenido al Administrador"

# Registro de modelos
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Columnas visibles en la lista de objetos
    list_display = ('name', 'email', 'created_at')
    
    # Campos para búsqueda rápida
    search_fields = ('name', 'email')
    
    # Filtros laterales en la interfaz del admin
    list_filter = ('created_at',)
    
    # Campos que se muestran en la vista de edición
    fields = ('name', 'email', 'is_active', 'created_at', 'updated_at')
    
    # Campos solo de lectura
    readonly_fields = ('created_at', 'updated_at')