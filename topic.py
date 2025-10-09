"""1-how big is your data
2-what are the name of coluns
shape and column
"""


import pandas as pd

data = {
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[10,20,30,65,33,23,45,35],
    "salary":[10000,20000,30000,45000,33000,23000,45000,35000],
    "Performance Score":[1,2,3,4,5,3,4,5] 
}

df=pd.DataFrame(data)
print(f'Shape: {df.shape}')
print(f'Columns Nmaes: {df.columns}')