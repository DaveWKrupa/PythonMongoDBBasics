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

conversion_rate_usd_to_gbp = 1.3

select_by_bathrooms = { "$match": {"property_type": "House", "price": {"$gt": 400}, "bathrooms": { "$gt": 1.0 }}}

organize_by_price = {
    "$sort": { "price": -1}
}

return_specified_fields = {
    "$project": {
        "property_type": 1,
        "price": 1,
        "bathrooms": 1,
        "gbp_price": {"$divide": ["$price", conversion_rate_usd_to_gbp]},
        "_id": 0,
    }
}

pipeline = [
    select_by_bathrooms,
    organize_by_price,
    return_specified_fields
]

results = listingAndReviews_collection.aggregate(pipeline)

for item in results:
    pprint.pprint(item)

client.close()