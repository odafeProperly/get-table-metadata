import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.db_config import DBConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy(
    engine_options={
        "pool_recycle": 115,  # automatically recycles connections before 2 minutes which is when the proxy gets stale
    }
)


def connectDB():
    postgres_uri = f'postgresql://{DBConfig.user}:{DBConfig.password}@{DBConfig.hostMaster}:{DBConfig.port}/{DBConfig.name}'
    engine = create_engine(postgres_uri)
    if not engine:
        print('unable to connect DB')
    session = sessionmaker(bind=engine)
    print(session)

def create_app(app_name):
    """
    Create Flask app and setup DB
    """
    app = Flask(app_name)

    # Connect SQLAlchemy to the Flask app
    global db
    db.init_app(app)

    return app