import matplotlib.pyplot as plt
import mindsdb_sdk

window = 50  # Replace with the desired window size for prediction
horizon = 10  # Replace with the desired horizon size for forecasting

server = mindsdb_sdk.connect()
server = mindsdb_sdk.connect('http://127.0.0.1:47334')
server = mindsdb_sdk.connect(email='anand00rohan@gmail.com', password='Rohan@Rohit47')
server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email='anand00rohan@gmail.com', password='Rohan@Rohit47')
csv_file_path = 'functions/main.csv'
# server.learn(from_data=csv_file_path, to_predict='close_price')
# result = server.predict(when_data=csv_file_path)
# print(result)
database = server.get_database('files')
print(database)

table = database.get_table('main')
print(table)
project = server.get_project('mindsdb')

# Define the model
model_name = "btcusd_predictor"

# Define the query
query = """
    SELECT *
    FROM models.btcusd_predictor
    WHERE date = '2021-05-01';
"""

# print the results of the query
result = database.query(query)
df = result.DataFrame()

print(result)