from flask import session, redirect, url_for, g
from functools import wraps
import config


# TODO: 登录拦截器
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('登录拦截器...')
        if config.CONFIG_USER_ID in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('cms.login'))

    return wrapper


# TODO: 权限角色拦截器
def permission_required(permission):
    def outer(func):
        @wraps(func)
        def inner(*args, **kwargs):
            print('权限角色拦截器...')
            user = g.cms_user
            if user.has_permission(permission):
                return func(*args, **kwargs)
            else:
                return redirect(url_for('cms.homepage'))

        return inner

    return outer
