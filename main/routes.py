from datetime import datetime
from flask import render_template, url_for, redirect, flash, request
from main.forms import RegisterAccount, LogInAccount, UpdateSponsorInfo, UpdateSponseeInfo, PostForm, FilterSponsees
from main.models import User, Post, fits_criteria
from main import db
from main import app
from flask_login import login_user, current_user, logout_user, login_required




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
       all_users = User.query.all()
       flash("You have registered!")
       return redirect(url_for('account'))
 
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
           flash("You have logged in!")
           return redirect(url_for('home'))
       else:
           flash("Incorrect username/password")
   return render_template("login.html", form = form)
 
 
@app.route("/logout")
def logout():
   logout_user()
   flash("You have signed out!")
   return redirect(url_for('home'))


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    if current_user.user_type=='Sponsor':
        return redirect(url_for('account_sponsor'))
    else:
        return redirect(url_for('account_sponsee'))

 
 
@app.route("/account_sponsor", methods=['GET', 'POST'])
@login_required
def account_sponsor():
  form = UpdateSponsorInfo()
  if current_user.name:
      form.name.data=current_user.name
  if current_user.address:
      form.address.data=current_user.address
  if current_user.phone:
      form.phone.data=current_user.phone
  if current_user.email:
      form.email.data=current_user.email
  if current_user.website:
      form.website.data=current_user.website
  if current_user.description:
      form.description.data=current_user.description
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
      return redirect(url_for('home'))


  return render_template('account_sponsor.html', form = form)

 
 
@app.route("/account_sponsee", methods=['GET', 'POST'])
@login_required
def account_sponsee():
    form = UpdateSponseeInfo()
    if current_user.name:
        form.name.data=current_user.name
    if current_user.address:
        form.address.data=current_user.address
    if current_user.phone:
        form.phone.data=current_user.phone
    if current_user.email:
        form.email.data=current_user.email
    if current_user.website:
        form.website.data=current_user.website
    if current_user.description:
        form.description.data=current_user.description
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
      return redirect(url_for('home'))

    return render_template('account_sponsee.html', form = form)
 
 
@app.route("/make_post", methods=['GET', 'POST'])
@login_required
def make_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data, description = form.description.data, user_id = current_user.id)
        if request.form.get('Education'):
            post.education = True
        if request.form.get('Technology'):
            post.technology = True 
        if request.form.get('Mathematics'):
            post.mathematics = True
        if request.form.get('Health'):
            post.health = True
        if request.form.get('Sports'):
            post.sports = True
        if request.form.get('Gaming'):
            post.gaming = True
        if request.form.get('Leadership'):
            post.leadership = True
        if request.form.get('Business'):
            post.business = True
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('find_sponsees'))
    return render_template('make_post.html', form = form)


@app.route("/find_sponsors", methods=['GET', 'POST'])
@login_required
def find_sponsors():
    all_users = User.query.all()


    return render_template('find_sponsors.html', users = all_users[::-1])


@app.route("/find_sponsees", methods=['GET', 'POST'])
@login_required
def find_sponsees():
      form = FilterSponsees()
      posts = Post.query.all()
      sorted_posts = sorted(posts, key=lambda by_date: by_date.post_date, reverse=True)
      if form.validate_on_submit():
          num_checked = 0
          checked = [False for i in range(8)]
          if request.form.get('Education'):
              checked[0]=True
              num_checked+=1
          if request.form.get('Technology'):
              checked[1]=True
              num_checked+=1
          if request.form.get('Mathematics'):
              checked[2]=True
              num_checked+=1
          if request.form.get('Health'):
              checked[3]=True
              num_checked+=1
          if request.form.get('Sports'):
              checked[4]=True
              num_checked+=1
          if request.form.get('Gaming'):
              checked[5]=True
              num_checked+=1
          if request.form.get('Leadership'):
              checked[6]=True
              num_checked+=1
          if request.form.get('Business'):
              checked[7]=True
              num_checked+=1
          
          if num_checked==0:
            sorted_posts = sorted(posts, key=lambda by_date: by_date.post_date, reverse=True)
            return render_template('find_sponsees.html', form = form, posts = sorted_posts)
          else:
            filtered_posts = []
            for i in range(num_checked+1,0,-1):
                filtered_posts.append(post for post in posts if fits_criteria(checked, post)==num_checked)
          return render_template('find_sponsees.html', form = form, posts = filtered_posts)
      return render_template('find_sponsees.html', form = form, posts = sorted_posts)