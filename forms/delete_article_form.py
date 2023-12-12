from flask_wtf import FlaskForm
from wtforms import HiddenField, SubmitField
from wtforms.validators import DataRequired


class DeleteArticleForm(FlaskForm):
    article_id = HiddenField(validators=[DataRequired()])
    submit = SubmitField(label="删除")
