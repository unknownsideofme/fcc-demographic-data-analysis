dff = df[df['salary']=='>50K'][['native-country' , 'salary']]
count = dff['native-country'].value_counts()
print(count.idxmax())