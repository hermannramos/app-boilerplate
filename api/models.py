from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)  # Campo de texto con límite de caracteres
    description = models.TextField(blank=True, null=True)  # Campo de texto largo opcional
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Campo numérico con decimales
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última actualización
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=80, null=False, blank=False)
    is_active = models.BooleanField(default=True, null=False, blank=False)

# Null=False asegura que el campo no sea NULL en la base de datos.
# Blank=False obliga a que este campo se rellene en los formularios de Django.

    def __str__(self):
        return self.name  # Representación legible del modelo
    
    def serialize(self):
        """Método para serializar los datos del usuario"""
        return {
            "id": self.id,
            "email": self.email,
            # No se incluye la contraseña por razones de seguridad
        }