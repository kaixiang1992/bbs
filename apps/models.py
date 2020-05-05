from exts import db
from datetime import datetime


# TODO: banner轮播图模型
class Banners(db.Model):
    __tablename__ = 'banner'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    link_url = db.Column(db.String(255), nullable=False)    # TODO: 跳转链接
    priority = db.Column(db.String(255), nullable=False)    # TODO: 权重
    create_time = db.Column(db.DATETIME, default=datetime.now)


# TODO: 板块模型
class Boards(db.Model):
    __tablename__ = 'boards'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    create_time = db.Column(db.DATETIME, default=datetime.now)