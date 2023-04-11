import mindsdb_sdk
import matplotlib.pyplot as plt
csv_file_path = 'functions/main.csv'
window = 50  # Replace with the desired window size for prediction
horizon = 10  # Replace with the desired horizon size for forecasting

# Initialize MindsDB
server = mindsdb_sdk.connect()
server = mindsdb_sdk.connect('http://127.0.0.1:47334')

server = mindsdb_sdk.connect(email='alissatroianonyc@gmail.com', password='B@nana$5900')
server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email='alissatroianonyc@gmail.com', password='B@nana$5900')

# mdb = mindsdb_sdk.model('btcusd_predictor')
database = server.get_database('files')
print(database)

table = database.list_tables()
print(table)

model_name = "btcusd_predictor"

# Define the query
query = """
SELECT *
FROM mindsdb.crypto4
WHERE date = "2019-01-02";
"""

result = mindsdb_sdk.query['SELECT * FROM mindsdb.crypto4 WHERE date = "2019-01-02";']

# # Print the forecasted values
print(result)

# # Generate x-axis values (e.g., timestamps, dates)
# x = range(len(result))

# # Plot the forecasted values
# plt.plot(x, result)
# plt.xlabel('Time')
# plt.ylabel('Close Price Forecast')
# plt.title('BTC/USD Close Price Forecast')
# plt.show()
