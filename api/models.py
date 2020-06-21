# from . import db 
from api import db, create_app
from datetime import datetime
from . import ma 
# Represented our movie table
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False,nullable=False)
    email = db.Column(db.String(200),unique=True,nullable=False) # change unique =True
    password = db.Column(db.String(60),unique=False,nullable=False)
    entries= db.Column(db.Integer, nullable = False,default=0)
    joindate= db.Column(db.DateTime,default=datetime.now())

# ,entries,joindate
    def __init__(self, name, email,password):
            self.name = name
            self.email = email
            self.password= password
            # self.entries=entries
            # self.joindate=joindate



    # # what  will display from DB
    # def __repr__(self):
    #     return f"Users('{self.name}','{self.email}')"

class UsersSchema(ma.ModelSchema):
    class Meta:
        model = Users

 

