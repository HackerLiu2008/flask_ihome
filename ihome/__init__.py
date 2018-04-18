#coding:utf-8
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect


from config import config
from ihome.utils.common import RegexConverter

# 创建链接mysql数据库对象
db = SQLAlchemy()

# 定义全局的redis——store
redis_store=None

def create_app(create_name):

    app = Flask(__name__)

    # 给app用类方法添加属性
    app.config.from_object(config[create_name])

    db.init_app(app)

    # 定义全局变量
    global redis_store
    # 创建链接redis数据库的对象
    redis_store=redis.StrictRedis(host=config[create_name].REDIS_HOST,port=config[create_name].REDIS_PORT)

    # csrf防护
    CSRFProtect(app)

    # 使FLASK——session扩展储存session到redis数据库
    Session(app)

    # ***需要在注册蓝图之前添加自定义路由转换器，以为要有自定义路由转换器后面的路由才能使用
    app.url_map.converters['re']=RegexConverter

    # 哪里注册蓝图就在哪里导入蓝图，避免导入时还不存在，但已经被导入（抽象的很）
    from ihome.api_1_0 import api
    # 注册蓝图api_1_0接口版本
    app.register_blueprint(api)

    from api_1_1 import api2
    # 注册蓝图api_1_1接口版本
    app.register_blueprint(api2)


    return app

