from flask import Flask
from flask import render_template,request,redirect,url_for,abort
from ..models import User,Citizen
from . import main
from .forms import SearchForm,AdminForm
from .. import db,photos
from flask_login import login_required,current_user
import markdown2

@main.route('/',methods = ['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The citizens Website Online'

    return render_template('index.html', title = title)

@main.route('/about',methods = ['GET','POST'])
def about():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'About UIP'

    return render_template('about.html', title = title)

@main.route('/search',methods= ['GET','POST'])
@login_required
def search():

    search_form = SearchForm()
    citizen = None
    if search_form.validate_on_submit():
        citizen = Citizen.query.filter_by(ID = search_form.ID.data).first()
    title = "citizens search"
    return render_template('search.html',search_form = search_form,title=title, citizen=citizen)
