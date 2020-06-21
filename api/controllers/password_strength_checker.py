from flask import Blueprint, jsonify, request
from api.passwordChecker import passwordChecker

# password strength checker : should you use this password for registertion
def password_checker():
    user_password =request.get_json()
    print(user_password)
    result=passwordChecker(user_password['password'])
    print(result)
    return jsonify(result),200