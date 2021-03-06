#!/usr/bin/env python
import os, sys

from datazilla.vendor import add_vendor_lib

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datazilla.settings.base")

    add_vendor_lib()

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
