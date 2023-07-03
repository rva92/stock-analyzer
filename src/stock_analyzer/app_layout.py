"""
The app layout is inspired by the dash example svm application:
https://github.com/plotly/dash-sample-apps/blob/main/apps/dash-svm/
"""
from datetime import date

from dash import dcc
from dash import html

import src.stock_analyzer.utils as utils

sp_500_list = utils.scrape_sp500_constituents()

banner_layout = html.Div(
    className="banner",
    children=[
        html.Div(
            className="container scalable",
            children=[
                html.H2(
                    id="banner-title",
                    children=[
                         html.A(
                            "Stock Analyzer"
                        )
                    ]
                )
            ]
        )
    ]
)

left_column_body = html.Div(
    id="left-column",
    children=[
        html.Section(
            id="stock-selector",
            className="card",
            children=[
                html.Div(
                    style={
                        "padding": "20px 10px 25px 4px"
                    },
                    children=[
                        html.P("Select Stock:"),
                        html.Div(
                            style={"margin-left": "6px"},
                            children=dcc.Dropdown(
                                id="stock-dropdown",
                                options=sp_500_list,
                                value="AAPL"
                            )
                        ),
                    ],
                ),
                html.Div(
                    style={
                        "padding": "20px 10px 25px 4px"
                    },
                    children=[
                        html.P("Select Date Range:"),
                        html.Div(
                            style={"margin-left": "6px"},
                            children=dcc.DatePickerRange(
                                id="date-picker",
                                min_date_allowed=date(2000, 1, 1),
                                max_date_allowed=date.today(),
                                initial_visible_month=date(2015, 1, 1),
                                end_date=date.today(),
                            )
                        ),
                    ],
                )
            ]
        )
    ]
)

right_column_body = html.Div(
    id="right-column",
    children=dcc.Graph(
        id="stock-price-chart",
        figure=dict(
            layout=dict(
                plot_bgcolor="#282b38", paper_bgcolor="#282b38"
            )
        )
    )
)

body_layout = html.Div(
    id="body",
    className="container scalable",
    children=[
        html.Div(
             id="app-container",
             children=[
                left_column_body,
                right_column_body,
            ]
        )
    ]
)

layout = html.Div(
    children=[
        banner_layout,
        body_layout,
        dcc.Store(id="stock-data")
    ]
)
