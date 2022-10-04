import os

basedir = os.path.dirname(os.path.abspath(__file__))
database_file = f"sqlite:///{os.path.join(basedir, 'users.db')}"

SECRET_KEY = "secretkey"
SQLALCHEMY_DATABASE_URI = database_file