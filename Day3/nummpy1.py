import numpy as np

stock_prices=np.random.uniform(100,500,size=(30,5)).astype(int)
print(stock_prices)

avg_ma=np.mean(stock_prices,axis=0).round(2)
max_val=np.max(stock_prices)
max_day,max_com=np.unravel_index(np.argmax(stock_prices),stock_prices.shape)
print("\n2. Highest Stock Price Recorded:")
print(f"Highest price recorded: {max_val}, At Day {max_day+1}, Company of {max_com+1}")

min_price=np.min(stock_prices)
max_price=np.max(stock_prices)
normalized_prices=(stock_prices-min_price)/(max_price-min_price)
print(normalized_prices)
