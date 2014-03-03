import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

#----------------------------------------
# initialization
#----------------------------------------

app = Flask(__name__)
app.config.from_object('config')
app.config.update(DEBUG = True)
db = SQLAlchemy(app)

from app import views, models
#----------------------------------------
# controllers
#----------------------------------------

@app.route("/")
def hello():
    return "Hello from Python!"

#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
