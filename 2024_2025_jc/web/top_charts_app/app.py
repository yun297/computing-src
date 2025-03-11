from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/top_charts")
def top_charts():
  top_charts_file = open('spotify_top_charts.csv', 'r', encoding = "utf-8", errors = "ignore")
  top_charts_csv = csv.reader(top_charts_file)
  top_charts_list = list(top_charts_csv)
  top_charts_file.close()

  return render_template("top_charts.html", top_charts_list = top_charts_list)

if __name__ == "__main__":
  app.run()
