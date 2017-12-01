from pymongo import MongoClient


def connect_to_db(db_name):
    client = MongoClient()
    db = client[db_name]
    return db


def insert_item(db, collection, data):
    mongo_collection = db[collection]
    result = mongo_collection.insert_one(data)
    return result
