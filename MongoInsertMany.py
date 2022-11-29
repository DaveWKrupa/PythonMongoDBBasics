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

new_magazines = [
    {
        "name": "Newsday",
        "publishdate": datetime.datetime.utcnow(),
        "numpages": 97
    },
    {
        "name": "Star Citizen Magazine",
        "publishdate": datetime.datetime.utcnow(),
        "numpages": 28
    }
]

result = magazines_collection.insert_many(new_magazines)
doc_ids = result.inserted_ids
print("number of new magazines: " + str(len(doc_ids)))
print(f"ids:  {doc_ids}")
client.close()