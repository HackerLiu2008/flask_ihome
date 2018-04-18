#coding:utf-8
from flask import current_app


from . import api
from ihome import redis_store

# @api.route('/index')
# def hello_world():
#     session['name']='liuxiao'
#
#     return 'Hello World!'


# @api.route('/<file_name>')
@api.route('/<file_name>')
def index(file_name):

    redis_store.set('name','liuxiao')
    file_name='html/'+file_name

    return current_app.send_static_file(file_name)