from typing import *
from datamodel import *
import random as rd
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import math
import datetime as dt
import yfinance as yf

class Trader:

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        global prices
        prices = []
        result = {}
        for product in state.order_depths.keys():
            if product == 'BANANAS':
                orderDepth = state.order_depths[product]
                orders = []

                bTrades = state.market_trades[product]
                numTrade = 0
                if numTrade < len(bTrades):
                    tradePrice = bTrades[numTrade].price

                

        return result


def ma(lst, windowSize):
    '''
    moving averages
    '''
    ma = []
    for i in range(len(lst)):
        if i < windowSize-1:
            windowAvg = int(np.sum(lst[0:i+1])/(i+1))
        else:
            windowAvg = int(np.sum(lst[i-(windowSize-1):i+1])/windowSize)
        ma.append(windowAvg)
    return ma



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
    ma5 = ma(priceLst, 5)
    ma10 = ma(priceLst, 10)
    ma30 = ma(priceLst, 30)

    fig = go.Figure()
    fig.add_trace(go.Scatter(name = "price",  y=priceLst))
    fig.add_trace(go.Scatter(name = "MA5", y=ma5))
    #fig.add_trace(go.Scatter(name = "MA10", y=ma10))
    #fig.add_trace(go.Scatter(name = "MA30", y=ma30))

    fig.show()

main()