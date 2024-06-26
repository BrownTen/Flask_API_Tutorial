from sqlalchemy import Select, asc, and_

from resouces import db

from entity.Student import Student


class StudentDao:
    def get_student_by_id(self, student_id):
        return db.session.get(Student, student_id)

    def get_student_by_info(self, student: Student):
        query = Select(Student).where(
            and_(
                Student.name == student.name,
                Student.gender == student.gender,
                Student.birthday == student.birthday
            )
        )
        return db.session.scalars(query).all()

    def get_students(self):
        query = Select(Student).order_by(asc(Student.name))
        return db.session.scalars(query).all()

    def create_student(self, student: Student):
        db.session.add(student)
        db.session.commit()
        return student

    def update_student_by_id(self, student: Student):
        exist_student = self.get_student_by_id(student.id)
        exist_student.name = student.name
        exist_student.gender = student.gender
        exist_student.birthday = student.birthday
        db.session.commit()
        return exist_student
