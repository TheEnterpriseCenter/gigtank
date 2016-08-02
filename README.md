SETUP- For the initial setup, you should have some familiarity with the following tools: 
• Virtualenv – http://www.virtualenv.org/en/latest/ 
• Flask – http://flask.pocoo.org/ 
• git/Github – http://try.github.io/levels/1/challenges/1 
• Heroku (basics) – https://devcenter.heroku.com/articles/getting-started-with-python 
• Python 2.7 and pip as well. • Heroku toolbelt - https://toolbelt.heroku.com/ 
• Node Package Manager - npm • Webpack - http://webpack.github.io/docs/installation.html

Set up a virtual environment - I use autoenv, but it is up to you - 
The env variables I use are in the .env file if you set your own. 
$ virtualenv venv

Activate the env …or deactivate(when done working) 

$ pip install requests

Now freeze your current package state 
$ pip freeze > requirements.txt

run real requirements 
$ pip install -r requirements.txt

Install Flask for this project 
$ pip install Flask==0.10.1

freeze requirements again 
$ pip freeze > requirements.txt

Run basic server then open http://127.0.0.1:5000/ 
$ python app.py http://localhost:5000/

add npm - $ npm install
add Webpack - $ npm install webpack -g
pip install gunicorn==19.4.5

If you have questions about requirements check the requirements.txt file
Dont forget to use enviornment variables if you are deployon heroku. 
