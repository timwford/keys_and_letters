import pandas as pd

data = pd.read_csv("data_dvorak.csv")

left = ['p','y','a','o','e','u','i','q','j','k','x','f']
right = ['g','c','r','l','d','h','t','n','s','b','m','w','v','z']

print(data.head())
print("left:")
print(data[data['letter'].isin(left)])
print("\n\nright:")
print(data[data['letter'].isin(right)])

right = data[data['letter'].isin(right)]
left = data[data['letter'].isin(left)]

leftWeighted = data['distance_from_home_row'] 
leftBlah = left['percent']

print(leftBlah)
print(leftWeighted)
print(left['percent'].sum())
print(right['percent'].sum())

print(set(left['letter'].to_list()) & set(right['letter'].to_list()))
print(right['percent'].sum() + left['percent'].sum())

import matplotlib.pyplot as plt

labels = 'left', 'right'
sizes = [left['percent'].sum(), right['percent'].sum()]
explode = (0.1, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()