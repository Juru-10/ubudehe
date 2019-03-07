from flask import Flask
from flask import render_template,request,redirect,url_for,abort
from ..models import User,Citizen,Searched
from . import main
from .forms import SearchForm
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

# @main.route('/user/<uname>/')
# def profile(uname):
#     user = User.query.filter_by(username = uname).first()
#
#     if user is None:
#         abort(404)
#
#     return render_template("profile/profile.html", user = user)
#
# @main.route('/user/<uname>/update/bio',methods = ['GET','POST'])
# @login_required
# def update_bio(uname):
#     user = User.query.filter_by(username = uname).first()
#     if user is None:
#         abort(404)
#
#     form = UpdateProfile()
#
#     if form.validate_on_submit():
#         user.bio = form.bio.data
#
#         db.session.add(user)
#         db.session.commit()
#
#         return redirect(url_for('.profile',uname=user.username))
#
#     return render_template('profile/update_bio.html',form =form)

@main.route('/search',methods= ['GET','POST'])
@login_required
def search():

    search_form = SearchForm()
    citizen = None
    if search_form.validate_on_submit():
        citizen = Citizen.query.filter_by(ID = search_form.ID.data).first()
        # print(citizen.status)
        # return redirect(url_for('main.search'))

    title = "citizens search"
    return render_template('search.html',search_form = search_form,title=title, citizen=citizen)


def search_citizen(ID):
    citizen = Citizen.query.filter_by(ID = ID).first()
    search_citizen_results = None

    if search_citizen_response['citizens']:
        search_citizen_list = search_citizen_response['citizens']
        search_citizen_results = citizen(fname,lname,ID,insurance)


    return search_citizen_results
