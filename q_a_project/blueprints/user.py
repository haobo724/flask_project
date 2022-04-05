import random
import string
from datetime import datetime

import wtforms
from flask import Blueprint,request,render_template,redirect,url_for,jsonify,session,flash
from forms import LoginForm,RegisterForm
from flask_mail import Message
from exts import mail,db
from models import EmailCpatchaModel,User
from werkzeug.security import generate_password_hash,check_password_hash
user_bp = Blueprint("user",__name__,url_prefix="/")



@user_bp.route("/login",methods=['GET', 'POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email).first()
            if not user :
                flash('您尚未注册')
                # raise wtforms.ValidationError("无邮箱")
                return redirect(url_for('user.login'))

            if check_password_hash(user.user_password,password) :
                flash('密码错误')

                # raise wtforms.ValidationError("密码错误")
                return redirect(url_for('user.login'))
            session['user_id']=user.id
            return redirect('/')
        else:
            flash('格式错误！')

            return redirect(url_for('user.login'))


@user_bp.route("/logout",methods=['GET'])
def logout():
    session.clear()
    return redirect('/')


@user_bp.route("/register",methods=['GET', 'POST'])
def register():
    if request.method =='GET':
        return render_template('register.html')
    else:
        form = RegisterForm(request.form)
        print('收到')
        if form.validate():
            email = form.email.data
            # captcha = form.captcha.data
            password = form.password.data
            username = form.username.data
            password_hash = generate_password_hash(password)
            user = User(email=email,user_password=password_hash,user_name=username)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.login'))
        else:
            return redirect(url_for('user.register'))

# memcached /redis /sql
@user_bp.route("/mail")
def send_mail():
    message = Message(subject = '测试',recipients=['s724724@gmail.com'],body='测试邮件')
    mail.send(message)
    return '成功'

@user_bp.route("/captcha",methods=['POST'])
def get_captcha():
    captcha_pool = string.digits+string.ascii_letters
    email = request.form.get("email")
    captcha_model = EmailCpatchaModel.query.filter_by(email=email).first()

    if email:
        captcha = random.sample(captcha_pool,4)
        captcha = "".join(captcha)
        message = Message(subject = '测试',recipients=[email],body=f'验证码{captcha}')
        mail.send(message)
        if captcha_model:
            captcha_model.captcha = captcha
            captcha_model.create_time = datetime.now()
            db.session.commit()
        else:
            captcha_model = EmailCpatchaModel(email=email,captcha=captcha)
            db.session.add(captcha_model)
            db.session.commit()

        return jsonify({'code':200})
    else:
        return jsonify({'code':400,'message':'请输入邮箱！'})
