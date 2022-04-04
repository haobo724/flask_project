from flask import Blueprint, Flask,Response,request,session,render_template

from exts import db,mail
from flask_migrate import Migrate
import config
from blueprints import qa_bp , user_bp ,others_bp
'''
SQLalchemy 是独立的ORM框架（Object-Relational Mapping，简称ORM）
当我们实现一个应用程序时（不使用O-R Mapping），我们可能会写特别多数据访问层的代码，从数据库保存、删除、读取对象信息，而这些代码都是重复的。
而使用ORM则会大大减少重复性代码。ORM主要实现程序对象到关系数据库数据的映射。
可以独立于flask，意味着可以适用于其他框架，比如Django

连接数据库的库，pymysql
'''


'''
程序运行时,对模型的更改映射到数据库中要使用flask migrate来更新数据，
分三步 flask db init ,这里的db 是flask 默认的command并非程序内变量名
flask db migrate -m "xxx"
flask db upgrade

'''


app = Flask(__name__)
app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)
app.register_blueprint(others_bp)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)
migrate = Migrate(app,db)




if __name__ == '__main__':
    app.run(debug=True)

