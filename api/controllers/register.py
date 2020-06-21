from flask import Blueprint, jsonify, request
from api.models import Users ,UsersSchema
from sqlalchemy.exc import SQLAlchemyError
from api import db, ma 
def handle_registration(bcrypt):
    if request.method=='POST':
        try: 
            
            user_data =request.get_json()# dict
           
            pw_hash = bcrypt.generate_password_hash(user_data['password']).decode('utf-8')

            # print(pw_hash)
            # print(user_data)
            # print(Users)
            print(user_data['name'],user_data['email'],pw_hash)
            new_user=Users(name=user_data['name'], email=user_data['email'],password=pw_hash )#add new user- object
            try:
                db.session.add(new_user)
                db.session.commit()
            except SQLAlchemyError as e:
                print(str(e))
                db.session.rollback()
            
            print(new_user.id, new_user.name, new_user.email,new_user.entries,new_user.joindate)
            # return jsonify('register'),200
            return {'id':new_user.id, 'name':new_user.name,'email':new_user.email,'entries':new_user.entries,'joindate':new_user.joindate}
        except:
            # return 'didnt save user'
            return jsonify('didnt save user!!'),400   
              
    else:
        # return 'something went worng , Please try again'
        return jsonify('something went wrong , Please try again'),400  