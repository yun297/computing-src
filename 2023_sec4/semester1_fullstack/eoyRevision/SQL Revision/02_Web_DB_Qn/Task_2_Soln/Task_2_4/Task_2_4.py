from flask import Flask, render_template, request
import sqlite3
import os
app = Flask(__name__)

curr_dir = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(curr_dir, "seating.db")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gen_seating/', methods=["GET", "POST"])
def gen_seating():
    if request.method == "GET":
        return render_template("input.html")
    else:
        cg_name = request.form["cg_name"]
        no_of_cols = int(request.form["no_of_cols"])

        query = """
        SELECT Student.Class, Student.IndexNo, Student.Name
        FROM Student, ClassGroup, SCR
        WHERE Student.MatricNo = SCR.MatricNo
        AND ClassGroup.ClassGroupID = SCR.ClassGroupID
        AND ClassGroup.ClassGroupName = ?
        ORDER BY Student.Class, Student.IndexNo
        """

        db = sqlite3.connect(db_file)
        cursor = db.execute(query, (cg_name,))
        data = cursor.fetchall()
        db.close()

        print(data)

        no_of_rows = len(data) // no_of_cols + 1

        processed_data = []

        for i in range(no_of_rows):
            row = []
            for j in range(no_of_cols):
                index = i * no_of_cols + j
                print(i, j, index)
                if index < len(data):
                    student_data = data[index]
                    row.append(
                        ("{}({})".format(student_data[0], student_data[1]), student_data[2]))

            processed_data.append(row)

        print(processed_data)

        return render_template(
            "result.html",
            processed_data=processed_data,
            cg_name=cg_name)


if __name__ == '__main__':
    app.run(debug=True)
