#!/bin/bash

echo "Iniciando configuración de PostgreSQL..."

# Crear usuario
psql -U postgres -c "DO \$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'user') THEN
      CREATE ROLE user LOGIN PASSWORD 'password';
   END IF;
END
\$$;"

# Crear base de datos
psql -U postgres -c "DO \$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'app_db') THEN
      CREATE DATABASE app_db OWNER user;
   END IF;
END
\$$;"

echo "Configuración completa."
