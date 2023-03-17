from typing import *
from datamodel import *
import numpy as np
import pandas as pd


class Trader:

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        global prices
        prices = []
        result = {}

        self.showTrades(state) 
        for product in state.position.keys():
            print(f"position: {product} {state.position[product]}")
            

        for product in state.order_depths.keys():
            if product == 'BANANAS': 
                inventory = 0
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
                    resting_prices = [round(p * spread+best_bid) for p in premium_interval]
                    volume_scaler = [0.7, 0.3, -0.3, -0.7]
                    resting_volumes = [round(0.7*(20-inventory)), round(0.3*(20-inventory)), 
                                       round(-0.3*(20+inventory)), round(-0.7*(20+inventory))]

                    orders = self.sendOrders(product, resting_prices, resting_volumes)
                    result[product] = orders  
                


            if product == 'PEARLS': 
                inventory = 0
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
                    resting_prices = [round(p * spread+best_bid) for p in premium_interval]
                    volume_scaler = [0.7, 0.3, -0.3, -0.7]
                    resting_volumes = [round(0.7*(20-inventory)), round(0.3*(20-inventory)), 
                                       round(-0.3*(20+inventory)), round(-0.7*(20+inventory))]

                    orders = self.sendOrders(product, resting_prices, resting_volumes)
                    result[product] = orders  

        print("="*50)
        return result
           
###take a list of prices, volumes of a product into orders
    def sendOrders(self, product, prices, volumes):
        orders = []
        for i in range(len(prices)):
            order = Order(product, prices[i], volumes[i])
            print(order)
            orders.append(order)
        return orders
        
###show trades method to be called in Trade::run()
    def showTrades(self, state: TradingState) :  
        print("")  
        for product in ["BANANAS", "PEARLS"]:
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
