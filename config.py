import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///{0}'.format(os.path.join(basedir, 'bridgerton.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
