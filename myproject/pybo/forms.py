from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    subject = StringField('title', validators=[DataRequired('require title')])
    content = TextAreaField('content', validators=[DataRequired('require content')])

class AnswerForm(FlaskForm):
    content = TextAreaField('content', validators=[DataRequired('require content')])