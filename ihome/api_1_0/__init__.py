#coding:utf-8

from flask import Blueprint


# 创建版本1.0的蓝图
api=Blueprint('api_1_0',__name__,url_prefix='/api/1.0')

from . import index