import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient

from bson.objectid import ObjectId

load_dotenv()
MONGODB_URI = os.environ["CONN_STRING"]

print(MONGODB_URI)

client = MongoClient(MONGODB_URI)

db = client.library

magazines_collection = db.magazines

doc_to_find = {"_id": ObjectId("638531c218ead65d1d0804db")}
result = magazines_collection.find_one(doc_to_find)
pprint.pprint(result)

client.close()