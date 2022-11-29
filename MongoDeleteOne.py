import os

from dotenv import load_dotenv
from pymongo import MongoClient

from bson.objectid import ObjectId

load_dotenv()
MONGODB_URI = os.environ["CONN_STRING"]

print(MONGODB_URI)

client = MongoClient(MONGODB_URI)

db = client.library

magazines_collection = db.magazines

id = {"_id": ObjectId("6376e4a890076a8594d57e58") }

result = magazines_collection.delete_one(id)
print("Documents deleted: " + str(result.deleted_count))

client.close()