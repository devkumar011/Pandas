import pandas as pd


data = {
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[10,20,30,65,33,23,45,35],
    "salary":[10000,20000,30000,45000,33000,23000,45000,35000],
    "Performance Score":[1,2,3,4,5,3,4,5] 
}
df = pd.DataFrame(data)

#display the data frame
print("Sample DataFrame")
print(df)
print("Names Single column return series")
name= df['Name']
print(name)

#selecting multiple columns 

subset = df [["Name"], "Salary"]
print('\nSubset with Name and Salary')


print(subset)