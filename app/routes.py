from flask import render_template, flash, redirect, url_for
from flask_login import login_user, current_user
from app import app, db
from app.forms import LoginForm
from app.models import User


@app.route('/')
@app.route('/index')
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
            return redirect(url_for('index'))

        # Invalid username or password
        else:
            flash("Invalid username or password")
            return redirect(url_for('login'))

    # Invalid form
    return render_template('login.html', title='Login', form=form)


@app.route('/ox')
def ox():
    return "Olly olly oxen free!"


@app.route('/bridgerton')
def bridgerton():
    return "Good afternoon, Your Grace.  [deep bow]"
