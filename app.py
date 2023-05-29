import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from datetime import date
from flask import Flask, render_template
import mindsdb_sdk 
from config import Config
from settings import MINDSDB_EMAIL, MINDSDB_PASSWORD
import pandas as pd
from pandas import DataFrame
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import base64
from io import BytesIO
from matplotlib.figure import Figure

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
    # save query data to a csv file
    query.fetch().to_csv('static/data/bitcoin.csv', index=False)
    # create a dataframe for data from query
    df = pd.read_csv('static/data/bitcoin.csv')
    btc_df = DataFrame.to_html(df, index=False)

    return render_template('coins/bitcoin.html', title='Bitcoin', btc_df=btc_df, query=query)

@app.route('/plot.png')
def plot_png():
        """
        Method to plot data from bitcoin.csv file
        """
        x = []
        y = []

        with open ('static/data/btc.csv','r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                x.append(row[0])
                y.append(row[1])

        fig = create_figure()
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    """
    Method to create a figure from bitcoin.csv file
    """
    df = pd.read_csv('static/data/btc.csv')
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(df['date'], df['Prediction'])
    return fig


@app.route('/ethereum', methods=['GET', 'POST'])
def ethereum():
    """
    Method to return ethereum prediction data when
    a user clicks the ethereum card on coins.html
    """
    project = server.get_project('mindsdb')
    query = project.query('SELECT T.Date as Date, T.price AS Price, Price_Explain FROM mindsdb.ethereum as T JOIN files.ethereum_data as P WHERE P.Date > LATEST LIMIT 7;')
    # save data to a csv file
    query.fetch().to_csv('static/data/eth.csv', index=False)
    eth_df = pd.read_csv('static/data/eth.csv')
    eth_df = DataFrame.to_html(eth_df, index=False)
    
    if DataFrame.empty:
        return render_template('coins/ethereum.html', query=query, eth_df=eth_df)
    else:
        return render_template('coins/ethereum.html', query=query, eth_df=eth_df)
    
# @app.route('/plot2.png')
# def plot2_png():
#     x = []
#     y = []
#     with open ('static/data/eth.csv','r') as csvfile:
#         lines = csv.reader(csvfile, delimiter=',')
#         for row in lines:
#             x.append(row[0])
#             y.append(row[1])

#     fig = create_figure()
#     output = io.BytesIO()
#     FigureCanvas(fig).print_png(output)
#     return Response(output.getvalue(), mimetype='image/png')

# def create_figure():
#     df = pd.read_csv('static/data/eth.csv')
#     fig = Figure()
#     axis = fig.add_subplot(1, 1, 1)
#     axis.plot(df['date'], df['Prediction'])
#     return fig


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
