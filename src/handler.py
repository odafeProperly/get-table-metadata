from src.service import MetaDataService
class MetaDataHandler :

    def __init__(self) -> None:
        self.service = MetaDataService()

    def get_meta_data(self):
        return self.service.get_meta_data()