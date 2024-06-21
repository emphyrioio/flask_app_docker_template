import os

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
instance_dir = os.path.join(basedir, "..", "instance", "db")


class Config:
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_BINDS = {
        "blueprint1": "sqlite:///" + os.path.join(instance_dir, "blueprint1.db"),
    }


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass
