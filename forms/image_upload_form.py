from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class ImageUploadForm(FlaskForm):
    image_file = FileField(label="选择图片:", validators=[FileRequired()])
    submit = SubmitField(label="上传")
