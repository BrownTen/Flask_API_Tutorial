from datetime import datetime

from flask_restful import Resource, reqparse

from resouces import api
from service.UserService import UserService


class LoginResource(Resource):
    user_service = UserService()

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, location='json', required=True, help='必须提供一个字符串描述*username*')
        parser.add_argument('password', type=str, location='json', required=True, help='必须提供一个字符串描述*password*')
        args = parser.parse_args()

        try:
            user, token = self.user_service.login(args.username, args.password)
        except Exception as e:
            return {'error': f'{e}'}, 503
        response = user.to_dict()
        response['token'] = token
        return response


api.add_resource(LoginResource, '/login')
