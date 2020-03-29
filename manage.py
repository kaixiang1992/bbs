from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from exts import db
from apps.cms import models as cms_model

manager = Manager(app=app)
Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)


# TODO: 初始化一个系统用户
@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-e', '--email', dest='email')
def create_default_user(username, password, email):
    cms_user = cms_model.CmsUser(username=username, password=password, email=email)
    db.session.add(cms_user)
    db.session.commit()
    print('初始化系统用户成功...')


if __name__ == '__main__':
    manager.run()
