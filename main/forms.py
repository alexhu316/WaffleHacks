from flask_wtf import FlaskForm
from flask_login import current_user
from main.models import User
from main import db
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class RegisterAccount(FlaskForm):
    username=StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    password=PasswordField('Password', validators=[DataRequired(), Length(min=1, max=20)])
    signup_submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
    

class LogInAccount(FlaskForm):
    username=StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password=PasswordField('Password', validators=[DataRequired(), Length(min=1, max=20)])

    login_submit = SubmitField("Log In")


class UpdateSponsorInfo(FlaskForm):
    interests = ['Education', 'Technology', 'Mathematics', 'Health', 'Physical Activity', 'Computers', 'Sports', 'Gaming', 'Leadership', 'Finance', 'Law', 'Business']
    name=StringField('Business Name', validators=[DataRequired(), Length(min=3)])
    email=StringField('Email', validators=[DataRequired(), Length(min=3)])
    phone=StringField('Phone Number', validators=[DataRequired(), Length(min=10)])
    address=StringField('Address', validators=[DataRequired(), Length(min=3)])
    website=StringField('Website', validators=[DataRequired()])
    description=StringField('Enter business description', validators=[DataRequired()])
    submit = SubmitField("Save")


class UpdateSponseeInfo(FlaskForm):
    interests = ['Education', 'Technology', 'Mathematics', 'Health', 'Physical Activity', 'Computers', 'Sports', 'Gaming', 'Leadership', 'Finance', 'Law', 'Business']
    name=StringField('Organization Name', validators=[DataRequired(), Length(min=3)])
    email=StringField('Email', validators=[DataRequired(), Length(min=3)])
    phone=StringField('Phone Number', validators=[DataRequired(), Length(min=10)])
    address=StringField('Address', validators=[DataRequired(), Length(min=3)])
    website=StringField('Website', validators=[DataRequired()])
    description=StringField('Enter organization description', validators=[DataRequired()])
    submit = SubmitField("Save")


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit_post = SubmitField("Post")
