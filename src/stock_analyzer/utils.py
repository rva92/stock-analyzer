from typing import List

import pandas as pd


def scrape_sp500_constituents() -> List[str]:
    wiki_sp500_list = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    ticker_list = pd.read_html(wiki_sp500_list)

    df = ticker_list[0]


    return df["Symbol"].to_list()
