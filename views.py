from flask import render_template, flash, redirect
from Chevere import app
from forms import LoginForm

user =  {'name': 'Sebastiani', 'lastname':'Aguirre'}


@app.route('/home')
def index():
	return render_template("home.html", user=user)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
		return redirect('/home')

	return render_template('login.html',
		form = form,
		providers =  app.config['OPENID_PROVIDERS'])
