from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
db = client["lostfoundDB"]
collection = db["reports"]

collection.drop()

with open("lost_items.json") as file:
    data = json.load(file)

collection.insert_many(data)