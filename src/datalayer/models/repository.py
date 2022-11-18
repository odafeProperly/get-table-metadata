from src.datalayer.models import UserDataModel

class MetaDataRepository:
    def get_meta_data(self):
        # return UserDataModel.get_meta_data()
        print(111, UserDataModel.metadata, UserDataModel)
        return {}