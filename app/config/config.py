import os

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
instance_dir = os.path.join(basedir, "..", "instance", "db")
db_name = "db.db"
db_path = os.path.join(instance_dir, db_name)


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + db_path


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass
