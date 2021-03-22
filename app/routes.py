from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Daphne"}
    posts = [
        {
            "author": {"username": "Anthony"},
            "body": "The Duke of Hastings is a rake.  He's not suitable for you."
        },
        {
            "author": {"username": "Daphne"},
            "body": "I propose an agreement.  You pretend to court me.  That will give you peace from the mamas of the ton.  Having a duke pursue me will allow me to attract more suitors."
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('We received login request for user {}, remember_me {}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)


@app.route('/ox')
def ox():
    return "Olly olly oxen free!"


@app.route('/bridgerton')
def bridgerton():
    return "Good afternoon, Your Grace.  [deep bow]"
