from flask import Blueprint, request
from untils import restful
from untils.captcha import Captcha
from exts import smsapi
from .forms import SMSCaptchaForm

bp = Blueprint('common', __name__, url_prefix='/c')


# @bp.route('/sms_captcha/', methods=['post'])
# def sms_captcha():
#     telephone = request.form.get('telephone')
#     if not telephone:
#         return restful.params_error(message='请传入手机号码！')
#     code = Captcha.gene_text(number=4)  # TODO: 获取随机4位数字字符串
#     resp = smsapi.send_sms(telephone=telephone, param=code)
#     if resp:
#         return restful.success(message='短信验证码发送成功!')
#     else:
#         return restful.params_error(message='短信验证码发送失败！')


# TODO: 发送短信验证码
@bp.route('/sms_captcha/', methods=['post'])
def sms_captcha():
    form = SMSCaptchaForm(request.form)
    if form.validate():
        telephone = form.telephone.data  # TODO: 获取手机号
        code = Captcha.gene_text(number=4)  # TODO: 获取随机4位数字字符串
        resp = smsapi.send_sms(telephone=telephone, param=code)
        if resp:
            return restful.success(message='短信验证码发送成功!')
        else:
            return restful.params_error(message='短信验证码发送失败！')
    else:
        return restful.params_error(message=form.get_random_error(), data=form.get_all_errors())
