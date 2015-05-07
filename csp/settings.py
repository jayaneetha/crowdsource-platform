"""
Django settings for csp project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v1*ah#)@vyov!7c@n&c2^-*=8d)-d!u9@#c4o*@k=1(1!jul6&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
APPEND_SLASH = True

# ALLOWED_HOSTS = [*]

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',
    'DEFAULT_AUTHENTICATION_CLASSES': (
         'oauth2_provider.ext.rest_framework.OAuth2Authentication',),
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        #'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
    #'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    #'PAGE_SIZE': 100
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope'}
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    #'django_extensions',
    'rest_framework',
    'oauth2_provider',
    'djangobower',
    'crowdsourcing',
    'autofixture',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'csp.urls'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,  'staticfiles/templates')],
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

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

WSGI_APPLICATION = 'csp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': dj_database_url.config()
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "crowdsource_dev"
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)
COMPRESS_ROOT = '/compress'
#Python 2
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'staticfiles/templates'),
)

# Bower configurations
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'staticfiles')

BOWER_INSTALLED_APPS = (
    'jquery#1.9',
    'underscore',
    'angular#1.3.14',
    'angular-route#1.3.14',
    'angular-animate#1.3.14',
    'angular-sanitize#1.3.14',
    'angular-animate#1.3.14',
    'angular-cookies#1.3.14',
    'bootstrap#3.3.2',
    'angular-loading-bar#0.7.1',
    'angular-bootstrap#0.12.1',
    'angular-strap#2.1.2',
    'ng-grid#2.0.14',
    'angular-smart-table#2.0.2',
)

# Email
EMAIL_HOST = 'localhost'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True

# Others
REGISTRATION_ALLOWED = True
PASSWORD_RESET_ALLOWED = True
EMAIL_ENABLED = False
EMAIL_SENDER = 'crowdsourcing.platform.demo@gmail.com'
EMAIL_SENDER_PASSWORD = 'crowdsourcing.demo.2015'
LOGIN_URL = '/login'
#SESSION_ENGINE = 'redis_sessions.session'

# Security
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
PYTHON_VERSION = 2
try:
    #from crowdresearch.settings import *
    from local_settings import *
except Exception as e:
    pass


GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}

FIXTURE_DIRS = (
   os.path.join(BASE_DIR, 'fixtures')
)
