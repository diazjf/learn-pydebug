from remote.config import Config

from flask import Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

# Import routes to use in application
from remote import routes