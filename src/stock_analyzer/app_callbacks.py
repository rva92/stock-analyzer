import datetime as dt

from dash import callback, Output, Input
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

    if data.empty:
        print("Could not extract data")

    return data.to_json(date_format="iso", orient="split")


@callback_manager.callback(
    Output("stock-price-chart", "figure"),
    Input("stock-data", "data"),
    Input("date-picker", "start_date"),
    Input("date-picker", "end_date"),
)
def update_graph(json_data, start_date, end_date):
    filtered_df = (
        pd.read_json(json_data, orient='split')
        .filter(f"Date >= {start_date} & Date <= {end_date}" )
    )

    if filtered_df.empty:
        return px.line()

    fig = px.line(filtered_df, x="Date", y="close")
    
    return fig