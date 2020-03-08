import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'do-or-do-not-there-is-no-try'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/ezgi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False