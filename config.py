from posixpath import realpath
from flask import app, config
from os.path import join, dirname, realpath




class Config(object):
    SECRET_KEY = 'qazwsxedc9'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS= False