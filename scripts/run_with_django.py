import os
import sys

import django


def setup_django():
    module, _ = os.path.split(__file__)
    sys.path.append(os.path.join(module, '..'))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled.settings")
    django.setup()
