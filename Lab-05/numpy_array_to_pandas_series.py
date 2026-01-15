# a Pandas program to convert a NumPy array to a Pandas Series

import numpy as np
import pandas as pd

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input("Enter value: ")))

np_array = np.array(arr)
print("\nNumPy Array:")
print(np_array)

series = pd.Series(np_array)
print("\nPandas Series:")
print(series)
