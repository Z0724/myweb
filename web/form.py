from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField, validators
from wtforms.validators import DataRequired, Email, EqualTo, email_validator
from wtforms import ValidationError
from web.model import User
from flask_pagedown.fields import PageDownField

# 首頁更新留言板
class IndexMessageForm(FlaskForm):
    mb_message = PageDownField('內容',validators=[DataRequired()])
    submit = SubmitField('送出')
