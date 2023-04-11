import matplotlib.pyplot as plt
import mindsdb_sdk

server = mindsdb_sdk.connect()
server = mindsdb_sdk.connect('http://127.0.0.1:47334')

server = mindsdb_sdk.connect(email='anand00rohan@gmail.com', password='Rohan@Rohit47')
server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email='anand00rohan@gmail.com', password='Rohan@Rohit47')

csv_file_path = 'functions/main.csv'
# server.learn(from_data=csv_file_path, to_predict='close_price')
# result = server.predict(when_data=csv_file_path)
# print(result)

databases = server.list_databases()

database = databases[1] # Database type object

query = database.query('select * from files.main limit 5')
print(query.fetch())
print(database)

# table = database.get_table('main')

project = server.get_project('mindsdb')

# # Define the query

query = """
    FORECAST close_price
    FROM mindsdb.{model_name}
    USING
      (SELECT open_price, high_price, low_price, close_price
       FROM my_data_to_predict)
"""

# query = """
#     CREATE MODEL mindsdb.btcusd_predictor
# FROM files
#   (SELECT open_price, high_price, low_price, close_price
#    FROM files.main)
# PREDICT close_price;
# """

model_name = "btcusd_predictor"
query = database.query('select * from main limit 5')
# print(query.fetch())

# Execute the query

# print(query.fetch())
result = database.query(query)

# create view
view = project.create_view(
      'view2',
      'select * from files.main join btcusd_predictor')

# get view
views = project.list_views()
view = views[0]
df = view.fetch()


# Access the forecasted values
model = project.get_model('btcusd_predictor')

result_df = model.predict(df)
result_df = model.predict(query)
print(result_df)

forecasted_values = result_df.predicted_values['close_price']

# Print the forecasted values
print(forecasted_values)

# Generate x-axis values (e.g., timestamps, dates)
x = range(len(forecasted_values))

# Plot the forecasted values
plt.plot(x, forecasted_values)
plt.xlabel('Time')
plt.ylabel('Close Price Forecast')
plt.title('BTC/USD Close Price Forecast')
plt.show()