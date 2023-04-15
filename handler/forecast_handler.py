_BINANCE_INTEGRATION = "my_binance"
_AGGREGATED_TRADE_DATA_TABLE = "aggregated_trade_data"

async def get_or_create_recent_trade_data_view(mdb, symbol):
    view_name = f"recent_{symbol}_view"
    all_views = await mdb.Views.getAllViews("mindsdb")
    existing_view = next((v for v in all_views if v["name"] == view_name), None)
    if existing_view:
        return existing_view
    # Get latest 1000m of data.
    view_select = f"SELECT * FROM {_BINANCE_INTEGRATION}.{_AGGREGATED_TRADE_DATA_TABLE} WHERE symbol = '{symbol.upper()}'"
    return await mdb.Views.createView(view_name, "mindsdb", view_select)

async def forecast_next_symbol_prices(mdb, symbol, model_name, limit=10):
    recent_view = await get_or_create_recent_trade_data_view(mdb, symbol)
    predict_query = f"SELECT m.* FROM {recent_view['name']} AS t JOIN mindsdb.{model_name} AS m WHERE m.open_time > LATEST LIMIT {limit}"
    predictions_response = await mdb.SQL.runQuery(predict_query)
    return predictions_response["rows"]
