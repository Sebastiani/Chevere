import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import basedir

#----------------------------------------
# initialization
#----------------------------------------

app = Flask(__name__)
#app.config.from_object('Chevere/config.py')
app.config.update(DEBUG = True)
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp') #uses basedir from config.py, don't know if its functional
from Chevere import views, models


