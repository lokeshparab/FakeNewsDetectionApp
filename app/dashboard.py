from app import app, db, session
from flask import render_template, request , redirect, url_for

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    
    if request.method == 'GET':

        if 'user' in session:

            labels =["01-01-2020",
                     "02-01-2020",
                     "03-01-2020",
                     "04-01-2020",
                     "05-01-2020",
                     "06-01-2020",
                     "07-01-2020",
                     "08-01-2020",
                     "00-01-2020"]
            
            values =[1597,
                     1456,
                     1908,
                     896,
                     755,
                     453,
                     1100,
                     1235,
                     1478]
            return render_template('dashboard.html', labels = labels, values=values)
        else: return redirect( url_for('login'))