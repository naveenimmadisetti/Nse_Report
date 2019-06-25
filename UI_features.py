# UI for prompting and showing the Data

from pymongo import MongoClient

client = MongoClient(port= 27017)
db_obj = client['NSE_DB']
collection_obj = db_obj['Nse_1']

req_symbol = "DHFL"
req = "%s" % req_symbol
"""
for record in collection_obj.find({"$and": [{"SYMBOL": req} , {"SERIES" : "EQ"}]}):
    print(record)
"""

#cur = collection_obj.find({'$and': [{"SYMBOL": "DHFL"}, {"SERIES": "EQ"}]})
#for idx in cur:
#    print(idx)

# Query on the single Object
#for record in collection_obj.find({"SYMBOL": req}):
#    print(record)
