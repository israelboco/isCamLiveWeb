# /config.py

class Config:
    SECRET_KEY = 'secret!'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///camlive.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False