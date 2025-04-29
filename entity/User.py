from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from resouces import db


class User(db.Model):
    __TableName__ = 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[str] = mapped_column(String, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password,
            'role': self.role
        }