from typing import *
from datamodel import *

class Trader:

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        result = {}

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

        return result