from flask import render_template, request,flash, redirect, url_for
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
import models 

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# print(os.environ['APP_SETTINGS'])


@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/about')
def about():
    return render_template('/about.html')

@app.route('/portal', methods=['POST', 'GET'])
def portal():
    if request.method == 'POST':
        video=Video(request.form['title'], request.form['slide_summary'])
        db.session.add(video)
        db.session.commit()
        flash('New entry was successfully posted')     

    return render_template('/portal.html')

if __name__ == '__main__':
    app.run()
