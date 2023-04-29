import os
from flask import Flask, render_template, request
import mindsdb_sdk 
from config import Config
from settings import MINDSDB_EMAIL, MINDSDB_PASSWORD
from forms import CoinForm
import pandas as pd
from pandas import DataFrame
# import handlers from scripts/get_models.py here
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


import json

@app.route('/ethereum', methods=['GET', 'POST'])
def ethereum():
    """
    Method to return ethereum prediction data when a user clicks the ethereum card on coins.html
    """
    project = server.get_project('mindsdb')
    query = project.query('SELECT T.Date as Date, T.Close as Prediction, Close_explain FROM mindsdb.eth_1 as T JOIN files.Ethereum as P WHERE P.Date > LATEST LIMIT 7;')
    # create a dataframe for data from query
    result = query.fetch()
    eth_df = DataFrame(result, columns=result.columns)
    eth_df['Date'] = eth_df['Date'].dt.strftime('%Y-%m-%d')
    eth_df['Prediction'] = eth_df['Prediction'].apply(lambda x: f'${x:,.2f}')

    return render_template('ethereum.html', eth_df=json.dumps(eth_df.to_dict(orient='records')))


if __name__ == '__main__':
    app.run(debug=True)
