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

id = {"_id": ObjectId("6376e4a890076a8594d57e58") }
update_magazine = {
    "$set": {"numpages": 42}
}

result = magazines_collection.update_one(id, update_magazine)
print("Documents updated: " + str(result.modified_count))
pprint.pprint(magazines_collection.find_one(id))
client.close()