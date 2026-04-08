from os import environ

SECRET_KEY = "tests-only-secret-key"
INSTALLED_APPS = [
    "django_pg_ultrasearch",
]
if environ.get("DJANGO_DB_BACKEND") == "postgresql" or environ.get("PGHOST"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": environ.get("PGDATABASE", "django_pg_ultrasearch"),
            "USER": environ.get("PGUSER", "postgres"),
            "PASSWORD": environ.get("PGPASSWORD", "postgres"),
            "HOST": environ.get("PGHOST", "127.0.0.1"),
            "PORT": environ.get("PGPORT", "5432"),
        },
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        },
    }

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
ROOT_URLCONF = "tests.urls"
USE_TZ = True
