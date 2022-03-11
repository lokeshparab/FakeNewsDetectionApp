from app import app, db, session
from db.model import Account
import hashlib

import re
import random
from flask import redirect, render_template, request, session, url_for


def register(fname,gender,age,email,user,pwd):

    existing_email = db.session.query(Account.email).filter_by(email=email).first()
    if existing_email is not None: 
        message = f"email {email} already exists."
    else:

        pwd = hashlib.sha256(pwd.encode()).hexdigest()

        new_account = Account(
					fname=fname, gender=gender, age=age,  email=email, username=user, password=pwd
				)
        db.session.add(new_account)
        db.session.commit()
        message = 'Registered succesfully, login to continue'
    return message

def login_detail(user,pwd):

    user_detail = db.session.query(Account).filter_by(username=user).first()

    if not user_detail:
        message = f"username {user} doesn't exists."

    elif user_detail.password != hashlib.sha256(pwd.encode()).hexdigest():
        message = "You have entered wrong password"

    else:
        session['user'] = user_detail.id
        message = 'Logged in succesfully'

    return message


@app.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'POST':

        if request.form.get('login'):

            user = request.form['username']
            pwd = request.form['password']

            if len(user)>0 and len(pwd)>0:
                message = login_detail(user,pwd)
                return redirect( url_for('dashboard',message=message) )

        elif request.form.get('register'):

            fname = request.form['fname']
            gender = request.form['gender']
            age = request.form['age']
            email = request.form['email']
            user = request.form['user']
            pwd = request.form['pwd']
            cpwd = request.form['cpwd']
            #validate entered data

            print('form')

            if len(fname) > 0 and len(gender)>0 and int(age)>0 and  re.fullmatch("^([a-zA-Z0-9\._-]+)@([a-zA-Z0-9-]+)(\.[a-z]+)?(\.([a-z]+))$", email) and len(pwd) > 0:
                if pwd != cpwd:
                    message = "Passwords entered do not match."
                else:
                    message = register(fname,gender,age,email,user,pwd)
    else:
        message = ''

        if 'user' in session: return redirect( url_for('dashboard',message=message) )


    return render_template('login.html',message=message)



@app.route('/login/forgetpassword', methods=['GET','POST'])
def changepass():

    if request.method == 'POST':
        pass
    return render_template('changepass.html')