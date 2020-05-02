from flask import Blueprint, views, render_template, request, session, redirect, url_for, flash, jsonify, g
from .froms import LoginForm, ResetPwdForm, ResetEamilForm
from .models import CmsUser, db, CMSPersmission
from .decorators import login_required, permission_required
from flask_mail import Message
from exts import mail
from untils import cacheuntil
import config
from untils import restful
import string
import random

bp = Blueprint('cms', __name__, url_prefix='/cms')


@bp.route('/')
@login_required
def homepage():
    return render_template('cms/cms_index.html')


# TODO: 登录视图函数
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
            errors = form.get_random_error()
            return self.get(messages=errors)


# TODO: 退出登录视图
class SignOutView(views.MethodView):
    decorators = [login_required]

    def get(self):
        # TODO: del session[config.CONFIG_USER_ID]
        # session.clear()
        del session[config.CONFIG_USER_ID]
        print('清除登录缓存信息...')
        print(session.get(config.CONFIG_USER_ID))
        return redirect(url_for(endpoint='cms.login'), 302)


# TODO: 个人信息
class ProfileView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('cms/cms_profile.html')


# TODO: 修改密码
class ResetPwdView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('cms/cms_resetpwd.html')

    def post(self):
        form = ResetPwdForm(request.form)
        if form.validate():
            oldpwd = form.oldpwd.data  # TODO: 旧密码
            newpwd = form.newpwd.data  # TODO: 新密码
            user = g.cms_user
            if user.check_password(raw_password=oldpwd):  # TODO: 校验用户输入密码是否正确
                if oldpwd == newpwd:
                    return jsonify({"code": 200, "message": "新密码不能与旧密码相同"})
                # TODO: 提交新密码
                user.password = newpwd
                db.session.commit()
                # return jsonify({"code": 200, "message": "密码修改成功"})
                return restful.success(message='密码修改成功', data={})
            else:
                # return jsonify({"code": 200, "message": "旧密码输入错误"})
                return restful.success(message='旧密码输入错误', data={})
        else:
            # return jsonify({"code": 400, "data": form.get_all_errors(), "message": ""})
            return restful.params_error(message=form.get_random_error(), data=form.get_all_errors())


# TODO: 修改邮箱
class ResetEmailView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('cms/cms_resetemail.html')

    def post(self):
        form = ResetEamilForm(request.form)
        if form.validate():
            email = form.email.data
            user = g.cms_user
            # TODO: 提交数据更改
            user.email = email
            db.session.commit()
            return restful.success(message='邮箱更改成功')
        else:  # TODO: 参数错误
            return restful.params_error(message=form.get_random_error(), data=form.get_all_errors())


# TODO: 测试发送邮箱
class EmailView(views.MethodView):
    decorators = [login_required]

    def get(self):
        message = Message('测试', recipients=['1058628890@qq.com', '31353wang@sina.com', '694588195@qq.com'],
                          body='flask mail发送的邮箱验证码：1234', sender='1058628890@qq.com')
        mail.send(message=message)
        return 'success'


# TODO: 发送邮箱验证码
class EmailCaptchaView(views.MethodView):
    decorators = [login_required]

    def get(self):
        email = request.args.get('email')
        if not email:
            return restful.params_error(message='邮箱输入不能为空')
        captcha = list(string.ascii_letters)  # TODO: [a-zA-z]拼连
        captcha.extend(list(string.digits))  # TODO: 字符串 '0123456789'拼连
        random_list = random.sample(captcha, 6)  # TODO: 随机从列表中抽取6个元素
        captcha_str = ''.join(random_list)
        message = Message('邮箱验证码',
                          recipients=[email],
                          body='您的验证码为：%s，有效期为5分钟!' % captcha_str,
                          sender='1058628890@qq.com')
        try:  # TODO: 捕获发送验证码异常
            mail.send(message=message)
        except:
            return restful.server_error(message='服务器错误，发送失败.')
        # TODO: redis存储对应邮箱验证码
        cacheuntil.set(key=email, value=captcha_str, ex=300)
        return restful.success(message='验证码发送成功')


# TODO: 板块管理
@bp.route('/boards/')
@login_required
@permission_required(CMSPersmission.BOARDER)
def boards():
    return render_template('cms/cms_boards.html')


# TODO: 评论管理
@bp.route('/comments/')
@login_required
@permission_required(CMSPersmission.COMMENTER)
def comments():
    return render_template('cms/cms_comments.html')


# TODO: CMS用户组管理
@bp.route('/croles/')
@login_required
@permission_required(CMSPersmission.ALL_PERMISSION)
def croles():
    return render_template('cms/cms_croles.html')


# TODO: CMS用户管理
@bp.route('/cusers/')
@login_required
@permission_required(CMSPersmission.CMSUSER)
def cusers():
    return render_template('cms/cms_cusers.html')


# TODO: 前台用户管理
@bp.route('/fusers/')
@login_required
@permission_required(CMSPersmission.FRONTUSER)
def fusers():
    return render_template('cms/cms_fusers.html')


# TODO: 帖子管理
@bp.route('/posts/')
@login_required
@permission_required(CMSPersmission.POSTER)
def posts():
    return render_template('cms/cms_posts.html')


# TODO: 轮播图管理
@bp.route('/banners')
@login_required
def banners():
    return render_template('cms/cms_banners.html')


bp.add_url_rule('/login/', endpoint='login', view_func=LoginView.as_view('login'))  # TODO: 登录
bp.add_url_rule('/signout/', endpoint='signout', view_func=SignOutView.as_view('signout'))  # TODO: 退出登录
bp.add_url_rule('/profile/', endpoint='profile', view_func=ProfileView.as_view('profile'))  # TODO: 个人信息
bp.add_url_rule('/resetpwd/', endpoint='resetpwd', view_func=ResetPwdView.as_view('resetpwd'))  # TODO: 修改密码
bp.add_url_rule('/resetemail/', endpoint='resetemail', view_func=ResetEmailView.as_view('resetemail'))  # TODO: 修改邮箱
bp.add_url_rule('/email/', endpoint='email', view_func=EmailView.as_view('email'))  # TODO: 发送邮箱
# TODO: 发送邮箱验证码
bp.add_url_rule('/email_captcha/', endpoint='emailcaptcha', view_func=EmailCaptchaView.as_view('emailcaptcha'))
