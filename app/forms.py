from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired

class MyForm(FlaskForm):
  "uploading photo along with description"
  description =TextAreaField('description', validators=[InputRequired()])
  photo = FileField('photo',  validators=[FileAllowed(['jpg', 'png']),FileRequired()])