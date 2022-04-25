import pandas as pd

df2 = pd.DataFrame({
    'country': ['France', 'USA', 'Ukrane', 'Russia', 'Italy', 'Great Britain', 'Germany'],
    'capital': ['Paris', 'Washington', 'Kiev', 'Moscow', 'Roma', 'London', 'Berlin'],
    'population': [66.99, 328.2, 41.98, 145.97, 62, 68, 83]
},
    index=['fr', 'us', 'ua', 'ru', 'it', 'uk', 'de'])

print(df2)
print(df2.loc[['us'], ['capital', 'country']])
print(df2.iloc[1, 1])
