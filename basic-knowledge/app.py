from flask import (Flask, jsonify,url_for,redirect,request,render_template)
import config

app = Flask(__name__,template_folder='templates')
# app.config.from_object(config)
# 1.如果是获取数据，一般为GET请求
# 2.如果是发送数据，一般为post请求
# 3.在@app.route 上添加methods参数，可以为列表传递多种请求类型
# 4.重定向分为，暂时性和永久性（少），使用函数redirect
# 5.模板（template，即html文件的使用）使用render_template，同时可以传参，参数使用字典
# 7.在html文件中可以使用一些过滤器来操作传入变量，或者做一些逻辑操作，比如测量字符长度，合并字符等等。flask中默认是jinjia2，
#   过滤器帮助文档 https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-filters
# 8.控制(包括block)语句的书写注意格式{% xxxx %}百分号和花括号贴贴，不要和变量贴贴 同时不要忘记写end
books = [{'id': 1, 'name': 'nihao'}, {'id': 2, 'name': 'nihao'}, {'id': 3, 'name': 'nihao'},
         {'id': 4, 'name': 'nihao'}, ]


@app.route('/control')
def control():
    context = {
        'age':18,
        'books': ['book1', 'book2']

    }
    return render_template("control.html",**context)


@app.route('/about')
def about():
    context = {
        'username':'user1',
        'books':['book1','book2']
    }
    return render_template("about.html",**context)
@app.route('/book/list')
def book_list():
    for book in books:
        book['url'] = url_for('book_detail',book_id=book['id'])#这个book_detail是视图函数名，要保持一致
    return jsonify(books)

@app.route('/profile')
def profile():
    '''
    传参的两种方式：
    1, 作为url的组成部分，比如book_detail 视图函数
    2，查询字符串 /url?id=xxxx 注意问号和=之间的东西
    
    :return: 
    '''
    user_id = request.args.get('id')
    if user_id:
        return '用户中心'
    else:
        return redirect(url_for('main_page'))


@app.route("/book/<int:book_id>")
def book_detail(book_id):#别忘了写这个传递参数，否则会报错，并且要保证这个参数和url中一致
    return 'book_id'

@app.route('/')
def main_page():
    return render_template("mainpage.html")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
