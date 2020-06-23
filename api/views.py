from flask import Blueprint, jsonify, request
from . import db, ma 
from flask_bcrypt import Bcrypt
from .models import Users ,UsersSchema
import api.controllers.register as register1 
import api.controllers.sginin as sginin1 
import api.controllers.images_entries_counter as images_counter 
import api.controllers.password_strength_checker as password_checker 
import os
# from flask import abort


main = Blueprint('main', __name__)
# bcrypt = Bcrypt(main)
bcrypt = Bcrypt()
# app = ClarifaiApp()
@main.route('/')
def hello_world():
    return 'Hello, World!'

## register- add user
@main.route('/register',methods=['POST'])
def register():
    return register1.handle_registration(bcrypt)
      
#sginin 
@main.route('/sginin',methods=['POST'])
def sginin():
    return sginin1.handle_sginin(bcrypt)


# users images entries counter  
@main.route('/image',methods=['PUT'])
def images_entries_counter():
    return images_counter.count_images_entries()
# # api call
# @main.route('/image_url',methods=['POST'])
# def handleApiCall():
#     return images_counter.handleApiCall()

#password strength checker
@main.route('/password_checker',methods=['POST'])
def password_strength_checker():
    return password_checker.password_checker()
    

## not used yet !!
# # displays all users- retun user from db
# @main.route('/display_users')
# def display_users():
#     users_list = Users.query.all()
#     print(users_list)
#     users = []
#     for user in users_list:
#         users.append({'name' : user.name, 'email' : user.email ,'password': user.password})#dic

#     return jsonify({'users' : users})


# @main.route('/profile/<string:id>')
# def get_user_profile(id):
#     try:
#         user_id = id
#         print(user_id)
#         user_data=Users.query.filter_by(id=user_id).first()
#         print(user_data)
#         # users_schema =UsersSchema(many=True)
#         # users_schema =UsersSchema()    
#         # output=users_schema.dump(user_data)
#         # print(output)
#         if  bool(user_data) :# dict is not empty      
#             # return jsonify('Done'),200
#             return {'name' : user_data.name, 'email' : user_data.email}
#         else:
#              return  jsonify('get user profile error'),400# error geting user
#     except:
#         return jsonify('something went worng , Please try again'),400



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    main.run(threaded=True, port = int(os.environ.get('PORT', 5000)))
