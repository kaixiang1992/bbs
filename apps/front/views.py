from flask import (
    Blueprint,
    views,
    render_template,
    make_response
)
from untils.captcha import Captcha
from io import BytesIO


bp = Blueprint('front', __name__)


@bp.route('/')
def homepage():
    return 'homepage'


# TODO: 注册页面视图
class SignupView(views.MethodView):
    def get(self):
        return render_template('front/front_signup.html')


# TODO: 图形验证码视图
@bp.route('/captcha/')
def CaptchaView():
    text, image = Captcha.gene_graph_captcha()
    out = BytesIO()
    # TODO: 将图片保存到IO中格式png
    image.save(out, 'png')
    # TODO: 保存完毕后，移动指针到起始位置
    out.seek(0)
    # TODO: 将IO读取出来转为image/png响应
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp


# TODO: 注册页面视图
bp.add_url_rule('/signup/', endpoint='signup', view_func=SignupView.as_view('signup'))
