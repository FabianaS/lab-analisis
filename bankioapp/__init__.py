from flask import Flask

__version__ = '1.0'

app = Flask('bankioapp', template_folder='../templates')
app.config.from_object('config')
app.debug = True

# Import all bankioapp controller files
from bankioapp.controllers import *
