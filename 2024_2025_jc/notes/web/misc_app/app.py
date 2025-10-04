from flask import Flask, render_template, request, url_for
from random import randint

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        # making a simple image with a table
        colours = ["red", "orange", "yellow", "green", "blue", "purple", "black"]

        image_arr = []

        for i in range(50):
            row = []

            for j in range(50):
                row.append(colours[randint(0, len(colours) - 1)])

            image_arr.append(row)
        
        return render_template("index.html", image_arr = image_arr)

    elif request.method == "POST":
        username = request.form.get("username")

        return f"""
<a href="{url_for("result", data = username)}">Go to <b>{username}</b>'s profile</a>
""" 

@app.route("/result/<data>", methods = ["GET"])
def result(data):
    return render_template("result.html", data = data)

if __name__ == "__main__":
    app.run()
