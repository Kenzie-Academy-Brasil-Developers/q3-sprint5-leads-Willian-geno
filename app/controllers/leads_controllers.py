from flask import jsonify, request
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Query
from app.exc.leads_exc import InvalidEmailError, InvalidKeysError
from app.models.leads_modles import Leads_modles
from app.configs.database import db
from sqlalchemy.exc import IntegrityError, NoResultFound
from datetime import datetime as dt


session:Session = db.session


def create_leads():
    data = request.get_json()

    keys = []
    for key in data.keys():
        keys.append(key)
    if keys.sort() != ['name', "phone", "email"].sort():
        return {'ErrorMsg':"Chaves Invalidas",
                "exemple":{
                    "email":"string, 'exemple@email.com'",
                    "name":"string, Exemplo da Silva",
                    "phone":"string, (00) 00000-0000",}}

    try:
        new_leads = Leads_modles(**data)
    except InvalidEmailError:
        return {'ErrorMsg':"Email Invalido, 'exemple@email.com'."},400
   
    try:
        session.add(new_leads)
        session.commit()
    except IntegrityError:
        return {"ErrorMsg":"Email e/ou Telefone já cadastrado"}, 400 

    return jsonify(new_leads), 200

def retrive_leads():
    base_query: Query = session.query(Leads_modles)

    records = base_query.all()

    serializer = [item.name for item in records]

    return jsonify(serializer),200

def retrive_leads_by_email():
    data = request.get_json()

    keys = []
    for key in data.keys():
        keys.append(key)
    if keys.sort() != ["email"].sort():
        return {'ErrorMsg':"Chave Invalida",
                "exemple":{
                    "email":"string, 'exemple@email.com'",}}


    print(data['email'])

    try:
        record: Query = session.query(Leads_modles).filter_by(email = data['email']).one()
    except NoResultFound:
         return {'ErrorMsg':"Email não encontrado"},400

    update = {
        'last_visit':dt.utcnow(),
        'visits': record.visits + 1
    }

    for key, value in update.items():
        setattr(record, key, value)

    session.commit()

    return jsonify(record), 200

def delete_leads_by_email():
    data = request.get_json()

    keys = []
    for key in data.keys():
        keys.append(key)
    if keys.sort() != ["email"].sort():
        return {'ErrorMsg':"Chave Invalida",
                "exemple":{
                    "email":"string, 'exemple@email.com'",}}


    try:
        record: Query = session.query(Leads_modles).filter_by(email = data['email']).one()
    except NoResultFound:
         return {'ErrorMsg':"Email não encontrado"},400

    session.delete(record)
    session.commit()

    return jsonify(record), 200


