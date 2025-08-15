from flask import Flask, request, render_template, url_for
import sqlite3

app = Flask(__name__)

@app.route('/', methods = ["GET"])
def index():
    conn = sqlite3.connect("school.db")
    cur = conn.cursor()

    cur.execute("""
SELECT * FROM People
    """)

    fetched = cur.fetchall()
    data = []

    for line in fetched:
        name = line[1]
        screen = line[3]
        type = line[4]

        entry = [name, screen]

        if screen[-5:] == "Staff":
            entry.append("Staff")
        elif type == 0:
            entry.append("Student")
        else:
            entry.append("Person")

        data.append(entry)

    print(data)
    
    return render_template("TASK4_3_Zhu_Yunsong.html", data = data)

if __name__ == "__main__":
    app.run()



