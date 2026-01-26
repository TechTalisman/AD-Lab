# This program reads employee data from a CSV file and calculates revised salaries based on years of experience

import pandas as pd

data = pd.read_csv("employee_salary_10.csv")
new_salary_list = []
 
for i in range(len(data)):
    experience = data.loc[i, "Experience"]
    salary = data.loc[i, "Salary"]

    if experience >= 5:
        new_salary = salary + (salary * 0.10)  
    else:
        new_salary = salary + (salary * 0.05)  

    new_salary_list.append(new_salary)

data["New_Salary"] = new_salary_list
print(data)
