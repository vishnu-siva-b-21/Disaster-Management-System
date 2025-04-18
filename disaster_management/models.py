from pymongo import MongoClient
from disaster_management.config import Config

def create_mongo_client(mongo_uri = Config.MONGO_URI):
    if not mongo_uri:
        raise ValueError("MongoDB URI not found in Config")
    return MongoClient(mongo_uri)

def init_database(client, db_name):
    return client.get_database(db_name)

def init_collection(db_name, coll_name):
    return db_name.get_collection(coll_name)