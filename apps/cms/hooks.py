from .views import bp
import config
from flask import session, g
from .models import CmsUser


@bp.before_request
def beforeRequest():
    if config.CONFIG_USER_ID in session:  # TODO: 登录后
        user_id = session.get(config.CONFIG_USER_ID)
        user = CmsUser.query.filter_by(id=user_id).one_or_none()
        if user:
            g.cms_user = user
