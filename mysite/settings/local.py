
from .base import *

# [ python manage.py runserver --settings=mysite.settings.local ]


INSTALLED_APPS += ['customer.apps.CustomerConfig', ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'E-com',
        'USER': 'postgres',
        'PASSWORD': '12345',
        'HOST': 'localhost'

    }
}

LOGIN_REDIRECT_URL = '/'
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True


SITE_ID = 2

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}


ACCOUNT_USERNAME_REQUIRED = True  # new
ACCOUNT_UNIQUE_EMAIL = True  # new
ACCOUNT_AUTHENTICATION_METHOD = ('username_email')


# email section

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'dota3hudai@gmail.com'
EMAIL_HOST_PASSWORD = '@ammaremail'
