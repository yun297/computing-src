from flask import Flask, render_template, request, url_for
import sqlite3

app = Flask(__name__)

@app.route('/', methods = ["GET"])
def index():
    return render_template("index.html")

@app.route('/form', methods = ["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")

    if request.method == "POST":
        customer_name = request.form.get("customer-name")
        product_name = request.form.get("product-name")
        
        fetched_rows = []

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute("""
            SELECT c.name, p.name, o.quantity FROM [orders] AS o
            INNER JOIN [customers] AS c ON c.id = o.customer_id
            INNER JOIN [products] AS p on p.id = o.product_id
            WHERE c.name = ? AND p.name = ?
        """, (customer_name, product_name))

        rows = cur.fetchall()

        for row in rows:
            fetched_rows.append(row)

        conn.close()

        return render_template("form.html", data = fetched_rows)

@app.route('/add', methods = ["GET"])
def add():
    return render_template("add.html")

@app.route('/confirm', methods = ["POST"])
def confirm():
    customer_id = request.form.get("customer-name")
    product_id = request.form.get("product-name")
    quantity = request.form.get("quantity")

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO Orders ("customer_id", "product_id", "quantity")
        VALUES (?, ?, ?)
    """, (customer_id, product_id, quantity))

    conn.commit()

    conn.close()

    return render_template("confirm.html")


if __name__ == "__main__":
    app.run()
