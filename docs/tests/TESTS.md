# Tests

## Models

## Creating MindsDB Models
1. Time Series Model Test 1 - Missing Window:
    1. Visit `cloud.mindsdb.com/editor`
    2. Input the following code:
    ```sql
    CREATE MODEL btcusd_model_1
    FROM files (
        SELECT * FROM test_data
        )
    PREDICT open_price, high_price, close_price
    ORDER BY date
    GROUP BY ticker;
    ```
    3. Notice model is not training
    4. Use `SELECT` statement to view model status:
    ```sql
    SELECT *
    FROM mindsdb.models
    WHERE name = "btcusd_model_1";
    ```
    5. Observe the following error:
    | NAME | ENGINE | PROJECT | VERSION | STATUS | ACCURACY | PREDICT | UPDATE_STATUS | MINDSDB_VERSION | ERROR | SELECT_DATA_QUERY | TRAINING_OPTIONS | CURRENT_TRAINING_PHASE | TOTAL_TRAINING_PHASES | TRAINING_PHASE_NAME | TAG | CREATED_AT |
    | ---- | ------ | ------- | ------- | ------ | -------- | ------- | ------------- | --------------- | ----- | ----------------- | ---------------- | ---------------------- | --------------------- | ------------------- | --- | ---------- |
    | btcusd_model_1 | lightwood | mindsdb | 1 | error | [NULL] | open_price | up_to_date | 23.4.3.2 | Exception: Missing mandatory timeseries setting: window, raised at: /usr/local/lib/python3.8/dist-packages/mindsdb/integrations/libs/ml_exec_base.py#135 | SELECT * FROM test_data | {'target': 'open_price', 'timeseries_settings': {'is_timeseries': True, 'order_by': 'date', 'group_by': ['ticker']}} | 1 | 5 | Generating problem definition | [NULL] | 2023-04-15 19:12:08.577797 |
    6. Refactor code to include `WINDOW` parameter:
    ```sql
    CREATE MODEL btcusd_model_1
    FROM files (
        SELECT * FROM test_data
        )
    PREDICT open_price, high_price, close_price
    ORDER BY date
    GROUP BY ticker
    WINDOW 10;
    ```
    7. Run the query and wait for model to finish training.
    8. Check model status using `SELECT` statement:
    ```sql
    SELECT *
    FROM mindsdb.models
    WHERE name = "btcusd_model_1";
    ```
    9. Observe the following output:
    | NAME | ENGINE | PROJECT | VERSION | STATUS | ACCURACY | PREDICT | UPDATE_STATUS | MINDSDB_VERSION | ERROR | SELECT_DATA_QUERY | TRAINING_OPTIONS | CURRENT_TRAINING_PHASE | TOTAL_TRAINING_PHASES | TRAINING_PHASE_NAME | TAG | CREATED_AT |
    | ---- | ------ | ------- | ------- | ------ | -------- | ------- | ------------- | --------------- | ----- | ----------------- | ---------------- | ---------------------- | --------------------- | ------------------- | --- | ---------- |
    | btcusd_model_1 | lightwood | mindsdb | 1 | complete | 0.95 | open_price | up_to_date | 23.4.3.2 | [NULL] | SELECT * FROM test_data | {'target': 'open_price', 'timeseries_settings': {'is_timeseries': True, 'order_by': 'date', 'window': 10, 'group_by': ['ticker']}} | 5 | 5 | Complete | [NULL] | 2023-04-15 19:17:58.216912 |
    10. Mark test, 'passed' as time-series_settings now includes `WINDOW` parameter.

2. Time Series Model Test 2 - Missing WHERE clause to specify coin type:
    1. Visit `cloud.mindsdb.com/editor`
    2. Input the following code:
    ```sql
    CREATE MODEL btcusd_model_2
    FROM files (
        SELECT * FROM test_data
        )
    PREDICT open_price, high_price, close_price
    ORDER BY date
    GROUP BY ticker
    WINDOW 10;
    ```
    3. Notice model is training, but the `ticker` column has not been specified in the predictor.
    4. Create a new model statement that includes the `WHERE` clause:
    ```sql
    CREATE MODEL btcusd_predictor
    FROM files (
        SELECT * FROM test_data
        WHERE ticker = 'btcusd'
        )
    PREDICT close_price
    ORDER BY date
    WINDOW 10;
    ```
    5. Run the query and wait for model to finish training.
    6. Check model status using `SELECT` statement:
    ```sql
    SELECT *
    FROM mindsdb.models
    WHERE name = "btcusd_predictor";
    ```
    7. Observe the following output:
    ```markdown
    | NAME | ENGINE | PROJECT | VERSION | STATUS | ACCURACY | PREDICT | UPDATE_STATUS | MINDSDB_VERSION | ERROR | SELECT_DATA_QUERY | TRAINING_OPTIONS | CURRENT_TRAINING_PHASE | TOTAL_TRAINING_PHASES | TRAINING_PHASE_NAME | TAG | CREATED_AT |
    | ---- | ------ | ------- | ------- | ------ | -------- | ------- | ------------- | --------------- | ----- | ----------------- | ---------------- | ---------------------- | --------------------- | ------------------- | --- | ---------- |
    | btcusd_predictor | lightwood | mindsdb | 1 | complete | 0.996 | close_price | up_to_date | 23.4.3.2 | [NULL] | SELECT * FROM test_data
        WHERE ticker = 'btcusd' | {'target': 'close_price', 'timeseries_settings': {'is_timeseries': True, 'order_by': 'date', 'window': 10}} | 5 | 5 | Complete | [NULL] | 2023-04-15 20:11:28.076188 |
    ```
    8. Notice **acccuracy** is now higher with one specific target column
    9. Mark test, 'passed'.
    
