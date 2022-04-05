from flask import Blueprint,request,render_template,g,redirect,url_for,flash
from decorators import login_required
from models import QuestionModel
from forms import QuestionForm
from exts import db
bp = Blueprint("qa",__name__,url_prefix="/")



@bp.route("/")
def index():
    questions=QuestionModel.query.order_by(db.text('-create_time')).all()
    return render_template('index.html',questions=questions)

@bp.route('/question/<int:question_id>')
@login_required
def question_detail(question_id):
    question = QuestionModel.query.filter_by(id=question_id).first()
    if question:
        return render_template('detail.html',question=question)
    else:
        return redirect('/')

@bp.route("/public_question",methods=['GET','POST'])
@login_required
def public_question():
    if request.method == 'GET':
        return render_template('public_question.html')
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title,content=content,author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect('/')
        else:
            flash('格式错误')
            return redirect(url_for('qa.public_question' ))