from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# Flask 初始化
app = Flask(__name__)

# Flask-RESTFul 初始化
api = Api(app)

# 数据库初始化
# 格式：{数据库}+{连接器}://{用户名}:{密码}@{数据库服务地址}/{数据库名称}
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:mysql@localhost/flask_api_tutorial'
db = SQLAlchemy(app)


from resouces import StudentResource
