from flask import render_template, flash, redirect
from Chevere import app
from forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
	return render_template("home.html")
