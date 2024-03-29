from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from puppycompanyblog.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo(
        'pass_confirm', message='Passwords must match!')])
    pass_confirm = PasswordField(
        'Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been registered already!')


class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('User Name', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[
                        FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user and user != current_user:
            raise ValidationError('Your email has been registered already!')

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user and user != current_user:
            raise ValidationError('Your username has been registered already!')
