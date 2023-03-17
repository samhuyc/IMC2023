# IMC2023
this git repo is for IMC prosperity challenge


# /3_14_2/bananaMA5    
### moving average mean reversion strategy
### simple moving average: okay frequency, low performance
- review order & trades
- better input for trade price, print current MA5
- test MA10, MA20, MA50, etc.
- fix positional limit
- Exponential, Cumulative, volume weighted ?

# /3_16_1/naiveResting
### simoutaneously send resting buys & sells orders; total directional movement + current inventory = 20 (full movement every iteration) 
### price/volume scaler determined by a constant vector * movement
- yields positive in both pearls and banana but underwhelming performance
- need a better log output---according to discord, the state.market_trades(); state.own_trades() have bugs, resulting in previous trades show up multiple times
- now is market volume, historical trade naive, need to incorporate; change scalers reacting to previous volume
- delta - neutral volume?


# Ideas: 
- momentum strat
- combination mean reversion + momentum (switch between volatility = standard dev.)

	