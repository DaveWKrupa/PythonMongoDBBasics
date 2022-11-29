import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
MONGODB_URI = os.environ["CONN_STRING"]

print(MONGODB_URI)

client = MongoClient(MONGODB_URI)

db = client.sample_airbnb

listingAndReviews_collection = db.listingsAndReviews

select_by_bathrooms = { "$match": {"bathrooms": { "$gt": 2.0 }}}

separate_by_type_calculate_average_price = {
    "$group": {"_id": "$property_type", "avg_price": { "$avg": "$price"}}
}

pipeline = [
    select_by_bathrooms,
    separate_by_type_calculate_average_price
]

results = listingAndReviews_collection.aggregate(pipeline)

for item in results:
    pprint.pprint(item)

client.close()