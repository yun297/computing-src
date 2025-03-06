from flask import Flask, render_template, redirect, url_for, request # render_template is used to render HTML files
import csv

app = Flask(__name__) # create app

@app.route("/") # decorator to route traffic to the function below
def home():
  return render_template("index.html")

@app.route("/hello")
def hello():
  # hello() function receives the value of name and cg from the URL
  
  name = request.args.get("name", "nameless person") # get the value of the name parameter, if not found, use "nameless person"
  cg = request.args.get("cg", "classless person") # get the value of the cg parameter, if not found, use "classless person"
  
  return render_template("welcome.html", name = name, cg = cg) # name and cg is passed to the welcome.html file

@app.route("/address/<your_name>")
def address(your_name):
  return redirect(url_for("hello", name = your_name, cg = "24S6B"))
  # "hello" refers to the function name, it is sending the value of your_name and cg to the hello function
  # your_name is the parameter in the address function, so when u access the link /address/your_name, it will redirect to /hello?name=your_name&cg=24S6B

@app.route("/server")
def server():
  name_value = input("What is your name? ") # get the value of the name parameter from the user
  class_value = input("What is your class? ")
  return redirect(url_for("hello", name = name_value, cg = class_value)) # redirect to the hello function, use url_for to pass the value of name and cg while redirecting

@app.route("/uni")
def uni():
  uni_file = open('2024_2025_jc/web/flask_app_6_mar/uni.csv', 'r')
  uni_csv = csv.reader(uni_file)
  uni_list = list(uni_csv) # 2D list
  uni_file.close()
  
  return render_template("uni.html", uni_list = uni_list)

# running the app
if __name__ == "__main__":
  app.run()