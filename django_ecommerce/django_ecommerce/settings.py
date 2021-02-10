from pathlib import Path
import environ


# django-environ settings
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool(
    "DEBUG"
)  # Don't forget to make this FALSE in the env file before deployment.

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Built in apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    # Local apps
    "users.apps.UsersConfig",
    "products.apps.ProductsConfig",
    "baskets.apps.BasketsConfig",
    # Third-party apps
    "crispy_forms",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_ecommerce.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "django_ecommerce.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env.str("DATABASE_NAME"),  # Change this setting in the env file.
        "USER": env.str("DATABASE_USER"),  # Change this setting in the env file.
        "PASSWORD": env.str(
            "DATABASE_PASSWORD"
        ),  # Change this setting in the env file.
        "HOST": env.str("DATABASE_HOST"),  # Change this setting in the env file.
        "PORT": env.str("DATABASE_PORT"),  # Change this setting in the env file.
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"

# Custom user section.
AUTH_USER_MODEL = "users.CustomUser"

# Redirection urls.
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

# E-mail //  via Gmail
# Host user linkten izin vermeli.
# Link:
# https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4NJd5JiEqULJC38WFF4b2WaT8Xg1X0yBALpCU0ljWyb3bCkCOYzDH19RLnO24eDR-Mgybo50Rj--GNxrujqlhaCQqd-Sg
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "admin@gmail.com"
EMAIL_HOST_PASSWORD = "password"

# Crispy template pack.
CRISPY_TEMPLATE_PACK = "bootstrap4"

# User uploaded images.
MEDIA_URL = "/"
MEDIA_ROOT = BASE_DIR / "media"

# Sitemap setting.
SITE_ID = 1
