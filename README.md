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

Currensee is an open-source project that uses MindsDB Python SDK to make blockchain price predictions. Currensee's time-series machine learning models were trained on historical datasets and powered by MindsDB. Currensee's tech stack includes Python, Flask, MindsDB Python SDK, HTML, CSS, and Bootstrap 5.

## Research & Planning
### User Stories

User stories were created during the planning phase of this project and were used to help guide the wireframing process. The following user stories were created for the MVP version of this app:

- As a user, I want the **‘About’** section to provide meaningful information about this software, so I can learn where the data is coming from and how the predictions are made. 

- As a user, I want to select a coin so I can view its' predictions

- As a user, I want to view price predictions from models that were trained on historical data, so I can recieve the most accurate predictions.

## Features
### Frontend Features

The financial app aims to provide the following features:

- **Cover Page**: Provides title, subtitle & open source project information for users & other developers

![Screenshot]('docs/images/cover.png')

- **Coins**: Provides an index page displaying coins currently supported by Currensee.

- **Coin Predictions** Clicking on a coin triggers a back end method that sends a request to MindsDB to retrieve the prediction data for the selected coin. The prediction data is then displayed on the front end on a new page. 

![Screenshot]()

### Backend Features

- **Cryptocurrency Data:** The models behind Currensee's predictions were trained on historical datasets and queried using MindsDB's Python SDK. The data is then displayed on the front end of the app.

- **Forecasting**: The app utilizes the MindsDB library, a machine learning tool, to create predictive models for forecasting cryptocurrency prices. These models are trained on historical data and are used to generate forecasts for future price trends.

- **Analysis**: The app performs various statistical and technical analysis on cryptocurrency data, such as calculating moving averages, relative strength index (RSI), and other indicators to provide insights into price trends and market behavior.

- **Visualization**: The app uses data visualization techniques to present the forecasted and analyzed data in graphical form, such as line charts, bar charts, and candlestick charts, to make it easier for users to interpret and understand the information.

## Technologies
The financial app is being developed using the following technologies:

- Python: A powerful programming language that is widely used in data analysis and machine learning tasks. It is used to implement the backend logic and data processing tasks.

- Flask: A popular web framework for Python that provides tools for building web applications efficiently.

- HTML: The HyperText Markup Language or HTML markup language was used to build the document's body and structure

- CSS: Cascading Style Sheets, the style-sheet language, was used to desribe the presentation of the HTML documents.

- Bootstrap 5: The Bootstrap framework was used to simplify cross-platform responsiveness and add overall structure and styling.

- [MindsDB](https://mindsdb.com/): MindsDB is an open-source machine learning tool that simplifies the process of building and deploying predictive models. Currensee will use MindsDB to create custom prediction models and train them on historical data.

- [MindsDB Python SDK](https://pypi.org/project/mindsdb-sdk/): Will be used to establish to the connection between MindsDB and this application.

- [Google Fonts](https://fonts.google.com/specimen/Inter?query=inter) - Used for applying font styles to all typography
## Credits
- [Bootstrap](https://getbootstrap.com/docs/5.3/examples/) - Bootsrap's documentation was used for code snippets pertaining to grid structure and layout

### Code

### MindsDB

- The article, ['Forecast Tesla Stock Prices using MindsDB'](https://dev.to/rutamhere/predict-tesla-stock-prices-using-mindsdb-40k5) was used as a reference when creating & training time-series models for Currensee.

- Thee article, ['Creating Views with MindsDB'](https://dev.to/rutamhere/creating-views-with-mindsdb-1mnf) was referenced when creating views for Currensee.

### UX

- [Visme](https://visme.co/blog/website-color-schemes/) - UX research.

- ["Psychology of Color in Financial App Design" from windmill.digital](https://www.windmill.digital/psychology-of-color-in-financial-app-design/) - UX research.

- [fontpair](https://www.fontpair.co/all) - This article was used to view trending font pairings. The font set used for this project was found in this article
### Media

- [Iconduck](https://iconduck.com/icons/82936/bitcoin-cash-cryptocurrency) = Bitcoin, Etherium and Doge Coin icon set was downloaded from this site.s
### Other
- [Kevsbest's article, "Top 5 AI Crypto Prediction Services Right Now"](https://kevsbest.com/ai-crypto-prediction-services-right-now/) was referenced while conducting competitor research.

