from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField, validators
from wtforms.validators import DataRequired, Email, EqualTo, email_validator
from wtforms import ValidationError
from web.model import User
from flask_pagedown.fields import PageDownField

# 登入
class LoginForm(FlaskForm):
    email = StringField('信箱', validators=[DataRequired(), Email()])
    password = PasswordField('密碼',validators=[DataRequired()])
    remember_me = BooleanField('保持登入')
    submit = SubmitField('登入')

# 註冊
class RegForm(FlaskForm):
    email = StringField('註冊信箱', validators=[DataRequired(), Email()])
    username = StringField('您的暱稱', validators=[DataRequired()])
    password = PasswordField('註冊密碼', validators=[DataRequired(), EqualTo('pass_confirm', message='密碼需要吻合')])
    pass_confirm = PasswordField('確認密碼', validators=[DataRequired()])
    submit = SubmitField('註冊')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('電子郵件已經被註冊過了')
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('使用者名稱已經存在')