from datetime import datetime
from flask import render_template, url_for, redirect, flash, request
from main.forms import RegisterAccount, LogInAccount, UpdateSponsorInfo, UpdateSponseeInfo, PostForm
from main.models import User, Post
from main import db
from main import app
from flask_login import login_user, current_user, logout_user, login_required


all_users = User.query.all()



 
@app.route("/", methods=['GET', 'POST'])
def home():
   
    return render_template("home.html")
 

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
 
 
@app.route("/account_sponsor", methods=['GET', 'POST'])
@login_required
def account_sponsor():
  form = UpdateSponsorInfo()
  if form.validate_on_submit():
      user = User.query.filter_by(id=current_user.id).first()
      user.name=form.name.data
      user.address=form.address.data
      user.phone=form.phone.data
      user.email=form.email.data
      user.website=form.website.data
      user.description=form.description.data
      user.email=form.email.data
      if request.form.get('Education'):
          user.education = True
      if request.form.get('Technology'):
          user.technology = True 
      if request.form.get('Mathematics'):
          user.mathematics = True
      if request.form.get('Health'):
          user.health = True
      if request.form.get('Sports'):
          user.sports = True
      if request.form.get('Gaming'):
          user.gaming = True
      if request.form.get('Leadership'):
          user.leadership = True
      if request.form.get('Business'):
          user.business = True
      db.session.commit()

  return render_template('account_sponsor.html', form = form)

 
 
 
@app.route("/account_sponsee", methods=['GET', 'POST'])
@login_required
def account_sponsee():
   form = UpdateSponseeInfo()
   if form.validate_on_submit():
      user = User.query.filter_by(id=current_user.id).first()
      user.name=form.name.data
      user.address=form.address.data
      user.phone=form.phone.data
      user.email=form.email.data
      user.website=form.website.data
      user.description=form.description.data
      user.email=form.email.data
      if request.form.get('Education'):
          user.education = True
      if request.form.get('Technology'):
          user.technology = True 
      if request.form.get('Mathematics'):
          user.mathematics = True
      if request.form.get('Health'):
          user.health = True
      if request.form.get('Sports'):
          user.sports = True
      if request.form.get('Gaming'):
          user.gaming = True
      if request.form.get('Leadership'):
          user.leadership = True
      if request.form.get('Business'):
          user.business = True
      db.session.commit()

   return render_template('account_sponsee.html',form = form)
 
 
@app.route("/make_post", methods=['GET', 'POST'])
@login_required
def make_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data, description = form.description.data, user_id = current_user.id)
        db.session.add(post)
        db.session.commit()

    return render_template('make_post.html',form = form)


@app.route("/find_sponsors", methods=['GET', 'POST'])
@login_required
def find_sponsors():
    return render_template('find_sponsors.html', users = all_users)


@app.route("/find_sponsees", methods=['GET', 'POST'])
@login_required
def find_sponsees():
      posts = Post.query.all()
      sorted_posts = sorted(posts, key=lambda by_date: by_date.post_date, reverse=True)
      return render_template('find_sponsees.html', posts = sorted_posts)
  
# {%for user in users}
# {%if user.user_type == 'Sponsor'}
#     <h1>user.name</h1>
#     <h1>user.phone</h1>
#     <h1>user.address</h1>
# {%endif%}
# {%endfor%}
