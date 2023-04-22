import os
from flask import Flask, render_template
import mindsdb_sdk 
from config import Config
from settings import MINDSDB_EMAIL, MINDSDB_PASSWORD
from forms import CoinForm
from flask_bootstrap import Bootstrap
from flask import request

app = Flask(__name__)

app.config.from_object(Config)
bootstrap = Bootstrap(app)

server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email=MINDSDB_EMAIL, password=MINDSDB_PASSWORD)

@app.route('/')
@app.route('/index')
def index():
    server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email=MINDSDB_EMAIL, password=MINDSDB_PASSWORD)
    # Use MindsDB server object here
    project = server.get_project('mindsdb')
    model = project.get_model('btcusd_predictor')
    return render_template('index.html', model=model)
    # run `flask run` command in terminal, then visit 127.0.0.1:5000 to test this function

@app.route('/coins', methods=['GET', 'POST'])
def coins():
    form = CoinForm()
    if form.validate_on_submit():
        # Use MindsDB server object he`re
        project = server.get_project('mindsdb')
        model = project.get_model('btcusd_prediction_mod')
        print(model)
        """
        user input from coins.html is passed to the mindsdb query function
        """
        query = project.query(user.input.data);
        return 'Your prediction data for Bitcoin is: ' + str(query.fetch())
    return render_template('coins.html', form=form, query=None)


@app.route('/bitcoin', methods=['GET', 'POST'])
def bitcoin():
    project = server.get_project('mindsdb')
    model = project.get_model('btcusd_prediction_mod')
    print(model)
    
    target = request.form.get('target')  # Get the selected target variable from the form
    
    # Construct the MindsDB query using the selected target variable
    query_str = f'SELECT {target} FROM mindsdb.btcusd_prediction_mod WHERE date="2019-01-05"'
    query = project.query(query_str)

    return render_template('bitcoin.html', query=query, target=target)


if __name__ == '__main__':
    app.run(debug=True)