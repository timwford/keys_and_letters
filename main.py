import pandas as pd

data = pd.read_csv("data.csv")

left = ['a','s','d','f','q','w','e','r','t','g','z','x','c','v']
right = ['y','u','i','o','p','h','j','k','l','b','n','m']

print(data.head())
print("left:")
print(data[data['letter'].isin(left)])
print("\n\nright:")
print(data[data['letter'].isin(right)])

right = data[data['letter'].isin(right)]
left = data[data['letter'].isin(left)]

print(left['percent'].sum())
print(right['percent'].sum())

print(set(left['letter'].to_list()) & set(right['letter'].to_list()))
print(right['percent'].sum() + left['percent'].sum())
