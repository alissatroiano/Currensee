from flask import Flask, render_template
import mindsdb_sdk 
from config import Config
from settings import MINDSDB_EMAIL, MINDSDB_PASSWORD
from pandas import DataFrame

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
    Method to return bitcoin prediction data when a
    user clicks the bitcoin card on coins.html
    """

    return render_template('bitcoin.html')


@app.route('/ethereum', methods=['GET', 'POST'])
def ethereum():
    """
    Method to return ethereum prediction data when
    a user clicks the ethereum card on coins.html
    """
    project = server.get_project('mindsdb')
    query = project.query('SELECT T.Date as Date, T.Close '
                          'as Close FROM mindsdb.eth_1 as T JOIN files.Ethereum '
                          'as P WHERE P.Date > LATEST LIMIT 7;')
    # create a dataframe for data from query
    eth_df = DataFrame.to_html(query.fetch(), index=False)

    return render_template('ethereum.html', query=query, eth_df=eth_df)


if __name__ == '__main__':
    app.run(debug=True)
