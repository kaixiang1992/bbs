from flask import (Blueprint, views, render_template)

bp = Blueprint('front', __name__)


@bp.route('/')
def homepage():
    return 'homepage'


# TODO: 注册页面视图
class SignupView(views.MethodView):
    def get(self):
        return render_template('front/front_signup.html')


# TODO: 注册页面视图
bp.add_url_rule('/signup/', endpoint='signup', view_func=SignupView.as_view('signup'))
