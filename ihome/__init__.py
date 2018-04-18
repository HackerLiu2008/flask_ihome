#coding:utf-8
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from config import config


# 创建链接mysql数据库对象
from ihome.api_1_0 import api

db = SQLAlchemy()

def create_app(create_name):

    app = Flask(__name__)

    # 给app用类方法添加属性
    app.config.from_object(config[create_name])

    db.init_app(app)

    # 创建链接redis数据库的对象
    redis_store=redis.StrictRedis(host=config[create_name].REDIS_HOST,port=config[create_name].REDIS_PORT)

    # csrf防护
    CSRFProtect(app)

    # 使FLASK——session扩展储存session到redis数据库
    Session(app)

    # 注册蓝图
    app.register_blueprint(api)


    return app

