from flask import Flask, render_template, url_for, request
import sqlite3


app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return render_template("TASK4_4_Zhu Yunsong_24S6B_0.html", data = None)

@app.route("/option1", methods = ["GET", "POST"])
def option1():
    if request.method == "GET":
        return render_template("TASK4_4_Zhu Yunsong_24S6B_1.html")
    else:
        conn = sqlite3.connect("CLINIC.db")
        cur = conn.cursor()

        patient_name = request.form.get("patient_name")
        appointment_date = request.form.get("appointment_date")

        cur.execute("""
SELECT a.AppointmentID, a.PatientID, a.StaffID, a.AppointmentDate, a.Diagnosis, p.Name, s.Name
FROM Appointment AS a
INNER JOIN Patient AS p ON p.PatientID = a.PatientID
INNER JOIN Staff AS s ON s.StaffID = a.StaffID
WHERE a.AppointmentDate = ? AND p.Name = ?
        """, (appointment_date, patient_name))

        data = cur.fetchall()
        conn.close()

        return render_template("TASK4_4_Zhu Yunsong_24S6B_1.html", data = data)

@app.route("/option2", methods = ["GET", "POST"])
def option2():
    if request.method == "GET":
        conn = sqlite3.connect("CLINIC.db")
        cur = conn.cursor()

        cur.execute("""
SELECT s.Name, s.Role, COUNT(*)
FROM Appointment AS a
INNER JOIN Staff AS s
ON a.StaffID = s.StaffID
GROUP BY s.StaffID
        """)

        data = cur.fetchall()
        print(data)

        return render_template("TASK4_4_Zhu Yunsong_24S6B_2.html", data = data)
    
    
if __name__ == "__main__":
    app.run()
