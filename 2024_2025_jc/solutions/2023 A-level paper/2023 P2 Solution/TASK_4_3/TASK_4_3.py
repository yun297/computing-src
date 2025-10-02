# Task 4.3

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # read file
    f = open('decompressedimage.txt','r') #open file for reading
    colours = f.read().strip().split('\n') #read content, remove whitespace, split by line
    f.close() #close file
    
    colourcodes = {'000':'red','001':'white','010':'yellow','011':'blue','100':'black','110':'green'}

    # convert to 2D list
    grid = []
    for row in range(9):
        grid.append(['']*9) # create empty row
        for col in range(9):
            code = colours[row * 9 + col]
            text = colourcodes[code] # convert code to text
            grid[row][col] = text # updates code grid
    return render_template("index.html", data=grid)


if __name__ == "__main__":
    app.run()
