import requests
import pandas as pd

final = pd.read_csv('main.csv')
print('before length : ', len(final))


def merge_tiingo_crypto_prices(ticker, start_date, append=False):
    """
    Fetches cryptocurrency price data from Tiingo API for a given ticker and start date,
    flattens the data, and saves it as a CSV file. Option to append data to an existing
    file is available.

    Args:
        ticker (str): The cryptocurrency ticker symbol (e.g., 'btcusd', 'ethusd', etc.).
        start_date (str): The start date for fetching price data in the format 'YYYY-MM-DD'.
        append (bool): If True, the fetched data will be appended to an existing file with the
            same name, otherwise a new file will be created. Default is False.
    """

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token 87f601b3fffb4764176595daa3886d5efa8aa033'
    }

    # Send GET request to the API
    requestResponse = requests.get(
        f"https://api.tiingo.com/tiingo/crypto/prices?tickers={ticker}&startDate={start_date}&resampleFreq=5min",
        headers=headers)

    # Convert the response to JSON
    data = requestResponse.json()
    print('length of current data fetched', len(data))
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
                [ticker, base_currency, quote_currency, date, open_price, high_price, low_price, close_price, volume])

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
        print("in if section")
        df.to_csv('main.csv', mode='a', header=False, index=False)
    else:
        print("in else section")
        df.to_csv('main_1.csv', index=False)

    print("Data has been successfully saved as main.csv")


# Function calling
merge_tiingo_crypto_prices('ethusd', '2023-01-02', append=True)

print('after length : ', len(final))
