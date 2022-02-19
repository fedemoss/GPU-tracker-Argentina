# -*- coding: utf-8 -*-
import pandas as pd
from flask import Flask, render_template
import datetime

e = datetime.datetime.now()

app = Flask(__name__, template_folder='C:/Users/mossney/Documents/Python Scripts/Flask intro/templates')


gpus = ['1660super', '580', '3070']
df2 = []
for gpu in gpus:
    df = pd.read_csv('gpu_{}.csv'.format(gpu))
    df = df.iloc[:10] #10 results
    df = df.drop(df.columns[[0]], axis=1) #drop 1rst
    df = df.to_html()
    df2.append(df)

@app.route("/")
def gpu1():
    #return render_template('index.html') #run html
    return 'Top GPUs for mining (Where to buy in Argentina)<h1>{} </h1> {} \ <h1> {} </h1> {} \ <h1> {} </h1> {} <h2>Current time {}</h2>'.format(gpus[0],df2[0], gpus[1], df2[1], gpus[2], df2[2], e)

ipv4 = '192.168.0.108'
if __name__ == '__main__':
    app.run(debug=True, host = ipv4)
