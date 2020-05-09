from functools import wraps
from flask import session, redirect, url_for
import config


# TODO: 前端页面登录拦截器
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if config.FRONT_USER_ID in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('front.signin'))

    return wrapper
