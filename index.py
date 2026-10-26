import pandas as pd

df = pd.read_csv("data.csv")
print(df)
grouped = df.groupby('category') ['quantity'].sum()
print(grouped)

total_sale = df['quantity'].sum()
print("Total sale:", total_sale)
print(pd)

