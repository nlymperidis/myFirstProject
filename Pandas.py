import pandas as pd
import numpy as np

df = pd.read_csv("finance_liquor_sales.csv")
cn = df.groupby('category_name')
print(cn.first())
print(cn.aggregate(np.sum))
