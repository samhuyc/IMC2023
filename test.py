## This file is a test for python3

class Trade:
    def __init__(self, price, volume):
        self.price = price
        self.volume = volume
    
    def is_buy(self):
        return self.volume > 0

    def __repr__(self) -> str:
        return f"Trade ({self.volume} @ ${self.price})"

class TradeTracker:
    def __init__(self):
        self.trades = []
    
    def add_trade(self, trade):
        self.trades.append(trade)

    def get_buy_trades(self):
        buy_trades = []
        for trade in self.trades:
            if trade.volume > 0: 
                buy_trades.append(trade)
    
        return buy_trades
    
    def average_traded_price(self):
        total = 0
        for trade in self.trades:
            total += trade.price
        
        return total/len(self.trades)

def main():

    tracker = TradeTracker()
    tracker.add_trade(Trade(7,4))
    tracker.add_trade(Trade(10, -3))
    print(tracker.get_buy_trades())
    print(tracker.average_traded_price())

main()