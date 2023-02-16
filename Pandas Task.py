import pandas as pd
import numpy as np

# First Task
L = np.array([5, 10, 15, 20, 25])
ds = pd.Series(L)
print("First Task: \n", ds)

# Second Task
data = {
    "col1": [1, 2, 3, 4, 7, 11],
    "col2": [4, 5, 6, 9, 5, 0],
    "col3": [7, 5, 8, 12, 1, 11]
}
df = pd.DataFrame(data)
ds2 = pd.Series(df['col1'])  # or ds2 = df.iloc[:, 0]
print("Second Task: \n", ds2)

# Third Task
tsk3 = pd.read_csv("data.csv")
print(tsk3.head(20), "\n")

# Fourth Task
for i, j in tsk3.iterrows():
    print(i, j)
