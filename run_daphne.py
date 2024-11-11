import os
from daphne.cli import CommandLineInterface
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jess.settings")
CommandLineInterface().run(["-p", "8001", "jess.asgi:application"])