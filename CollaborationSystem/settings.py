"""
Django settings for CollaborationSystem project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from machina import get_apps as get_machina_apps
from machina import MACHINA_MAIN_TEMPLATE_DIR
from machina import MACHINA_MAIN_STATIC_DIR

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'myf0)*es+lr_3l0i5$4^)^fb&4rcf(m28zven+oxkd6!(6gr*6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['10.129.132.103']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_comments_xtd',
    'django_comments',
    'Community',
    'UserRolesPermission',
    'BasicArticle',
    'Group',
    'rest_framework',
    'widget_tweaks',
    'reversion',
    'reversion_compare',
    'haystack',
    'mptt',
    'corsheaders',
    'rolepermissions',
    'rest_framework.authtoken',
    'workflow',
    'social_django',
    'pysolr',
    'search',
    'webcontent'
] + get_machina_apps()

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'machina.apps.forum_permission.middleware.ForumPermissionMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'CollaborationSystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), MACHINA_MAIN_TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'machina.core.context_processors.metadata',
                'django.template.context_processors.media',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
 'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
 'social_core.backends.google.GoogleOpenId',  # for Google authentication
 'social_core.backends.google.GoogleOAuth2',  # for Google authentication
 'social_core.backends.github.GithubOAuth2',  # for Github authentication
 'social_core.backends.facebook.FacebookOAuth2',  # for Facebook authentication

 'django.contrib.auth.backends.ModelBackend',
)



WSGI_APPLICATION = 'CollaborationSystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), MACHINA_MAIN_STATIC_DIR]

LOGIN_URL = 'login/'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_REDIRECT_URL = 'user_dashboard'

CORS_ORIGIN_ALLOW_ALL=True

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='735919351499-ajre9us5dccvms36ilhrqb88ajv4ahl0.apps.googleusercontent.com'  #Paste CLient Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'I1v-sHbsogVc0jAw9M9Xy1eM' #Paste Secret Key

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST ='localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD =''
EMAIL_PORT = 25
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL="collaboratingcommunity@cse.iitb.ac.in"



CACHES = {
  'default': {
    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
  },
  'machina_attachments': {
    'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
    'LOCATION': '/tmp',
  }
}

HAYSTACK_CONNECTIONS = {
  'default': {
    'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
  },
}
SITE_ID=1

COMMENTS_APP='django_comments_xtd'

COMMENTS_XTD_MAX_THREAD_LEVEL = 1  # default is 0

COMMENTS_XTD_LIST_ORDER = ('-thread_id', 'order')

COMMENTS_XTD_APP_MODEL_OPTIONS = {
    'Group.grouparticles': {
        'allow_flagging': True,
        'allow_feedback': True,
        'show_feedback': True,
    }
}

COMMENTS_XTD_APP_MODEL_OPTIONS = {
    'Community.communityarticles': {
        'allow_flagging': True,
        'allow_feedback': True,
        'show_feedback': True,
    }
}

ROLEPERMISSIONS_MODULE = 'UserRolesPermission.roles'

REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES': (
      'rest_framework.authentication.TokenAuthentication',
    )
}


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

GOOGLE_RECAPTCHA_SECRET_KEY = '6Lfsk0MUAAAAAFdhF-dAY-iTEpWaaCFWAc1tkqjK'

SESSION_COOKIE_AGE = 1800
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
