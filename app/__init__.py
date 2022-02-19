from flask import Flask, render_template, request, redirect, url_for, session
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import random
import os

load_dotenv()

app = Flask(__name__, template_folder = '../templates')

app.static_folder = '../static'
app.secret_key = str(random.randint(111, 999)).encode()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../db/data.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

app.config['MAIL_SERVER'] = os.environ['MAIL_SERVER']
app.config['MAIL_PORT'] = os.environ['MAIL_PORT']
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_DEFAULT_SENDER'] = os.environ['MAIL_USERNAME']
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
mail = Mail(app)

def session_check(page): return 'user' in session



#def email_validate(email):
 #   pass



#def send_email(name,email,subject):

 #   if email_validate(email):
  #      # send email to company
   #     pass

    #else:
        # display flash message for invalid email
     #   pass   
