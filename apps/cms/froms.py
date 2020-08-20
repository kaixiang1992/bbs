from wtforms import StringField, IntegerField, ValidationError
from wtforms.validators import Length, Email, DataRequired, EqualTo
from ..froms import BaseForm  # TODO: 引入公共表单类来基层
from flask import g
from untils import cacheuntil


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


# TODO: 修改邮箱校验器
class ResetEamilForm(BaseForm):
    email = StringField(validators=[Email(message='请输入正确的邮箱'), DataRequired(message='邮箱输入不能为空')])
    captcha = StringField(validators=[Length(min=6, max=6, message='验证码输入错误')])

    def validate_email(self, field):  # TODO: 验证邮箱
        email = field.data  # TODO: 输入邮箱
        user = g.cms_user  # TODO: 全局g对象用户信息
        if email == user.email:  # TODO: 修改相同邮箱
            raise ValidationError(message='不能修改相同的邮箱')
        return True

    def validate_captcha(self, field):  # TODO: 验证邮箱验证码
        email = self.email.data  # TODO: 输入邮箱
        captcha = field.data  # TODO: 输入邮箱验证码
        captcha_cache = cacheuntil.get(email).decode('utf-8')  # TODO: redis缓存邮箱验证码 bytes类型需decode解码
        if captcha_cache and captcha_cache.lower() == captcha.lower():  # TODO: 忽略验证码大小写比对
            return True
        raise ValidationError(message='邮箱验证码输入错误')


# TODO: 新增轮播图片校验器
class AddBanerForm(BaseForm):
    name = StringField(validators=[DataRequired(message='图片名称必须填写')])
    image_url = StringField(validators=[DataRequired(message='图片地址必须填写')])
    link_url = StringField(validators=[DataRequired(message='跳转链接必须填写')])
    priority = StringField(validators=[DataRequired(message='权重必须填写')])


# TODO: 更改轮播图片校验器
class UpdateBannerForm(AddBanerForm):
    banner_id = StringField(validators=[DataRequired(message='图片ID不能为空')])


# TODO: 新增板块校验器
class AddBoardsForm(BaseForm):
    name = StringField(validators=[DataRequired(message='板块名称不能为空')])


# TODO: 修改板块校验器
class UpdateBoardsForm(AddBoardsForm):
    board_id = StringField(validators=[DataRequired(message='板块ID不能为空')])


# TODO: 精华帖子板块校验器
class HighlightPostFrom(BaseForm):
    post_id = IntegerField(validators=[DataRequired(message='帖子ID不能为空')])
