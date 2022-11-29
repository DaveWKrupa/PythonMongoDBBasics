import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URI = os.environ["CONN_STRING"]

print(MONGODB_URI)

client = MongoClient(MONGODB_URI)

db = client.library

magazines_collection = db.magazines

new_magazine = {
    "name": "Dude Weekly",
    "publishdate": datetime.datetime.utcnow(),
    "numpages": 68
}

result = magazines_collection.insert_one(new_magazine)
doc_id = result.inserted_id
print(doc_id)
client.close()