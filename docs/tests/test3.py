import matplotlib.pyplot as plt
csv_file_path = 'functions/main.csv'
window = 50  # Replace with the desired window size for prediction
horizon = 10  # Replace with the desired horizon size for forecasting



from mindsdb import MindsDB

# Initialize MindsDB
mdb = MindsDB()
model_name = "btcusd_predictor"
# Define the query
query = """
    FORECAST close_price
    FROM mindsdb.{model_name}
    USING
      (SELECT open_price, high_price, low_price, close_price
       FROM my_data_to_predict)
"""

# Execute the query
result = mdb.query(query)

# Access the forecasted values
forecasted_values = result.predicted_values['close_price']

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