import pandas as pd

data = {
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[10,20,30,65,33,23,45,35],
    "salary":[10000,20000,30000,45000,33000,23000,45000,35000],
    "Performance Score":[1,2,3,4,5,3,4,5] 
}

df=pd.DataFrame(data)
print(df)

df['Bonus'] = df['salary'] * 0.1
print(df) 

#using insert() method 
#df.insert(loc, " Column_Nmae", some_data)

df.insert(0, "Employee ID", [10,20,30 ,40,50,60,70,80])
print(df)