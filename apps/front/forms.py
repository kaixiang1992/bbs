from apps.froms import BaseForm
from wtforms import StringField, ValidationError, IntegerField
from wtforms.validators import Regexp, EqualTo, Length, Optional, DataRequired
from untils import cacheuntil


# TODO: 注册表单校验器
class SignupFrom(BaseForm):
    telephone = StringField(validators=[Regexp(regex=r'1[356789]\d{9}', message='请输入正确的手机号')])  # TODO: 手机号
    sms_captcha = StringField(validators=[Regexp(regex=r'[a-zA-Z0-9]{4}',
                                                 message='请输入正确的短信验证码')])  # TODO: 短信验证码
    username = StringField(validators=[Length(min=6, max=12, message='请输入正确的用户昵称')])  # TODO: 用户昵称
    password1 = StringField(validators=[Regexp(regex=r'\w{8,12}', message='请输入正确的密码')])  # TODO: 密码
    password2 = StringField(validators=[EqualTo(fieldname='password1')])  # TODO: 二次密码
    graph_captcha = StringField(validators=[Regexp(regex=r'[a-zA-Z0-9]{4}',
                                                   message='请输入正确的图片验证码')])

    # TODO: 校验用户输入短信验证码
    def validate_sms_captcha(self, field):
        sms_captcha = field.data
        sms_captcha_red = cacheuntil.get(self.telephone.data).decode('utf-8')  # TODO: 读取redis缓存短信验证码
        if not sms_captcha_red or sms_captcha.lower() != sms_captcha_red.lower():
            raise ValidationError(message='短信验证码输入错误')

    # TODO: 校验用户输入图片验证码
    def validate_graph_captcha(self, field):
        graph_captcha = field.data
        graph_captcha_red = cacheuntil.get(graph_captcha.lower()).decode('utf-8')  # TODO: 读取redis缓存图片验证码
        if not graph_captcha_red:
            raise ValidationError(message='图片验证码输入错误')


# TODO: 登录表单校验器
class SigninForm(BaseForm):
    telephone = StringField(validators=[Regexp(regex=r'1[356789]\d{9}', message='请输入正确的手机号')])  # TODO: 手机号
    password = StringField(validators=[Regexp(regex=r'\w{8,12}', message='请输入正确的密码')])  # TODO: 密码
    remember = StringField()  # TODO: 记住我


# TODO: 发布帖子校验器
class APostForm(BaseForm):
    title = StringField(validators=[DataRequired(message='标题不能为空')])
    context = StringField(validators=[DataRequired(message='内容不能为空')])
    board_id = IntegerField(validators=[DataRequired(message='板块必须选择')])


# TODO: 发布评论校验器
class ACommentForm(BaseForm):
    content = StringField(validators=[DataRequired(message='评论内容不能为空')])
    post_id = IntegerField(validators=[DataRequired(message='帖子ID不能为空')])
