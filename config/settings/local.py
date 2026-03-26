# settings/local.py
from .base import *

# ─── MODO DEPURACIÓN ────────────────────────────────────────

DEBUG = True

# Acepta cualquier host en desarrollo (más cómodo)
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# ─── BASE DE DATOS ──────────────────────────────────────────

# SQLite local — simple, sin configurar nada extra
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ─── EMAIL ──────────────────────────────────────────────────

# En desarrollo, los emails se imprimen en la consola en vez de enviarse
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ─── SEGURIDAD RELAJADA (solo desarrollo) ───────────────────

# En local NO usamos HTTPS, así que desactivamos algunas protecciones
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False