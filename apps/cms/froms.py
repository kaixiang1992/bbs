from wtforms import StringField, IntegerField
from wtforms.validators import Length, Email, DataRequired, EqualTo
from ..froms import BaseForm    # TODO: 引入公共表单类来基层


# TODO: 登录表单校验器
class LoginForm(BaseForm):
    email = StringField(validators=[Email(message='邮箱格式输入有误')])
    password = StringField(validators=[Length(min=6, max=12, message='密码为6-12位字母或数字'),
                                       DataRequired(message='密码不能输入为空')])
    remember = IntegerField()  # TODO: 非必填选项


# TODO: 修改密码校验器
class ResetPwdForm(BaseForm):
    oldpwd = StringField(validators=[Length(min=6, max=12, message='密码为6-12位字母或数字'),
                                     DataRequired(message='原密码不能为空')])
    newpwd = StringField(validators=[Length(min=6, max=12, message='密码为6-12位字母或数字'),
                                     DataRequired(message='新密码输入不能为空')])
    newpwd2 = StringField(validators=[Length(min=6, max=12, message='密码为6-12位字母或数字'),
                                      EqualTo(fieldname='newpwd', message='两次密码输入不一致')])
