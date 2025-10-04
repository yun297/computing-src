from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/handle_request", methods = ["POST"])
def handle_request():
    text_input = request.form.get("text_input")
    date_input = request.form.get("date_input")
    select_input = request.form.get("select_input")
    radio_input = request.form.get("radio_input")
    checkbox_inputs = request.form.getlist("checkbox_input") # using get() will only give you one option

    inputs = [text_input, date_input, select_input, radio_input, checkbox_inputs]
    
    return render_template("handle_request.html", data = inputs)

if __name__ == "__main__":
    app.run()
