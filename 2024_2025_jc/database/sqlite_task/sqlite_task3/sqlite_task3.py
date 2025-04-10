from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    selected_region = None
    fetched_rows = []

    if request.method == "POST":
        selected_region = request.form.get("region")

        conn = sqlite3.connect("Northwind_small.sqlite")
        cursor = conn.cursor()

        cursor.execute(
            """
                SELECT e.FirstName, e.LastName, e.BirthDate, t.TerritoryDescription, r.RegionDescription
                FROM [Employee] as e
                INNER JOIN [EmployeeTerritory] as et
                ON e.Id = et.EmployeeId
                INNER JOIN [Territory] as t
                ON et.TerritoryId = t.Id
                INNER JOIN Region as r
                ON t.RegionId = r.Id
                WHERE r.RegionDescription = ?
            """, (selected_region, )
        )

        rows = cursor.fetchall()

        for row in rows:
            fetched_rows.append(row)
    
        return render_template("index.html", selected_region = selected_region, data = fetched_rows)

    elif request.method == "GET":
        return render_template("index.html", selected_region = selected_region, data = fetched_rows)

if __name__ == "__main__":
    app.run()
