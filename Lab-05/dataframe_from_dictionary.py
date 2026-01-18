# This program creates a Pandas DataFrame from a dictionary and displays it.

import pandas as pd

n = int(input("Enter number of records: "))

names = []
ages = []

for i in range(n):
    names.append(input("Enter name: "))
    ages.append(int(input("Enter age: ")))

data = {'Name': names, 'Age': ages}

print("\nDictionary:")
print(data)

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)
