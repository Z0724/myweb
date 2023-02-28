import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    pass

class BaseConfig():
    SECRET_KEY=os.getenv('SECRET_KEY')
    SESSION_PROTECTION = os.getenv('SESSION_PROTECTION')

class MysqlConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS=os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_ECHO = os.getenv('SQLALCHEMY_ECHO')

config = {
    'MysqlConfig': MysqlConfig
}