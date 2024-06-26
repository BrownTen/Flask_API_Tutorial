from datetime import datetime

from sqlalchemy import Integer, String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from resouces import db


class Student(db.Model):
    __TableName__ = 'student'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    gender: Mapped[str] = mapped_column(String, nullable=False)
    birthday: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'birthday': self.birthday.strftime('%Y-%m-%d') if self.birthday is not None else ''
        }
