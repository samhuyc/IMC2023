from typing import *
from datamodel import *

class Trader:

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        result = {}
        print("")
        print(f"timestamp = {state.timestamp}")
        print("")

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

        return result

'''
        for product in ["PEARLS", "BANANAS"]:
            if product in state.order_depths:
                order_depth = state.order_depths[product]
                if product in state.position:
                    print(f"{product} position {state.position[product]}")
                if len(order_depth.sell_orders) > 0:
                    best_ask = min(order_depth.sell_orders.keys())
                    best_ask_volume = order_depth.sell_orders[best_ask]
                    print(f"{product} best ask is {best_ask} at quantity {best_ask_volume}")
                if len(order_depth.buy_orders) > 0:
                    best_bid = min(order_depth.buy_orders.keys())
                    best_bid_volume = order_depth.sell_orders[best_bid]
                    print(f"{product} best ask is {best_bid} at quantity {best_bid_volume}")
'''