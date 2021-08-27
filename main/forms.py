from flask_wtf import FlaskForm
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
    username=StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    password=PasswordField('Password', validators=[DataRequired(), Length(min=1, max=20)])

    login_submit = SubmitField("Log In")
