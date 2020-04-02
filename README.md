# bbs
python flask Actual combat

### Flask项目实战

* 项目结构
    * apps
        * cms `后台管理系统`
        * common `公共组件部分`
        * front `前台页面部分`
    * static `静态文件目录`
    * templates `html模板目录`
    * config.py `配置参数项`
    * exts.py `外部扩展`
    * manage.py `数据库命令映射文件`

* V1.0.0 --- 559.【Flask项目实战】项目结构搭建
* V1.0.1 --- 560.【Flask项目实战】cms用户模型定义
    * 涉及知识点
        * [flask_sqlalchemy](http://wangkaixiang.cn/python-flask/di-liu-zhang-ff1a-sqlalchemy-shu-ju-ku/di-si-jie-ff1aflask-sqlalchemy.html)
        * [flask_script](http://wangkaixiang.cn/python-flask/di-qi-zhang-ff1a-flask-script.html)
        * [flask_migrate](http://wangkaixiang.cn/python-flask/di-ba-zhang-ff1a-flask-migrate.html)
    * manage.py生成数据库
    ```shell script
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    ```
    * 初始化系统用户
    ```shell script
    python manage.py create_default_user -u admin -p admin123 -e admin@qq.com
    ```
    * 加密用户输入密码
    ```python
    # TODO: 加密密码字符串
    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)
    ```
    * 校验用户输入密码是否正确
    ```python
    # TODO: 校验用户输入密码是否正确
    def check_password(self, raw_password):
        result = check_password_hash(pwhash=self.password, password=raw_password)
        return result
    ```
* V1.0.2
    * 涉及知识点
        * [类视图](http://wangkaixiang.cn/python-flask/di-wu-zhang-ff1a-shi-tu-gao-ji/di-yi-jie-ff1a-lei-shi-tu.html)
        * [WTF表单校验](http://wangkaixiang.cn/python-flask/di-jiu-zhang-ff1a-flask-wtf.html)
        * [ORM过滤条件](http://wangkaixiang.cn/python-flask/di-liu-zhang-ff1a-sqlalchemy-shu-ju-ku/di-si-jie-ff1a-sqlalchemy-de-orm-2.html)
        * [cookie和session](https://github.com/kaixiang1992/python-flask/blob/master/519/519.md)
        * [重定向](http://wangkaixiang.cn/python-flask/di-san-zhang-ff1a-flask-ru-men-2014-2014-url/di-san-jie-ff1a-url-yu-shi-tu-han-shu.html)
    * 561.【Flask项目实战】cms后台登录界面完成 `2020/03/29 21:41`
    * 562.【Flask项目实战】cms后台登录功能完成 `2020/03/29 22:58`
* V1.0.3
    * 涉及知识点
        * [装饰器](http://wangkaixiang.cn/python-advance/di-er-zhang-ff1a-zhuang-shi-qi/di-er-jie-ff1a-zhuang-shi-qi.html)
    * 563.【Flask项目实战】cms后台登录限制 `2020/03/30 22:48`
* V1.0.4
    * 涉及知识点
        * [宏](http://wangkaixiang.cn/python-flask/di-si-zhang-ff1a-flask-ru-men-ff08-mo-ban-ff09/di-liu-jie-ff1a-hong-he-import-yu-ju.html)
        * [上下文](http://wangkaixiang.cn/python-flask/di-shi-zhang-ff1a-shang-xia-wen.html)
    * 564.【Flask项目实战】cms后台模版渲染完成 `2020/03/31 22:40`
    * 565.【Flask项目实战】cms用户名渲染和注销功能实现 `2020/04/02 22:55`

##### 欠：10+40+12 = 60节课