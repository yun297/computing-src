from flask import Flask, render_template, request, url_for
import sqlite3

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/arrival", methods = ["GET"])
def arrival():
    conn = sqlite3.connect("Airport.db")
    cur = conn.cursor()

    cur.execute("""
SELECT arrivalTime, departure, flightNum FROM Flight
WHERE Flight.destination = "Singapore (SIN)"
    """)

    data = cur.fetchall()
    conn.close()

    return render_template("arrival.html", data = data)

@app.route("/departure", methods = ["GET"])
def departure():
    conn = sqlite3.connect("Airport.db")
    cur = conn.cursor()

    cur.execute("""
SELECT departureTime, destination, flightNum FROM Flight
WHERE Flight.departure = "Singapore (SIN)"
    """)

    data = cur.fetchall()
    conn.close()

    return render_template("departure.html", data = None)

@app.route("/query_flight", methods = ["GET", "POST"])
def query_flight():
    if request.method == "GET":
        return render_template("query_flight.html")
    
    elif request.method == "POST":
        flight_num = request.form.get("flight_num")
        conn = sqlite3.connect("Airport.db")
        cur = conn.cursor()

        cur.execute("""
SELECT flightNum, departure, destination, departureTime, arrivalTime FROM Flight
WHERE Flight.flightNum = ?
        """, (flight_num, ))

        data = cur.fetchall()
        conn.close()

        return render_template("query_flight.html", data = data)
    
if __name__ == "__main__":
    app.run()
