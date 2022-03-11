#import imp
#from unittest import result
#from crypt import methods
#from email import message
#from pyexpat.errors import messages
#from crypt import methods
from flask import render_template, request, redirect, url_for
#from flask_mail import Mail, Message
from app import app, session
from app.detect import *
from app.contact import *
from app.login import *
from app.view_profile import *



@app.route('/', methods=['GET'])
def home():
    return render_template('homepage.html')


@app.route('/aboutus', methods=['GET'])
def aboutus():
    return render_template('aboutus.html')

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html')
    else: return redirect( url_for('login'))
    

@app.route('/logout', methods=['GET','POST'])
def logout():
    session.pop('user', None)
    message = 'Logged out succesfully'
    return redirect(url_for('home', message=message))

@app.route('/detect/result')
def result(app,data,newlink,date,result):
    return render_template('result.html',app,data,newlink,date,result)



@app.route('/help')
def help():
    if 'user' in session:
        return render_template('help.html')
    else: 
        return redirect( url_for('login'))






if __name__ == '__main__':
    app.run(debug=True)