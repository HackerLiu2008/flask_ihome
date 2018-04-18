#coding:utf-8

from flask import Blueprint


# 创建版本1.0的蓝图,第一个参数蓝图名，第二个参数当前模块明，第三个参数在url匹配地址中加前缀
api=Blueprint('api_1_0',__name__,url_prefix='/api/1.0')

from . import index