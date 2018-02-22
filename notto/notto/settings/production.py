"""
Production Settings
"""

from .base import *  # noqa: F401, F403
from .secret import generate as generate_secret

DEBUG = False
SECRET_KEY = generate_secret()
