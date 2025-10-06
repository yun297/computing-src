#Take note that this code will not work as there is no data.json file
import json

with open('data.json', 'r') as file: 
    content = json.load(file) #content variable will contain a list of dictionaries, where each dictionary represents a record