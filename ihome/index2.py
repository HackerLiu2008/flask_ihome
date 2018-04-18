#coding:utf-8
from flask import current_app

from ihome import api2


@api2.route('/<re(".*"):file_name>')
def index(file_name):
    # 判断用户填的是否为空后缀，为空怎帮他默认index。html
    if not file_name:
        file_name='index.html'

    # 为网址左上角添加小logo
    if file_name != 'favicon.ico':
        file_name='html/%s' %file_name

    return current_app.send_static_file(file_name)


