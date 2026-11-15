"""
Django settings for the Keshtyar portal.

Every deploy-specific value is read from environment variables (or a local
.env file). See .env.example for the full list.
"""

import os
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env', override=False)


def env_bool(name, default=False):
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.strip().lower() in {'1', 'true', 'yes', 'on'}


def env_int(name, default):
    raw = os.environ.get(name, '').strip()
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        raise ImproperlyConfigured(f'{name} must be a whole number, got {raw!r}.') from None


def env_csv(name, default=''):
    return [item.strip() for item in os.environ.get(name, default).split(',') if item.strip()]


def with_scheme(origin):
    # Django requires a scheme here; a bare domain used to be dropped silently.
    return origin if origin.startswith(('http://', 'https://')) else f'https://{origin}'


# Core

SECRET_KEY = (
    os.environ.get('SECRET_KEY')
    or os.environ.get('DJANGO_SECRET_KEY')
    or ''
).strip().strip('\'"')
if not SECRET_KEY:
    raise ImproperlyConfigured(
        'SECRET_KEY is missing. Set it in .env for local work, or in the PaaS environment for production.'
    )

DEBUG = env_bool('DEBUG', default=False)

ALLOWED_HOSTS = env_csv('ALLOWED_HOSTS', '127.0.0.1,localhost,.liara.run,.liara.ir')
CSRF_TRUSTED_ORIGINS = [
    with_scheme(origin)
    for origin in env_csv('CSRF_TRUSTED_ORIGINS', 'https://*.liara.run,https://*.liara.ir')
]
app_url = os.environ.get('APP_URL', '').strip().rstrip('/')
if app_url:
    origin = with_scheme(app_url)
    if origin not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.append(origin)
for host in ALLOWED_HOSTS:
    if host in {'*', ''} or host.startswith('.'):
        continue
    origin = f'https://{host}'
    if origin not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.append(origin)


# HTTPS
# The platform terminates HTTPS and forwards the original scheme and host.

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
SESSION_COOKIE_SECURE = env_bool('SESSION_COOKIE_SECURE', default=not DEBUG)
CSRF_COOKIE_SECURE = env_bool('CSRF_COOKIE_SECURE', default=not DEBUG)
SECURE_SSL_REDIRECT = env_bool('SECURE_SSL_REDIRECT', default=False)
SECURE_HSTS_SECONDS = env_int('SECURE_HSTS_SECONDS', 0)
if not DEBUG:
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_REFERRER_POLICY = 'same-origin'


# Applications

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
]

MIDDLEWARE = [
    'config.middleware.HealthCheckMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'accounts.context_processors.portal',
            ],
        },
    },
]


# Database
# DATABASE_URL wins, then the POSTGRESQL_DB_* variables, then local SQLite.

DB_CONN_MAX_AGE = env_int('DB_CONN_MAX_AGE', 60)


def postgres_from_url(url):
    parsed = urlparse(url)
    scheme = parsed.scheme.split('+')[0]
    if scheme not in {'postgres', 'postgresql'}:
        raise ImproperlyConfigured('DATABASE_URL must be a PostgreSQL URL.')
    config = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': unquote(parsed.path.lstrip('/')),
        'USER': unquote(parsed.username or ''),
        'PASSWORD': unquote(parsed.password or ''),
        'HOST': parsed.hostname or '',
        'PORT': str(parsed.port or 5432),
        'CONN_MAX_AGE': DB_CONN_MAX_AGE,
        'CONN_HEALTH_CHECKS': True,
    }
    sslmode = parse_qs(parsed.query).get('sslmode', [''])[0]
    if sslmode:
        config['OPTIONS'] = {'sslmode': sslmode}
    return config


def sqlite_path():
    configured = os.environ.get('SQLITE_PATH', '').strip()
    path = Path(configured) if configured else BASE_DIR / 'DB' / 'db.sqlite3'
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


database_url = os.environ.get('DATABASE_URL', '').strip()
postgres_host = os.environ.get('POSTGRESQL_DB_HOST', '').strip()

if database_url:
    DATABASES = {'default': postgres_from_url(database_url)}
elif postgres_host:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRESQL_DB_NAME', 'postgres'),
            'USER': os.environ.get('POSTGRESQL_DB_USER', ''),
            'PASSWORD': os.environ.get('POSTGRESQL_DB_PASS', ''),
            'HOST': postgres_host,
            'PORT': os.environ.get('POSTGRESQL_DB_PORT', '5432'),
            'CONN_MAX_AGE': DB_CONN_MAX_AGE,
            'CONN_HEALTH_CHECKS': True,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': sqlite_path(),
        }
    }

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Authentication

AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization

LANGUAGE_CODE = 'fa'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True


# Static files (served by WhiteNoise after collectstatic)

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
    },
}


# Logging
# Without this, DEBUG=False swallows every 500 and nothing reaches the platform logs.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'plain': {'format': '%(asctime)s %(levelname)s %(name)s %(message)s'},
    },
    'handlers': {
        'console': {'class': 'logging.StreamHandler', 'formatter': 'plain'},
    },
    'root': {
        'handlers': ['console'],
        'level': os.environ.get('LOG_LEVEL', 'INFO').upper(),
    },
    'loggers': {
        'django.request': {'handlers': ['console'], 'level': 'ERROR', 'propagate': False},
    },
}


# Project

SITE_NAME = 'کشتیار'
