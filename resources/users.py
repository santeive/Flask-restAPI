import sqlite3
from flask_restful import Resource, Api, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
            type = str,
            required = True,
            help = "This field cannot be blank"
    )
    parser.add_argument('password',
            type = str,
            required = True,
            help = "This field cannot be blank"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        #We need to have this in front of the connection creation
        #Always after the data parse
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created seccessfully"}, 201
