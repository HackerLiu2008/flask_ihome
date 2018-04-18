#coding:utf-8
from flask import session

from . import api

@api.route('/index')
def hello_world():
    session['name']='liuxiao'

    return 'Hello World!'