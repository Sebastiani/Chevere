from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from Chevere import app, db, lm, oid
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN

user =  {'name': 'Sebastiani', 'lastname':'Aguirre'}


@app.route('/home')
def index():
	return render_template("home.html", user=user)

@app.route('/signin', methods = ['POST']
def signin():
	#here goes the make account function, based on the login below.
	
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('index'))
		
	form = LoginForm()
	if form.validate_on_submit():
		session['remember_me'] =  form.remember_me.data
		return oid.try_login(form.openid.data, ask_for = ['name', 'email']) #if successful, it will asynchronously call @after_login

	return render_template('login.html',
		form = form,
		providers =  app.config['OPENID_PROVIDERS'])
		
@oid.after_login
def after_login(resp):    #resp is the response sent by the oid.try_login 
	if resp.email is None or resp.email == "":
		flash('Invalid login. Please try again.')
		return redirect(url_for('login'))
	user = User.query.filter_by(email = resp.email).first()
	if user is None:
		name =  resp.name
		if nickname is None or nickname == "":
			name = resp.email.split('@')[0]
			user = User(name = name, email = resp.email, role =  ROLE_USER) #User(fields1, fields2, ..)creates a new user in the db
			db.session.add(user)
			db.session.commit()
	remember_me = False
	if 'remember_me' in session:
		remember_me =  session['remember_me']
		session.pop('remember_me', None)
	login_user(user, remember = remember_me)
	return redirect(request.args.get('next') or url_for('index'))
	
@lm.user_loader
def load_user(id):
	return User.query.get(int(id))
