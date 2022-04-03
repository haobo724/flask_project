from flask import Blueprint,request,render_template
from forms import LoginForm

user_bp = Blueprint("user",__name__,url_prefix="/user")



@user_bp.route("/login",methods=['GET', 'POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            return "登录成功"
        else:
            return "登录失败"



@user_bp.route("/register",methods=['GET', 'POST'])
def register():
    if request.method =='GET':
        return render_template('register.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            return "登录成功"
        else:
            return "登录失败"