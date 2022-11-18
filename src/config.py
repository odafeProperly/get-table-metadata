import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(
    engine_options={
        "pool_recycle": 115,  # automatically recycles connections before 2 minutes which is when the proxy gets stale
    }
)

def create_app(app_name):
    """
    Create Flask app and setup DB
    """
    app = Flask(app_name)
    # POSTGRES_URI = f'postgresql://{DBConfig.user}:{DBConfig.password}@{DBConfig.hostMaster}:{DBConfig.port}/{DBConfig.name}'

    # Connect SQLAlchemy to the Flask app
    global db
    db.init_app(app)

    return app