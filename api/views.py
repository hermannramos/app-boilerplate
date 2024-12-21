from django.http import JsonResponse, HttpResponse
from api.utils import generate_sitemap, json_response
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
from django.http import JsonResponse
from api.models import User
import json


@ensure_csrf_cookie
def csrf_token_view(request):
    """Devuelve el token CSRF para configurarlo en el cliente."""
    csrf_token = get_token(request)
    return JsonResponse({"csrfToken": csrf_token})

def root_view(request):
    """Endpoint principal para verificar si el servidor está en ejecución."""
    return json_response({
        "status": "running",
        "message": "Backend Boilerplate API is up and running."
    })

def hello_world(request):
    """Endpoint de prueba para devolver un mensaje de saludo."""
    return json_response({"message": "¡Hola, mundo!"})


def sitemap_view(request):
    """Genera un sitemap en formato HTML."""
    return HttpResponse(generate_sitemap(), content_type="text/html")


def create_user(request):
    """Endpoint para crear un usuario."""
    if request.method == "POST":
        try:
            # Parsear el cuerpo de la solicitud
            body = json.loads(request.body)

            # Validar los campos obligatorios
            required_fields = ["name", "email", "password"]
            for field in required_fields:
                if field not in body:
                    return JsonResponse({"success": False, "error": f"'{field}' es obligatorio."}, status=400)

            # Crear el usuario en la base de datos
            user = User.objects.create(
                name=body["name"],
                email=body["email"],
                password=body["password"],  # Se debe encriptar para producción
                description=body.get("description", ""),
                price=body.get("price", 0.0),
                is_active=body.get("is_active", True),
            )

            return JsonResponse({"success": True, "user": user.serialize()}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Método no permitido."}, status=405)