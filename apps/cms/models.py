from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


# TODO: 用户类
class CmsUser(db.Model):
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(100), nullable=False, name='password')
    email = db.Column(db.String(50), nullable=False, unique=True)
    create_time = db.Column(db.DateTime, default=datetime.now)

    # TODO: 子类重写__init__方法
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    @property
    def password(self):
        return self._password

    # TODO: 加密密码字符串
    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    # TODO: 校验用户输入密码是否正确
    def check_password(self, raw_password):
        result = check_password_hash(pwhash=self.password, password=raw_password)
        return result

    # TODO: 获取用户所有权限
    @property
    def permissions(self):
        if not self.roles:
            return 0
        all_permissions = 0
        # TODO: 遍历用户所有权限
        for role in self.roles:
            permission = role.permissions
            # TODO: 或运算：0|1=1 0|0=0 相当于Python if条件中的or
            all_permissions |= permission
        return all_permissions

    # TODO: 验证用户是否拥有某个权限
    def has_permission(self, permission):
        # permissions = self.permissions
        # TODO: 与运算：0&1=0 1&1=1 相当于python if条件中的and
        # result = permissions & permission == permission
        # return result

        return self.permissions & permission == permission

    # TODO: 验证用户是否为开发者
    @property
    def is_developer(self):
        return self.has_permission(CMSPersmission.ALL_PERMISSION)

    def __repr__(self):
        return '<CmsUser(username=%s, email=%s)>' % (self.username, self.email)

# user = CMSUser()
# print(user.password)
# user.password = 'abc'

# 密码：对外的字段名叫做password
# 密码：对内的字段名叫做_password


# TODO: 权限列表
class CMSPersmission(object):
    # 255的二进制方式来表示 1111 1111
    ALL_PERMISSION = 0b11111111
    # 1. 访问者权限
    VISITOR = 0b00000001
    # 2. 管理帖子权限
    POSTER = 0b00000010
    # 3. 管理评论的权限
    COMMENTER = 0b00000100
    # 4. 管理板块的权限
    BOARDER = 0b00001000
    # 5. 管理前台用户的权限
    FRONTUSER = 0b00010000
    # 6. 管理后台用户的权限
    CMSUSER = 0b00100000
    # 7. 管理后台管理员的权限
    ADMINER = 0b01000000


# TODO: 用户权限中间关联表
cms_users_role = db.Table(
    'cms_users_role',
    db.Column('id', db.Integer, primary_key=True, autoincrement=True, default=1),
    db.Column('cms_role_id', db.Integer, db.ForeignKey('cms_role.id'), primary_key=True),
    db.Column('cms_user_id', db.Integer, db.ForeignKey('cms_user.id'), primary_key=True),
    db.Column('create_time', db.DATETIME, default=datetime.now)
)


# TODO: 权限角色
class CmsRole(db.Model):
    __tablename__ = 'cms_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    desc = db.Column(db.TEXT, nullable=True)
    # TODO: 默认访问者权限
    permissions = db.Column(db.Integer, default=CMSPersmission.VISITOR)
    create_time = db.Column(db.DATETIME, default=datetime.now)

    users = db.relationship('CmsUser', secondary=cms_users_role, backref=db.backref('roles', uselist=True),
                            uselist=True)


    def __repr__(self):
        return '<CmsRole(name=%s, desc=%s)>' % (self.name, self.desc)
