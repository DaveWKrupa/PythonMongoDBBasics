import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URI = os.environ["CONN_STRING"]

print(MONGODB_URI)

client = MongoClient(MONGODB_URI)

db = client.library

magazines_collection = db.magazines

filter = {"name": {"$in": ["National Geographic", "International Geographic", "Oceanic Geographic"] } }

result = magazines_collection.delete_many(filter)
print("Documents deleted: " + str(result.deleted_count))

client.close()