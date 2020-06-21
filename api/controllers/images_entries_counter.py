
from flask import Blueprint, jsonify, request
from api.models import Users ,UsersSchema
from sqlalchemy.exc import SQLAlchemyError
from api import db, ma 
"""
# users images entries counter
"""

# #initialize with your api key.
# app = ClarifaiApp(api_key='8da3226684994f8faf45b80b68ec4f93')

# def handleApiCall():
#     if request.method=='POST':
#         try:
#             res=app.models.predict(ClarifaiApp.FACE_DETECT_MODEL, request.get_json())
#             return jsonify(res),200
#         except:
#             return jsonify("cannt work with clarfai api")
#     else:
#         return jsonify('something went worng , Please try again'),400

def count_images_entries():
    if request.method=='PUT':
        try: 
            user_id =request.get_json()# dict
            print(user_id)
            user=Users.query.filter_by(id=user_id['id']).first()
            user.entries += 1
            try:
                db.session.commit()
                print(user.entries)
            except SQLAlchemyError as e:
                print(str(e))
                db.session.rollback()
            # return jsonify('Done'),200
            return jsonify(user.entries),200
        except:
            return jsonify('user id not found'),400
    else:
        return jsonify('something went worng , Please try again'),400