_BINANCE_INTEGRATION = "my_binance"
_AGGREGATED_TRADE_DATA_TABLE = "aggregated_trade_data"

async def get_latest_aggregated_trade_data(mdb, symbol, limit=1000):
    binance_query = f"SELECT * FROM {_BINANCE_INTEGRATION}.{_AGGREGATED_TRADE_DATA_TABLE} WHERE symbol='{symbol.upper()}' LIMIT {limit}"
    trade_data_response = await mdb.SQL.run_query(binance_query)
    if not trade_data_response.rows:
        return []
    return trade_data_response.rows
