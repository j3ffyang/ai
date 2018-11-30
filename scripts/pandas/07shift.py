
import pandas as pd
carriage_fin = pd.read_csv('./carriage_fin_data.csv')

# print(carriage_fin)
# shift
print(carriage_fin.shift(1))

carriage_fin = pd.read_csv('./carriage_fin_data.csv', index_col='Date')
print(carriage_fin.head())
print(carriage_fin.shift(1).head())
print(carriage_fin.shift(-1).head())

# calculate the stock price delta
carriage_fin = pd.read_csv('./carriage_fin_data.csv', index_col='Date')
carriage_fin['previous_closing_price'] = carriage_fin['Close'].shift(1)
print(carriage_fin['previous_closing_price'])

carriage_fin['closing_price_delta'] = carriage_fin['Close'] - carriage_fin['previous_closing_price']
print(carriage_fin['closing_price_delta'])

# weekly return
carriage_fin['Weekly Returns'] = ((carriage_fin['Close'] - carriage_fin['Close'].shift(7))/carriage_fin['Close'])*100
print(carriage_fin['Weekly Returns'])
