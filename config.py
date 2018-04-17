#coding:utf-8
import redis


class Confin(object):
    '''工程配置信息'''
    DEBUG = True
    # 链接数据库路径  部开启改动查询
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/ihome'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    # 添加秘钥
    SECRET_KEY = 'liuxiao'
    # flas_session的配置信息

    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒

class Development(Confin):
    '''开发环境下的配置'''
    pass

class Production(Confin):
    '''生产环境，线上，部署之后'''
    DEBUG = False
    PERMANENT_SESSION_LIFETIME = 3600*24

    #更换mysql数据库

class UnitTest(Confin):
    '''测试环境'''
    TESTING=True
    # 更换mysql数据库



config={

    'dev':Development,
    'pro':Production,
    'test':UnitTest,
}