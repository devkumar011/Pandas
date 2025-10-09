import pandas as pd


data = {
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[10,20,30,65,33,23,45,35],
    "salary":[10000,20000,30000,45000,33000,23000,45000,35000],
    "Performance Score":[85,90,78,92,88,95,80,89] 
}
df = pd.DataFrame(data)
   
high_salary = df[df['salary']>50000]
print('Employees with salary > 50000')
print(high_salary)

filtered = df[(df['salary']>20000) & (df['Age']>30)]
print('Employees with salary > 50000 and Age > 30')
print(filtered)

# using or condition
filtered_or = df[(df['Age']>35) | (df['Performance Score']>90)]
print ('Employees older than 35 OR performance score > 90')
print(filtered_or)