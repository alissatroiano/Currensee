from flask import Flask
import mindsdb_sdk 
from config import MINDSDB_CREDENTIALS

app = Flask(__name__)


@app.route('/')
def index():
    server = mindsdb_sdk.connect('https://cloud.mindsdb.com', **MINDSDB_CREDENTIALS)
    # Use MindsDB server object here
    project = server.get_project('mindsdb')
    model = project.get_model('btcusd_predictor')
    return 'Connected to MindsDB server. Your BTC model is: {}'.format(model.name)


if __name__ == '__main__':
    app.run(debug=False)

# _BINANCE_INTEGRATION = "my_binance"
# _AGGREGATED_TRADE_DATA_TABLE = "aggregated_trade_data"
# mdb = mindsdb_sdk
# # print(dir(mdb))
# btc_model = mindsdb_sdk.model
# # mdb.learn(from_data='main.csv', to_predict='close_price')
# print(btc_model)

# @app.route('/')
# @app.route('/get_coins')
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


# if __name__ == '__name__':
#     app.run('0.0.0.0')
# else:
#     print("Sorry")
