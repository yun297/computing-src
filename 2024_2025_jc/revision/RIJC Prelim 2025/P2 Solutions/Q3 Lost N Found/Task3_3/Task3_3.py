from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import json
from datetime import datetime


app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["lostfoundDB"]
collection = db["reports"]


@app.route("/")
def home():
    return redirect(url_for("view_reports"))

@app.route("/reports")
def view_reports():
    reports = list(collection.find().sort("date_lost", 1))
    return render_template("reports.html", reports=reports)

def validatedate(lostdate):
    if len(lostdate) == 10:
        try:
            lostdate = datetime.strptime(lostdate, "%Y-%m-%d")
        except:
            return False
    else:
        return False


@app.route('/submit', methods = ["GET", 'POST'])
def check():
    if request.method == "POST":
        try:
            # date = request.form['date_lost']
            # date = datetime.datetime.strptime(date, '%Y-%m-%d')
            
            results = collection.insert_one(dict(request.form))
            print(results)
            client.close()
            return 'success'
        except:
            return 'invalid date'
    else:
        return render_template("submit.html") 

# @app.route("/submit", methods=["GET", "POST"])
# def submit():
#     if request.method == "POST":
#         if validatedate(request.form["date_lost"]):
#             item = {
#                 "item_name": request.form["item_name"],
#                 "description": request.form["description"],
#                 "category": request.form["category"],
#                 "date_lost": request.form["date_lost"],
#                 "location": request.form["location"]
#             }
#             collection.insert_one(item)
#             return redirect(url_for("view_reports"))
#         else:
#             return "Invalid date!"
        
#     return render_template("submit.html")


if __name__ == "__main__":
    app.run(port=5566, debug=True)
