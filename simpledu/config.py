class BaseConfig(object):
    SECRET_KEY='make sure to set a very very secret key'

class DevelopmentConfig(BaseConfig):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root@localhost:3306/simpledu?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    pass

configs={
        'development':DevelopmentConfig,
        'production':ProductionConfig,
        'testing':TestingConfig
        }

