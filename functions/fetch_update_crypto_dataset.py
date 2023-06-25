import requests
import pandas as pd
import datetime


def fetch_and_update_crypto_prices(tickers, append=True):
    """
    Fetches daily cryptocurrency price data from Tiingo API for a list of tickers,
    and appends the data to an existing CSV file.

    Args:
        tickers (list): A list of cryptocurrency ticker symbols (e.g., 'btcusd', 'ethusd', etc.).
        append (bool): If True, the fetched data will be appended to an existing file with the
            same name, otherwise a new file will be created. Default is True.
    """

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token 87f601b3fffb4764176595daa3886d5efa8aa033'
    }

    # Get the current date in the format 'YYYY-MM-DD'
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')

    # Loop through each ticker in the list
    for ticker in tickers:
        # Send GET request to the API
        requestResponse = requests.get(
            f"https://api.tiingo.com/tiingo/crypto/prices?tickers={ticker}&startDate={current_date}&resampleFreq=1day",
            headers=headers)

        # Convert the response to JSON
        data = requestResponse.json()

        # Create an empty list to store flattened data
        flattened_data = []

        # Loop through each dictionary in the list
        for item in data:
            ticker = item['ticker']
            base_currency = item['baseCurrency']
            quote_currency = item['quoteCurrency']
            price_data = item['priceData']

            # Flatten the price data and append to the list
            for sub_item in price_data:
                date = sub_item['date']
                open_price = sub_item['open']
                high_price = sub_item['high']
                low_price = sub_item['low']
                close_price = sub_item['close']
                volume = sub_item['volume']
                flattened_data.append(
                    [ticker, base_currency, quote_currency, date, open_price, high_price, low_price, close_price,
                     volume])

        # Create a DataFrame from the flattened data
        df = pd.DataFrame(flattened_data,
                          columns=['ticker', 'base_currency', 'quote_currency', 'date', 'open_price', 'high_price',
                                   'low_price', 'close_price', 'volume'])

        # Convert the date column to datetime object
        df['date'] = pd.to_datetime(df['date'])

        # Extract the date part of the datetime object and convert to string in desired format
        df['date'] = df['date'].dt.strftime('%Y-%m-%d')

        # Save the DataFrame as a CSV, either by appending or creating a new file
        if append:
            df.to_csv('main.csv', mode='a', header=False, index=False)
        else:
            df.to_csv('main.csv', index=False)

    print("Data has been successfully updated in main.csv")


# Function calling with list of tickers and append=True
tickers_list = ['btcusd', 'ethusd','fldcbtc']  # Add more tickers as needed
fetch_and_update_crypto_prices(tickers_list, append=True)
