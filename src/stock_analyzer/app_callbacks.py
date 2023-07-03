"""
Only two call backs are defined which are:

update_stock_selection:
    When the user selects a new stock, the data is updated to represent that new selection. The data is stored in a dcc.Store item and thus embedded directly into the html.

update_graph:
    Currently one graph is updated with the new data, however the same callback is meant to dictate the update of all future added graphs as well.
    The callback is triggered when 1) the data is changed which happends when the update_stock_selection callback is activated and 2) when the date range selection change.
"""

import datetime as dt

from dash import callback, Output, Input, html, dcc
import pandas as pd
import plotly.express as px
import yfinance as yf

from src.stock_analyzer.callback_manager import CallbackManager


callback_manager = CallbackManager()


@callback_manager.callback(
        Output("stock-data", "data"),
        Input("stock-dropdown", "value")
)
def update_stock_selection(stock_symbol: str):
    if stock_symbol is None:
        stock_symbol = "AAPL"
    
    ticker = yf.Ticker(stock_symbol)
    data = ticker.history(
        start="2000-01-01",
        end=dt.datetime.now().strftime("%Y-%m-%d")
    ).reset_index()

    data["Date"] = pd.to_datetime(data["Date"].dt.date)

    if data.empty:
        print("Could not extract data")

    return data.to_json(date_format="iso", orient="split")


@callback_manager.callback(
    Output("right-column", "children"),
    Input("stock-data", "data"),
    Input("date-picker", "start_date"),
    Input("date-picker", "end_date"),
)
def update_graph(json_data, start_date, end_date):
    if start_date is not None:
        start_date_obj = dt.date.fromisoformat(start_date)

    else:
        start_date_obj = dt.date(2015, 1, 1)
    
    if end_date is not None:
        end_date_obj = dt.date.fromisoformat(end_date)
    else:
        end_date_obj = dt.date.today()

    start_date_str = str(start_date_obj)
    end_date_str = str(end_date_obj)

    filtered_df = (
        pd.read_json(json_data, orient='split')
        .query(f"(Date >= @start_date_str) & (Date <= @end_date_str)" )
    )

    if filtered_df.empty:
        return px.line()

    fig = px.line(filtered_df, x="Date", y="Close")
    
    fig.layout = {"plot_bgcolor": "#282b38", "paper_bgcolor": "#282b38"}

    return html.Div(
        id="stock-price-chart-container",
        children=dcc.Loading(
            className="graph-wrapper",
            children=dcc.Graph(id="stock-price-chart", figure=fig),
            style={"display": "none"},
        ),
    )