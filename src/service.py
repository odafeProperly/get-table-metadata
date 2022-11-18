from src.repository import MetaDataRepository


class MetaDataService :

    def __init__(self) -> None:
        self.reposotory = MetaDataRepository()

    def get_meta_data(self):
        return {}