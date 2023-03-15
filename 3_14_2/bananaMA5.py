from typing import *
from datamodel import *

import numpy as np
import pandas as pd


class Trader:

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        global prices
        prices = []
        result = {}

        for product in state.order_depths.keys():
            if product == 'BANANAS':
                bTrades = state.market_trades[product]
                numTrade = 0
                sumPrice = 0
                while numTrade < len(bTrades):
                    tradePrice = bTrades[numTrade].price
                    sumPrice += tradePrice
                    numTrade += 1
                if numTrade > 0:
                    prices.append(sumPrice/numTrade)
                    ma5 = ma(prices,5)
                    acceptable_price = ma5[len(ma5)-1]
                else:
                    acceptable_price = 0

                order_depth = state.order_depths[product]
                orders = []

                if len(order_depth.sell_orders) > 0:
                    best_ask = min(order_depth.sell_orders.keys())
                    best_ask_volume = order_depth.sell_orders[best_ask]
                    if best_ask < acceptable_price:
                        orders.append(Order(product, best_ask, -best_ask_volume))

                if len(order_depth.buy_orders) != 0:
                    best_bid = max(order_depth.buy_orders.keys())
                    best_bid_volume = order_depth.buy_orders[best_bid]
                    if best_bid > acceptable_price:
                        orders.append(Order(product, best_bid, -best_bid_volume))

                result[product] = orders              

##show trade
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
##
        return result

##moving average
def ma(lst, windowSize):
    ma = []
    for i in range(len(lst)):
        if i < windowSize-1:
            windowAvg = int(np.sum(lst[0:i+1])/(i+1))
        else:
            windowAvg = int(np.sum(lst[i-(windowSize-1):i+1])/windowSize)
        ma.append(windowAvg)
    return ma
##

