from flask import Flask, render_template, request, url_for
import sqlite3

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/round/<number>", methods = ["GET"])
def round(number):
    conn = sqlite3.connect("Task4.db")
    cur = conn.cursor()

    cur.execute("""
SELECT c.name, s.score FROM scores AS s
INNER JOIN competitor AS c ON c.id = s.id
WHERE s.round = ?
ORDER BY s.score DESC
    """, (number, ))

    rows = cur.fetchall()
    conn.close()

    return render_template("round.html", data = rows, number = number)

@app.route("/mean", methods = ["GET"])
def mean():
    conn = sqlite3.connect("Task4.db")
    cur = conn.cursor()

    cur.execute("""
SELECT c.name, ROUND(AVG(s.score), 2) AS average_score FROM scores AS s
INNER JOIN competitor AS c ON c.id = s.id
GROUP BY c.id
ORDER BY c.name
    """)

    rows = cur.fetchall()
    conn.close()

    data = []

    for row in rows:
        data.append([row[0], f"{row[1]:.2f}"])

    return render_template("mean.html", data = data)

@app.route("/qualifiers", methods = ["GET"])
def qualifiers():
    conn = sqlite3.connect("Task4.db")
    cur = conn.cursor()

    cur.execute("""
SELECT
	c.name,
	SUM(s.score) AS total,
	SUM(s.score) > 250
FROM scores AS s
INNER JOIN competitor AS c ON c.id = s.id
GROUP BY c.id
ORDER BY total DESC
    """)

    rows = cur.fetchall()
    conn.close()

    return render_template("qualifiers.html", data = rows)

if __name__ == "__main__":
    app.run()
