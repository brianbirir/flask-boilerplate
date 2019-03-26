class Config:
    DEBUG = False
    TESTING = False
    SECRET = b'\xcf\x92W\x88w\x85s\xebiE\xfe\x13\xb9\x92\xe3\xee'


class ProductionConfig(Config):

    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
