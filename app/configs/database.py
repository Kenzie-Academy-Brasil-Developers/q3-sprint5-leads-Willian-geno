from flask import Flask 
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app:Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    
    app.db=db

    from app.models.leads_modles import Leads_modles