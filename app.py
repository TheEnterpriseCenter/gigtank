from flask import render_template, request, flash, redirect, url_for, redirect
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
import models 

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# print(os.environ['APP_SETTINGS'])

from models import *
import models

@app.route('/')
def index():
    return render_template('/index.html')
    
@app.route('/about')
def about():
    return render_template('/about.html')

# @app.route('/portal')
# def portal():
#     return render_template('/portal.html')

@app.route('/partners')
def partners():
    return render_template('/partners.html')

@app.route('/contact')
def contact():
    return render_template('/contact.html')

@app.route('/search', methods = ['GET'])
def search():
    search = ['search']
    # print("The search videao is '" + search + "'")
    return render_template('/search.html')
    # return redirect('/search.html')

@app.route('/workbook')
def workbook():
    return render_template('/workbook.html')

@app.route('/portal')
def portal():
    # if request.method == 'POST':
    #     video=Video(request.form['title'], request.form['slide_summary'])
    #     db.session.add(video)
    #     db.session.commit()
    #     flash('New entry was successfully posted')     

    return render_template('/portal.html')

if __name__ == '__main__':
    app.run()
