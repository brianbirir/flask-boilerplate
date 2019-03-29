from datetime import datetime
from flask_restful import Resource, reqparse
from src.model import UserModel


class User(Resource):

    @staticmethod
    def get_user_details_parsed_args():
        """
        method for parsing arguments received from the request
        :return: parsed arguments
        """
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str,
                            help='Email address used to login. This should be a string',
                            required=True)
        parser.add_argument('name', type=str, help='The name of the user', required=True)
        return parser.parse_args()

    @staticmethod
    def get_user_id_parsed_args():
        """
        method for parsing user id arg received from the request
        :return: parsed user id
        """
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, help='The ID for the user', required=True)
        return parser.parse_args()

    @staticmethod
    def get_user_password_parsed_args():
        """
        method for parsing user password arg received from the request
        :return: parsed user id
        """
        parser = reqparse.RequestParser()
        parser.add_argument('password', type=str, help='The password for the user', required=True)
        return parser.parse_args()

    @staticmethod
    def check_existing_user(email_address):
        """
        method for checking for existing user during user registration.
        the email address column has the unique value property on the users table
        :return: query object
        """
        return UserModel.query.filter_by(email=email_address).first()

    def get(self):
        data = self.get_user_id_parsed_args()

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
        data_user_details = self.get_user_details_parsed_args()
        data_password = self.get_user_password_parsed_args()

        try:
            # check if user exists by using email address value
            if not self.check_existing_user(data_user_details['email']):
                user = UserModel(
                    email=data_user_details['email'],
                    name=data_user_details['name'],
                    password=UserModel.generate_hash(data_password['password'])
                )
                user.save_to_db()
                return {"message": "User {} was created".format(data_user_details['name'])}, 200
            else:
                return {"message": "That email address already exists"}, 400

        except Exception as e:
            return {"message": str(e)}, 500

    def put(self):
        data_user_id = self.get_user_id_parsed_args()
        data_user_details = self.get_user_details_parsed_args()
        data_password = self.get_user_password_parsed_args()

        try:
            user = UserModel.query.filter_by(id=data_user_id['user_id']).first()

            if user:
                user.email = data_user_details['email']
                user.name = data_user_details['name']
                user.password = UserModel.generate_hash(data_password['password'])
                user.updated_at = datetime.utcnow()
                user.save_to_db()
                return {"message": "User {} was updated".format(data_user_details['name'])}, 200
            else:
                return {"message": "This user does not exist"}, 404

        except Exception as e:
            return {"message": str(e)}, 500

    def delete(self):
        data_user_id = self.get_user_id_parsed_args()

        try:
            user = UserModel.query.filter_by(id=data_user_id['user_id']).first()

            if user:
                user.delete_from_db()
                return {"message": "This user has been deleted successfully"}, 200
            else:
                return {"message": "This user does not exist"}, 404
        except Exception as e:
            return {"message": str(e)}, 500
