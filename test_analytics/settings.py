"""
Django settings for test_analytics project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ncd_r5!6(igws8s(+q+4(z!$3tieo-mttn1_#%phv$+vv*i2xl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'util',
    'shsql.apps.ShSQLConfig',
    'kpi.apps.KPIConfig',
    'facebook.apps.FacebookConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_results'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test_analytics.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'test_analytics.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
db = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sfox',
        'USER': 'admin',
        'PASSWORD': '6uBAG5qgBKkN5GzP',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
db_file = '{}/local_db.json'.format(BASE_DIR)
if os.path.isfile(db_file):
    with open(db_file) as f:
        conn = json.load(f)
        db = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': conn['db_name'],
                'USER': conn['username'],
                'PASSWORD': conn['password'],
                'HOST': conn['hostname'],
                'PORT': conn['port'],
            }
        }
DATABASES = db


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# Celery settings
# http://docs.celeryproject.org/en/latest/userguide/configuration.html

CELERY_BROKER_URL = 'amqp://nadia:N4a9R8a8DuTtXcn3@localhost:5672//sfdata'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

from .celery_schedule import configure_celery_tasks
CELERY_BEAT_SCHEDULE = configure_celery_tasks()

REDSHIFT_PATH = '{}/redshift.json'.format(BASE_DIR)
with open(REDSHIFT_PATH, 'r') as f:
    redshift_settings = json.load(f)
    redshift_credentials = redshift_settings['credentials']

REDSHIFT_CLUSTER_JDBCURL = redshift_settings['ClusterJDBCURL']
REDSHIFT_ROLE_ARN = redshift_settings['RoleARN']
REDSHIFT_BUCKET_ARN = redshift_settings['BucketARN']

REDSHIFT_SCHEMA = 'sfox_prod'
REDSHIFT_HOSTNAME = redshift_credentials['host']
REDSHIFT_PORT = redshift_credentials['port']
REDSHIFT_USERNAME = redshift_credentials['user']
REDSHIFT_PASSWORD = redshift_credentials['password']
REDSHIFT_DB_NAME = redshift_credentials['dbname']

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'signalfox.views': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