### Training MindsDB Models
1. Time Series Error 1:
    1. Visit `cloud.mindsdb.com/editor`
    2. Input the following code to run prediction query on `btcusd_predictor` model:
    ```sql
    ```
    3. Observe error message in output:
    ```markdown
    ```
    4. Update `CREATE MODEL` query to include larger **WINDOW** and **HORIZON** paramaters (can train on up tp 5 years past/historical data, can predict up to 5 years into the future):
    ```sql
    CREATE MODEL btcusd_predictions
    FROM files (
        SELECT * FROM test_data
        WHERE ticker = 'btcusd'
        )
    PREDICT close_price
    ORDER BY date
    WINDOW 1825
    HORIZON 1825;
    ```
    5. Run the query and wait for model to finish training.
    6. Query the model and observe the following output:
    ```markdown
    ```
### Application Tests
1. Import MindsDB Test 1:
    1. Add mindsdb import statements to `app.py`
    2. Receive error message: `ModuleNotFoundError: No module named 'mindsdb'`
    3. Reinstall MindsDB using `pip install mindsdb`
    4. Attempt to import MindsDB again
    5. Receive error message: `ModuleNotFoundError: No module named 'mindsdb'`

2. `import mindsdb` TypeError Test 1:
    1. Add import statement `from mindsdb.__about__ import __version__` to `app.py`
    2. Define `mdb` as `mdb = mindsdb()`
    3. Receive a TypeError: `TypeError: 'module' object is not callable`
    4. Add the following code to determine attributes:
    ```python
    obj = mindsdb.__about__
    attributes = dir(obj)
    print(attributes)
    ```
    5. Review output in the console which reads:
    ```
    ['__author__', '__builtins__', '__cached__', '__copyright__', '__description__', '__doc__', '__email__', '__file__', '__github__', '__license__', '__loader__', '__name__', '__package__', '__package_name__', '__pypi__', '__spec__', '__title__', '__version__']
    ```
    6.  Refactor and run the following code:
    ```python
    mdb = mindsdb.__about__.__version__
    print(dir(mdb))
    ```
    7. Observe output:
    ```
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
    ```
    8. Refactor and run the following code:
    ```python
    mdb = mindsdb
    print(dir(mdb))
    ```
    9. Review the output in the terminal:
    ```
    ['__about__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__']
    ```

3. Python SDK Test 1:
    1. Wirth `import mindsdb_sdk` at the top of `app.py`, add the following code:
    ```python
    mdb = mindsdb_sdk
    print(dir(mdb))
    ```
    2. Observe output:
    ```
    ['Server', '__about__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', 'connect', 'connectors', 'database', 'model', 'name', 'project', 'query', 'server', 'utils']
    ```
    3. Refactor and run the following code:
    ```python
    mdb = mindsdb_sdk.__about__.__version__
    print(dir(mdb))
    ```
    4. Observe output:
    ```python
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
    ```
    5. Refactor and run the following code:
    ```python
    mdb = mindsdb_sdk.__dict__
    print(dir(mdb))
    ```
    6. Observe output:
    ```
    ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
    ```
    7. Finally, run the following code to list attributes of  `mindsdb_sdk`:
    ```python
    mdb = mindsdb_sdk
    print(dir(mdb))
    ```
    8. Observe output:
    ```
    ['Server', '__about__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', 'connect', 'connectors', 'database', 'model', 'name', 'project', 'query', 'server', 'utils']
    ```
    9. Refactor and run the following code:
    ```python
    mdb = mindsdb_sdk.model
    print(dir(mdb))
    ```
    10. Observe output:
    ```
   ['AdjustPredictor', 'Constant', 'Describe', 'Identifier', 'Join', 'List', 'Model', 'ModelVersion', 'Query', 'RetrainPredictor', 'Select', 'Star', 'Union', 'Update', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'annotations', 'dict_to_binary_op', 'parse_sql', 'pd', 'query_traversal']
    ```

4. Querying MindsDB Models with the Python SDK
    1. Attempt to call a model in `app.py`
    ```python
    mindsdb_sdk.model = 'btcusdt_model_1'
    print(mindsdb_sdk.model)
    ```
    2. Receive error: `TypeError: 'module' object is not callable`
    3. Refactor code to read:
    ```python
    mindsdb_sdk.model = 'btcusdt_model_1'
    print(mindsdb_sdk.model)
    ```
    4. Mark test as 'pass' after determining proper way to call a model using the SDK. 
 
5. Training MindsDB Models with the Python SDK
    1. Attempt to train a model in `app.py`
    ```python


    mdb = mindsdb_sdk.connect()
    print(dir(mdb)
