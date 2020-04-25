# TODO: 阿里短信验证码sdk
import requests
import os
from .captcha import Captcha


class AlismsAPI(object):
    APPCODE = '210f36a382794959819558b6d9022e0a'

    def __init__(self, app=None):
        self.url = 'https://feginesms.market.alicloudapi.com/codeNotice'
        self.headers = {
            'Authorization': 'APPCODE %s' % AlismsAPI.APPCODE,
        }
        if app:
            self.init_app(app)

    def init_app(self, app):
        try:
            self.params = {
                'sign': '1',
                'skin': '1'
            }
        except Exception as e:
            raise ValueError('请填写正确的阿里短信配置！')

    def send_sms(self, telephone, **params):
        code = Captcha.gene_text(number=4)  # TODO: 获取随机4位数字字符串
        updateparam = {
            'phone': telephone,
        }
        updateparam.update(params)
        self.params.update(updateparam)  # TODO: 更新请求参数字典
        print('短信发送参数：')
        print(self.params)
        resp = requests.get(url=self.url, params=self.params, headers=self.headers)
        try:
            data = resp.json()
            if data.get('Code') == 'OK':
                return data
            else:
                return False
        except:
            return False
