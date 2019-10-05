from flask_wtf import FlaskForm
from wtforms  import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, email, EqualTo



class RegistrationsForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), length(min=5, max=10)])
    email = StringField('email', validators=[DataRequired(), email()])
    password = PasswordField('passwprd', validators=[DataRequired()])
    confirm_password = PasswordField('confirm password', validators=[DataRequired(), EqualTo('password')])

    sumbit = SubmitField('signup')


class LoginForm(FlaskForm):
   
    email = StringField('email', validators=[DataRequired(), email()])
    password = PasswordField('passwprd', validators=[DataRequired()])
    remember = BooleanField('Remember me')


    sumbit = SubmitField('signup')
