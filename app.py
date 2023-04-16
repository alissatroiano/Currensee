import os
from flask import Flask, render_template, request
import mindsdb_sdk 
from config import MINDSDB_EMAIL, MINDSDB_PASSWORD
from forms import BitcoinForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY_STR', 'your-secret-key')
server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email=MINDSDB_EMAIL, password=MINDSDB_PASSWORD)

@app.route('/')
def index():
    server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email=MINDSDB_EMAIL, password=MINDSDB_PASSWORD)
    # Use MindsDB server object here
    project = server.get_project('mindsdb')
    model = project.get_model('btcusd_predictor')
    return 'Connected to MindsDB server. The BTC model is: {}'.format(model.name)    
    # run `flask run` command in terminal, then visit 127.0.0.1:5000 to test this function

@app.route('/bitcoin', methods=['GET', 'POST'])
def bitcoin():
    form = BitcoinForm()
    if form.validate_on_submit():
        try:
            input_data = {'coin': form.coin.data}
            project = server.get_project('mindsdb')
            model = project.get_model('crypto4')
            prediction = model.predict(input_data)
            target = prediction[0]['close_price']
            lower_bound = prediction[0]['close_price_confidence']['lower_bound']
            upper_bound = prediction[0]['close_price_confidence']['upper_bound']
            return render_template('bitcoin.html', target=target, lower_bound=lower_bound, upper_bound=upper_bound, form=form)
        except Exception as e:
            print(str(e))
            return render_template('500.html'), 500
    return render_template('bitcoin.html', form=form)
# run `flask run``, then visit 127.0.0.1:5000/bitcoin/ to test this function

if __name__ == '__main__':
    app.run('0.0.0.0')
else:
    print("Sorry")
