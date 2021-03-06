import os

gettext_noop = lambda s: s

PROJECT_APP_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PROJECT_ROOT = os.path.abspath(os.path.dirname(PROJECT_APP_ROOT))
PUBLIC_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, 'public'))

SECRET_KEY = 'OVERWRITE_THIS_AND_KEEP_SECRET'

DEBUG = False
TEMPLATE_DEBUG = False
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

SITE_ID = 1

ALLOWED_HOSTS = (
    '.leffalippu.fi',
)

ADMINS = (
    ('Jaakko Luttinen', 'jaakko.luttinen@iki.fi'),
)
MANAGERS = ADMINS

REGISTRATION_OPEN = True
LOGIN_REDIRECT_URL = '/'

# Application definition

ROOT_URLCONF = 'leffalippu.urls'
WSGI_APPLICATION = 'leffalippu.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin_views',
    'registration',
    'leffalippu',

    # 'leffalippu.apps.accounts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Templates

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

# Database

# Internationalization
LANGUAGE_CODE = 'fi'
LANGUAGES = (
    'fi', gettext_noop('Finnish'),
    'en', gettext_noop('English'),
)

TIME_ZONE = 'Europe/Helsinki'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = os.path.join(PROJECT_ROOT, 'locale')

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static')
MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'include_html': True,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['null'],
            'level': 'DEBUG',
        },
        'py.warnings': {
            'handlers': ['null'],
            'level': 'WARNING',
            'propagate': False,
        }
    }
}




## # Django settings for leffalippu project.

## import os
## path = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)

## DEBUG = True
## TEMPLATE_DEBUG = DEBUG

## ADMINS = (
##     # ('Your Name', 'your_email@example.com'),
## )

## MANAGERS = ADMINS

## DATABASES = {
##     'default': {
##         'ENGINE':   'django.db.backends.sqlite3',
##         'NAME':     path('database.sqlite'),
##         'USER':     '',
##         'PASSWORD': '',
##         'HOST':     '',
##         'PORT':     '',
##     }
## }

## # Email settings. Use dummy settings here, overwrite in local_settings.py
## EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
## EMAIL_ADDRESS = 'info@leffalippu.fi'
## # SMTP:
## #EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
## #EMAIL_HOST = 'host.com'
## #EMAIL_PORT = 25
## #EMAIL_HOST_USER = 'username'
## #EMAIL_HOST_PASSWORD = 'password'
## #EMAIL_USE_TLS = False
## # Sendmail:
## #EMAIL_BACKEND = 'leffalippu.sendmail.EmailBackend'
## #SENDMAIL_BIN = 'sendmail' # or use absolute path


## CRON_CLASSES = [
##     "leffalippu.models.ExpirationCronJob",
## ]

## EXPIRATION_MINUTES = 15

## # Local time zone for this installation. Choices can be found here:
## # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
## # although not all choices may be available on all operating systems.
## # On Unix systems, a value of None will cause Django to use the same
## # timezone as the operating system.
## # If running in a Windows environment this must be set to the same as your
## # system time zone.
## TIME_ZONE = 'Europe/Helsinki'

## # Language code for this installation. All choices can be found here:
## # http://www.i18nguy.com/unicode/language-identifiers.html
## LANGUAGE_CODE = 'fi-fi'

## SITE_ID = 1

## # If you set this to False, Django will make some optimizations so as not
## # to load the internationalization machinery.
## USE_I18N = True

## # If you set this to False, Django will not format dates, numbers and
## # calendars according to the current locale.
## USE_L10N = True

## # If you set this to False, Django will not use timezone-aware datetimes.
## USE_TZ = True

## # Absolute filesystem path to the directory that will hold user-uploaded files.
## # Example: "/home/media/media.lawrence.com/media/"
## MEDIA_ROOT = path('media/')

## # URL that handles the media served from MEDIA_ROOT. Make sure to use a
## # trailing slash.
## # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
## MEDIA_URL = '/media/'

## # Absolute path to the directory static files should be collected to.
## # Don't put anything in this directory yourself; store your static files
## # in apps' "static/" subdirectories and in STATICFILES_DIRS.
## # Example: "/home/media/media.lawrence.com/static/"
## STATIC_ROOT = path('sitestatic/')

## # URL prefix for static files.
## # Example: "http://media.lawrence.com/static/"
## STATIC_URL = '/static/'

## # Additional locations of static files
## STATICFILES_DIRS = (
##     # Put strings here, like "/home/html/static" or "C:/www/django/static".
##     # Always use forward slashes, even on Windows.
##     # Don't forget to use absolute paths, not relative paths.
## )

