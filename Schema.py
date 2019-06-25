
import pymongo
from pymongo import MongoClient

client = MongoClient(port= 27017)
db_obj = client['NSE_DB']
collection_Nse_1 = db_obj['Nse_1']
collection_Nse_2 = db_obj['Nse_2']

#creating the index for the collection
#collection_Nse_1.create_index([('SYMBOL', pymongo.ASCENDING) , ('SERIES' , pymongo.ASCENDING)],
#                              background = True)

# now getting the symbol and the series and making them as the Indexes
#cur = collection_Nse_1.find({} , {'SYMBOL' : 1, 'SERIES' : 1})

cur_distinct = collection_Nse_1.distinct({"SYMBOL" , "SERIES"})

for idx in cur_distinct:
    collection_Nse_2.insert_one()

#collection_Nse_2.insert_many(cur)

collection_Nse_2.create_index([('SYMBOL', pymongo.ASCENDING), ('SERIES', pymongo.ASCENDING)],
                                  background=True)

