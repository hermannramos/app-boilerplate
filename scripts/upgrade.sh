#!/bin/bash

# Realiza nuevas migraciones
echo "Creando nuevas migraciones..."
pipenv run python manage.py makemigrations || { echo "Error al crear nuevas migraciones"; exit 1; }

# Aplica las migraciones
echo "Aplicando migraciones..."
pipenv run python manage.py migrate || { echo "Error al aplicar migraciones"; exit 1; }

echo "Migraciones actualizadas correctamente."