import os
basedir = os.path.abspath(os.path.dirname(__file__))

TOKEN = '712887773:AAGQnjxut9i371Q55D4mGcFDcfeVHnD0avs'

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False