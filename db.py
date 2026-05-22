from pymongo import MongoClient

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.client = MongoClient("mongodb://localhost:27017/")
            cls._instance.database = cls._instance.client["centro_sanitario"]
        return cls._instance

    def get_database(self):
        return self.database