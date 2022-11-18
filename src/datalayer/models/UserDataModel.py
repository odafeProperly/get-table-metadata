from dataclasses import dataclass
from sqlalchemy import Column, String
from src.config import db
from sqlalchemy import MetaData

metadata_obj = MetaData()
@dataclass
class UserDataModel(db.Model):
    __tablename__ = 'User'
    metadata_obj
    id = Column(String, primary_key=True, nullable=False)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    othernames = Column(String(20), nullable=False)
    email = Column(nullable=False, unique=True)
    password = Column(nullable=False)
    role = Column(nullable=False)

    def __repr__(self) -> str:
        return f'<User {self.email}>'

    def get_meta_data(self): 
        return MetaData()

