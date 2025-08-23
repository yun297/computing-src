from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("TASK4_4.html", result = None)
    elif request.method == "POST":
        name = request.form.get("name")

        conn = sqlite3.connect("LIBRARY.db")
        cur = conn.cursor()

        cur.execute("""
SELECT l.date, l.reason FROM Latecoming AS l
RIGHT JOIN Student AS s
ON l.stu_id = s.stu_id
WHERE s.name = ?
        """, (name,))

        fetched = cur.fetchall()
        result = []

        for line in fetched:
            result.append(line)

        conn.close()

        return render_template("TASK4_4.html", result = result)
        

if __name__ == "__main__":
    app.run()
