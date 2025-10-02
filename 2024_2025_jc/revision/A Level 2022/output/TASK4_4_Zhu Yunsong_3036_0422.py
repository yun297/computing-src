from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    conn = sqlite3.connect("LIBRARY.db")
    cur = conn.cursor()

    cur.execute("""
SELECT m.FamilyName, m.GivenName, b.Title FROM Loan AS l
INNER JOIN Member AS m ON l.MemberNumber = m.MemberNumber
INNER JOIN Book AS b ON l.BookID = b.BookID
WHERE l.Returned = "FALSE"
    """)

    rows = cur.fetchall()
    
    return render_template("index.html", data = rows)

if __name__ == "__main__":
    app.run()
