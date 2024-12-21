from django.http import JsonResponse
from django.urls import get_resolver, reverse
import json

def load_json_file(filepath: str) -> dict:
    """Carga un archivo JSON desde el disco."""
    with open(filepath, 'r') as file:
        return json.load(file)

def json_response(data: dict, status: int = 200) -> JsonResponse:
    """Devuelve una respuesta JSON con un formato consistente."""
    return JsonResponse({"success": True, "data": data}, status=status)


class APIException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        super().__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


def api_exception_handler(exception, context):
    """Handler global para APIException en Django."""
    if isinstance(exception, APIException):
        response_data = exception.to_dict()
        return JsonResponse(response_data, status=exception.status_code)
    return None

def generate_sitemap():
    """Genera un sitemap básico de todas las rutas disponibles."""
    urls = []
    resolver = get_resolver()

    for route in resolver.url_patterns:
        try:
            url_name = route.name
            if url_name:
                url = reverse(url_name)
                urls.append(url)
        except Exception:
            continue  # Ignora rutas que no se pueden resolver

    links_html = "".join([f'<li><a href="{link}" target="_blank">{link}</a></li>' for link in urls])
    return """
        <div style="text-align: center;">
            <h1>Welcome to your Django API!</h1>
            <p>Below are the available endpoints:</p>
            <ul style="text-align: left;">
                """ + links_html + """
            </ul>
        </div>
    """