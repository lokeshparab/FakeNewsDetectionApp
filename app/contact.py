from app import app, mail
from flask import render_template, request
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

    return render_template('contact.html')