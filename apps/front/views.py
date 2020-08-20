from flask import (
    Blueprint,
    views,
    render_template,
    request,
    url_for,
    session,
    g,
    abort
)
from exts import db
from .forms import SignupFrom, SigninForm, APostForm, ACommentForm
from ..models import Banners, Boards, PostModel, CommentModel
from .models import FrontUserModel
from .decorators import login_required
from flask_paginate import Pagination, get_page_parameter
from untils import restful, safeutils
import config

bp = Blueprint('front', __name__)


# TODO: 首页视图
@bp.route('/', endpoint='index')
def homepage():
    banners = Banners.query.order_by(Banners.priority.desc()).all()
    boards = Boards.query.all()
    bd = request.args.get('bd', type=int, default=None)  # TODO: 板块ID
    page = request.args.get(get_page_parameter(), type=int, default=1)  # TODO: 读取页数
    start = (page - 1) * config.PER_PAGE
    end = start + config.PER_PAGE
    query_obj = None
    total = None
    if bd:
        query_obj = PostModel.query.filter_by(board_id=bd).order_by(PostModel.create_time.desc())
        posts = query_obj.slice(start, end)
        total = query_obj.count()
    else:
        query_obj = PostModel.query.order_by(PostModel.create_time.desc())
        posts = query_obj.slice(start, end)
        total = query_obj.count()
    pagination = Pagination(bs_version=3, page=page, total=total)
    context = {
        'banners': banners,
        'boards': boards,
        'posts': posts,
        'pagination': pagination,
        'cruent_board_id': bd
    }
    return render_template('front/front_index.html', **context)


# TODO: 帖子详情
@bp.route('/post/<post_id>/', endpoint='postdetails')
def post_details(post_id):
    post = PostModel.query.filter_by(id=post_id).one_or_none()
    comments = CommentModel.query.filter_by(post_id=post_id).order_by(CommentModel.create_time.desc())
    if not post:
        abort(404)
    context = {
        'post': post,
        'comments': comments
    }
    return render_template('front/front_post_detail.html', **context)


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
        # if return_to and return_to != cururl and return_to != url_for(endpoint='front.signup') and safeutils(return_to):
        #     return render_template('front/front_signin.html', return_to=return_to)
        # else:
        #     return render_template('front/front_signin.html')
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


# TODO: 发布帖子视图
class APostView(views.MethodView):
    decorators = [login_required]

    def get(self):
        boards = Boards.query.all()
        return render_template('front/front_apost.html', boards=boards)

    def post(self):
        form = APostForm(request.form)
        if form.validate():
            title = form.title.data
            context = form.context.data
            board_id = form.board_id.data
            author_id = g.front_user.id
            post_item = PostModel(title=title, context=context, board_id=board_id, author_id=author_id)
            db.session.add(post_item)
            db.session.commit()
            return restful.success(message='帖子发布成功')
        else:
            return restful.params_error(message=form.get_random_error(), data=form.get_all_errors())


# TODO: 发布评论
class AComment(views.MethodView):
    decorators = [login_required]

    def post(self):
        form = ACommentForm(request.form)
        if form.validate():
            content = form.content.data
            post_id = form.post_id.data
            author_id = g.front_user.id
            post = PostModel.query.get(post_id)
            if post:
                comment = CommentModel(content=content, post_id=post_id, author_id=author_id)
                db.session.add(comment)
                db.session.commit()
                return restful.success(message='评论发布成功')
            else:
                return restful.params_error(message='评论帖子不存在')
        else:
            return restful.params_error(message=form.get_random_error(), data=form.get_all_errors())


# TODO: 注册页面视图
bp.add_url_rule('/signup/', endpoint='signup', view_func=SignupView.as_view('signup'))
# TODO: 登录页面视图
bp.add_url_rule('/signin/', endpoint='signin', view_func=SigninView.as_view('signin'))
# TODO: 发布帖子视图
bp.add_url_rule('/apost/', endpoint='apost', view_func=APostView.as_view('apost'))
# TODO: 发布评论视图
bp.add_url_rule('/acomment/', endpoint='acomment', view_func=AComment.as_view('acomment'))
