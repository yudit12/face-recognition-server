from flask import Blueprint, jsonify, request
from api.models import Users ,UsersSchema
from sqlalchemy.exc import SQLAlchemyError
from api import db, ma 
def handle_sginin(bcrypt):
    if request.method=='POST':
        try: 
            user_data =request.get_json()# dict 

            # exists = db.session.query(Users.id).filter_by(email=user_data['email'], password=user_data['password']).scalar() is not None 
            #check valid password
            user= Users.query.filter_by( email=user_data['email']).first()
            print(user.id, user.name, user.email,user.entries,user.joindate) 
            pw_hash = user.password
            # print(pw_hash) 
            exists_password=bcrypt.check_password_hash(pw_hash, user_data['password'])
            print(exists_password) 
            #check if valid email   
            exists_email = db.session.query(Users.id).filter_by(email=user_data['email']).scalar() is not None 
            
            print(exists_email)     
            if exists_email and exists_password :
                print(user_data)       
                # return jsonify('loggin in'),200
                return {'id':user.id, 'name':user.name,'email':user.email,'entries':user.entries,'joindate':user.joindate}
            else:
                return jsonify('error loggin in'),400

        except:
            return jsonify('error loggin in!!'),400
    else:
        return jsonify('something went worng , Please try again'),400