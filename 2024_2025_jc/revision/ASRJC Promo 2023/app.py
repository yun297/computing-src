from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":
        m = request.form.get("m").lower().strip()
        k = request.form.get("k")

        k_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
        k_string = k_strings[int(k) - 1]

        ret_str = ""

        for letter in k_string:
            if letter in m:
                ret_str += letter

        if ret_str == "":
            ret_str = "Nil"

        return render_template("index.html", ret_str = ret_str)


if __name__ == "__main__":
    app.run()
