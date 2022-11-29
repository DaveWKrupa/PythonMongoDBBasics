import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URI = os.environ["CONN_STRING"]

print(MONGODB_URI)

client = MongoClient(MONGODB_URI)

db = client.library

magazines_collection = db.magazines

#filter = {"publishdate": { "$lt": datetime.datetime.utcnow()} }
filter = {"publishdate": { "$ne": "Harkin Publishing"} }
update_magazine = {
    "$set": {"publisher": "Harkin Publishing"}
}

result = magazines_collection.update_many(filter, update_magazine)
print("Documents updated: " + str(result.modified_count))

client.close()
