import os
import ssl
from flask import Flask, render_template, request
import mindsdb_sdk 
from config import Config
from settings import MINDSDB_EMAIL, MINDSDB_PASSWORD
from forms import CoinForm
import pandas as pd


app = Flask(__name__)

app.config.from_object(Config)

server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email=MINDSDB_EMAIL, password=MINDSDB_PASSWORD)
import mindsdb_sdk


@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/coins')
def coins():
    project = server.get_project('mindsdb')
    # database = server.get_database('files')
    btc_model = project.get_model('btcusd_prediction_mod')
    bit_query = project.query('SELECT close_price FROM btcusd_prediction_mod WHERE Date = "2023-04-30";')
    # database = server.get_database('files')
    eth_model = project.get_model('ethereum_predictions')
    # view = project.get_view('eth_view')
    # df = view.fetch()
    # btc_table = df.head(20).to_html(index=False)


    return render_template('coins.html', title='Coins', bit_query=bit_query)


@app.route('/bitcoin', methods=['GET', 'POST'])
def bitcoin():
    """
    Method to return bitcoin prediction data when a user clicks the bitcoin card on coins.html
    """
    project = server.get_project('mindsdb')
    # database = server.get_database('files')
    model = project.get_model('btcusd_prediction_mod')
    view = project.get_view('eth_view')
    df = view.fetch()
    btc_table = df.head(20).to_html(index=False)

    return render_template('bitcoin.html', model=model, view=view, df=df, btc_table=btc_table)


@app.route('/ethereum', methods=['GET', 'POST'])
def ethereum():
    """
    Method to return ethereum prediction data when a user clicks the ethereum card on coins.html
    """
    # project = server.get_project('mindsdb')
    # databases = server.get_database('files')
    # model = project.get_model('ethereum_predictions')
    # query = project.query('SELECT EP.Close, Date FROM ethereum_predictions as EP JOIN files.Ethereum as E WHERE E.Date > "2023-04-26" LIMIT 1;')
    # print(query.fetch())
    return render_template('ethereum.html')


if __name__ == '__main__':
    app.run(ssl_context='adhoc')
