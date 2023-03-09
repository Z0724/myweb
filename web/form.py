from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired

from flask_pagedown.fields import PageDownField

# 首頁更新留言板
class IndexMessageForm(FlaskForm):
    mb_message = PageDownField('內容',validators=[DataRequired()])
    submit = SubmitField('送出')
