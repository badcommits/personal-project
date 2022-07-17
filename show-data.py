from pymongo import MongoClient
import json
from bson import json_util

client = MongoClient("mongodb://username:password@192.168.49.2:31001/")
database = client["test_db"]
collection = database["test_col"]

all_data = list(collection.distinct('name'))
print(json.dumps(all_data, default=json_util.default))