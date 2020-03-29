from wtforms import StringField, IntegerField, Form
from wtforms.validators import Length, Email, DataRequired


class LoginForm(Form):
    email = StringField(validators=[Email(message='邮箱格式输入有误')])
    password = StringField(validators=[Length(min=6, max=12, message='密码为6-12位字母或数字'),
                                       DataRequired(message='密码不能输入为空')])
    remember = IntegerField()  # TODO: 非必填选项
