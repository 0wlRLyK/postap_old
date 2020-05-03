"""
Django settings for postap project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '63&hf6if7i)i9pji(1a7!yll*-p%71i!@qh9jj&0^txy%o1wzz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'nucleus',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # EXTENSIONS OF DEFAULT DJANGO FUNCTIONALITY
    'betterforms',
    'extra_views',
    'tinymce',
    'taggit',
    'stdimage',

    # POSTAP APPS
    'entries',
    'gallery',

    'django_cleanup.apps.CleanupConfig',
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

ROOT_URLCONF = 'postap.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'tmp'),
                 # MACHINA_MAIN_TEMPLATE_DIR,
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'nucleus.context_processors.nucleus',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'postap.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# путь до папки media, в общем случае она пуста в начале

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    # MACHINA_MAIN_STATIC_DIR
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# /////////-------
# ADMIN INTERFACE
# /////////-------
_ = lambda s: s

NUCLEUS = {
    'sidebar': {
        # Title
        'title': _('POSTAP ADMINISTRATING'),

        # # Footer
        # 'footer': {
        #     'title': _('Custom title'),
        #     'description': _('Longer text displayed below the title'),
        # },

        # Navigation
        'navigation': {

            # Application
            'entries': {
                'title': _('Записи'),  # Override title
                'icon': 'admin/ui/img/entries/entries.svg'  # Optional
            },
            'EntryNews': {
                'title': _('Новости'),
                'icon': 'admin/ui/img/entries/news.svg'  # Optional
            },
            'CategoriesNews': {
                'title': _('Категории новостей'),
                'icon': 'admin/ui/img/entries/category.svg'  # Optional
            },
            'EntryArticle': {
                'title': _('Статьи'),
                'icon': 'admin/ui/img/entries/news.svg'  # Optional
            },
            'CategoriesArticle': {
                'title': _('Категории статей'),
                'icon': 'admin/ui/img/entries/category.svg'  # Optional
            },
            'Gallery': {
                'title': _('Галереи'),
                'icon': 'admin/ui/img/entries/gallery.svg'  # Optional
            },

        }
    }
}
