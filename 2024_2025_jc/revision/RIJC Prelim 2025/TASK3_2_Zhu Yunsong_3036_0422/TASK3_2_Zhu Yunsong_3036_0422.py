from flask import Flask, render_template, request
from pymongo import MongoClient

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

if __name__ == "__main__":
    app.run()
