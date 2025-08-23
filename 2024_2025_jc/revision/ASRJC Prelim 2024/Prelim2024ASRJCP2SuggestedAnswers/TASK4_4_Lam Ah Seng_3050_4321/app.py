from flask import Flask, render_template, request, url_for, send_from_directory
import os
import random
import csv
from datetime import datetime
from werkzeug.utils import secure_filename


app = Flask(__name__)

def substitution(main_text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""

    # create a dictionary for mapping of chars
    mapping = dict()
    for i in range(26):
        mapping[alphabet[i]] = key[i]

    # encrypt text
    for char in main_text:
        if not char.isalpha():  # non-alphabetical remains unchanged
            encrypted += char
        else:
            if char.islower():
                encrypted += mapping[char]
            else:
                encrypted += mapping[char.lower()].upper()

    return encrypted


def generate_key():
    """Generates a random 26-letter key"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = ""
    used_letters = []

    while len(key) < 26:
        # generate random letter
        index = random.randint(0, 25)
        random_letter = alphabet[index]

        # add letter if not used before
        if random_letter not in used_letters:
            key += random_letter
            used_letters.append(random_letter)

    return key


@app.route("/", methods=["GET", "POST"])
def home():
    success_msg = None
    
    if request.method == "POST":
        file = request.files["image"]
        if file.filename == "":
            return "No file selected."
    
        # ensure safe filename
        original_filename = secure_filename(file.filename)
        
        # extract extension
        filename, file_ext = original_filename.rsplit(".", 1)
        
        # get or generate key
        key = request.form["key"]
        if key == "" or len(key) != 26:
            key = generate_key()
        
        # encrypt and save file
        encrypted = substitution(filename, key) + "." + file_ext
        path = os.path.join("uploads", encrypted)
        file.save(path)
        
        # store info in file
        # file closes after with block
        with open("uploads.txt", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([encrypted, str(datetime.now())])
            
        success_msg = f"Upload complete. Saved as '{encrypted}' with key '{key}'."
    
    # GET method
    entries = []
    # extract data from file
    try:
        # file closes after with block
        with open("uploads.txt", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                entries.append(row)
    except FileNotFoundError:
        pass
    
    return render_template("index.html", entries=entries, success_msg=success_msg)

@app.route("/uploads/<filename>")
def get_file(filename):
    return send_from_directory("uploads", filename)


if __name__ == "__main__":
    app.run(debug=True)
