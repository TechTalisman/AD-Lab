# to convert Pandas Series of lists into a single flattened Series

import pandas as pd

n = int(input("Enter number of lists: "))
data = []

for i in range(n):
    lst = list(map(int, input("Enter list elements separated by space: ").split()))
    data.append(lst)

s = pd.Series(data)
print("\nOriginal Series:")
print(s)

new_s = s.explode()
print("\nConverted Single Series:")
print(new_s)
