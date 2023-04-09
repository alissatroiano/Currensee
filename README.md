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
