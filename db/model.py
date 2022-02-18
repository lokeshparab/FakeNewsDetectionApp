#from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///noduesapp.sqlite"
db = SQLAlchemy(app)

class Rcords(db.Model) : 
	__tablename__ = 'Records'

	#Creation of attributes in tables

	id          = db.Column(db.Column, primary_key= True)
	Account_id  = db.Column(db.Integer,Foreignkey('Account.id'))
	Datatype_id = db.Column(db.Integer,Foreignkey('Datatype.id'))
	App_id      = db.Column(db.Integer,Foreignkey('app.id'))
	Detect_id   = db.Column(db.Integer,Foreignkey('detect.id'))

    
class Account_info(db.Model):
    __tablename__ = 'Account_info'

    #Creation of attributes in Account_info

    Fullname   = db.Column(String(255), nullable=False, unique=True)
    Gender     = db.Column(String(255), nullable=False, unique=True)
    Ages       = db.Column(db.integer, nullable=False, unique=True)
    email      = db.Column(String(255), nullable=False, unique=True)
    Username   = db.Column(String(255), nullable=False, unique=True)
    password   = db.Column(String(255), nullable=False)
    Account_id = db.Column(db.Integer, primary_key= True)

    Account_record = db.relationship('Accountrecord',backref='Account_record',lazy=True)

class Detect(db.Model):
    __tablename__ = 'Detect'

    detct_id = db.Column(db.integer, nullable=False, unique=True)
    Result   = db.Column(String(255), nullable=False, unique=True)

    Account_detect = db.relationship('Accountdetect',backref='Account_detect',lazy=True)


class Datatype(db.Model):
    __tablename__ = 'Datatype'

    id     = db.Column(db.integer, nullable=False, unique=True)
    Result = db.Column(String(255), nullable=False, unique=True)

    Account_datatype = db.relationship('Accountdatatype',backref='Account_datatype',lazy=True)

class App(db.Model):
    __tablename__ = 'App'

    id     =db.Column(db.integer, nullable=False, unique=True)
    Result =db.Column(String(255), nullable=False, unique=True)
   
    Account_app = db.relationship('Accountapp',backref='Account_app',lazy=True)





    


    
    


   