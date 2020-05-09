from flask import Flask
import config
from apps.cms import bp as cms_bp
from apps.common import bp as common_bp
from apps.front import bp as front_bp
from apps.ueditor import bp as ueditor_bp
from exts import db, mail, smsapi
from flask_wtf import CSRFProtect
import os

app = Flask(__name__)


def create_app():
    app.config.from_object(config)
    app.register_blueprint(cms_bp)
    app.register_blueprint(common_bp)
    app.register_blueprint(front_bp)
    app.register_blueprint(ueditor_bp)
    db.init_app(app=app)
    mail.init_app(app=app)
    smsapi.init_app(app=app)
    CSRFProtect(app)  # TODO: csrf保护
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)
