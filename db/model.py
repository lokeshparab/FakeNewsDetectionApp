#from sqlalchemy import Column, Integer, String, ForeignKey, Index
#from sqlalchemy.orm import relationship
#from flask_login import UserMixin 
#from app import application, db # ignore

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///noduesapp.sqlite"
db = SQLAlchemy(app)

#def getForeignKey(reference) : 
#	return Column(db.BigInteger().with_variant(db.Integer, "sqlite"), ForeignKey(reference), nullable=False)

class Records(db.Model) : 
	__tablename__ = 'Records'

	#Creation of attributes in tables

	id = Column(db.Integer(), primary_key= True)

    
	Account_id = Column(db.BigInteger().with_variant(db.Integer, "sqlite"),Foreignkey('Account.id'))
	Datatype_id = Column(db.BigInteger().with_variant(db.Integer, "sqlite"),Foreignkey('Datatype.id'))
	App_id =Column(db.BigInteger().with_variant(db.Integer, "sqlite"),Foreignkey('app.id'))
	Detect_id = Column(db.BigInteger().with_variant(db.Integer, "sqlite"),Foreignkey('detect.id'))


    Detect=relationship("Detect",back_populate="Records")
    Datattype=relationship("Dataeype",back_populate="Records")
    App=relationship("App",back_populate="Records")
    
    
class Account_info(db.Model):
    __tablename__ = 'Account_info'

    #Creation of attributes in Account_info

    Fullname=Column(String(255), nullable=False, unique=True)
    Gender=Column(String(255), nullable=False, unique=True)
    Ages=Column(db.integer, nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    Username=Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    Account_id=Column(db.BigInteger().with_variant(db.Integer, "sqlite"), primary_key= True)

    # creating class constructor to store values in database

    def __init__(self, Fullname, Gender, email, Username,password) : 
        self.Fullname = Fullname
        self.Gender = Gender
        self.email = email
        self.Username=Username
        self.password = password


class Detect(db.Model):
    __tablename__ = 'Detect'

    detct_id=Column(db.integer, nullable=False, unique=True)
    Result=Column(String(255), nullable=False, unique=True)

    Records=relationship("Records",back_populate="Detect")

class Datatype(db.Model):
    __tablename__ = 'Datatype'

    id=Column(db.integer, nullable=False, unique=True)
    Result=Column(String(255), nullable=False, unique=True)

    Records=relationship("Records",back_populate="Datatype")

class App(db.Model):
    __tablename__ = 'App'

    id=Column(db.integer, nullable=False, unique=True)
    Result=Column(String(255), nullable=False, unique=True)
