from .common import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@*hvrr99_9-8ehovqqapkl5l$45@_c6pvhm#5od-geiuun9v=h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "ecommerce",
        'HOST': "127.0.0.1",
        'PORT': 5432,
        'USER': "",
        'PASSWORD': "",
    }
}