## # List of finder classes that know how to find static files in
## # various locations.
## STATICFILES_FINDERS = (
##     'django.contrib.staticfiles.finders.FileSystemFinder',
##     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
## #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
## )

## # OVERWRITE THE FOLLOWING KEYS IN LOCAL_SETTINGS.PY
## #
## # Make this unique, and don't share it with anybody.
## SECRET_KEY = 'ykw0$v$-q811*0r^vl9j3m81jk=d3xwz5tkcwx+^84fwtm9@qp'
## # Key for encrypting the order ID for the customer
## #PUBLIC_URL_KEY = 'abc123'
## # Key for encrypting the order ID for the bitcoin payment system
## #PRIVATE_URL_KEY = 'qwerty'
## # 8 character key for encrypted models
## CHAR8KEY = '8charkey'
## RECAPTCHA_PUBLIC_KEY = '76wtgdfsjhsydt7r5FFGFhgsdfytd656sad75fgh'
## RECAPTCHA_PRIVATE_KEY = '98dfg6df7g56df6gdfgdfg65JHJH656565GFGFGs'
## RECAPTCHA_USE_SSL = False
## CALLBACK_CHAR8KEY = '8charkey'
## CALLBACK_SECRET = 'sfjk230sdfkl' # maybe not necessary


## BITCOIN_ADDRESS = '1GtBp71e33TDwbQHeZxo1dJdFmxVgfjrVu'
## BITCOIN_FEE = 0.6

## # This URL is used as a base for blockchain.info payment system. You may want to
## # change it in order to make SSL/HTTPS work.
## # CHANGE THIS in local_settings.py
## CALLBACK_BASEURL = 'https://domain.com/site-directory'



## # List of callables that know how to import templates from various sources.
## TEMPLATE_LOADERS = (
##     'django.template.loaders.filesystem.Loader',
##     'django.template.loaders.app_directories.Loader',
## #     'django.template.loaders.eggs.Loader',
## )

## MIDDLEWARE_CLASSES = (
##     'django.middleware.locale.LocaleMiddleware',
##     'django.middleware.common.CommonMiddleware',
##     'django.contrib.sessions.middleware.SessionMiddleware',
##     'django.middleware.csrf.CsrfViewMiddleware',
##     'django.contrib.auth.middleware.AuthenticationMiddleware',
##     'django.contrib.messages.middleware.MessageMiddleware',
##     # Uncomment the next line for simple clickjacking protection:
##     # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
## )

## ROOT_URLCONF = 'leffalippu.urls'

## # Python dotted path to the WSGI application used by Django's runserver.
## WSGI_APPLICATION = 'leffalippu.wsgi.application'

## TEMPLATE_DIRS = (
##     # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
##     # Always use forward slashes, even on Windows.
##     # Don't forget to use absolute paths, not relative paths.
##     path('templates/')
## )

## INSTALLED_APPS = (
##     'django.contrib.auth',
##     'django.contrib.contenttypes',
##     'django.contrib.sessions',
##     'django.contrib.sites',
##     'django.contrib.messages',
##     'django.contrib.staticfiles',
##     # Uncomment the next line to enable the admin:
##     'django.contrib.admin',
##     # Uncomment the next line to enable admin documentation:
##     # 'django.contrib.admindocs',
##     'leffalippu',
##     #'south',
##     'mail_templated',
##     'django_cron',
##     #'captcha',
##     'admin_views',
## )

## # A sample logging configuration. The only tangible logging
## # performed by this configuration is to send an email to
## # the site admins on every HTTP 500 error when DEBUG=False.
## # See http://docs.djangoproject.com/en/dev/topics/logging for
## # more details on how to customize your logging configuration.
## LOGGING = {
##     'version': 1,
##     'disable_existing_loggers': False,
##     'filters': {
##         'require_debug_false': {
##             '()': 'django.utils.log.RequireDebugFalse'
##         }
##     },
##     'handlers': {
##         'mail_admins': {
##             'level': 'ERROR',
##             'filters': ['require_debug_false'],
##             'class': 'django.utils.log.AdminEmailHandler'
##         }
##     },
##     'loggers': {
##         'django.request': {
##             'handlers': ['mail_admins'],
##             'level': 'ERROR',
##             'propagate': True,
##         },
##     }
## }

## # Use local settings to overwrite these
## try:
##     execfile(path('local_settings.py'))
## except IOError:
##     pass
