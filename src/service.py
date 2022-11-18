from src.datalayer.models.repository import MetaDataRepository


class MetaDataService :

    def __init__(self) -> None:
        self.reposotory = MetaDataRepository()

    def get_meta_data(self):
        return self.reposotory.get_meta_data()