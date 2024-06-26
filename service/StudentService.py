from dao.StudentDao import StudentDao
from entity.Student import Student


class StudentService:
    student_dao = StudentDao()

    def get_students(self):
        return self.student_dao.get_students()

    def get_student_by_id(self, student_id: int):
        return self.student_dao.get_student_by_id(student_id)

    def update_student(self, student: Student):
        exist_student = self.student_dao.get_student_by_id(student.id)
        if not exist_student: raise Exception(f'Student Has Nont Been Exist, student_id: {student.id}')
        student.name = student.name if student.name != '' else exist_student.name
        student.gender = student.gender if student.gender != '' else exist_student.gender
        student.birthday = student.birthday if student.birthday is not None else exist_student.birthday
        update_student = self.student_dao.update_student_by_id(student)
        return update_student

    def create_student(self, student: Student):
        if self.student_dao.get_student_by_info(student):
            raise Exception('Student Has Been Exist')
        return self.student_dao.create_student(student)
