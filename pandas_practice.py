import pandas as pd

df=pd.read_csv("data.csv", index_col="Name")
pokemon = input("enter a pokemon name:")
try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")