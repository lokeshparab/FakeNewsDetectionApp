from email import message
from unittest import result

#from numpy import record
from app import app, db, session
from db.model import Datatype, Detect, Records, App
from flask import render_template, request , redirect, url_for

import pickle
#import pandas as pd
import re
import string
import datetime

import requests
from bs4 import BeautifulSoup


vectorization = pickle.load(open('static/model/vector_model.sav','rb'))
linear_clf = pickle.load(open('static/model/model_lc.sav','rb'))
DT = pickle.load(open('static/model/model_dt.sav','rb'))
GBC = pickle.load(open('static/model/model_gbc.sav','rb'))
LR = pickle.load(open('static/model/model_lr.sav','rb'))
#RFC = pickle.load(open('model_rfc.sav','rb'))

def urllink(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    htmldata = requests.get(url, headers=headers).text
    #r = requests.get(url)  
    #htmldata = r.text
    soup = BeautifulSoup(htmldata, 'html.parser')
    data = ''
    for data1 in soup.find_all("p"):
        text = data1.get_text()
        text = text.lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub("\\W"," ",text) 
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)
        data += text

    return data

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
    new_x_test = [news]
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
            url=None
            result=None
            data=None
            if re.search('^https?://\S+|www\.\S+', news):
                url = news
                data = urllink(news)
                result = detect_text(urllink(news))
            else:
                result = detect_text(wordopt(news))
                data = news
            #datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            new_record = Records(
                data = news,
                date = datetime.datetime.utcnow(),
                account_id  = session['user'],
                datatype_id = 1,
                app_id      = 6,
                detect_id   = result
            )
            db.session.add(new_record)
            db.session.commit()

            detect = db.session.query(Detect.result).filter_by(id=result).first()
            print(detect)
            r =[None ,data ,None ,url ,detect[0]]

            #return redirect( url_for('result', r =[None ,data ,None ,url ,detect] ) )
            return render_template('result.html', App_ = r[0], data = r[1], date = r[2], newslink=r[3], detect=r[4] )
        elif request.form.get('submitmsg'):

            app = request.form['apps']
            messages = request.form.get('message')
            date = request.form['date'] 
            d = date.split('T')
            d[0] = d[0].split('-')
            d[1] = d[1].split(':')
            print('date',d)
            #print('todays',datetime.datetime.utcnow(),type(datetime.datetime.utcnow()))
            result = detect_text(wordopt(messages))
            date = datetime.datetime( int(d[0][0]) , int(d[0][1]), int(d[0][2]), int(d[1][0]) ,int(d[1][1]) )
            new_record = Records(
                data = messages,
                date = date ,
                account_id  = session['user'],
                datatype_id = 2,
                app_id      = app,
                detect_id   = result
            )
            db.session.add(new_record)
            db.session.commit()

            App_ = db.session.query(App.app).filter_by(id=app).first()
            detect = db.session.query(Detect.result).filter_by(id=result).first()
            
            r = [App_[0] ,messages ,date ,None ,detect[0]] 
            #return redirect( url_for('result', r = [App_ ,messages ,date ,None ,detect] ) )
            return render_template('result.html', App_ = r[0], data = r[1], date = r[2], newslink=r[3], detect=r[4] )
    else:
        if 'user' not in session:
            return redirect( url_for('login') )
   
    return render_template('detect.html')

@app.route('/detect/result',methods=["GET"])
def result(r):
    return render_template('result.html',App_ = r[0], data = r[1], date = r[2], newslink=r[3], detect=r[4] )