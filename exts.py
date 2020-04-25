from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail  # TODO: 发送邮箱验证码服务
from untils.alisms import AlismsAPI  # TODO: 发送短信服务

db = SQLAlchemy()
mail = Mail()
smsapi = AlismsAPI()
