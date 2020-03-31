from flask import session, redirect, url_for
from functools import wraps
import config


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if config.CONFIG_USER_ID in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('cms.login'))

    return wrapper
