from app import app, db, session
from db.model import Account, Records
from flask import render_template, request, redirect, url_for

@app.route('/profile')
def profile():
    # user_detail = db.session.query(Account).filter_by(username=session['user']).first()
    if 'user' in session:
        profile = db.session.query(Account).filter_by(id=session['user']).first()
        print(profile)
    else:
        return redirect( url_for('login') )
    return render_template('profile.html')

@app.route('/view')
def view():
    if 'user' in session:
        records = db.session.execute('''SELECT Records.id, Records.data, Records.date, Datatype.datatype , App.app, Detect.result 
                                                    From Records JOIN Datatype JOIN App JOIN Detect 
                                                    WHERE Records.datatype_id == Datatype.id AND 
                                                          Records.app_id==App.id AND 
                                                          Records.detect_id==Detect.id AND
                                                          Records.account_id == :account''',{'account':session['user'] } )
        #print(record)
        
        return render_template('view.html', records = records)

    
    else:
        return redirect( url_for('login') )
