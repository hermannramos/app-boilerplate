# Imagen base de Python con soporte para Node.js (Django + React)
FROM mcr.microsoft.com/devcontainers/python:0-3.11

# Configuración de entorno
ENV PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

# Instala Node.js y npm
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends \
    nodejs \
    npm \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Instala dependencias de PostgreSQL
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends \
    postgresql-client \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Instala psycopg2 para conectar Django con PostgreSQL
RUN pip install psycopg2-binary

# Copia los archivos necesarios
COPY . .