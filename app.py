import os
from flask import Flask, render_template, request, redirect, url_for
import mindsdb_sdk 
from config import Config
from settings import MINDSDB_EMAIL, MINDSDB_PASSWORD
from forms import CoinForm

app = Flask(__name__)
app.config.from_object(Config)

# Import secret key from environment variable
# secret_key = os.environ.get("SECRET_KEY", "")
print(Config.SECRET_KEY)
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY_STR', 'your-secret-key')
server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email=MINDSDB_EMAIL, password=MINDSDB_PASSWORD)

@app.route('/')
def index():
    server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email=MINDSDB_EMAIL, password=MINDSDB_PASSWORD)
    # Use MindsDB server object here
    project = server.get_project('mindsdb')
    model = project.get_model('btcusd_predictor')
    return render_template('index.html', model=model)
    # run `flask run` command in terminal, then visit 127.0.0.1:5000 to test this function

@app.route('/bitcoin', methods=['GET', 'POST'])
def bitcoin():
    form = CoinForm()
    if form.validate_on_submit():
        # Use MindsDB server object here
        project = server.get_project('mindsdb')
        model = project.get_model('btcusd_prediction_mod')
        print(model)
        query = project.query('SELECT close_price FROM mindsdb.btcusd_prediction_mod WHERE date="2019-01-05"');
        return 'Your prediction data for Bitcoin is: ' + str(query.fetch())
    return render_template('bitcoin.html', form=form, query=None)
# run `flask run``, then visit 127.0.0.1:5000/bitcoin/ to test this function

#     form = CoinForm()
#     if form.validate_on_submit():
#         # Use MindsDB server object here
#         project = server.get_project('mindsdb')
#         databases = server.list_databases()
#         model = project.get_model('ethusd_prediction_mod')
#         query = project.query('SELECT * FROM mindsdb.ethusd_prediction_mod WHERE date="2019-01-05"');
#         close_price_prediction = query.fetch()
#         # We need to strip the query.fetch() so the result is just the close_price. Right now this returns: 'Your prediction data for Bitcoin is: date ... close_price_max 0 2019-01-05 ... 3796.056272 [1 rows x 14 columns]'
#         return 'Your prediction data for Ethereum is: ' + str(query.fetch())
#     return render_template('ethereum.html', form=form, query=None)

if __name__ == '__main__':
    app.run('0.0.0.0')