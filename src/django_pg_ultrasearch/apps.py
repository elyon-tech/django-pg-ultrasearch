from django.apps import AppConfig


class DjangoPgUltrasearchConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_pg_ultrasearch"
    label = "pg_ultrasearch"
    verbose_name = "PostgreSQL Ultra Search"
