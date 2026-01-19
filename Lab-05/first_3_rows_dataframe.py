# Program to get the first 3 rows of a given Pandas DataFrame

import pandas as pd

n = int(input("Enter number of rows: "))
data = []

for i in range(n):
    data.append(int(input("Enter value: ")))

df = pd.DataFrame({'Values': data})
print("\nOriginal DataFrame:")
print(df)

print("\nFirst 3 Rows:")
print(df.head(3))
