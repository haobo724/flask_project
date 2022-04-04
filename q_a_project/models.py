from datetime import datetime

from exts import db

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # 外键，db.ForeignKey("表名.字段名")，数据库层面不推荐直接访问
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # relationship

    author = db.relationship("User", backref='articles')


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(200), nullable=False)
    user_password = db.Column(db.String(200), nullable=False)


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
    email = db.Column(db.String(200),nullable=False,unique=True)
    captcha = db.Column(db.String(10),nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
