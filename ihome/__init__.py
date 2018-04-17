#coding:utf-8
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from config import Confin
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app = Flask(__name__)




# 给app用类方法添加属性
app.config.from_object(Confin)

# 创建链接mysql数据库对象
db=SQLAlchemy(app)

# 创建链接redis数据库的对象
redis_store=redis.StrictRedis(host=Confin.REDIS_HOST,port=Confin.REDIS_PORT)

# csrf防护
CSRFProtect(app)

# 使FLASK——session扩展储存session到redis数据库
Session(app)

# 创建脚本管理器的对象
manage=Manager(app)

# 让迁移时，db和app关系
Manager(app,db)

# 将数据库迁移的脚本，命令添加到脚本管理器对象
manage.add_command('db',MigrateCommand)

