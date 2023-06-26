import pandas as pd
from prophet import Prophet


def forecast_crypto_price(crypto_name):
    # Load your dataset into a pandas DataFrame
    df = pd.read_csv('/content/main.csv')

    # Filter the data for a specific crypto
    df_crypto = df[df['ticker'] == crypto_name]

    # Rename columns for compatibility with Prophet
    df_crypto = df_crypto.rename(columns={'date': 'ds', 'close_price': 'y'})

    # Convert 'ds' column to datetime format
    df_crypto['ds'] = pd.to_datetime(df_crypto['ds'])

    df_crypto = df_crypto.ffill()
    print(df_crypto.isnull().sum())

    # Set 'cap' value based on the highest 'close_price' value
    cap = df_crypto['y'].max()
    df_crypto['cap'] = cap

    df_crypto['floor'] = -1000  # unused in linear growth

    # Create and fit the Prophet model
    model = Prophet(growth='flat')
    model.fit(df_crypto)

    # Define a future DataFrame for forecasting
    future = model.make_future_dataframe(periods=1800)  # Forecast for the next 365 days
    future['floor'] = -1000
    future['cap'] = cap

    # Make predictions
    forecast = model.predict(future)

    # Plot the forecast
    model.plot(forecast)


# fucntion calling
# crypto_name = 'btcusd'
# forecast_crypto_price(crypto_name)
