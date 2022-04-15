import pandas as pd

data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
print(data[1])
print(data.loc[1:3])
print(data.iloc[1])
print(data.at[1])