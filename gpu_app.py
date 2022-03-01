from flask import Flask, render_template
from database_connection import create_connection
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/gpus')
def gpus():
    return render_template('gpus.html')

@app.route('/rtx3070')
def rtx3070():
    cur = create_connection('tracker.db')
    rtx3070_list = [dict(row) for row in cur.execute("SELECT * FROM rtx3070").fetchall()]
    return render_template('3070.html', items=rtx3070_list)

@app.route('/rx580')
def rx580():
    cur = create_connection('tracker.db')
    rx580_list = [dict(row) for row in cur.execute("SELECT * FROM rx580").fetchall()]
    return render_template('580.html', items=rx580_list)

@app.route('/1660super')
def super1660():
    cur = create_connection('tracker.db')
    super1660_list = [dict(row) for row in cur.execute("SELECT * FROM gtx1660super").fetchall()]
    return render_template('1660.html', items=super1660_list)

@app.route('/rtx3080')
def rtx3080():
    cur = create_connection('tracker.db')
    rtx3080_list = [dict(row) for row in cur.execute("SELECT * FROM rtx3080").fetchall()]
    return render_template('3080.html', items=rtx3080_list)

@app.route('/rtx3090')
def rtx3090():
    cur = create_connection('tracker.db')
    rtx3090_list = [dict(row) for row in cur.execute("SELECT * FROM rtx3090").fetchall()]
    return render_template('3090.html', items=rtx3090_list)

@app.route('/rtx3060ti')
def rtx3060ti():
    cur = create_connection('tracker.db')
    rtx3060ti_list = [dict(row) for row in cur.execute("SELECT * FROM rtx3060ti").fetchall()]
    return render_template('3060ti.html', items=rtx3060ti_list)

@app.route('/6700xt')
def rx6700xt():
    cur = create_connection('tracker.db')
    rx6700xt_list = [dict(row) for row in cur.execute("SELECT * FROM rx6700xt").fetchall()]
    return render_template('6700xt.html', items=rx6700xt_list)

