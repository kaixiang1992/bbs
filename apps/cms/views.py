from flask import Blueprint, views, render_template, request, session, redirect, url_for, flash
from .froms import LoginForm
from .models import CmsUser
from .decorators import login_required
import config

bp = Blueprint('cms', __name__, url_prefix='/cms')


@bp.route('/')
@login_required
def homepage():
    return 'cms homepage'


class LoginView(views.MethodView):
    def get(self, messages=None):
        return render_template('cms/login.html', messages=messages)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CmsUser.query.filter(CmsUser.email == email).one_or_none()
            if user and user.check_password(password):  # TODO: 账号密码校验成功
                session[config.CONFIG_USER_ID] = user.id
                if remember == 1:  # TODO: 记住密码
                    session.permanent = True
                flash(message='登录成功')
                return redirect(url_for('cms.homepage'))
            else:
                message = '账号或密码错误...'
                flash(message=message)
                return self.get(messages=message)
        else:
            # TODO: form.errors.popitem()元祖：('password', ['密码为6-12位字母或数字'])
            errors = form.errors.popitem()[1][0]
            return self.get(messages=errors)


bp.add_url_rule('/login/', endpoint='login', view_func=LoginView.as_view('login'))
