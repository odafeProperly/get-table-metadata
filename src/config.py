import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.db_config import DBConfig

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
    postgres_uri = f'postgresql://{DBConfig.user}:{DBConfig.password}@{DBConfig.hostMaster}:{DBConfig.port}/{DBConfig.name}'
    app.config["SQLALCHEMY_DATABASE_URI"] = postgres_uri

    # Connect SQLAlchemy to the Flask app
    global db
    db.init_app(app)

    return app