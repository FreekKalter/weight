from flask import render_template, request, send_file
import sqlite3
from datetime import date
from . import app

db = '/data/weight.db'


@app.route("/")
def root():
    return send_file('static/index.html')


@app.route('/clear')
def clear():
    conn = sqlite3.connect(db)
    try:
        conn.execute('''DROP TABLE weigths''')
    except sqlite3.OperationalError:
        pass
    conn.execute('''CREATE TABLE weigths (date text, weight real)''')
    conn.commit()
    conn.close()
    return "created new table weigths"


@app.route("/insert", methods=['POST'])
def insert():
    converted = 0.0
    try:
        converted = float(request.form['weigth'])
    except ValueError:
        return 'Weigth not valid number'

    conn = sqlite3.connect(db)
    with conn:
        conn.execute('insert into weigths values (?, ?)', (date.today(), converted))
    conn.close()
    return send_file('static/graph.html')


@app.route("/graph")
def graph():
    return send_file('static/graph.html')


@app.route('/data.tsv')
def data():
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('select * from weigths order by date')
    all = cur.fetchall()
    s = 'date\tGewicht\n'
    for row in all:
        s = s + '{}\t{}\n'.format(row[0], row[1])
    return(s)


@app.route('/get')
def get():
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('select * from weigths')
    all = cur.fetchall()
    return(render_template('table.html', rows=all))
