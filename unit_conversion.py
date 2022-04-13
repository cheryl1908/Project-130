import pandas as pd

df=pd.read_csv("dwarf_stars.csv")
print(df.head())
print(df.columns)

df=df.dropna()
print(df.dtypes)

df["Radius"] = 0.102763*df["Radius"]
df["Mass"] = 0.000954588*df["Mass"]

print(df.head())
print(df.columns)

df.drop(['Unnamed:0'],axis=1,inplace=True)
df.reset_index(drop=True,inplace=True)

df.to_csv('unit_coverted_stars.csv')

print(df.dtypes)