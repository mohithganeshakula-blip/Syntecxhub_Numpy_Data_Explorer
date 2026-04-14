

#task 2

#Read csv

import pandas as pd

data = pd.read_csv("E-commers.csv")
print(data.head())

#Tail

print(data.tail())

#types
print("Data types")
print(data.dtypes)
print(" ")

#statistics
print("Mean")
print(data.mean(numeric_only=True))
print(" ")
#median
print("Median")
print(data.median(numeric_only=True))
print(" ")
#min
print("Min")
print(data.min(numeric_only=True))
print(" ")
#max
print("Max")
print(data.max(numeric_only=True))
print(" ")
#count
print("Count")
print(data.count())

print(" ")

#Filter 
print("Filter_data")

filtered=[(data["price"]>500)&(data["quantity"]>2)]

print(filtered)

#revnue

data["revnue"]=data["price"]*data["quantity"]

#Result

result=data.groupby("state")[["revnue"]].sum()
print(result)

#creating the dataset
print("To_csv")
state=result.to_csv("State_Wise_Revenue.csv",index=False)
print(state)

print(result)
