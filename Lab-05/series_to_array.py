# a Pandas program to convert a given Series to a NumPy array

import pandas as pd

n = int(input("Enter number of elements: "))
data = []

for i in range(n):
    data.append(int(input("Enter value: ")))

s = pd.Series(data)
print("\nPandas Series:")
print(s)
arr = s.to_numpy()
print("\nConverted NumPy Array:")
print(arr)
