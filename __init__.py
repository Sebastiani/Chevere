import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

#----------------------------------------
# initialization
#----------------------------------------

app = Flask(__name__)
#app.config.from_object('Chevere/config.py')
app.config.update(DEBUG = True)
#db = SQLAlchemy(app)

from Chevere import views, models


