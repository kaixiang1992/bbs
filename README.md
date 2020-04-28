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
        * [模板继承](http://wangkaixiang.cn/python-flask/di-si-zhang-ff1a-flask-ru-men-ff08-mo-ban-ff09/di-ba-jie-ff1a-mo-ban-ji-cheng.html)
        * [set语句](http://wangkaixiang.cn/python-flask/di-si-zhang-ff1a-flask-ru-men-ff08-mo-ban-ff09/di-qijie-ff1a-include-he-set-yu-ju.html)
        * [CSRF保护](http://wangkaixiang.cn/python-flask/di-jiu-zhang-ff1a-flask-wtf.html)
    * 564.【Flask项目实战】cms后台模版渲染完成 `2020/03/31 22:40`
    * 565.【Flask项目实战】cms用户名渲染和注销功能实现 `2020/04/02 22:55`
    * 566.【Flask项目实战】cms模版抽离和个人信息页面完成 `2020/04/05 11:29`
    * 567.【Flask项目实战】cms登录页面CSRF保护 `2020/04/05 15:33`
    * 568.【Flask项目实战】cms后台修改密码界面布局完成 `2020/04/05 16:50`
    * 569.【Flask项目实战】cms后台修改密码ajax功能完成 `2020/04/05 17:10`
    * 570.【Flask项目实战】cms后台密码修改服务器逻完成 `2020/04/05 17:59`
    * 571.【Flask项目实战】优化json数据的返回 `2020/04/05 22:22`
    * 572.【Flask项目实战】sweetalert提示框用法讲解 `2020/04/05 22:58`
    * 573.【Flask项目实战】sweetalert优化修改密码结果反馈 `2020/04/06 23:07`
* V1.0.5
    * 涉及知识点
        * [flask-mail](https://pythonhosted.org/Flask-Mail/)
        * [string](https://docs.python.org/zh-cn/3.7/library/string.html)
        * [random](https://docs.python.org/zh-cn/3.7/library/random.html)
        * [redis](http://wangkaixiang.cn/python-flask/di-shi-sizhang-ff1a-redis-jiao-cheng.html)
        * [字符串编码解码](http://wangkaixiang.cn/python3/liu-3001-zi-fu-chuan.html)
    * 574.【Flask项目实战】修改邮箱界面完成 `2020/04/06 23:30`
    * 575.【Flask项目实战】Flask-Mail的使用以及邮箱配置 `2020/04/08 22:26`
    * 576.【Flask项目实战】发送邮箱验证码 `2020/04/08 23:06`
    * 577.【Flask项目实战】修改邮箱功能完成 `2020/04/09 22:35`
* V1.0.6
    * 578.【Flask项目实战】二进制及其相关运算 `2020/04/11 11:42`
    * 579.【Flask项目实战】权限和角色模型定义 `2020/04/13 22:13`
    * 580.【Flask项目实战】权限判断功能完成 `2020/04/13 23:17`
    * 581.【Flask项目实战】客户端权限验证功能完成 `2020/04/14 22:02`
    * 582.【Flask项目实战】服务端权限验证功能完成 `2020/04/14 23:04`
* V1.0.7
    * 涉及知识点
        * [字典](http://wangkaixiang.cn/python3/jiu-3001-zi-dian.html)
    * 583.【Flask项目实战】前台用户模型创建（1） `2020/04/20 22:45`
    * 584.【Flask项目实战】前台用户模型创建（2） `2020/04/20 23:10`
    * 585.【Flask项目实战】注册界面完成 `2020/04/20 23:31`
    * 586.【Flask项目实战】图形验证码生成技术详解 `2020/04/21 23:11`
    * 587.【Flask项目实战】点击更换图形验证码 `2020/04/22 21:17`
    * 588.【Flask项目实战】发送短信验证码 `2020/04/22 22:10`
    * 589.【Flask项目实战】注册页面对接短信验证码接口 `2020/04/25 11:32`
    * 590.【Flask项目实战】短信验证码接口加密和js代码混淆 `2020/04/25 22:47`
    * 591.【Flask项目实战】缓存验证码 `2020/04/26 21:13`
    * 592.【Flask项目实战】注册功能前端逻辑代码完成 `2020/04/26 21:45`
    * 593.【Flask项目实战】注册功能后台逻辑代码完成 `2020/04/26 22:05`
    * 594.【Flask项目实战】注册完成跳转会上一个页面 `2020/04/26 23:08`
    * 595.【Flask项目实战】登录界面完成 `2020/04/27 22:21`
    * 596.【Flask项目实战】登录功能完成 `2020/04/27 22:47`
* V1.0.8
    * 597.【Flask项目实战】首页导航条实现和代码抽离 `2020/04/27 22:47`
    * 598.【Flask项目实战】首页轮播图实现 `2020/04/28 22:52`