from typing import Dict
import pymongo


class Database:
    URI = "mongodb://localhost:27017/pricing"
    DATABASE = pymongo.MongoClient(URI).get_database()

    @staticmethod
    def insert(collection: str, data: Dict):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def remove(collection: str, query: Dict):
        Database.DATABASE[collection].remove(query)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: Dict, data: Dict):
        return Database.DATABASE[collection].update( query, data, upsert=True)


