from flask import Flask, render_template, redirect, url_for, request
import csv

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/form")
def form():
  top_charts_file = open('spotify_top_charts.csv', 'r', encoding = "utf-8", errors = "ignore")
  top_charts_csv = csv.reader(top_charts_file)
  top_charts_list = list(top_charts_csv)
  top_charts_file.close()

  genres = []
  for album in top_charts_list:
      for genre in album[19].split(","):
        if genre.strip() not in genres:
          genres.append(genre)  

  genres.sort()
  
  return render_template("form.html", genres = genres)

@app.route("/top_charts", methods=['GET', 'POST'])
def top_charts():
  try:
    query = request.form["energy"]
  except:
    print("typecast error")
    query = -1
    
  top_charts_file = open('spotify_top_charts.csv', 'r', encoding = "utf-8", errors = "ignore")
  top_charts_csv = csv.reader(top_charts_file)
  top_charts_list = list(top_charts_csv)
  top_charts_file.close()
  
  filtered_list = [top_charts_list[0]]

  if request.method == "GET":
    filtered_list = top_charts_list
    
  elif request.method == "POST":
    if query:
      energy = float(query)
      for album in top_charts_list[1:]:
        if float(album[21]) > energy:
          filtered_list.append(album)
    else:
      filtered_list = top_charts_list

  return render_template("top_charts.html", top_charts_list = filtered_list)

if __name__ == "__main__":
  app.run()
