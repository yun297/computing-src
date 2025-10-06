from pymongo import MongoClient
import json

client = MongoClient("127.0.0.1", 27017)

client.drop_database("lostfoundDB")

lostfoundDB = client["lostfoundDB"]
reports = lostfoundDB["reports"]

json_file = open("lost_items.json", 'r')
json_data = json.load(json_file)

reports.insert_many(json_data)
