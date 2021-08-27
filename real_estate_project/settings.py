"""
Django settings for real_estate_project project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$4l&awa%b^s-y(+c5o_n%3!ed$2x!)(gr(1jzacbb%@uj)a%3h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.0.106','localhost', 'shareable-real-estate.herokuapp.com']

RAZOR_KEY_ID = "rzp_test_Xx2uoyrz9mcc8g"
RAZOR_KEY_SECRET = "iNCMtMDwbeiKS8HVBILcXhkm"

BUNDLE_ID = "4d49a901-4734-4852-ab52-fed7ca0070ec"
FUNDING_ID = "487fedb8-a30b-48f7-9575-5f20d8be9889"
AUTH_TOKEN = "eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwidGFnIjoiX3RoZU13ODh5MEZOdlNBMDZzU1FwUSIsImFsZyI6IkExMjhHQ01LVyIsIml2IjoibDlpNU9xUUlaY0piQTF4aiJ9.4zhgblK7DTV6HOlPS5a0z2mFL6cgIcGWCHVKRz9jy2k.uZmP8gikbjUSDwyAWCe6Cw.QJSJx_Wm8wmZbeBDci2s7lY6-yNTUorI7Ut4pmltJGo2A4MdPIF1MWA3gFPSgeiCWXInJUSOe3oD0jE8tL1Bv6VXm9prlVq2gy5f0ak3hw9YD1W8kvROP2JnhyBCuqVnr7XOFx1luSb1euG-Is-gNA70-cyfGUN3fY9lTxH7Y5FMvE506dgcaV2pWCHpZAXWC2TrTwDm3T5T54PwUp_Fnymf0yvYZ-JhChI7CfwK73Fh2L9OEw42TePvejBraHUAqwFARCltuhe2NM_IBHHefvkE5wetenZhb9W5U0hfxJofy7vgbNXddfNNVSPIeRMKdlEsCjvVrh6DzwmE5pxFcjRksSnmyYCahejiY9ywgs3R3PqiR1H73WuaRt-Y-wuCGwOcFQ6zn1-k2bnTKt_KbQ.5kdD6Ay8EMLmoUzqeGcOKw"
IFI_ID = "140793"
ZETA_BASE_URL = "https://fusion.preprod.zeta.in/api/v1/ifi/"+IFI_ID
ADMIN_HOLDER_ID = "d3a12421-24f6-4e6e-98ac-3dbdddab8657"
ADMIN_ACCOUNT_ID = "5a7c963d-4fcf-443c-860b-5b1511a10dfe"
FUNDING_ID = "487fedb8-a30b-48f7-9575-5f20d8be9889"
HEADERS = {
    "X-Zeta-AuthToken" : AUTH_TOKEN,
    "Content-Type": "application/json",
    "Cache-Control" : 'no-cache'
}
DEFAULT_FROM_EMAIL = 'shareable.real.estate@gmail.com'
SERVER_EMAIL = 'shareable.real.estate@gmail.com'
# Application definition
# EMAIL_HOST_PASSWORD="lifu htht mufe byzd"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'seller_app',
    'homepage_app',
    'buyer_app'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'real_estate_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'real_estate_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,  'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/



EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Activate Django-Heroku.
django_heroku.settings(locals())