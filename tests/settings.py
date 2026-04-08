SECRET_KEY = "tests-only-secret-key"
INSTALLED_APPS = [
    "django_pg_ultrasearch",
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
ROOT_URLCONF = "tests.urls"
USE_TZ = True
