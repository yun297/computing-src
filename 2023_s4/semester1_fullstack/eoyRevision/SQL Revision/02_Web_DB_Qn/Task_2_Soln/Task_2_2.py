import csv
import os
import sqlite3

curr_dir = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(curr_dir, "seating.db")

files = ["students.csv", "classgroups.csv", "scr.csv"]
tables = ["Student", "ClassGroup", "SCR"]


def read_data():
    for i in range(len(files)):
        # read csv file
        with open(os.path.join(curr_dir, "data_files", files[i])) as f:
            csv_reader = csv.reader(f)
            header = next(csv_reader)

            data = []
            for row in csv_reader:
                data.append(row)

        # write to db
        db = sqlite3.connect(db_file)
        for row in data:
            query = "INSERT INTO {} {} VALUES ({})".format(
                tables[i],
                tuple(header),
                ",".join(["?"]*len(row)))
            db.execute(query, tuple(row))

        db.commit()
        db.close()


read_data()
