import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sichereswort'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bme:geheim@localhost/paitararbeit'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:'PASSWORD'@'DB-Adresse'/'datenbank-name''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
