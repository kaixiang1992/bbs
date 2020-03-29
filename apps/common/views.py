from flask import Blueprint

bp = Blueprint('common', __name__, url_prefix='/common')


@bp.route('/')
def homepage():
    return 'common homepage'
