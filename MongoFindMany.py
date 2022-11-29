import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
MONGODB_URI = os.environ["CONN_STRING"]

print(MONGODB_URI)

client = MongoClient(MONGODB_URI)

db = client.library

magazines_collection = db.magazines

docs_to_find = {"numpages": {"$gt": 1}}
cursor = magazines_collection.find(docs_to_find)

num_docs = 0
for doc in cursor:
    num_docs += 1
    pprint.pprint(doc)
    print()

print("# of docs found: " + str(num_docs))

