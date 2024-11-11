import os
import django
from daphne.cli import CommandLineInterface
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jess.settings")
django.setup()
CommandLineInterface().run(["-p", "8001", "jess.asgi:application"])