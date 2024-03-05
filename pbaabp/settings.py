"""
Django settings for pbaabp project.

Generated by 'django-admin startproject' using Django 4.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

import environ

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(BASE_DIR / ".env")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-l+*3%+le)@z#dwiv5x7(kw#hp&qqa$tkzf)gdm%%e)m^02c5w6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost"])
CSRF_TRUSTED_ORIGINS = env.list("DJANGO_CSRF_TRUSTED_ORIGINS", default=["http://localhost"])

# Application definition

INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Addons
    "allauth",
    "allauth.account",
    "allauth.mfa",
    "django_recaptcha",
    "djstripe",
    "email_log",
    "ordered_model",
    # Our apps
    "pbaabp",
    "pages",
    "membership",
    "profiles",
    "events",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "pbaabp.middleware.TimezoneMiddleware",
]

ROOT_URLCONF = "pbaabp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "pbaabp.wsgi.application"
ASGI_APPLICATION = "pbaabp.asgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {"default": env.db("DATABASE_URL")}


# Authentication
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
    "sesame.backends.ModelBackend",
]


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Celery

_REDIS_URL = env("REDIS_URL", default="redis://redis:6379/0")
if _REDIS_URL.startswith("rediss://"):
    _REDIS_URL = _REDIS_URL + "?ssl_cert_reqs=none"

CELERY_BROKER_URL = _REDIS_URL
CELERY_RESULT_BACKEND = _REDIS_URL
CELERY_BEAT_SCHEDULE = {}

# MAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = env("DJANGO_EMAIL_SUBJECT_PREFIX", default="[Philly Bike Action]")

EMAIL_BACKEND = 'email_log.backends.EmailBackend'
EMAIL_LOG_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("DJANGO_EMAIL_HOST", default="smtp.mailgun.org")
EMAIL_PORT = env.int("DJANGO_EMAIL_PORT", default=587)
EMAIL_USE_TLS = env.bool("DJANGO_EMAIL_USE_TLS", default=True)
EMAIL_HOST_USER = env("DJANGO_EMAIL_HOST_USER", default=None)
EMAIL_HOST_PASSWORD = env("DJANGO_EMAIL_HOST_PASSWORD", default=None)

# https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL", default="Philly Bike Action <noreply@bikeaction.org>"
)
# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)

# Discord
DISCORD_BOT_TOKEN = env("DISCORD_BOT_TOKEN")

# Wordpress
WP_URL = env("WP_URL", default="https://bikeaction.org")
WP_LOGIN_EMAIL = env("WP_LOGIN_EMAIL")
WP_LOGIN_PASS = env("WP_LOGIN_PASS")

# Mailchimp
MAILCHIMP_API_KEY = env("MAILCHIMP_API_KEY")
MAILCHIMP_AUDIENCE_ID = env("MAILCHIMP_AUDIENCE_ID")

# django-allauth
ACCOUNT_FORMS = {
    "signup": "profiles.forms.ProfileSignupForm",
}
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"

# django-sesame
SESAME_MAX_AGE = 300

# django-recaptcha
if DEBUG:
    SILENCED_SYSTEM_CHECKS = ["django_recaptcha.recaptcha_test_key_error"]
else:
    RECAPTCHA_PUBLIC_KEY = env("RECAPTCHA_PUBLIC_KEY", default=None)
    RECAPTCHA_PRIVATE_KEY = env("RECAPTCHA_PRIVATE_KEY", default=None)

# dj-stripe
STRIPE_LIVE_SECRET_KEY = env("STRIPE_LIVE_SECRET_KEY", default=None)
STRIPE_LIVE_PUBLIC_KEY = env("STRIPE_LIVE_PUBLIC_KEY", default=None)
STRIPE_TEST_SECRET_KEY = env("STRIPE_TEST_SECRET_KEY", default=None)
STRIPE_TEST_PUBLIC_KEY = env("STRIPE_TEST_PUBLIC_KEY", default=None)
STRIPE_SECRET_KEY = STRIPE_TEST_SECRET_KEY if DEBUG else STRIPE_LIVE_SECRET_KEY
STRIPE_PUBLIC_KEY = STRIPE_TEST_PUBLIC_KEY if DEBUG else STRIPE_LIVE_PUBLIC_KEY
STRIPE_LIVE_MODE = not DEBUG
DJSTRIPE_USE_NATIVE_JSONFIELD = True
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"
