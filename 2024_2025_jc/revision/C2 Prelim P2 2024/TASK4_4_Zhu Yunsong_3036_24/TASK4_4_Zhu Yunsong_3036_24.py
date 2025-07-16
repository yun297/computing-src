from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def form():
    if request.method == "GET":
        return render_template("form.html")

@app.route("/table", methods = ["POST"])
def table():
    if request.method == "POST":
        date = request.form.get("date")

        conn = sqlite3.connect("TRIP.db")
        cur = conn.cursor()

        cur.execute("""
        SELECT c.Name, f.DepartCity, f.ArrivalCity, t.Seat
        FROM Customer AS c
        INNER JOIN Ticket as t ON t.CustomerNo = c.CustomerNo
        INNER JOIN Flight as f ON t.FlightNo = f.FlightNo
        WHERE t.Date = ?
        """, (date, ))

        flights = cur.fetchall()

        print(flights)

        return render_template("table.html", flights=flights)
    

if __name__ == "__main__":
    app.run()
