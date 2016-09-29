from flask import Flask
from flask import render_template, request, redirect, url_for
import sqlite3
from datetime import date

app = Flask(__name__)


@app.route("/")
def root():
    return redirect(url_for('static', filename="index.html"))


@app.route('/clear')
def clear():
    conn = sqlite3.connect('weigth.db')
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

    conn = sqlite3.connect('weigth.db')
    with conn:
        conn.execute('insert into weigths values (?, ?)', (date.today(), converted))
    conn.close()
    return redirect(url_for('graph'))


@app.route("/graph")
def graph():
    return render_template('graph.html')


@app.route('/data.tsv')
def data():
    conn = sqlite3.connect('weigth.db')
    cur = conn.cursor()
    cur.execute('select * from weigths order by date')
    all = cur.fetchall()
    s = 'date\tGewicht\n'
    for row in all:
        s = s + '{}\t{}\n'.format(row[0], row[1])
    return(s)


@app.route('/get')
def get():
    conn = sqlite3.connect('weigth.db')
    cur = conn.cursor()
    cur.execute('select * from weigths')
    all = cur.fetchall()
    return(render_template('table.html', rows=all))

if __name__ == '__main__':
    app.run(debug=True)
