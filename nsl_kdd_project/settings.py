"""
Django settings for nsl_kdd_project project.
"""

import os
from pathlib import Path

# ===========================
# RUTAS BASE
# ===========================
BASE_DIR = Path(__file__).resolve().parent.parent

# ===========================
# SECRET_KEY y DEBUG
# ===========================
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "clave_por_defecto_para_desarrollo"
)

DEBUG = os.environ.get("DJANGO_DEBUG", "False") == "True"

# ===========================
# ALLOWED_HOSTS
# ===========================
# Permite múltiples hosts separados por coma
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost").split(",")

# ===========================
# APPS INSTALADAS
# ===========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',  # Tu app principal
]

# ===========================
# MIDDLEWARE
# ===========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ===========================
# URLS Y WSGI
# ===========================
ROOT_URLCONF = 'nsl_kdd_project.urls'
WSGI_APPLICATION = 'nsl_kdd_project.wsgi.application'

# ===========================
# TEMPLATES
# ===========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ]},
    },
]

# ===========================
# BASE DE DATOS
# ===========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Para producción recomendable usar Postgres
    }
}

# ===========================
# VALIDACIÓN DE CONTRASEÑAS
# ===========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ===========================
# CONFIGURACIÓN DE IDIOMA Y ZONA HORARIA
# ===========================
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

# ===========================
# ARCHIVOS ESTÁTICOS
# ===========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # Carpeta para desarrollo
STATIC_ROOT = BASE_DIR / "staticfiles"    # Carpeta para collectstatic en producción

# ===========================
# MEDIA
# ===========================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# ===========================
# CARPETA PARA ARFF FILES
# ===========================
ARFF_FILES_DIR = BASE_DIR / "datasets" / "NSL-KDD"
