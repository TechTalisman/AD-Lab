import pandas as pd

data = pd.read_csv("missing_marks_10.csv")

print("Missing values:")
print(data.isnull())
 
mean_marks = data["Marks"].mean()

data["Marks"] = data["Marks"].fillna(mean_marks)

print("\nFinal Output:")
print(data)
