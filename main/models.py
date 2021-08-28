from main import db, login_manager
from flask_login import UserMixin
 
 
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
   def __repr__(self):
       return (f'{self.username}, {self.password}')
