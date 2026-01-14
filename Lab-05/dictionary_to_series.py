# to convert a user-defined dictionary into a Pandas Series using Pandas library

import pandas as pd

n = int(input("Enter number of elements: "))
data = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

print("\nDictionary:")
print(data)
s = pd.Series(data)
print("\nConverted Pandas Series:")
print(s)
