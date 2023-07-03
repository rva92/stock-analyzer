# Stock Analyzer

## tl;dr
A simple python project used to test out a variety  techs around the implementation of Python projects. Notice, it is not a serious attempt to build a stock analyzer tool.

## Introduction
Through my work and my previous projects I have tried a lot of different things Python related. However, I felt I missed a project that summoned up some of the important tools around my Python projects.  This project is an attempt to address address that issue. 

The project builds around a simple dash application which displays some simple stock analytics for a user defined stock from the SP500.  The analytics are not meaning full and the should be seen as a serious approach towards defining a stock recommendation system.

Instead, I use this simple application as both an example of how I use tools in Python projects such as MyPy, templates and containerization, but also a playground to try out new things e.g., setting up a CI/CD pipeline using GitHubActions or alike, hosting application on a seriver (Azure, AWS or RaspBerryPie; locally). 

## Project Structure
The project follows a simple structure that builds around the dash callbacks. I have split the callbacks and layout into separate files for better maintainability and overview. To aid this I have taken inspiration in the callback_manager from the [stackoverflow](https://stackoverflow.com/questions/62102453/how-to-define-callbacks-in-separate-files-plotly-dash).

The SP500 index is scraped from wikipedia [here](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies) using pandas strong read_html function (similar can easily be done with BeautifoulSoup).

The stock data is extracted from the [yfinance package](https://github.com/ranaroussi/yfinance) which is an open-source tool build around Yahoo's publicly available APIs. 

## Visualization and Metrics
Currently, only one graph is displayed which depicts the (ca adjusted) stock prices over time within the selected date range. The same data can be seen on Yahoo Finance own web page. 

## Disclaimer
The stock analyzer presented in this application is not a good way to get stock trade recommendations and the author can in no way be held responsible for any decision made based on the application nor the validity of the data or calculations. DO NOT TRADE BASED ON THIS TOOL!

