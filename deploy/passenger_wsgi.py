import os
import sys

from core.wsgi import application

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))
