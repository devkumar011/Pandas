import pandas as pd

data = {
    "Name":['Ram',None ,'Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[10,None,30,65,33,23,45,35],
    "salary":[10000,None,30000,45000,33000,23000,45000,35000],
    "Performance Score":[1,None,3,4,5,3,4,5] 
}

df = pd.DataFrame(data)

print(df)

df.dropna(0 , inplace=True)
print(df)