from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    selected_option = request.args.get("option", "No option selected")
    return render_template("index.html", selected_option=selected_option)

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        selected_option = request.form.get("options")
        return redirect(url_for("index", option=selected_option))
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
