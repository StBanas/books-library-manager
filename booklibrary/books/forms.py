from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class BookForm(FlaskForm):
    author = StringField('Author', validators=[DataRequired(), Length(min=2, max=40)])
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=60)])
    ocr_text = TextAreaField('Text extracted from cover of book')
    submit = SubmitField('Save')


class TopForm(FlaskForm):
    author1 = StringField('Author', validators=[DataRequired(), Length(min=2, max=40)])
    title1 = StringField('Title', validators=[DataRequired(), Length(min=1, max=60)])
    submit = SubmitField('Insert')
