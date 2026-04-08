from django.apps import apps

import django_pg_ultrasearch


def test_app_config_is_registered() -> None:
    config = apps.get_app_config("pg_ultrasearch")

    assert config.name == "django_pg_ultrasearch"
    assert config.default_auto_field == "django.db.models.BigAutoField"


def test_version_is_exposed() -> None:
    assert django_pg_ultrasearch.__version__ == "0.1.0"
