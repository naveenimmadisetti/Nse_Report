# import librararies
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

#print(root.filename) # just Testing

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

# push the json to the DB
client = MongoClient(port= 27017)
db_obj = client['NSE_DB']
collection_obj = db_obj['Nse_1']
with open(json_path) as data_obj:
    db_data = json.load(data_obj)
collection_obj.insert_many(db_data)
client.close()


