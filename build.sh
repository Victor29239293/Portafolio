#!/usr/bin/env bash
# exit on error
set -o errexit

# instalar dependencias
pip install -r requirements.txt

# recolectar archivos estáticos
python manage.py collectstatic --no-input

# aplicar migraciones
python manage.py migrate
