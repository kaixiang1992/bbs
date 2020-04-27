import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root123@127.0.0.1:3300/bbs?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# TODO: session秘钥key
SECRET_KEY = os.urandom(24)
# TODO: user_id key
CONFIG_USER_ID = 'abajghjgj'
FRONT_USER_ID = 'a56529231332524'
# TODO: 邮箱配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = "1058628890@qq.com"
MAIL_PASSWORD = "xykgytfhsvumbfgg"
MAIL_DEFAULT_SENDER = "1058628890@qq.com"

