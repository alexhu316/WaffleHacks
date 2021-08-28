from main import db, login_manager
from datetime import datetime
from flask_login import UserMixin
 

def fits_criteria(checked_boxes, post):
   matches = 0
   if checked_boxes[0]:
      if post.education:
         matches+=1
   if checked_boxes[1]:
      if post.technology:
         matches+=1
   if checked_boxes[2]:
      if post.math:
         matches+=1
   if checked_boxes[3]:
      if post.health:
         matches+=1
   if checked_boxes[4]:
      if post.sports:
         matches+=1
   if checked_boxes[5]:
      if post.gaming:
         matches+=1
   if checked_boxes[6]:
      if post.leadership:
         matches+=1
   if checked_boxes[7]:
      if post.business:
         matches+=1
   return matches
   

 
@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))
 
 
class User(db.Model, UserMixin):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(20), unique=True, nullable=False)
   password = db.Column(db.String(60), nullable=False)
   user_type = db.Column(db.String(7), nullable=False)
   name = db.Column(db.String(30))
   phone = db.Column(db.String(15))
   address = db.Column(db.String(40))
   website = db.Column(db.String(30))
   email = db.Column(db.String(30))
   description = db.Column(db.String(200))
   education = db.Column(db.Boolean)
   technology = db.Column(db.Boolean)
   mathematics = db.Column(db.Boolean)
   health = db.Column(db.Boolean)
   sports = db.Column(db.Boolean)
   gaming = db.Column(db.Boolean)
   leadership = db.Column(db.Boolean)
   business = db.Column(db.Boolean)
   posts = db.relationship('Post', backref='author', lazy=True)
   def __repr__(self):
       return (f'{self.username}, {self.password}')


class Post(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(30),nullable = False)
   description = db.Column(db.String(200),nullable = False)
   post_date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   education = db.Column(db.Boolean)
   technology = db.Column(db.Boolean)
   mathematics = db.Column(db.Boolean)
   health = db.Column(db.Boolean)
   sports = db.Column(db.Boolean)
   gaming = db.Column(db.Boolean)
   leadership = db.Column(db.Boolean)
   business = db.Column(db.Boolean)