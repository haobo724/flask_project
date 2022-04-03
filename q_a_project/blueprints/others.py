from flask import Blueprint, Flask,Response,request,session,render_template
from exts import db
from models import Article, User, UserExtension

app = Blueprint("other",__name__,url_prefix="/")



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