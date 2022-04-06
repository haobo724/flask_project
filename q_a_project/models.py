from datetime import datetime

from exts import db


class QuestionModel(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # 外键，db.ForeignKey("表名.字段名")，数据库层面不推荐直接访问
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    create_time = db.Column(db.String(200), nullable=False, default=datetime.now)
    # < img class ="side-question-avatar" src="{{ url_for('static',filename='image/PC181211.jpg') }}" alt="" >

    # relationship

    author = db.relationship("User", backref='questions')


class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    # 外键，db.ForeignKey("表名.字段名")，数据库层面不推荐直接访问
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    create_time = db.Column(db.String(200), nullable=False, default=datetime.now)

    # relationship

    author = db.relationship("User", backref='answers')
    # 这样可以通过question访问answer，即使question的model那边没有绑定，这边绑定一个就成了。具体表现就是相当于question.answers 就可以访问该问题下所有回答
    question = db.relationship("QuestionModel", backref=db.backref('answers', order_by=create_time.desc()))


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(200), nullable=False)
    user_password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    join_time = db.Column(db.String(200), nullable=False, default=datetime.now)


class UserExtension(db.Model):
    __tablename__ = 'user_extension'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    school = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # 不让用列表 uselist=False
    user = db.relationship("User", backref=db.backref('extension', uselist=False))


class EmailCpatchaModel(db.Model):
    __tablename__ = 'email_capther'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    captcha = db.Column(db.String(10), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
