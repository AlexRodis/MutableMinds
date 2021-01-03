import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or\
        '2dc1ff0736667ebe83a51cf66f44e48dfbc1759f2596174aff462b791cbce4eed997994e6c4dd8c8695470367c'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///site.db'
    FLASK_ADMIN_SWATCH = 'cosmo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    