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
   - [ML Features](#ml-features)
- [Technologies](#technologies)
    - [Languages](#languages)
    - [Frameworks](#frameworks)
- [Tests](docs/tests/TESTS.md)
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

User stories were created during the planning phase of this project and were used to help guide the wireframing process. The following user stories were created for the MVP version of this app:

- As a user, I want the **‘About’** section to provide meaningful information about this software, so I can learn where the data is coming from and how the predictions are made. 

- As a user, I want to fill out a search form so I can view my desired coin's predictions

- As a user, I want to filter predictions using relevant parameters so I can preview the most useful data

- As a user, I want to view meaningful data insights & predictions based on my coin's historical data, so I can make informed decisions about my cryptocurrency(s).

- As a user, I want to be able to view the website from my mobile device so I can check out coin predictions when I'm on the go.

The following user stories were created for the advanced version (future release) of this app:

## Features
### Frontend Features

The financial app aims to provide the following features:

- **Cover Page**: Provides title, subtitle & open source project information for users & other developers

![Screenshot]()

- **Coins**: Provides an index page displaying coins currently supported by Currensee. ***This section is still in development.***

![Screenshot]()

- **Navigation**: A fixed navigation loading from the base template (`base.html`) makes it easy to navigate the app from any page  users the ability to navigate the app from any page or section includes external links (MindsDB, developer's GitHub, Slack, etc.)

![Screenshot]()

### Backend Features

- **Cryptocurrency Data:** The app fetches real-time cryptocurrency data using APIs and stores it in a dataset (CSV file) for analysis and forecasting.

- **Forecasting**: The app utilizes the MindsDB library, a machine learning tool, to create predictive models for forecasting cryptocurrency prices. These models are trained on historical data and are used to generate forecasts for future price trends.

- **Analysis**: The app performs various statistical and technical analysis on cryptocurrency data, such as calculating moving averages, relative strength index (RSI), and other indicators to provide insights into price trends and market behavior.

- **Visualization**: The app uses data visualization techniques to present the forecasted and analyzed data in graphical form, such as line charts, bar charts, and candlestick charts, to make it easier for users to interpret and understand the information.


## MindsDB Machine Learning Models

The following time-series models were created using [MindsDB](https://cloud.mindsdb.com/) and are being queried to retrieve the prediction data displayed on the front-end of this application:

- **btcusd_prediction_mod**: This model was trained on historical data for the BTC/USD pair and is used to generate forecasts for future price trends.

```sql
    CREATE MODEL btcusd_prediction_mod
    FROM files (
        SELECT * FROM test_data
        WHERE ticker = 'btcusd'
        LIMIT 2000
        )
    PREDICT close_price
    ORDER BY date
    WINDOW 3650
    HORIZON 14;
```

**Ethereum Model**

The following SQL query was used to create the `ethusd_prediction_mod` model:

```sql
CREATE MODEL ethusd_prediction_mod
FROM files (
    SELECT * FROM test_data
    WHERE ticker = 'ethusd'
    LIMIT 2000
    )
PREDICT close_price
ORDER BY date
WINDOW 3650
HORIZON 14;
```


### Advanced Features

Be
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
