from .views import bp
import config
from flask import session, g
from .models import CmsUser


@bp.before_request
def beforeRequest():
    # print('存储session信息....')
    # print(config.CONFIG_USER_ID in session)
    if config.CONFIG_USER_ID in session:  # TODO: 登录后
        user_id = session.get(config.CONFIG_USER_ID)
        # print(user_id)
        user = CmsUser.query.filter_by(id=user_id).one_or_none()
        if user:
            g.cms_user = user
