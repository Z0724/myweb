import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    pass

class BaseConfig():
    SECRET_KEY=os.getenv('SECRET_KEY')
    SESSION_PROTECTION = os.getenv('SESSION_PROTECTION')
    TIMEZONE = os.getenv('TIMEZONE')

class MysqlConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS=os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_ECHO = os.getenv('SQLALCHEMY_ECHO')
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')

config = {
    'MysqlConfig': MysqlConfig
}