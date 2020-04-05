from flask import Blueprint, views, render_template, request, session, redirect, url_for, flash, jsonify, g
from .froms import LoginForm, ResetPwdForm
from .models import CmsUser, db
from .decorators import login_required
import config
from untils import restful

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
            return restful.params_error(message="", data=form.get_all_errors())


bp.add_url_rule('/login/', endpoint='login', view_func=LoginView.as_view('login'))  # TODO: 登录
bp.add_url_rule('/signout/', endpoint='signout', view_func=SignOutView.as_view('signout'))  # TODO: 退出登录
bp.add_url_rule('/profile/', endpoint='profile', view_func=ProfileView.as_view('profile'))  # TODO: 个人信息
bp.add_url_rule('/resetpwd/', endpoint='resetpwd', view_func=ResetPwdView.as_view('resetpwd'))  # TODO: 修改密码
