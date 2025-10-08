import pandas as pd

import pandas as pd

data={
    "Nmae":['Ram','Shyam','Ghanshyam'],
    "Age":[10,20,30],
    }
df  = pd.DataFrame(data)
print(df)

print("Displaying the info of data set")
print(df.info())