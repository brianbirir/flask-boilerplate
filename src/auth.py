from datetime import datetime
from flask_restful import Resource, reqparse
from src.model import UserModel


class Login(Resource):

    @staticmethod
    def get_login_details():
        """
        method for parsing login data from the request
        :return: parsed login arguments
        """
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, help='The email of the user is required', required=True)
        parser.add_argument('password', type=str, help='The password of the user', required=True)
        return parser.parse_args()
    
    def post(self):
        data = self.get_login_details()

        try:
            user = UserModel.query.filter_by(email=data['email']).first()

            # return 404 response if user's email does not exist
            if not user:
                return {"message":"This user does not exist"}, 404
            else:
                # verify password and return 403 response if it's wrong
                if UserModel.verify_hash(data['password'], user.password):
                    response = {
                        "user_id": user.id,
                        "message": "Logged in as {}".format(user.name)
                    }
                    return response, 200
                else:
                    return {"message":"wrong user credentials"}, 403
            pass
        except Exception as e:
            return {"message": str(e)}, 500


class Logout(Resource):
    pass


class TokenGeneration(Resource):
    pass
