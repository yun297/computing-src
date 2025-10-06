from flask import Flask, render_template, redirect, url_for
from pymongo import MongoClient
import json
from datetime import datetime


app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["lostfoundDB"]
collection = db["reports"]


@app.route("/")
@app.route("/reports")
def view_reports():
    reports = list(collection.find().sort("date_lost", 1))
    return render_template("reports.html", reports=reports)


if __name__ == "__main__":
    app.run(port=5566, debug=True)
