import os
from pathlib import Path
from django.utils.translation import gettext as _
from django.contrib import admin
from django.urls import reverse_lazy
import dj_database_url
ALLOWED_HOSTS = []

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-bn_x$=on8z1c#3gu87s7bme84ql281%-9sv63z_f_i=rck+46+"

DEBUG = "RENDER" not in os.environ
RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

INSTALLED_APPS = [
    "corsheaders",
    "rest_framework",
    "chartjs",
    "jazzmin",
    "django_tables2",
    "actividades_de_usuario.apps.ActividadesDeUsuarioConfig",
    "ensueño.apps.EnsueñoConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]


JAZZMIN_SETTINGS = {
    "development_mode": True,
    "show_ui_builder": True,
    "related_modal_active": True,
    "navigation_icons": "smart",
    "custom_dashboard": "reportes.dashboard_admin.MyCustomDashboard",
    "site_title": "En sueño",
    "site_header": "En sueño",
    "site_brand": "En sueño",
    "site_logo": None,
    "welcome_sign": "Bienvenido al restaurante Ensueño",
    "copyright": "En sueño",
    "user_avatar": "images/avatar.png",
    "topmenu_links": [
        {
            "name": "Ensueño",
            "url": reverse_lazy("admin:index"),
            "permissions": ["auth.view_user"],
        },
        {
            "name": "Reportes",
            "url": "/pagina-personalizada/",
            "permissions": ["auth.view_user"],
        },
        {"model": "auth.User"},
    ],
    "show_explorer": True,
    "navigation_expanded": True,
    "usermenu_title": "Configuración de Usuario",
    "models": {
        "auth": {
            "models": {
                "user": {"label": "Administrators"},
            },
        },
    },
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["Reportes", "ensueño", "auth", "actividades_de_usuario"],
    "custom_links_order": {
        "ensueño": [
            {
                "name": "Reportes",
                "url": "/pagina-personalizada/",
                "icon": "fas fa-link",
            },
        ],
    },
    "custom_links": {
        "ensueño": [
            {
                "name": "Reportes",
                "url": "/pagina-personalizada/",
                "icon": "fas fa-link",
            },
        ],
    },
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "users.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "admin.LogEntry": "fas fa-file",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-arrow-circle-right",
    "related_modal_active": True,
    "show_ui_builder": True,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    "nav_active": {
        "custom_dashboard": "custom_dashboard",
    },
    "changeform_format": "horizontal_tabs",
}


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "accent": "accent-orange",
    "brand_colour": "navbar-light",
    "navbar": "navbar-orange navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "show_sidebar": False,
    "sidebar": "sidebar-light-orange",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "restaurante.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "restaurante.wsgi.application"


DATABASES = {
    "default": dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default="mysql://root:@localhost:3306/bdrestauranteintegrador",
        conn_max_age=600,
    )
}


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


LANGUAGE_CODE = "es-pe"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Agrega estas líneas para definir STATIC_ROOT
STATIC_ROOT = BASE_DIR / "staticfiles"
if not DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"

CELERY_IMPORTS = ("actividades_de_usuario.tasks",)
CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "10.0.2.2", "paneladministrativo-restaurante.onrender.com"]