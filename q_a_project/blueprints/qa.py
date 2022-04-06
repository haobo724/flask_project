from flask import Blueprint, request, render_template, g, redirect, url_for, flash
from decorators import login_required
from models import QuestionModel, Answer
from forms import QuestionForm, CommentForm
from exts import db
from sqlalchemy import or_

bp = Blueprint("qa", __name__, url_prefix="/")


@bp.route("/search")
def search():
    q = request.args.get("q")
    questions = QuestionModel.query.filter(
        or_(QuestionModel.title.contains(q), QuestionModel.content.contains(q))).order_by(db.text('-create_time'))
    return render_template('index.html', questions=questions)


@bp.route("/")
def index():
    questions = QuestionModel.query.order_by(db.text('-create_time')).all()
    return render_template('index.html', questions=questions)


@bp.route('/question/<int:question_id>')
@login_required
def question_detail(question_id):
    question = QuestionModel.query.filter_by(id=question_id).first()
    if question:
        return render_template('detail.html', question=question)
    else:
        return redirect('/')


@bp.route('/comment/<int:question_id>', methods=['POST'])
@login_required
def comment(question_id):
    form = CommentForm(request.form)
    if form.validate():
        content = form.content.data
        print(g.user)
        answer_model = Answer(content=content, author=g.user, question_id=question_id)
        db.session.add(answer_model)
        db.session.commit()
        return redirect(url_for('qa.question_detail', question_id=question_id))
    else:
        flash('表单验证失败')
        return redirect(url_for('qa.question_detail', question_id=question_id))


@bp.route("/public_question", methods=['GET', 'POST'])
@login_required
def public_question():
    if request.method == 'GET':
        return render_template('public_question.html')
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect('/')
        else:
            flash('格式错误')
            return redirect(url_for('qa.public_question'))
