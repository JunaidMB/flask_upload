import os 
class Config(object):
    DEBUG = False
    TESTING = False

    UPLOAD_FOLDER = os.path.join(os.getcwd(), "app/uploads/")
    MODEL_FOLDER =  os.path.join(os.getcwd(), "app/model/")
    MODEL_WEIGHTS = os.path.join(os.getcwd(), "app/model/3051crop_weight_200.h5") 

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True

    SESSION_COOKIE_SECURE = False