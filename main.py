import dash
from src.stock_analyzer import app_layout
from src.stock_analyzer.app_callbacks import callback_manager

# TODO: Finished app layout with settings bar and display column
# TODO: Scrape sp500 index constituents
# TODO: Set up data load
# TODO: Integrate data with app



app = dash.Dash(
    __name__,
    meta_tags=[
        {
            "name": "viewport",
            "content": "width-device-width, initial-scale=1.0",
        }
    ],
)

app.title = "StockAnalyzer"
app.layout = app_layout.layout

callback_manager = callback_manager

callback_manager.attach_to_app(app)


server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)