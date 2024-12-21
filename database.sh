#!/bin/bash

# Verifica si las variables necesarias están configuradas
check_env_variables() {
  if [ -z "$POSTGRES_DB" ] || [ -z "$POSTGRES_USER" ] || [ -z "$POSTGRES_PASSWORD" ]; then
    echo "Faltan variables de entorno necesarias: POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD"
    exit 1
  fi
}

# Espera a que PostgreSQL esté disponible
wait_for_postgres() {
  echo "Esperando a que PostgreSQL esté disponible..."
  until PGPASSWORD="$POSTGRES_PASSWORD" psql -h db -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "SELECT 1" >/dev/null 2>&1; do
    sleep 3
  done
  echo "PostgreSQL está disponible."
}

# Espera a que Django pueda conectarse a la base de datos
wait_for_django_connection() {
  echo "Esperando a que Django pueda conectarse a la base de datos..."
  until pipenv run python manage.py migrate --plan >/dev/null 2>&1; do
    sleep 3
  done
  echo "La conexión con la base de datos está lista."
}

# Maneja las migraciones de Django
run_migrations() {
  echo "Aplicando migraciones"
  pipenv run migrate
}

# Actualiza el esquema de la base de datos
# Ejecuta upgrade (combina makemigrations + migrate)
upgrade_database() {
  echo "Actualizando la base de datos..."
  pipenv run upgrade
}

# Resetea la base de datos
reset_database() {
  echo "Reseteando la base de datos"
  pipenv run reset_db
}

# Inicia el servidor de desarrollo de Django
start_server() {
  echo "Iniciando el servidor Django en http://0.0.0.0:8000"
  pipenv run start
}

# Crear un superusuario automáticamente
create_superuser() {
  echo "Creando superusuario..."
  pipenv run python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'password')
else:
    print('El superusuario ya existe.')
  " || {
    echo "Error al crear el superusuario."
    exit 1
  }
}

# Ejecución de las funciones
check_env_variables
wait_for_postgres
wait_for_django_connection
run_migrations
upgrade_database
create_superuser
start_server