import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# TODO IMPLEMENT DATABASE URL *
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:elcomy@localhost:5432/fyyur'
