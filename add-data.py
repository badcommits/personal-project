from pymongo import MongoClient
import json
from bson import json_util

client = MongoClient("mongodb://localhost:27017/")
database = client["test_db"]
collection = database["test_col"]

all_data = list(collection.find())
print(json.dumps(all_data, default=json_util.default))
