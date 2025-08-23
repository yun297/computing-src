from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])

def main():
    if request.method == "GET":
        return render_template("TASK4_4_Zhu_Yunsong_24S6B.html")

    elif request.method == "POST":
        date = request.form.get("date")
        Date = ''.join(date.split('-'))

        conn = sqlite3.connect("STORE.db")
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT d.DonutName, SUM(s.Quantity) AS TotalQuantity
            FROM [Sale] AS s
            INNER JOIN [Donut] AS d ON s.DonutID = d.DonutID
            WHERE s.Date = ?
            GROUP BY d.DonutName
            ORDER BY TotalQuantity DESC
        """, (Date, ))

        rows = cursor.fetchall()
        
        return render_template("TASK4_4_Zhu_Yunsong_24S6B.html", donuts = rows)

if __name__ == "__main__":
    app.run()
