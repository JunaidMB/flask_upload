class Config(object):
    DEBUG = False
    TESTING = False

    UPLOAD_FOLDER = "/Users/junaid.buttibm.com/Developer/flask_upload/app/uploads/"

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True

    SESSION_COOKIE_SECURE = False