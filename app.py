from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/test_db")
database = client["test_db"]
collection = database["test_col"]

@app.route("/")
def main_page():
    return "<h1>Hello World</h1>"

# get names for all books
@app.route("/data")
def get_data():
    all_data = collection.distinct('name')
    return str(all_data)

if __name__ == "__main__":
    app.run(debug=False)