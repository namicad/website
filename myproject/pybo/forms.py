from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo

class QuestionForm(FlaskForm):
    subject = StringField('title', validators=[DataRequired('require title')])
    content = TextAreaField('content', validators=[DataRequired('require content')])

class AnswerForm(FlaskForm):
    content = TextAreaField('content', validators=[DataRequired('require content')])

class UserCreateForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('password', validators=[DataRequired(), EqualTo('password2', 'Password does not match.')])
    password2 = PasswordField('check password', validators=[DataRequired()])

class LoginForm(FlaskForm):
    id = StringField('id', validators=[DataRequired(), Length(min=3, max=25)])