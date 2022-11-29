from pymongo import MongoClient

from Configuration import Configuration
section_dict = Configuration.config(filename='Database.ini',
                                          section='mongodb')

mongodb_uri = section_dict["conn_string"]
print(mongodb_uri)
client = MongoClient(mongodb_uri)
#client = MongoClient("mongodb+srv://davekrupa:bhu65*VFR@cluster0.ik3qs1o.mongodb.net/?retryWrites=true&w=majority")

for db_name in client.list_database_names():
    print(db_name)