import wtforms
from wtforms.validators import length, email,EqualTo
from models import EmailCpatchaModel,User

class LoginForm(wtforms.Form):
    # email = wtforms.StringField(validators=[length(min=5, max=20), email()])
    email = wtforms.StringField(validators=[length(min=8, max=20)])
    password = wtforms.StringField(validators=[length(min=6, max=20) ])


class RegisterForm(wtforms.Form):
    # email = wtforms.StringField(validators=[length(min=5, max=20), email()])
    email = wtforms.StringField(validators=[length(min=8, max=20)])
    captcha = wtforms.StringField(validators=[length(min=4, max=4)])
    password = wtforms.StringField(validators=[length(min=6, max=20) ])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])
    username = wtforms.StringField(validators=[length(min=6, max=20) ])

    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCpatchaModel.query.filter_by(email=email).first()
        if not captcha_model or captcha_model.captcha.lower()!=captcha.lower():
            print(captcha_model.captcha.lower())
            print(captcha.lower())
            print(captcha_model)
            raise wtforms.ValidationError("邮箱验证码错误")
        else:

            print('captcha 验证通过')

    def validate_email(self, field):
        email = field.data
        User_model = User.query.filter_by(email=email).first()
        if User_model:
            print('邮箱已存在')
            raise wtforms.ValidationError("邮箱已存在")
        else:
            print('email 验证通过')
