# settings/production.py
import dj_database_url
from .base import *
from decouple import config

# ─── MODO DEPURACIÓN ────────────────────────────────────────

# OBLIGATORIO: False en producción
# Con DEBUG=True en producción se exponen rutas internas, errores
# detallados y configuración del proyecto a cualquier visitante
DEBUG = False

# ─── HOSTS PERMITIDOS ───────────────────────────────────────

# Solo acepta peticiones desde estos dominios
# Coma separados, sin espacios
ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    cast=lambda v: [s.strip() for s in v.split(',')]
)
# Ejemplo de valor en Render:
# ALLOWED_HOSTS = cuatro-patas.onrender.com,cuatropatas.cl,www.cuatropatas.cl

# ─── BASE DE DATOS ──────────────────────────────────────────

# Lee la URL de conexión desde la variable de entorno DATABASE_URL
# La convierte al formato que Django entiende
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}
# conn_max_age=600 → mantiene la conexión abierta hasta 10 minutos
# (evita reconectarse a Supabase en cada petición)

# ─── EMAIL ──────────────────────────────────────────────────

# En producción se usa un servidor SMTP real (ej: Gmail, SendGrid)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')

# ─── SEGURIDAD HTTPS ────────────────────────────────────────

# Redirige todas las peticiones HTTP a HTTPS automáticamente
# (el usuario escribe http:// → el servidor responde con 301 a https://)
SECURE_SSL_REDIRECT = True

# Le dice a Django que confíe en el header HTTP_X_FORWARDED_PROTO
# Render y Cloudflare actúan como proxies: Django recibe HTTP internamente,
# pero el usuario real llega por HTTPS. Este header le dice a Django
# que la conexión con el usuario SÍ es HTTPS.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ─── HSTS (HTTP Strict Transport Security) ─────────────────

# Le indica al navegador que SIEMPRE use HTTPS para este dominio
# durante los próximos N segundos (incluso si el usuario escribe http://)
SECURE_HSTS_SECONDS = 31536000          # 1 año = 365 * 24 * 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True   # aplica también a subdominos (www, api, etc.)
SECURE_HSTS_PRELOAD = True              # permite registrar el dominio en lista HSTS global

# ⚠️ CUIDADO: una vez activo HSTS, si remueves HTTPS el sitio se vuelve
# inaccesible durante SECURE_HSTS_SECONDS segundos. Activarlo solo cuando
# HTTPS esté completamente configurado y funcionando.

# ─── COOKIES SEGURAS ────────────────────────────────────────

# La cookie de sesión solo se envía por HTTPS (nunca por HTTP sin cifrar)
SESSION_COOKIE_SECURE = True

# La cookie del token CSRF solo se envía por HTTPS
CSRF_COOKIE_SECURE = True

# La cookie de sesión no es accesible desde JavaScript del navegador
# (previene ataques XSS que intenten robar la sesión)
SESSION_COOKIE_HTTPONLY = True

# Tiempo máximo de sesión (en segundos)
SESSION_COOKIE_AGE = 3600  # 1 hora

# Expirar la sesión cuando el usuario cierra el navegador
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # False = la sesión dura SESSION_COOKIE_AGE

# ─── PROTECCIÓN XSS Y CLICKJACKING ─────────────────────────

# Envía el header X-Content-Type-Options: nosniff
# Impide que el navegador "adivine" el tipo de contenido y ejecute
# scripts disfrazados de imágenes u otros archivos
SECURE_CONTENT_TYPE_NOSNIFF = True

# Activa el filtro XSS del navegador (para navegadores antiguos)
SECURE_BROWSER_XSS_FILTER = True

# ─── LOGGING EN PRODUCCIÓN ─────────────────────────────────

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',  # solo mostrar WARNING y ERROR en producción
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}