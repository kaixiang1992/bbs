from flask import Blueprint, request, make_response
from untils import restful, cacheuntil
from untils.captcha import Captcha
from exts import smsapi
from .forms import SMSCaptchaForm
from io import BytesIO

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
            cacheuntil.set(telephone, code)  # TODO: redis存储短信验证码
            return restful.success(message='短信验证码发送成功!')
        else:
            return restful.params_error(message='短信验证码发送失败！')
    else:
        return restful.params_error(message=form.get_random_error(), data=form.get_all_errors())


# TODO: 图形验证码视图
@bp.route('/captcha/')
def CaptchaView():
    text, image = Captcha.gene_graph_captcha()
    cacheuntil.set(text.lower(), text.lower())  # TODO: redis存储图片验证码
    out = BytesIO()
    # TODO: 将图片保存到IO中格式png
    image.save(out, 'png')
    # TODO: 保存完毕后，移动指针到起始位置
    out.seek(0)
    # TODO: 将IO读取出来转为image/png响应
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp
