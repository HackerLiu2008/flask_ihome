#coding:utf-8
from flask import session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from ihome import create_app,db

app=create_app('pro')
# 创建脚本管理器的对象
manage=Manager(app)

# 让迁移时，db和app关系
Migrate(app,db)

# 将数据库迁移的脚本，命令添加到脚本管理器对象
manage.add_command('db',MigrateCommand)




@app.route('/')
def hello_world():
    session['name']='liuxiao'

    return 'Hello World!'


if __name__ == '__main__':
    app.run()
