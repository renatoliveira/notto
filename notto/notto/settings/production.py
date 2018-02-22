"""
Production Settings
"""

# pylint: disable=W0401, W0614
from .base import *
from .secret import generate as generate_secret

DEBUG = False
SECRET_KEY = generate_secret()
