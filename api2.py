import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+ os.path.join(app.root_path, 'sqlite.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)

db.create_all()

class DoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200))
    gender= db.Column(db.String(10))

