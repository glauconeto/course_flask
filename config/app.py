import os
from flask import Flask, Config
import settings

class MyConfig(Config):
    FOO = BAR

class Config(object):
    FOO = "BAR"
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory'

# Contexto de config // Quando criamos o app
app = Flask(__name__)

app.config.from_pyfile('application.cfg', silent=True)

# dicts app.config update
# objects app.config from object
# python from_pyfile

# env vars


@app.route("/")
def index():
    # contexto de request
    return f"CodeShow {app.config['FOO']}"