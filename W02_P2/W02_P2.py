#%% imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% read data
data = pd.read_csv("data/netflix_titles.csv")
data.head()
# %%    Question 1

sizes = data["type"].value_counts()
labels = ["Movies", "TV Shows"]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%")
fig.suptitle("Percentage: Movies v/s TV Shows")
plt.show()
plt.savefig("Question1.jpeg")
# %%    Question 2
shows = data["country"].value_counts().head(5)
regions = shows.index.tolist()
shows = shows.tolist()
shows.reverse()
regions.reverse()

fig, ax = plt.subplots()
ax.bar(regions, shows)
fig.suptitle("Top 5 regions having the highest number of shows")
ax.set_xlabel("Regions -->")
ax.set_ylabel("Total number of shows -->")
plt.show()
plt.savefig("Question2.jpeg")

# %%    Question 3

# %%    Question 4

# %%    Question 5
