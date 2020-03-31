import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root123@127.0.0.1:3300/bbs?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# TODO: session秘钥key
SECRET_KEY = os.urandom(24)
# TODO: user_id key
CONFIG_USER_ID = 'abajghjgj'
