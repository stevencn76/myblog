from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField


class ImageUploadForm(FlaskForm):
    image_file = FileField(label="选择图片:", validators=[FileRequired()])
    submit = SubmitField(label="上传")
