from dataclasses import dataclass
from sqlalchemy import Column, String, Integer, Table
from src.config import db
from sqlalchemy import MetaData

metadata = MetaData()

UserDataModel = Table('user', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(16), nullable=False),
    Column('email_address', String(60)),
    Column('password', String(20), nullable=False)
)