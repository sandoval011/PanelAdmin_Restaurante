#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurante.settings')
    try:
        from django.core.management import execute_from_command_line

        # Agregamos estas líneas para cargar las aplicaciones antes de ejecutar cualquier comando
        from django.conf import settings
        settings.INSTALLED_APPS

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
