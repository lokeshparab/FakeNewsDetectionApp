#from enum import unique
#from datetime import date
#from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.sqlite"
db = SQLAlchemy(app)

class Records(db.Model) : 
    __tablename__ = 'Records'

    #Creation of attributes in tables

    id          = db.Column(db.Integer, primary_key= True)

    data        = db.Column(db.String(700), nullable= False)
    date        = db.Column(db.Datetime, nullable= False)

    account_id  = db.Column(db.Integer,db.Foreignkey('Account.id'), nullable=False)
    datatype_id = db.Column(db.Integer,db.Foreignkey('Datatype.id'), nullable=False)
    app_id      = db.Column(db.Integer,db.Foreignkey('app.id'), nullable=True)
    detect_id   = db.Column(db.Integer,db.Foreignkey('detect.id'), nullable=False)

    
class Account(db.Model):
    __tablename__ = 'Account'

    #Creation of attributes in Account_info
    account_id = db.Column(db.Integer, primary_key= True )

    fname       = db.Column(db.String(128), nullable=False )
    gender     = db.Column(db.String(7), nullable=False )
    ages       = db.Column(db.Integer, nullable=False )
    email      = db.Column(db.String(40), nullable=False, unique=True)
    username   = db.Column(db.String(40), nullable=False, unique=True)
    password   = db.Column(db.String(128), nullable=False)
    

    account_record = db.relationship('Records',backref='record',lazy=True)

class Detect(db.Model):
    __tablename__ = 'Detect'

    detect_id = db.Column(db.Integer, primary_key= True)

    result   = db.Column(db.String(4), nullable=False, unique=True)

    account_detect = db.relationship('Records',backref='detect',lazy=True)


class Datatype(db.Model):
    __tablename__ = 'Datatype'

    id                  = db.Column(db.Integer,  primary_key= True)

    datatype            = db.Column(db.String(7), nullable=False, unique=True)

    account_datatype    = db.relationship('Records',backref='datatype',lazy=True)

class App(db.Model):
    __tablename__ = 'App'

    id      = db.Column(db.Integer,  primary_key= True)

    app     = db.Column(db.String(10), nullable=False, unique=True)
   
    account_app = db.relationship('Records',backref='app',lazy=True)
  