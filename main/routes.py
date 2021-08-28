from flask import render_template, url_for, redirect, flash, request
from main.forms import RegisterAccount, LogInAccount, UpdateSponsorInfo
from main.models import User
from main import db
from main import app
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'Alex Hu',
        'title': 'Blog Post 1',
        'content': "I'm awesome, I'm cool",
        'date': 'August 19, 2021'
    },
    {
        'author': 'Jennifer Ying',
        'title': 'Blog Post 2',
        'content': "I'm a stinky poo poo head",
        'date': 'August 20, 2021'
    }
]

@app.route("/", methods=['GET', 'POST'])
def home():
    # return redirect(url_for('register'))
    return render_template("home.html", posts = posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterAccount()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data, user_type = str(request.form.get('type-select')))
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        return redirect(url_for('home'))

    return render_template("register.html", form = form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LogInAccount()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=True)
            return redirect(url_for('home'))
        else:
            flash("login unsuccessful")
    return render_template("login.html", form = form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account_sponsor")
@login_required
def account_sponsor():
   form = UpdateSponsorInfo()
   if form.validate_on_submit():
       pass
  
   return render_template('account_sponsor.html',form = form)



@app.route("/account_sponsee")
@login_required
def account_sponsee():
    form = UpdateSponsorInfo()
    return render_template('account_sponsee.html')


