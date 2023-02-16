import pandas as pd
import numpy as np

data = pd.read_csv('Matplotlib/1.supermarket.csv')

print(data.columns,'\n')

x = data.groupby('item_name')
x = x.sum()
print(x.head())
