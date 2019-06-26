#import
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import csv
import json
from pymongo import MongoClient
import pandas as pd
import pathlib


root = Tk()
root.filename = filedialog.askopenfilename(initialdir = "/" , title = "Select CSV File" , filetypes =
(("csv files" , "*.csv"),("all files" , "*.*")))

# just Testing
#print(root.filename)

# this csv_path will have the path of the csv file Selected
csv_path = root.filename

"""
#Verification via pandas
csv_file = pd.read_csv(csv_path)
print(csv_file)
"""

# array to read the csv by row by row and got appended
arr = []
with open(csv_path) as csv_obj:
    csv_reader = csv.DictReader(csv_obj)

    #Just Testing
    #print(csv_reader)

    for csv_row in csv_reader:
        arr.append(csv_row)

# gui to get the name of the file
master = tk.Tk()
tk.Label(master, text="File Name").grid(row=0)
e1 = tk.Entry(master)
e1.grid(row=0, column=1)
tk.Button(master, text='Ok', command=master.quit).grid(row=1,column=0,sticky=tk.W,pady=4)
tk.mainloop()

#test file name from GUI
#print("File Name: %s\n" % (e1.get()))

# this json_path variable will get the filename that is prompted by the tkinter
json_path = pathlib.Path('%s.json' % (e1.get()))

#Dumping the CSV array to the Json
with open(json_path, 'a') as json_obj:
    json_obj.write(json.dumps(arr , indent= 4))


# DB Connection via pymongo mongo client

client = MongoClient(port= 27017)
db_obj = client['NSE_DB_2']
collection_Nse_1 = db_obj['Nse_1']
collection_Nse_2 = db_obj['Nse_2']
collection_Nse_3 = db_obj['Nse_3']

# Loading the JSON file into object'values'
jsonfile = open(json_path , 'r')
values = json.load(jsonfile)

# Parsing through the json and Validating the Schema By FIND
for obj in values:
    symbol = obj['SYMBOL']
    series = obj[' SERIES']
    date = obj[' DATE1']
    avg = obj[' AVG_PRICE']
    ttl = obj[' TTL_TRD_QNTY']
    turnover = obj[' TURNOVER_LACS']
    Prev_Close = obj[' PREV_CLOSE']
    Open_Price = obj[' OPEN_PRICE']
    High_Price = obj[' HIGH_PRICE']
    Low_Price = obj[' LOW_PRICE']
    Last_Price = obj[' LAST_PRICE']
    Close_Price = obj[' CLOSE_PRICE']
    No_of_Trades = obj[' NO_OF_TRADES']
    Delivery_Qty = obj[' DELIV_QTY']
    Delivery_Per = obj[' DELIV_PER']

    # If condition to map the values
    cur_obj = collection_Nse_1.find({"$and" : [{"SYMBOL" : symbol} , {"SERIES" : series}]})
    cur_list = list(cur_obj)
    if not cur_list:
        doc_obj = collection_Nse_1.insert_one({"SYMBOL": symbol, "SERIES": series})

        doc_2 = collection_Nse_2.insert_one({"Nse_1_id": doc_obj.inserted_id, "DATE": date,
                                             "AVG": avg, "TURN_OVER": turnover, "VOLUME": ttl})
        doc_3 = collection_Nse_3.insert_one({"Nse_1_id": doc_obj.inserted_id, "DATE": date,
                                             "PREV_CLOSE": Prev_Close, "OPEN_PRICE": Open_Price,
                                             "HIGH_PRICE": High_Price,
                                             "LOW_PRICE": Low_Price, "LAST_PRICE": Last_Price,
                                             "CLOSE_PRICE": Close_Price,
                                             "NO_OF_TRADES": No_of_Trades, "DELIVERY_QTY": Delivery_Qty,
                                             "DELIVERY_PER": Delivery_Per})
    else:
        cur_dict = cur_list[0]
        cur_dict_id = cur_dict['_id']
        doc_2 = collection_Nse_2.insert_one({"Nse_1_id": cur_dict_id, "DATE": date,
                                             "AVG": avg, "TURN_OVER": turnover, "VOLUME": ttl})
        doc_3 = collection_Nse_3.insert_one({"Nse_1_id": cur_dict_id, "DATE": date,
                                             "PREV_CLOSE": Prev_Close, "OPEN_PRICE": Open_Price,
                                             "HIGH_PRICE": High_Price,
                                             "LOW_PRICE": Low_Price, "LAST_PRICE": Last_Price,
                                             "CLOSE_PRICE": Close_Price,
                                             "NO_OF_TRADES": No_of_Trades, "DELIVERY_QTY": Delivery_Qty,
                                             "DELIVERY_PER": Delivery_Per})


    """
    doc_obj = collection_Nse_1.insert_one({"SYMBOL" : symbol , "SERIES" : series})

    doc_2 = collection_Nse_2.insert_one({"Nse_1_id" : doc_obj.inserted_id , "DATE" : date ,
                                         "AVG" : avg , "TURN_OVER" : turnover , "VOLUME" : ttl})
    doc_3 = collection_Nse_3.insert_one({"Nse_1_id": doc_obj.inserted_id, "DATE": date,
                                         "PREV_CLOSE" : Prev_Close ,"OPEN_PRICE" : Open_Price , "HIGH_PRICE" : High_Price,
                                         "LOW_PRICE" : Low_Price , "LAST_PRICE" : Last_Price , "CLOSE_PRICE" : Close_Price,
                                         "NO_OF_TRADES" : No_of_Trades , "DELIVERY_QTY" : Delivery_Qty ,
                                         "DELIVERY_PER" : Delivery_Per})
                                         
    """

