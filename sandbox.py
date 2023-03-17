from typing import *
from datamodel import *
import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import math
import random as rd
import datetime as dt
import yfinance as yf

class Trader:

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        global prices
        prices = []
        result = {}

        for product in state.order_depths.keys():
            inventory = 0
            if product == 'BANANAS': 
                if product in state.position.keys():
                    inventory = state.position[product]
                order_depth = state.order_depths[product]
                orders = []

                if len(order_depth.sell_orders) > 0 and len(order_depth.buy_orders) > 0:
                    best_ask = min(order_depth.sell_orders.keys())
                    best_ask_volume = order_depth.sell_orders[best_ask]
                    best_bid = max(order_depth.buy_orders.keys())
                    best_bid_volume = order_depth.buy_orders[best_bid]
                    spread = best_ask - best_bid
                    
                ##design orders in 
                # {low premium: + high volume, high premium: + low volume} 
                # {high discount: - low volume, low discount: - high volume}
                    premium_interval = [0.1, 0.4, 0.6, 0.9]
                    resting_prices = [p * spread for p in premium_interval]
                    volume_scaler = [0.7, 0.3, -0.3, -0.7]
                    resting_volumes = [q * inventory for q in volume_scaler]

                    self.sendOrders(product, resting_prices, resting_volumes)

                    result[product] = orders   
           
    
    def sendOrders(self, product, prices, volumes):
        orders = []
        for i in range(len(prices)):
            orders.append(Order(product, prices[i], volumes[i]))
        
        return orders
        
###show trades method to be called in Trade::run()
    def showTrades(self, state: TradingState) :    
        for product in ["BANANAS"]:
            if product in state.market_trades:
                tradeLst = state.market_trades[product]
                for i in range(len(tradeLst)):
                    price = tradeLst[i].price
                    volume = tradeLst[i].quantity
                    print(f"{volume} of {product} traded @ {price}")
            
            if product in state.own_trades:
                tradeLst = state.own_trades[product]
                for i in range(len(tradeLst)):
                    price = tradeLst[i].price
                    volume = tradeLst[i].quantity
                    if tradeLst[i].buyer == "SUBMISSION":
                        print(f"{volume} of {product} traded @ {price} (SELF BUY)")  
                    else:
                        print(f"{volume} of {product} traded @ {price} (SELF SELL)") 



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
    
    priceLst = randomTrend(1)
    ma5 = ma(priceLst, 5)
    ma10 = ma(priceLst, 10)
    ma30 = ma(priceLst, 30)

    fig = go.Figure()
    fig.add_trace(go.Scatter(name = "price",  y=priceLst))
    fig.add_trace(go.Scatter(name = "MA5", y=ma5))
    fig.add_trace(go.Scatter(name = "MA10", y=ma10))
    fig.add_trace(go.Scatter(name = "MA30", y=ma30))

    fig.show()

main()