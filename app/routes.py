from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'Anthony'},
            'body': 'The Duke of Hastings is a rake.  He is not suitable for you.'
        },
        {
            'author': {'username': 'Daphne'},
            'body': 'I propose an agreement.  You pretend to court me.  That will give you peace from the mamas of the ton.  Having a duke pursue me will allow me to attract more suitors.'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # If user currently log in, don't let them log in a second time
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # Display form for a user who's not yet logged in
    form = LoginForm()

    # Valid form
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        # Valid username and password
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)

        # Invalid username or password
        else:
            flash("Invalid username or password")
            return redirect(url_for('login'))

    # Invalid form
    return render_template('login.html', title='Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    # If user currently log in, don't let them log in a second time
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # Present the registration form
    form = RegistrationForm()

    # Check if all fields are kosher.  If so, register user.
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/ox')
def ox():
    return "Olly olly oxen free!"


@app.route('/bridgerton')
@login_required
def bridgerton():
    return "Good afternoon, Your Grace.  [deep bow]"
