from .views import bp
import config
from flask import session, g
from .models import CmsUser, CMSPersmission


# TODO: 在每次请求之前执行
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


# TODO: 上下文处理器。返回的字典中的键可以在模板上下文中使用
@bp.context_processor
def contextProcessor():
    print('上下文处理器....')
    return {"CMSPermission": CMSPersmission}
