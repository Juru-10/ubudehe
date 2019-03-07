from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class SearchForm(FlaskForm):
    ID = StringField('Search',validators=[Required()])
    submit = SubmitField('Submit')
