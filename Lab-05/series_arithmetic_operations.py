# This program creates two pandas Series from user input and performs element-wise arithmetic operations (addition, subtraction, multiplication, and division).

import pandas as pd

n = int(input("Enter number of elements: "))

list1 = []
list2 = []

print("Enter elements for Series 1:")
for i in range(n):
    list1.append(int(input()))

print("Enter elements for Series 2:")
for i in range(n):
    list2.append(int(input()))

s1 = pd.Series(list1)
s2 = pd.Series(list2)

print("\nSeries 1:")
print(s1)
print("Series 2:")
print(s2)

print("\nAddition:")
print(s1 + s2)
print("\nSubtraction:")
print(s1 - s2)
print("\nMultiplication:")
print(s1 * s2)
print("\nDivision:")
print(s1 / s2)
