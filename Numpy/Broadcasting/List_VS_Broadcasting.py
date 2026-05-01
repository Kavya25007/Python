#Solve a problem through loops vs Broadcasting

#Through Loops
prices = [100, 120 , 300, 400]
discount = 10

final_prices = []

for price in prices:
    final_price =price - (price*discount/100)
    final_prices.append(final_price)

print(final_prices)

#Through Broadcasting
import numpy as np
prices = np.array([100, 120, 300 , 400])
discount = 10

final_prices = prices - (prices * discount / 100)
print(final_prices)
