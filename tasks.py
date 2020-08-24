from flask import Flask
from celery import Celery
import config
from flask_mail import Message  # TODO: 发送邮箱验证码服务
from exts import mail, smsapi

app = Flask(__name__)
app.config.from_object(config)
mail.init_app(app)
smsapi.init_app(app)


# 运行本文件
# 在Windows操作系统上：
# celery -A tasks.celery worker --pool=solo --loglevel=info
# 在*nix操作系统上：
# celery -A tasks.celery worker --loglevel=info

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


celery = make_celery(app)


# TODO: 异步发送邮箱验证码
@celery.task
def send_mail(subject, recipients, body, sender):
    message = Message(subject=subject, recipients=recipients, body=body, sender=sender)
    mail.send(message)


# TODO: 异步发送短信验证码
@celery.task
def send_sms(telephone, code):
    smsapi.send_sms(telephone=telephone, param=code)
