from flask import render_template, request,flash, redirect, url_for
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# print(os.environ['APP_SETTINGS'])

import models 

@app.route('/')
def index():
    return "GigTank!"

@app.route('/portal')
def portal():
    return render_template('/portal.html')

if __name__ == '__main__':
    app.run()
