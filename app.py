import os
from flask import Flask, render_template, request
import mindsdb_sdk 
from config import Config
from settings import MINDSDB_EMAIL, MINDSDB_PASSWORD
from forms import CoinForm
import pandas as pd
# import numpy as np # linear algebra


app = Flask(__name__)

app.config.from_object(Config)

server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email=MINDSDB_EMAIL, password=MINDSDB_PASSWORD)
import mindsdb_sdk


@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/coins')
def coins():
    return render_template('coins.html', title='Coins')


@app.route('/bitcoin', methods=['GET', 'POST'])
def bitcoin():
    """
    Method to return bitcoin prediction data when a user clicks the bitcoin card on coins.html
    """

    return render_template('bitcoin.html')


@app.route('/ethereum', methods=['GET', 'POST'])
def ethereum():
    """
    Method to return ethereum prediction data when a user clicks the ethereum card on coins.html
    """
    # project = server.get_project('mindsdb')
    # databases = server.get_database('files')
    # model = project.get_model('ethereum_predictions')
    df = pd.read_csv('bitcoin.csv')
    # print(df)
    header = df.head()
    print(header)

    # query = project.query('SELECT EP.Close, Date FROM ethereum_predictions as EP JOIN files.Ethereum as E WHERE E.Date > "2023-04-26" LIMIT 1;')
    # print(query.fetch())
    return render_template('ethereum.html')


if __name__ == '__main__':
    app.run()
