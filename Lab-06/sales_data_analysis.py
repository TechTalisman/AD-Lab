# This program analyzes sales data to compute total and average sales per product using groupby

import pandas as pd
data = pd.read_csv("sales_data_10.csv")

result = data.groupby("Product")["Sales"].agg(
    Total_Sales="sum",
    Average_Sales="mean"
)
 
result["Average_Sales"] = result["Average_Sales"].round(2)
print(result)
