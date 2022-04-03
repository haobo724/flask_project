from flask import Blueprint,request,render_template
from forms import LoginForm

bp = Blueprint("qa",__name__,url_prefix="/")



@bp.route("/",)
def index():
    return render_template('index.html')