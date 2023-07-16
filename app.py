from flask import Flask, render_template, request,redirect,url_for,jsonify
import json
from datetime import datetime
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

import sqlite3
@app.route("/save", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        companyname= request.form.get("companyname")
        examtype = request.form.get("examtype")
        questionname = request.form.get("questionname")
        questionlink = request.form.get("questionlink")
        year = request.form.get("year")

        with sqlite3.connect('intern.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO company(companyname, examtype, questionname, questionlink, year) VALUES (?, ?, ?, ?, ?)",
                        (companyname, examtype, questionname, questionlink, year))
            conn.commit()
        return render_template("response.html", companyname=companyname, examtype=examtype, questionname=questionname, questionlink=questionlink, year=year)

    return render_template("index.html")
@app.route('/alldatas')
def render_alldatas():
    with sqlite3.connect('intern.db') as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM company")
        data = c.fetchall()
        # Retrieve column names
        column_names = [desc[0] for desc in c.description]
    json_data = [dict(zip(column_names, row)) for row in data]
    return jsonify(json_data)
@app.route("/displayall")
def displayall():
    with sqlite3.connect('intern.db') as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM company")
        data = c.fetchall()
    return render_template("alldatas.html", data=data)
if __name__ == '__main__':
    app.run(debug=True)
