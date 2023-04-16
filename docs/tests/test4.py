from flask import Flask, jsonify
import asyncio
from mindsdb import mdb
from mindsdb_native import MySQLBackend
import pandas as pd

app = Flask(__name__)

_BINANCE_INTEGRATION = "my_binance"
_AGGREGATED_TRADE_DATA_TABLE = "aggregated_trade_data"

# Define the MindsDB backend
backend = MySQLBackend(
    host='<your_db_host>',
    user='<your_db_username>',
    password='<your_db_password>',
    database='<your_db_name>',
    port='<your_db_port>'
)

# Initialize the MindsDB instance
mdb.DBHandler.initialize(db_configs={
    'mysql': backend
})

@app.route('/get_latest_trade_data/<symbol>/<int:limit>', methods=['GET'])
def get_latest_trade_data(symbol, limit):
    binance_query = f"SELECT * FROM {_BINANCE_INTEGRATION}.{_AGGREGATED_TRADE_DATA_TABLE} WHERE symbol='{symbol.upper()}' LIMIT {limit}"
    trade_data_response = mdb.SQL.run_query(binance_query)
    if not trade_data_response.rows:
        return []
    return jsonify(trade_data_response.rows)

@app.route('/forecast_prices/<symbol>/<model_name>/<int:limit>', methods=['GET'])
def forecast_prices(symbol, model_name, limit):
    view_name = f"recent_{symbol}_view"
    # Create a temporary view of the latest trade data
    view_select = f"SELECT * FROM {_BINANCE_INTEGRATION}.{_AGGREGATED_TRADE_DATA_TABLE} WHERE symbol = '{symbol.upper()}'"
    mdb.Views.createView(view_name, "mindsdb", view_select)
    # Use the temporary view to make predictions
    predict_query = f"SELECT m.* FROM {view_name} AS t JOIN mindsdb.{model_name} AS m WHERE m.open_time > LATEST LIMIT {limit}"
    predictions_response = mdb.SQL.runQuery(predict_query)
    return jsonify(predictions_response["rows"])

if __name__ == '__main__':
    app.run(debug=True)
