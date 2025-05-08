from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return render_template("TASK4_1_Zhu_Yunsong_24S6B.html")

@app.route("/health_records", methods = ["GET"])
def health_records():
    fetched_rows = []

    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    cur.execute("""
        SELECT s.Name, s.Gender, hr.Weight, hr.Height
        FROM [Student] AS s
        LEFT JOIN [StudentHealthRecord] AS hr
        ON s.StudentID = hr.StudentID
        ORDER BY s.Gender ASC, s.Name DESC
    """)

    rows = cur.fetchall()

    for row in rows:
        fetched_rows.append(row)

    conn.close()
    
    return render_template("TASK4_2_Zhu_Yunsong_24S6B.html", health_records = fetched_rows)

@app.route("/health_stats", methods = ["GET"])
def health_stats():
    fetched_rows = []

    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            s.Gender,
        COUNT(*) AS TotalStudents,
        AVG(hr.Weight) AS AverageWeight,
        AVG(hr.Height) AS AverageHeight
        FROM [Student] AS s
        LEFT JOIN [StudentHealthRecord] AS hr
            ON s.StudentID = hr.StudentID
        GROUP BY s.Gender;
    """)

    rows = cur.fetchall()

    for row in rows:
        fetched_rows.append(row)

    conn.close()
    
    return render_template("TASK4_3_Zhu_Yunsong_24S6B.html", health_stats = fetched_rows)

@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("TASK4_4_Zhu_Yunsong_24S6B.html")

    elif request.method == "POST":
        StudentID = int(request.form.get("StudentID"))
        Name = request.form.get("Name")
        Gender = request.form.get("Gender")
        Weight = float(request.form.get("Weight"))
        Height = float(request.form.get("Height"))

        conn = sqlite3.connect("students.db")
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO [Student] (StudentID, Name, Gender)
            VALUES (?, ?, ?);
        """, (StudentID, Name, Gender))
        conn.commit()

        cur.execute("""
            INSERT INTO [StudentHealthRecord] (StudentID, Weight, Height)
            VALUES (?, ?, ?);
        """, (StudentID, Weight, Height))
        conn.commit()
        
        conn.close()

        return render_template("TASK4_4_Zhu_Yunsong_24S6B.html")

if __name__ == "__main__":
    app.run()
