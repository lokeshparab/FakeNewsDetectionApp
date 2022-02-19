from app import app, db, session
from db.model import Account
from flask import render_template, request, redirect, url_for

@app.route('/profile')
def profile():

   # user_detail = db.session.query(Account).filter_by(username=session['user']).first()
    return render_template('profile.html')

@app.route('/view')
def view():
    return render_template('view.html')