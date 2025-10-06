from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods = ["GET"])
@app.route("/reports", methods = ["GET"])
def reports():
    client = MongoClient("127.0.0.1", 27017)
    lostfoundDB = client["lostfoundDB"]
    reports = lostfoundDB["reports"]

    report_data = list(reports.find().sort("date_lost", 1))

    client.close()

    return render_template("reports.html", data = report_data)

@app.route("/submit", methods = ["GET", "POST"])
def submit():
    if request.method == "GET":
        return render_template("form.html")

    elif request.method == "POST":
        item_name = request.form.get("item_name")
        description = request.form.get("description")
        category = request.form.get("category")
        date_lost = request.form.get("date_lost")
        location = request.form.get("location")

        valid_date = True
        
        if date_lost:
            try:
                datetime.strptime(date_lost, "%Y-%m-%d")
            except ValueError:
                valid_date = False

        if not valid_date:
            return render_template("form.html", wrong_format = True)
        else:
            client = MongoClient("127.0.0.1", 27017)
            lostfoundDB = client["lostfoundDB"]
            reports = lostfoundDB["reports"]

            new_item = {
                "item_name": item_name,
                "description": description,
                "category": category,
                "date_lost": date_lost,
                "location": location,
                "recovered": False
            }

            reports.insert_one(new_item)

            client.close()
            
            return redirect("/")
        
@app.route("/search", methods = ["GET", "POST"])
def search():
    if request.method == "GET":
        return render_template("search.html")

    elif request.method == "POST":
        category = request.form.get("category")
        date_lost = request.form.get("date_lost")

        if category == '' and date_lost == '':
            query = {}
        elif category == '':
            query = {"date_lost": {"$eq": date_lost}}
        elif date_lost == '':
            query = {"category": {"$eq": category}}
        else:
            query = {"$and": [
                {"category": {"$eq": category}},
                {"date_lost": {"$eq": date_lost}}
            ]}

        client = MongoClient("127.0.0.1", 27017)
        lostfoundDB = client["lostfoundDB"]
        reports = lostfoundDB["reports"]

        report_data = list(reports.find(query))

        return render_template("search.html", data = report_data)

if __name__ == "__main__":
    app.run()
