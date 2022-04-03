from flask import Blueprint

user_bp = Blueprint("user",__name__,url_prefix="/user")



@user_bp.route('/list')
def user_list():
    return "user列表"