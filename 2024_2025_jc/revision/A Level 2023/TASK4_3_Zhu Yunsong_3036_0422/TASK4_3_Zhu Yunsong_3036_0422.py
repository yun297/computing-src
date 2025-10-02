from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    file = open("decompressedimage.txt", 'r')

    colour_chart = {
        "000": "red",
        "001": "white",
        "010": "yellow",
        "011": "blue",
        "100": "black",
        "110": "green"
    }

    colours = []

    for line in file:
        colours.append(colour_chart[line.strip()])

    colours_grouped = []

    for i in range(0, len(colours), 9):
        colours_grouped.append(colours[i:i+9])
    
    return render_template("index.html", data = colours_grouped)

if __name__ == "__main__":
    app.run()
