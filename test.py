import pandas as pd    
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv("adult.data.csv")
dff = df[df['salary']=='>50K'][['native-country' , 'salary']]
count = dff['native-country'].value_counts()
print(count)