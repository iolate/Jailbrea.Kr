import sys, os
sys.path.insert(0, os.path.dirname(__file__))
os.environ['APP_SETTINGS'] = 'settings.cfg'
from flask_app import app as application
