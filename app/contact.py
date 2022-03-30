from app import app, mail, session
from flask import render_template, request , redirect, url_for
from flask_mail import Message

def send_email(name,email,subject):

    msg = Message(
                name+' query from '+ email,
                sender = email,
                recipients = ['vu1f1819026@pvppcoe.ac.in'],
                body = subject
               )
    mail.send(msg)

@app.route('/contact' , methods=["GET","POST"])
def contact():

    if request.method == 'POST' and request.form.get('submit'):
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']

        send_email(name,email,subject)

    else:
        if 'user' not in session:
            return redirect( url_for('login') )

    return render_template('contact.html')