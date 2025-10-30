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
# CONFIGURACIÓN BÁSICA
# ===========================
DEBUG = True  # Cambiar a False en producción
ALLOWED_HOSTS = ["nsl-5vec.onrender.com"]
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

ROOT_URLCONF = 'nsl_kdd_project.urls'

# ===========================
# TEMPLATES
# ===========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Carpeta global de templates
        'APP_DIRS': True,  # Detecta templates dentro de apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'nsl_kdd_project.wsgi.application'

# ===========================
# BASE DE DATOS
# ===========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Archivo SQLite
    }
}

# ===========================
# VALIDACIÓN DE CONTRASEÑAS
# ===========================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
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
# ARFF FILES
# ===========================
# Carpeta relativa dentro del proyecto para tus archivos ARFF
ARFF_FILES_DIR = BASE_DIR / "datasets" / "NSL-KDD"
SECRET_KEY = 'xKUg2Ng0C9KOL9lR5BSeaovzJpsUsUro7FhnQT6C3hwV14-Cf63WA0nAqIEuSs2VbBE'
