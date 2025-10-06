#1 mark - all Flask related statement are present (import statements, creation of flask object, starting the server)
#Importing all the required libraries
import flask
from flask import render_template, request
import sqlite3
import csv

app = flask.Flask(__name__) #create a Flask object
napfa_results = []

def load_results():
    with open("napfa_results.csv", "r", newline="") as infile:
        records = csv.reader(infile, delimiter = ",")
        for record in records:
            napfa_results.append((record[0], record[1], int(record[2]), int(record[3]), int(record[4]), int(record[5]), float(record[6]), float(record[7])))

def quick_sort(column, order_input, alist):
    if len(alist) <= 1: #1 mark - base case
        return alist
    else:
        pivot = alist[0] #1 mark - choosing a pivot
        left = []
        right = []

        for i in range(1, len(alist)):
            if order_input == "ascending": #2 marks - algorithm adjusted according to selected ascending/descending and station
                if alist[i][column] < pivot[column]:
                    left.append(alist[i])
                else:
                    right.append(alist[i])
            else:
                if alist[i][column] > pivot[column]:
                    left.append(alist[i])
                else:
                    right.append(alist[i])

        left = quick_sort(column, order_input, left) #1 mark - sorting done recursively
        right = quick_sort(column, order_input, right)

        print("combining", left + [pivot] + right)
        return left + [pivot] + right #1 mark - correct merging of data


@app.route('/', methods=['GET','POST'])  #1 mark- correct implementation of index/home method
def home():

    if request.method == "GET": #check if request is GET method (web app accessed by typing url in browser)
        load_results() #1 mark - read and store data in csv file into local list
        return render_template('napfa.html',  html_records = napfa_results)  #1 mark - render correct html template with sending original records to html file 
        
    else: #request is POST method (web app accessed by submitting html form with POST method)
        

        station_input = request.form['station'] #1 mark - extracting what user selected in the html form input 'station'
        order_input = request.form['order'] #1 nark - extracting what user selected in the html form input 'order'

        print(f"station_input: {station_input}, order_input: {order_input}")
        '''
        Column number based on station
        2 - Sit Ups
        3 - Standing Broad Jump
        4 - Sit And Reach
        5 - Pull-ups/Inclined Pull-ups
        6 - Shuttle Run
        7 - 2.4km Run
        '''
        column = -1
        if station_input == "sit_up":
            column = 2
        elif station_input == "standing_broad_jump":
            column = 3
        elif station_input == "sit_and_reach":
            column = 4
        elif station_input == "pull_ups":
            column = 5
        elif station_input == "shuttle_run":
            column = 6
        elif station_input == "2.4km_run":
            column = 7

        sorted_list = quick_sort(column, order_input, napfa_results) #1 mark - chose either quick sort or merge sort (not in place)
        return render_template('napfa.html', html_records = sorted_list) #1 mark - render correct html template with sending sorted records to html file 
        


if __name__ == '__main__':
	app.run() #calling the Flask object’s run() method to start the server
