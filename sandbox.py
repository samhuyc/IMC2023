from typing import *
from datamodel import *
import random as rd
import numpy as np
import pandas as pd
import plotly.express as px
import math
import datetime as dt
import yfinance as yf

class Trader:

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        result = {}
        for product in state.order_depths.keys():
            if product == 'PEARLS':
                orderDepth = state.order_depths[product]

        return result
    
    def ma(lst, newEntry, windowSize):
        new_lst = lst.copy()
        if len(new_lst) < windowSize:
            new_lst.append(newEntry)
        else: 

            print('')
        return lst

def randomTrend(vol):
    '''
    Created to make a random stock-like trend
    '''
    start = dt.datetime(2011, 1, 1)
    end = dt.datetime(2021, 1, 1)
    stock_data = yf.download('MSFT', start, end)

    returns = stock_data['Adj Close'].pct_change()
    daily_vol = vol*returns.std()
    T = 252
    count = 0
    price_list = []
    last_price = stock_data['Adj Close'][-1]

    price = last_price * (1 + np.random.normal(0, daily_vol))
    price_list.append(price)

    for y in range(T):
        if count == 251:
            break
        price = price_list[count]* (1 + np.random.normal(0, daily_vol))
        price_list.append(price)
        count += 1

    return price_list


def main():
    
    priceLst = randomTrend(3)
    fig = px.line(priceLst)
    fig.show()


main()