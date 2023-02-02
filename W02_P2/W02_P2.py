#%% imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%% read data
data = pd.read_csv("data/netflix_titles.csv")
data.head()
# %%    Question 1

sizes = data["type"].value_counts()
labels = ["Movies", "TV Shows"]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%")
fig.suptitle("Percentage: Movies v/s TV Shows")
plt.savefig("Question1.png")
plt.show()

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
plt.savefig("Question2.png")
plt.show()

# %%    Question 3
data["date_added"] = pd.to_datetime(data["date_added"])
data["year"] = data["date_added"].dt.year#.astype(dtype="int")
data["month"] = data["date_added"].dt.month#.astype(dtype="int")

movies = data[data["type"] == "Movie"]
shows = data[data["type"] == "TV Show"]

movie_pivot = pd.pivot_table(movies, index=["month"], columns=["year"], aggfunc='count')["date_added"]
show_pivot = pd.pivot_table(shows, index=["month"], columns=["year"], aggfunc='count')["date_added"]

movie_heat = sns.heatmap(movie_pivot).set_title("Movie Heatmap")
plt.show()

show_heat = sns.heatmap(show_pivot).set_title("TV Show Heatmap")
plt.show()

# %%    Question 4


# %%    Question 5
