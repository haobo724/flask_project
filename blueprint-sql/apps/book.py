from flask import Blueprint

book_bp = Blueprint("book",__name__,url_prefix="/book")



@book_bp.route('/list')
def book_list():
    return "图书列表"