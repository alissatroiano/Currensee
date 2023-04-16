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

# @app.route('/')
# @app.route('/get_bitcoin')
# def get_bitcoin():
#       """
#       Returns bitcoin prediction data from MindsDB
#       MindsDB Prediction Model Name: btcusd_predictor
#       ticker: BTCUSD
#       target: close_price
#       """
#       project = server.get_project('mindsdb')
#       models = project.list_models()
 #       print(models)
#       # model = models[0]
#       model = project.get_model('btcusd_predictor')
#       if request.method == 'GET':
#             return jsonify(model.predict())
#       else:
#         return jsonify({'error': 'Invalid request method'})

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



# def get_coins():
#             server = mindsdb_sdk.connect()
#             server = mindsdb_sdk.connect('http://127.0.0.1:47334')

#             server = mindsdb_sdk.connect(email='alissatroianonyc@gmail.com', password='B@nana$5900')
#             server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email='alissatroianonyc@gmail.com', password='B@nana$5900')

#         databases = server.list_databases()
#         print(databases)
        
#         return render_template('index.html', databases=databases)


# @app.route('/predict', methods=['POST'])
# def predict():
#     """
#     Checks the status of a model (generating, training, error, or complete).
#     Example usage: python ./scripts/getStatus.py --name btcusdt_model
#     """
#     # Initialize argument parser
#     parser = argparse.ArgumentParser(description='Check the status of a MindsDB model')
#     parser.add_argument('-c', '--config-path', default='./config/mindsdb-config.json',
#                     help='path to config JSON file used for connecting to MindsDB.')
#     parser.add_argument('-n', '--name', required=True,
#                     help='name of the model to check the status for')
#     args = parser.parse_args()


#     # Load MindsDB configuration from JSON file
#     with open(args.config_path) as f:
#         config = json.load(f)


#     # Connect to MindsDB
#     async def main():
#         mdb = mindsdb.Predictors(**config)
#         await mdb.connect()
#         return await mdb.get_model(model_name=args.name)
    
#     # Check model status
#     async def check_model_status():
#         try:
#             model = await main()
#             if model:
#                 print(f"Status of model {model.name} is {model.status}")
#             else:
#                 print(f"Model with name {args.name} does not exist")
#         except Exception as e:
#             print(f"Fetching model failed with error: {e}")

#     # Return on the front-end
#     return render_template('coins.html', prediction_text='Model status is {}'.format(check_model_status()))


if __name__ == '__main__':
    app.run('0.0.0.0')
else:
    print("Sorry")
