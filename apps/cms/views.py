from flask import Blueprint

bp = Blueprint('cms', __name__, url_prefix='/cms')


@bp.route('/')
def homepage():
    return 'cms homepage'
