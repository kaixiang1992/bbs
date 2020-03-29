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