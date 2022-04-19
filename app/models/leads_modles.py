from dataclasses import dataclass
from email.policy import default
from app.configs.database import db
import datetime as dt
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import validates

from app.exc.leads_exc import InvalidEmailError, InvalidKeysError

@dataclass
class Leads_modles(db.Model):
    caeate_data = dt.datetime.utcnow() 
    
    id:int
    name:str
    email:str
    phone:str
    creation_date:str
    last_visit:str
    visits:int

    __tablename__="leads"

    id=Column (Integer, primary_key=True)
    name=Column(String, nullable=False)
    email=Column(String, unique=True, nullable=False)
    phone=Column(String, unique=True, nullable=False)
    creation_date=Column(DateTime, default=caeate_data)
    last_visit=Column(DateTime, default=caeate_data)
    visits=Column(Integer, default=1)

    @validates("email")
    def validete_email(self, key, email):
        if '@' and ".com" not in email:
            raise InvalidEmailError

        return email
    
    
    @validates("phone")
    def validete_phone(self, key, phone):
        print(key)
        print(phone)
        return phone
