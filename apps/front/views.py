from flask import (
    Blueprint,
    views,
    render_template,
    request
)
from exts import db
from .forms import SignupFrom
from .models import FrontUserModel
from untils import restful, safeutils

bp = Blueprint('front', __name__)


@bp.route('/')
def homepage():
    return render_template('front/front_test.html')


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


# TODO: 注册页面视图
bp.add_url_rule('/signup/', endpoint='signup', view_func=SignupView.as_view('signup'))
