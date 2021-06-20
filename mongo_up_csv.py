import pandas as pd
from pymongo import MongoClient
# Load csv dataset
data = pd.read_csv('tid.csv',dtype={'googleid':object,'name':object})
# Connect to MongoDB
client =  MongoClient("mongodb+srv://arun:arunkhegde@practicecapestone.dvybu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['trackandgoogleid']#dbname
collection = db['test']#collenction
#data.reset_index(inplace=True)
data_dict = data.to_dict("records")
# Insert collection
collection.insert_many(data_dict)

print(data)