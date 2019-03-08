from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class SearchForm(FlaskForm):
    ID = StringField('Search',validators=[Required()])
    submit = SubmitField('Submit')

class AdminForm(FlaskForm):
    fname = StringField('Search',validators=[Required()])
    lname = StringField('Search',validators=[Required()])
    ID = StringField('Search',validators=[Required()])
    category = SelectField('category',choices=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4')])
    status = SelectField('status',choices=[('Single','Single'),('Married','Married'),('Divorced','Divorced')])
    insurance = SelectField('insurance',choices=[('MS','Mutuel de Sante'),('RSSB','RSSB'),('MMI','MMI'),('Private','Private')])
    submit = SubmitField('Submit')
