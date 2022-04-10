from app import app, db, session
from flask import render_template, request , redirect, url_for
import pandas as pd
import os

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    print(os.listdir())
    df = pd.read_csv("static/analysis/AnalysisofNews.csv")
    channels = list(df['newschannel'].values)
            
    labels =["08-01-2021",
            "09-01-2021",
            "10-01-2021",
            "11-01-2021",
            "12-01-2021",
            "01-01-2022",
            "02-01-2022",
            "03-01-2022",
            "04-01-2022"]
            
    values =[1597,
            1456,
            1908,
            896,
            755,
            453,
            1100,
            1235,
            1478]
    
    if request.method == 'GET':

        if 'user' in session:
            
            return render_template('dashboard.html', labels = labels, values=values, channels=channels)
        else: return redirect( url_for('login'))
    else:
        if 'user' in session:
            if request.form.get('submit'):
                channel = request.form.get('newschannel')
                data = df[df['newschannel']==channel].values[0]
                real = data[1] / ( data[1] + data[2] ) * 100
                fake = data[2] / ( data[1] + data[2] ) * 100
                dataset = [real,fake]
            return render_template('dashboard.html', labels = labels, values=values, channels=channels , dataset= dataset)
        else: return redirect( url_for('login'))