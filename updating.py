import pandas as pd


data = {
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[10,20,30,65,33,23,45,35],
    "salary":[10000,20000,30000,45000,33000,23000,45000,35000],
    "Performance Score":[1,2,3,4,5,3,4,5] 
}

df=pd.DataFrame(data)

#.loc()
#df.loc[row_index,"Column Name"] = new_value
 

df.loc[0,'Salary'] = 55000
print(df)