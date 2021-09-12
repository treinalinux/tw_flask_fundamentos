# DEBUG = True

USERNAME = 'root'
PASSWORD = 'maria@123'
SERVER = 'localhost'
DB = 'flask_fundamentos'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'

SQLALCHEMY_TRACK_MODIFICATIONS = True
