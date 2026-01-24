# This program reads student marks from a CSV file, calculates total and average marks, and determines pass or fail result

import pandas as pd

data = pd.read_csv("student_marks_10.csv")

data["Total"] = data["Maths"] + data["Science"] + data["English"]
data["Average"] = data["Total"] / 3
data["Average"] = data["Average"].round(2)

result_list = []

for avg in data["Average"]:
    if avg >= 50:
        result_list.append("Pass")
    else:
        result_list.append("Fail")

data["Result"] = result_list
print(data)
