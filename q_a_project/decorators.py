from flask import g ,redirect,url_for
from functools import wraps
def login_required(func):
    #不能忘记写，这个装饰器保证了被wrap的函数名不会被改变，否则被这个装饰器（login——required）装饰的函数名字都会变成warpper
    @wraps(func)
    def wrapper(*args, **kwargs):
        if hasattr(g,"user"):
            return func(*args,**kwargs)
        else:

            return redirect(url_for('user.login'))
    return wrapper