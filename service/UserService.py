import jwt

from dao.UserDao import UserDao
from common.constants import JWT_SECRET_KEY


class UserService:
    user_dao = UserDao()

    def login(self, username: str, password: str):
        exist_user = self.user_dao.query_user_by_name(username)
        if not exist_user: raise Exception('User Not Found')
        if exist_user.password != password: raise Exception('Password Not Correct')
        jwt_access_token = jwt.encode(exist_user.to_dict(), JWT_SECRET_KEY, algorithm='HS256')
        return exist_user, jwt_access_token
