
import pandas as pd
carriage_fin = pd.read_csv('./carriage_fin_data.csv', index_col='Date')
carriage_fin['Weekly Returns'] = ((carriage_fin['Close'] - carriage_fin['Close'].shift(7))/carriage_fin['Close'])*100
print(carriage_fin['Weekly Returns'])

carriage_fin.to_csv('./carriage_fin_generated.csv')
# carriage_fin.to_csv('./carriage_fin_generated_col_selected.csv', columns = ['Volume', 'Weekly Returns'])
