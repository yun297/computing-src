from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    conn = sqlite3.connect("SUPERMARKET.db")
    cur = conn.cursor()

    cur.execute("""
SELECT c.Name, i.Name, p.Quantity FROM Purchase AS p
INNER JOIN Item AS i ON i.ItemID = p.ItemID
INNER JOIN Customer AS c ON c.CustomerNumber = p.CustomerNumber
WHERE p.DateTime > 20240000
    """)

    data = cur.fetchall()

    conn.close()

    return render_template("index.html", data = data)


if __name__ == "__main__":
    app.run()
