from sqlalchemy import Select, asc, and_

from resouces import db

from entity.User import User

class UserDao:
    def query_user_by_name(self, username: str):
        query = Select(User).where(User.name == username)
        return db.session.scalars(query).first()