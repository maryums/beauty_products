import sqlite3
import random
from flask import Flask, session, render_template, request, g

app = Flask(__name__)
app.secret_key = "234e_blahblahhah_"

@app.route("/")
def index():
    data = get_db()
    return render_template("index.html", all_data=data)

@app.route("/add_items", methods=["post"])
def add_items():
    return request.form["select_items"]


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('product_list.db')
        cursor = db.cursor()
        cursor.execute("select name from products")
        all_data = cursor.fetchall()
        all_data =  [str(val[0]) for val in all_data]
    return all_data

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()