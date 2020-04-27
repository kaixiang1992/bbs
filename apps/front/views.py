from flask import (
    Blueprint,
    views,
    render_template,
    request,
    url_for,
    session
)
from exts import db
from .forms import SignupFrom, SigninForm
from .models import FrontUserModel
from untils import restful, safeutils
import config

bp = Blueprint('front', __name__)


# TODO: 注册页面视图
class SignupView(views.MethodView):
    def get(self):
        referrer = request.referrer
        cururl = request.url
        if referrer and referrer != cururl and safeutils.is_safe_url(referrer):
            return render_template('front/front_signup.html', return_to=referrer)
        return render_template('front/front_signup.html')

    def post(self):
        form = SignupFrom(request.form)
        if form.validate():
            telephone = form.telephone.data
            username = form.username.data
            password = form.password1.data
            user = FrontUserModel(telephone=telephone, username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return restful.success(message='注册成功')
        else:
            return restful.params_error(message=form.get_random_error(), data=form.get_all_errors())


# TODO: 登录页面视图
class SigninView(views.MethodView):
    def get(self):
        return_to = request.referrer
        cururl = request.url
        if return_to and return_to != cururl and return_to != url_for(endpoint='front.signup') and safeutils(return_to):
            return render_template('front/front_signin.html', return_to=return_to)
        else:
            return render_template('front/front_signin.html')

    def post(self):
        form = SigninForm(request.form)
        if form.validate():  # TODO: 表单验证通过
            telephone = form.telephone.data
            password = form.password.data
            remember = form.remember.data
            user = FrontUserModel.query.filter_by(telephone=telephone).one_or_none()
            if user and user.check_password(raw_password=password):  # TODO: 用户信息存在且密码校验正确
                session[config.FRONT_USER_ID] = user.id  # TODO: 缓存session
                if remember:  # TODO: 记住密码，存储31天
                    session.permanent = True
                return restful.success(message='登录成功')
            else:
                return restful.params_error(message='手机号或密码输入错误')
        else:
            return restful.params_error(message=form.get_random_error(), data=form.get_all_errors())


# TODO: 注册页面视图
bp.add_url_rule('/signup/', endpoint='signup', view_func=SignupView.as_view('signup'))
# TODO: 登录页面视图
bp.add_url_rule('/signin/', endpoint='signin', view_func=SigninView.as_view('signin'))
