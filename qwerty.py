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

import matplotlib.pyplot as plt

labels = 'left', 'right'
sizes = [left['percent'].sum(), right['percent'].sum()]
explode = (0.1, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()