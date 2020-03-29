from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


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

# user = CMSUser()
# print(user.password)
# user.password = 'abc'

# 密码：对外的字段名叫做password
# 密码：对内的字段名叫做_password
