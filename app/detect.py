from unittest import result

from numpy import record
from app import app, db, session
from db.model import Records
from flask import render_template, request , redirect, url_for

import pickle
import pandas as pd
import re
import string
import datetime

vectorization = pickle.load(open('static/model/vector_model.sav','rb'))
linear_clf = pickle.load(open('static/model/model_lc.sav','rb'))
DT = pickle.load(open('static/model/model_dt.sav','rb'))
GBC = pickle.load(open('static/model/model_gbc.sav','rb'))
LR = pickle.load(open('static/model/model_lr.sav','rb'))
#RFC = pickle.load(open('model_rfc.sav','rb'))
def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text

def detect_text(news):
    new_x_test = [wordopt(news)]
    new_xv_test = vectorization.transform(new_x_test)
    pred_LR = LR.predict(new_xv_test)
    pred_DT = DT.predict(new_xv_test)
    pred_GBC = GBC.predict(new_xv_test)
    #pred_RFC = RFC.predict(new_xv_test)
    if [pred_DT[0],pred_GBC[0],pred_LR[0]].count(0)>2:
        return 1
    else: return 2
    print(pred_LR, pred_DT, pred_GBC)

    

@app.route('/detect',methods=["GET", "POST"] )
def detect():
    
    if request.method == "POST":

        if request.form.get('submitnews'):
            news = request.form.get('news')
            result = detect_text(news)
            #datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            new_record = Records(
                data = news,
                date = datetime.datetime.utcnow(),
                account_id  = session['user'],
                datatype_id = 1,
                app_id      =6,
                detect_id   = result
            )
            db.session.add(new_record)
            db.session.commit()

            return render_template('detect.html',r1=result,flag=1)
        
        elif request.form.get('submitmsg'):

            app = request.form['apps']
            messages = request.form.get('message')
            date = request.form['date'] 
            d = date.split('T')
            d[0] = d[0].split('-')
            d[1] = d[1].split(':')
            print('date',d)
            #print('todays',datetime.datetime.utcnow(),type(datetime.datetime.utcnow()))
            result = detect_text(messages)

            new_record = Records(
                data = messages,
                date = datetime.datetime( int(d[0][0]) , int(d[0][1]), int(d[0][2]), int(d[1][0]) ,int(d[1][1]) ),
                account_id  = session['user'],
                datatype_id = 2,
                app_id      = app,
                detect_id   = result
            )
            db.session.add(new_record)
            db.session.commit()

            return render_template('detect.html',r4=result)
    
    else:
        if 'user' not in session:
            return redirect( url_for('login') )
   
    return render_template('detect.html')