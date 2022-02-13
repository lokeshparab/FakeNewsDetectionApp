#import imp
#from unittest import result
#from crypt import methods
#from email import message
#from pyexpat.errors import messages
from flask import Flask, render_template, request, redirect, url_for
from app import detect_text
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('homepage.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/aboutus', methods=['GET'])
def aboutus():
    return render_template('aboutus.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/detect',methods=["GET", "POST"] )
def detect():
    
    if request.method == "POST":

        news = request.form.get('news')
        app = request.form.get('apps')
        messages = request.form.get('message')

        if news== None:

            r1,r2,r3 = detect_text(messages)
            return render_template('detect.html',r4=r1 ,rt5=r2, r6=r3)

        else:

            r1,r2,r3 = detect_text(news)
            return render_template('detect.html',r1=r1 ,rt2=r2, r3=r3)
   
    return render_template('detect.html')

@app.route('/view')
def view():
    return render_template('view.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')



if __name__ == '__main__':
    app.run(debug=True)