import os
from flask import Flask, render_template
import mindsdb_sdk 
from config import Config
from settings import MINDSDB_EMAIL, MINDSDB_PASSWORD
from forms import CoinForm
from flask_bootstrap import Bootstrap5 as Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config.from_object(Config)

server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email=MINDSDB_EMAIL, password=MINDSDB_PASSWORD)


@app.route('/')
# @app.route('/index')
def index():
    server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email=MINDSDB_EMAIL, password=MINDSDB_PASSWORD)
    # Use MindsDB server object here
    project = server.get_project('mindsdb')
    model = project.get_model('btcusd_predictor')
    
    return render_template('index.html', title='Home', model=model)
    # run `flask run` command in terminal, then visit 127.0.0.1:5000 to test this function

@app.route('/coins', methods=['GET', 'POST'])
def coins():
    form = CoinForm()
        # Use MindsDB server object he`re
    project = server.get_project('mindsdb')
    model = project.get_model('btcusd_prediction_mod')
    print(model)
    query = project.query('SELECT close_price FROM mindsdb.btcusd_prediction_mod WHERE date="2019-01-05"')
    return render_template('coins.html', form=form, query=None)

@app.route('/bitcoin', methods=['GET', 'POST'])
def bitcoin():
    """
    Method to return bitcoin prediction data when a user clicks the bitcoin card on coins.html
    """
    project = server.get_project('mindsdb')
    model = project.get_model('btcusd_prediction_mod')
    print(model)
    query = project.query('SELECT close_price FROM mindsdb.btcusd_prediction_mod WHERE date="2019-01-05"');
    # result = model.query.with_entities('close_price'.column_name).fetch()

    return render_template('bitcoin.html', query=query)
# run `flask run``, then visit 127.0.0.1:5000/bitcoin/ to test this function

@app.route('/ethereum', methods=['GET', 'POST'])
def ethereum():
    """
    Method to return ethereum prediction data when a user clicks the ethereum card on coins.html
    """
    project = server.get_project('mindsdb')
    model = project.get_model('ethereum_predictions')
    query = project.query('SELECT * FROM ethereum_predictions as EP JOIN files.Ethereum as E WHERE E.Date > "current_timestamp" LIMIT 1;')
    return render_template('ethereum.html', query=query, model=model)


if __name__ == '__main__':
    app.run(debug=True)