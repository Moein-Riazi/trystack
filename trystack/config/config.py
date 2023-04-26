from os import environ

class Config:

    ENV = environ.get("TRYSTACK_API_ENV", "production")

    DEBUG = bool(int(environ.get("TRYSTACK_API_DEBUG", "0")))

    TESTING = DEBUG

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:moein@localhost:3306/trystack"#environ.get("TRYSTACK_API_DATABASE_URI", None)

    SQLALCHEMY_RECORD_MODIFICATIONS = DEBUG

    SQLALCHEMY_RECORED_QUERIES = DEBUG

    SQLALCHEMY_ECHO = DEBUG