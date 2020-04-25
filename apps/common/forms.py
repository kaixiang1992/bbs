from apps.froms import BaseForm
from wtforms import StringField
from wtforms.validators import DataRequired, Regexp, Length
import hashlib


# TODO: 发送短信验证码Form表单校验
class SMSCaptchaForm(BaseForm):
    salt = 'q3423805gdflvbdfvhsdoa`#$%'  # TODO: 前后端约定的加密盐
    telephone = StringField(validators=[Regexp(r'1[356789]\d{9}', message='手机号格式错误')])  # TODO: 校验手机号
    timestamp = StringField(validators=[DataRequired(message='timestamp字段不能为空'),
                                        Length(min=13, max=13, message='timestamp字段格式错误')])  # TODO: 校验时间戳
    sign = StringField(validators=[DataRequired(message='sign字段不能为空')])  # TODO: 校验sign字段

    def validate(self):
        result = super(SMSCaptchaForm, self).validate()  # TODO: 校验表单输入规则
        if result:
            telephone = self.telephone.data  # TODO: 手机号
            timestamp = self.timestamp.data  # TODO: 时间戳
            sign = self.sign.data  # TODO: 前端传递加密字符串

            # TODO: md5(timestamp+telphone+salt)
            # TODO: md5函数必须要传一个bytes类型的字符串进去
            sign2 = hashlib.md5((timestamp+telephone+self.salt).encode(encoding='utf-8')).hexdigest()
            if sign == sign2:   # TODO: 比对前端传递加密字符串
                return True
            else:
                return False
        else:
            return False
