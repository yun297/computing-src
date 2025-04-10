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
            """, (selected_region, ) # tuple
        )

        rows = cursor.fetchall()

        for row in rows:
            fetched_rows.append(row)

        conn.close()
    
        return render_template("index.html", selected_region = selected_region, data = fetched_rows)

    elif request.method == "GET":
        return render_template("index.html", selected_region = selected_region, data = fetched_rows)

@app.route("/add_employee", methods=["GET", "POST"])
def add_employee():
    if request.method == "GET":
        conn = sqlite3.connect("Northwind_small.sqlite")
        cursor = conn.cursor()
        
        cursor.execute("SELECT Id, TerritoryDescription FROM Territory") # get territory
        
        territories = cursor.fetchall()
        conn.close()
        
        return render_template("add_employee.html", territories=territories)

    elif request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        birthday = request.form.get("birth_date")
        territory_id = request.form.get("territory")

        conn = sqlite3.connect("Northwind_small.sqlite")
        cursor = conn.cursor()

        # Insert into Employee table
        cursor.execute(
            "INSERT INTO Employee (FirstName, LastName, BirthDate) VALUES (?, ?, ?)",
            (first_name, last_name, birthday)
        )
        employee_id = cursor.lastrowid  # get the new employee ID

        # Insert into EmployeeTerritory table
        cursor.execute(
            "INSERT INTO EmployeeTerritory (EmployeeId, TerritoryId) VALUES (?, ?)",
            (employee_id, territory_id)
        )

        conn.commit()
        conn.close()

        return render_template("acknowledge.html")

if __name__ == "__main__":
    app.run()
