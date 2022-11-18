import json
from flask import Flask, request, Response
from flask.views import MethodView
from src.handler import MetaDataHandler
from sqlalchemy import MetaData

class MetaDataView(MethodView):

    def __init__(self) -> None:
        self.handler = MetaDataHandler()
        
    def get(self):
        """
        get meta data of a table
        """
        return self.handler.get_meta_data()