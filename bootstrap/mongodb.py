import logging

from pymongo import ASCENDING
from pymongo import MongoClient


logger = logging.getLogger(__name__) 


MONGODB_CLIENT = MongoClient('172.17.0.1', 27017)


def install(app):
    
    try:
        db = MONGODB_CLIENT.get_default_database("viacep")
        app.db = db.get_collection("addresses")
        db.addresses.create_index([("cep", ASCENDING)], unique=True)
        MONGODB_CLIENT.server_info()
        
    except Exception as exc:
        logger.error(f"Error connecting to MongoDB: {exc}")
        