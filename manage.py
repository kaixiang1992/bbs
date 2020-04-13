from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from exts import db
from apps.cms import models as cms_model

manager = Manager(app=create_app())
Migrate(app=create_app(), db=db)
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


# TODO: 初始化创建权限数据
@manager.command
def create_default_roles():
    # 1. 访问者（可以修改个人信息）
    visitor = cms_model.CmsRole(name='访问者', desc='只能相关数据，不能修改。')
    visitor.permissions = cms_model.CMSPersmission.VISITOR

    # 2. 运营角色（修改个人个人信息，管理帖子，管理评论，管理前台用户）
    operator = cms_model.CmsRole(name='运营', desc='管理帖子，管理评论,管理前台用户。')
    operator.permissions = cms_model.CMSPersmission.VISITOR | cms_model.CMSPersmission.POSTER \
                           | cms_model.CMSPersmission.CMSUSER | cms_model.CMSPersmission.COMMENTER \
                           | cms_model.CMSPersmission.FRONTUSER

    # 3. 管理员（拥有绝大部分权限）
    admin = cms_model.CmsRole(name='管理员', desc='拥有本系统所有权限。')
    admin.permissions = cms_model.CMSPersmission.VISITOR | cms_model.CMSPersmission.POSTER | \
                        cms_model.CMSPersmission.CMSUSER | cms_model.CMSPersmission.COMMENTER | \
                        cms_model.CMSPersmission.FRONTUSER | cms_model.CMSPersmission.BOARDER

    # 4. 开发者
    developer = cms_model.CmsRole(name='开发者', desc='开发人员专用角色。')
    developer.permissions = cms_model.CMSPersmission.ALL_PERMISSION

    db.session.add_all([visitor, operator, admin, developer])
    db.session.commit()


# TODO: 初始化用户权限
@manager.option('-e', '--email', dest="email")
@manager.option('-i', '--id', dest='id')
def add_user_role(email, id):
    user = cms_model.CmsUser.query.filter_by(email=email).one_or_none()
    print(user)
    if user:
        role = cms_model.CmsRole.query.get(id)
        print(role)
        if role:
            role.users.append(user)
            db.session.add(role)
            db.session.commit()
            print('%s 用户权限添加成功！' % email)
        else:
            print('id为：%s，角色不存在' % id)
    else:
        print('%s 邮箱不存在！' % email)


# TODO: 测试用户是否拥有某个权限
@manager.option('-e', '--email', dest='email')
@manager.option('-i', '--id', dest='id')
def test_user_permission(email, id):
    user = cms_model.CmsUser.query.filter_by(email=email).one_or_none()
    print(user)
    if user:
        role = cms_model.CmsRole.query.get(id)
        print(role)
        if role:
            if user.has_permission(permission=role.permissions):
                print('%s 权限，%s 该用户拥有！' % (role.name, user.email))
            else:
                print('%s 权限，%s 该用户权限不足！' % (role.name, user.email))
        else:
            print('id为：%s，角色不存在' % id)
    else:
        print('%s 邮箱不存在！' % email)


if __name__ == '__main__':
    manager.run()
