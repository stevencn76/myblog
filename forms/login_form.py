from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField(label="用户名:", validators=[DataRequired()])
    password = PasswordField(label="密码:", validators=[DataRequired()])
    submit = SubmitField(label="登陆")
