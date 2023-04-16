# Currensee

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
-[Research & Planning](#research-&-planning)
   - [User Stories](#user-stories)
   - [Wireframes](#wireframes)
- [Features](#features)
   - [Frontend Features](#frontend-features)
   - [Backend Features](#backend-features)
- [Technologies](#technologies)
    - [Languages](#languages)
    - [Frameworks](#frameworks)
- [Tests](#tests)
    - [Creating MindsDB Models](#creating-mindsdb-models)
    - [Testing MindsDB Models](#testing-mindsdb-models)
    - [Testing the App](#testing-the-app)
- [Deployment](#deployment)
- [Credits](#credits)
    - [Code](#code)
    - [Content](#content)
    - [Media](#media)
    - [Other](#other)

## Introduction

This financial app is a data-driven application that provides forecasting and analysis of cryptocurrencies. It is currently in the development phase and is being built using Python, Django, API, and MindsDB.

## Research & Planning
### User Stories

User stories were created during the planning phase of this project and were used to help guide the wireframing process:

- As a user, I want the **‘About’** section to provide meaningful information about this software, so I can learn where the data is coming from and how the predictions are made. 

- As a user, I want to fill out a search form so I can view my desired coin's predictions

- As a user, I want to filter predictions using relevant parameters so I can preview the most useful data

- As a user, I want to view meaningful data insights & predictions based on my coin's historical data, so I can make informed decisions about my cryptocurrency(s).

- As a user, I want to be able to view the website from my mobile device so I can check out coin predictions when I'm on the go.

## Features
### Frontend Features

The financial app aims to provide the following features:

- **About**: Provides information about this application and how it was implemented ***(includes information about MindsDB and referenes the data used to make the predictions.)***

![Screenshot]()

- **Predictor Tool**: This feature lets the user choose from a list of coins then redirects them to a page (or pop-up modal) containing the coin's prediction data.

![Screenshot]()

- **Navigation**: Gives users the ability to navigate the app from any page or section and includes external links (MindsDB, developer's GitHub, Slack, etc.)

![Screenshot]()

### Backend Features

- **Cryptocurrency Data:** The app fetches real-time cryptocurrency data using APIs and stores it in a dataset (CSV file) for analysis and forecasting.

- **Forecasting**: The app utilizes the MindsDB library, a machine learning tool, to create predictive models for forecasting cryptocurrency prices. These models are trained on historical data and are used to generate forecasts for future price trends.

- **Analysis**: The app performs various statistical and technical analysis on cryptocurrency data, such as calculating moving averages, relative strength index (RSI), and other indicators to provide insights into price trends and market behavior.

- **Visualization**: The app uses data visualization techniques to present the forecasted and analyzed data in graphical form, such as line charts, bar charts, and candlestick charts, to make it easier for users to interpret and understand the information.

-
## Technologies
The financial app is being developed using the following technologies:

- Python: A powerful programming language that is widely used in data analysis and machine learning tasks. It is used to implement the backend logic and data processing tasks.

- Django: A popular web framework for Python that provides tools for building web applications efficiently. It is used to develop the server-side components of the app, handle user authentication, and manage database operations.

- HTML: The HyperText Markup Language or HTML markup language was used to build the document's body and structure

- CSS: Cascading Style Sheets, the style-sheet language, was used to desribe the presentation of the HTML documents.

- Bootstrap 5: The Bootstrap framework was used to simplify cross-platform responsiveness and add overall structure and styling.

- API: Application Programming Interface (API) is used to fetch real-time cryptocurrency data from external sources, such as cryptocurrency exchanges, and integrate it into the app.

- [MindsDB](https://mindsdb.com/): MindsDB is an open-source machine learning tool that simplifies the process of building and deploying predictive models. Currensee will use MindsDB to create custom prediction models and train them on historical data.

- [MindsDB Python SDK](): Will be used to establish to the connection between MindsDB and this application.

- [Google Fonts](https://fonts.google.com/specimen/Inter?query=inter) - Used for applying font styles to all typography

## Tests

### Creating MindsDB Models
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

## Credits
- [Bootstrap](https://getbootstrap.com/docs/5.3/examples/) - Bootsrap's documentation was used for code snippets pertaining to grid structure and layout

### Code

### UX

- [Visme](https://visme.co/blog/website-color-schemes/) - UX research.

- ["Psychology of Color in Financial App Design" from windmill.digital](https://www.windmill.digital/psychology-of-color-in-financial-app-design/) - UX research.

- [fontpair](https://www.fontpair.co/all) - This article was used to view trending font pairings. The font set used for this project was found in this article

### Media
### Other
- [Kevsbest's article, "Top 5 AI Crypto Prediction Services Right Now"](https://kevsbest.com/ai-crypto-prediction-services-right-now/) was referenced while conducting competitor research.
