from flask_restful import Resource, reqparse
from src.model import UserModel

parser = reqparse.RequestParser()


class User(Resource):

    def get(self):
        parser.add_argument('user_id', type=int, help='The ID for the user', required=True)
        data = parser.parse_args()

        try:
            user = UserModel.query.filter_by(id=data['user_id']).first()

            if user:
                response = {
                    "user_id": user.id,
                    "name": user.name,
                    "email": user.email
                }
                return response, 200
            else:
                return {"message": "This user does not exist"}, 404
        except Exception as e:
            return {"message": str(e)}, 500

    def post(self):
        parser.add_argument('email', type=int, help='Email address used to login', required=True)
        parser.add_argument('name', type=str, help='The name of the user', required=True)
        parser.add_argument('password', type=str, help='The password for the user', required=True)
        data = parser.parse_args()
        user = UserModel(
            email=data['email'],
            name=data['name'],
            password=UserModel.generate_hash(data['password'])
        )

        try:
            user.save_to_db()
            return {"message": "User {} was created".format(data['name'])}, 200
        except Exception as e:
            return {"message": str(e)}, 500

    def update(self):
        pass

    def delete(self):
        parser.add_argument('user_id', type=int, help='The ID for the user', required=True)
        data = parser.parse_args()

        try:
            user = UserModel.query.filter_by(id=data['user_id']).first()

            if user:
                user.delete_from_db()
                return {"message": "This user has been deleted successfully"}, 200
            else:
                return {"message": "This user does not exist"}, 404
        except Exception as e:
            return {"message": str(e)}, 500
