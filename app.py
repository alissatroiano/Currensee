from flask import Flask, render_template
import mindsdb_sdk 
from config import Config
from settings import MINDSDB_EMAIL, MINDSDB_PASSWORD
import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

app = Flask(__name__)

app.config.from_object(Config)

server = mindsdb_sdk.connect('https://cloud.mindsdb.com',
            email=MINDSDB_EMAIL, password=MINDSDB_PASSWORD)

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
    project = server.get_project('mindsdb')
    query = project.query('SELECT T.date as date, T.price as Prediction, price_explain FROM mindsdb.bitcoin_model as T JOIN files.bitcoin_data as P WHERE P.Date > LATEST LIMIT 7')
    # create a dataframe for data from query
    btc_df = pd.DataFrame.to_html(query.fetch(), index=False)
    # create a plot
    plt.style.use('seaborn')
    plt.figure(figsize=(10, 5))
    plt.plot(btc_df['date'], btc_df['Prediction'], color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)
    plt.xticks(rotation=45)
    plt.show()
    plt.savefig('static/images/bitcoin.png')

    return render_template('coins/bitcoin.html', query=query, 
                           btc_df=btc_df)

@app.route('/ethereum', methods=['GET', 'POST'])
def ethereum():
    """
    Method to return ethereum prediction data when
    a user clicks the ethereum card on coins.html
    """
    project = server.get_project('mindsdb')
    query = project.query('SELECT T.Date as Date, T.price AS Price, Price_Explain FROM mindsdb.ethereum as T JOIN files.ethereum_data as P WHERE P.Date > LATEST LIMIT 7;')
    # create a dataframe for data from query
    eth_df = DataFrame.to_html(query.fetch(), index=False)

    return render_template('coins/ethereum.html', query=query, eth_df=eth_df)


@app.route('/dogecoin', methods=['GET', 'POST'])
def dogecoin():
    """
    Method to return dogecoin prediction data when
    a user clicks the dogecoin card on coins.html
    """
    project = server.get_project('mindsdb')
    query = project.query('SELECT T.date as Date, T.Price as Prediction, Price_Explain FROM mindsdb.dogecoin as T JOIN files.dogecoin as P WHERE P.Date > LATEST LIMIT 7;')
    # create a dataframe for data from query
    doge_df = DataFrame.to_html(query.fetch(), index=False)

    return render_template('coins/dogecoin.html', query=query, doge_df=doge_df)


@app.route('/dogecoin', methods=['GET', 'POST'])
def litecoin():
    """
    Method to return dogecoin prediction data when
    a user clicks the dogecoin card on coins.html
    """
    project = server.get_project('mindsdb')
    query = project.query('SELECT T.date as Date, T.Price as Prediction, Price_Explain FROM mindsdb.dogecoin as T JOIN files.dogecoin as P WHERE P.Date > LATEST LIMIT 7;')
    # create a dataframe for data from query
    doge_df = DataFrame.to_html(query.fetch(), index=False)

    return render_template('coins/dogecoin.html', query=query, doge_df=doge_df)


if __name__ == '__main__':
    app.run(debug=True)
