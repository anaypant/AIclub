import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv('Food Dataset Generic.csv')
index = (df["Food Type"].value_counts())
values = (df["Food Type"].value_counts())
index = list(index.index)
values = list(values.values)


plt.bar(index, values)
plt.title("Distribution of Dataset before personalization.")
plt.xlabel("Type of Food")
plt.ylabel("Amount of samples")
plt.show()