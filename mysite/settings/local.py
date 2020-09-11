
from .base import *

# [ python manage.py runserver --settings=mysite.settings.local ]



INSTALLED_APPS += [ ]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'E-com',
        'USER':'postgres',
        'PASSWORD':'12345',
        'HOST':'localhost'

    }
}



#static section

STATIC_URL = '/static/'
STATIC_DIRS= [os.path.join(BASE_DIR,'static')]



SITE_ID = 1






#email section

EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='dota3hudai@gmail.com'
EMAIL_HOST_PASSWORD='@ammaremail'
