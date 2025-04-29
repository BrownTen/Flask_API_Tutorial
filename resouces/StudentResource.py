from datetime import datetime

import jwt
from flask import request
from flask_restful import Resource, reqparse

from common.api_tools import token_required
from entity.Student import Student
from resouces import api
from service.StudentService import StudentService
from common.constants import JWT_SECRET_KEY

class StudentResource(Resource):
    student_service = StudentService()

    # 获取服务器资源
    @token_required()
    def get(self, student_id):
        student = self.student_service.get_student_by_id(student_id)
        if student:
            return student.to_dict()
        else:
            return {'error': f'Student Not Found For ID: {student_id}'}, 503

    # 修改服务器资源
    def put(self, student_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, location='json', required=False, default='', help='提供一个字符串*姓名*')
        parser.add_argument('gender', type=str, location='json', required=False, default='', help='提供一个字符串*姓名*')
        parser.add_argument('birthday', type=str, location='json', required=False, default=None, help='提供一个字符串*姓名*')

        args = parser.parse_args()
        name = args.name
        gender = args.gender
        birthday = datetime.strptime(args.birthday, '%Y-%m-%d') if args.birthday is not None else None

        try:
            student = Student(id=student_id, name=name, gender=gender, birthday=birthday)
            self.student_service.update_student(student)
        except Exception as e:
            # import logging
            # log = logging.getLogger()
            # log.error(f'{str(e)}', exc_info=True)
            return {'error': str(e)}, 503
        return student.to_dict()


class StudentListResource(Resource):
    student_service = StudentService()

    def get(self):
        student_list = self.student_service.get_students()
        return [student.to_dict() for student in student_list]

    # 向服务器添加资源
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, location='json', required=True, default='', help='提供一个字符串*姓名*')
        parser.add_argument('gender', type=str, location='json', required=True, default='', help='提供一个字符串*姓名*')
        parser.add_argument('birthday', type=str, location='json', required=False, default=None, help='提供一个字符串*姓名*')

        args = parser.parse_args()
        name = args.name
        gender = args.gender
        birthday = datetime.strptime(args.birthday, '%Y-%m-%d') if args.birthday is not None else None

        try:
            student = Student(name=name, gender=gender, birthday=birthday)
            self.student_service.create_student(student)
        except Exception as e:
            return {'error': str(e)}, 503
        return student.to_dict()


api.add_resource(StudentResource, '/student/<int:student_id>')
api.add_resource(StudentListResource, '/students')
