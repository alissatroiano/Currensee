from settings import MINDSDB_EMAIL, MINDSDB_PASSWORD, SECRET_KEY, MDB_URI, DATABASE_URI
import mindsdb_sdk

DATABASE_URI = DATABASE_URI
if DATABASE_URI.startswith("postgres://"):
    DATABASE_URI = DATABASE_URI.replace("postgres://", "postgresql://", 1)

class Config:
    MINDSDB_EMAIL = MINDSDB_EMAIL
    MINDSDB_PASSWORD = MINDSDB_PASSWORD
    SECRET_KEY = SECRET_KEY
    MDB_URI = MDB_URI
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///testdb.sqlite"
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    DEBUG = False
    DEBUG_TB_ENABLED = False