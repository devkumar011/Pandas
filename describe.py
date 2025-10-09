#step1 samplw data frame

#what is describe function
#The describe() method in pandas is used to generate a summary of statistical information about your DataFrame or Series.
#It gives a quick overview of your data by showing key statistics such as count, mean, standard deviation, minimum, 25%, 50%, 75%, and maximum values for all numerical columns.



import pandas as pd

data = {
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[10,20,30,65,33,23,45,35],
    "salary":[10000,20000,30000,45000,33000,23000,45000,35000],
    "Performance Score":[1,2,3,4,5,3,4,5] 
}

df = pd.DataFrame(data)
print("Sample DataFrame")
print(df )
print("Descriptive Statistics")
print(df.describe())