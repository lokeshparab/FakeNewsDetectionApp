#import imp
#from unittest import result
#from crypt import methods
#from email import message
#from pyexpat.errors import messages
#from crypt import methods
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mail import Mail, Message
from app import *
import random
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


app.config['MAIL_SERVER'] = os.environ['MAIL_SERVER']
app.config['MAIL_PORT'] = os.environ['MAIL_PORT']
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_DEFAULT_SENDER'] = os.environ['MAIL_USERNAME']
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
mail = Mail(app)

app.secret_key = str(random.randint(111, 999)).encode()



def send_email(name,email,subject):

    msg = Message(
                name+' query from '+ email,
                sender = email,
                recipients = ['vu1f1819026@pvppcoe.ac.in'],
                body = subject
               )
    mail.send(msg)


@app.route('/', methods=['GET'])
def home():
    return render_template('homepage.html')


@app.route('/login', methods=['GET'])
def login():

    if request.method == 'POST':

        if request.form.get('login'):

            user = request.form['username']
            pwd = request.form['password']

        elif request.form.get('register'):

            fname = request.form['name']
            gender = request.form['gender']
            age = request.form['age']
            email = request.form['email']
            user = request.form['user']
            pwd = request.form['pwd']

        session['user'] = user

    else:
        pass

    return render_template('login.html')


@app.route('/login/forgetpassword')
def changepass():

    if request.method == 'POST':
        pass
    return render_template('changepass.html')

@app.route('/aboutus', methods=['GET'])
def aboutus():
    return render_template('aboutus.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/detect',methods=["GET", "POST"] )
def detect():
    
    if request.method == "POST":

        if request.form.get('submitnews'):
            news = request.form.get('news')
            r1,r2,r3 = detect_text(news)
            return render_template('detect.html',r1=r1 ,rt2=r2, r3=r3,flag=1)
        
        elif request.form.get('submitmsg'):
            messages = request.form.get('message')
            r1,r2,r3 = detect_text(messages)
            return render_template('detect.html',r4=r1 ,rt5=r2, r6=r3)
    
    else:
        pass
   
    return render_template('detect.html')

@app.route('/detect/result')
def result():
    return render_template('result.html')

@app.route('/view')
def view():
    return render_template('view.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/contact' , methods=["GET","POST"])
def contact():

    if request.method == 'POST' and request.form.get('submit'):
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']

        send_email(name,email,subject)

    return render_template('contact.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')



if __name__ == '__main__':
    app.run(debug=True)