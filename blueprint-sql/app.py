from flask import Blueprint, Flask,Response,request,session,render_template
from apps.book import book_bp
from apps.user import user_bp
from exts import db
from flask_migrate import Migrate
import config
from models import Article, User, UserExtension
from forms import LoginForm
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
app.register_blueprint(book_bp)
app.register_blueprint(user_bp)
app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app,db)

@app.route("/set_cookie")
def set_cookie():
    user_id = request.cookies.get("user_id")
    print("user_id",user_id)
    return "获取cookie"

@app.route("/get_cookie")
def get_cookie():
    response = Response("cookie 设置")
    response.set_cookie("user_id","xxx")
    return response

@app.route("/set_session")
def set_session():
    '''在flask里，session是把数据经过加密，然后用session作为key，存放在cookie中
    比如在这个小例子中，userid被加密后放入cookie中，就不是明文了，安全系数提高

    '''
    session["user_id"]  ="xxx"
    session["user_pass"]  ="xxxx"

    return "session 创建成功"

@app.route("/get_session")
def get_session():
    user_id = session.get("user_id")
    print("user_id",user_id)
    return "获取session"


@app.route("/login",methods=['GET', 'POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            return "登录成功"
        else:
            return "登录失败"

#  -------------------数据库相关---------------------------

@app.route('/article')
def article_view():
    artice = Article(title='haha',content ='xxxxx')
    db.session.add(artice)
    db.session.commit()
    # filter_result = Article.query.filter_by(id=1)[0]
    # filter_result.title='qqq'
    # db.session.commit()

    # print(filter_result.title)
    # print(filter_result)
    # Article.query.filter_by(id=1).delete()
    # db.session.commit()
    return "操作成功"

@app.route('/otm')
def otm():
    article = Article(title='otm添加的文章',content='xxx')
    user = User(user_name='otm添加的name',user_password='otm添加的password')
    article.author = user
    db.session.add(article)
    db.session.commit()
    #反向引用
    print(user.articles[0].title)
    return "操作成功"

@app.route('/oto')
def oto():
    extension = UserExtension(school='大学')
    # user = User.query.filter_by(id=1).first()
    user = User.query.filter_by(id=1).first()
    user.extension = extension
    db.session.add(user)
    db.session.commit()
    #反向引用
    print(user.articles[0].title)
    return "操作成功"

@app.route('/')
def mainpage():
    engine = db.get_engine()
    with engine.connect() as conn:
        result = conn.execute('select 1')
        print(result.fetchone())
    return "首页"
if __name__ == '__main__':
    app.run(debug=True)

