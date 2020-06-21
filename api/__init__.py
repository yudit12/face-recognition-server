#https://www.youtube.com/watch?v=Urx8Kj00zsI

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from flask_bcrypt import Bcrypt
db = SQLAlchemy()
ma = Marshmallow()
def create_app():
    app = Flask(__name__)
    # bcrypt = Bcrypt(app)
    app.config['SECRET_KEY']='b726da71426e92068ed89850620b1522'
    ENV = 'dev'
    if ENV == 'dev':
        app.debug=True
        app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1234@localhost/postgres'
    else:
        app.debug=False
        app.config['SQLALCHEMY_DATABASE_URI']=''#production

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)
    
    from .views import main
    app.register_blueprint(main)

    return app

