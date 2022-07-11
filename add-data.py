from pymongo import MongoClient
import json
from bson import json_util

client = MongoClient("mongodb://localhost:27017/")
database = client["test_db"]
collection = database["test_col"]

# sample data
data = [{"name": "Return of the Native", "author": "Thomas Hardy"}, {"name": "Dracula", "author": "Bram Stoker"}]

# insert data
inserted_data = collection.insert_many(data)

all_data = list(collection.find())
print(json.dumps(all_data, default=json_util.default))