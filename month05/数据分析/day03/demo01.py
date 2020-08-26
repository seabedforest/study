import pandas as pd
data=pd.read_json('ratings.json')
print(data)

s1=data.to_json(orient='records')
s2=data.to_json(orient='index')
s3=data.to_json(orient='columns')
s4=data.to_json(orient='values')

print(s1)
print(s2)
print(s3)
print(s4)