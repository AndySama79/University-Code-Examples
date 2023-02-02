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
y_movie = movies.groupby('year').size()
m_movie = movies.groupby('month').size()

y_show = shows.groupby('year').size()
m_show = shows.groupby('month').size()

year = data.groupby('year').size()
month = data.groupby('month').size()

year_x1 = year.index.tolist()
month_x1 = month.index.tolist()

year_x2 = y_show.index.tolist()
month_x2 = m_show.index.tolist()

year_x3 = y_movie.index.tolist()
month_x3 = m_movie.index.tolist()

#   Year-Wise distribution
fig, ax = plt.subplots()
ax.plot(year_x2, y_show)
ax.plot(year_x3, y_movie)
ax.plot(year_x1, year)
ax.set_xlabel("year -->")
ax.set_ylabel("Movies/TV Shows -->")
ax.legend(["TV Shows", "Movies", "Total Shows"], loc="upper right")
fig.suptitle("Year-wise distribution")
plt.tight_layout()
plt.savefig("Question4a.png")
plt.show()

#   Month-Wise distribution
fig, ax = plt.subplots()
ax.plot(month_x2, m_show)
ax.plot(month_x3, m_movie)
ax.plot(month_x1, month)
ax.set_xlabel("month -->")
ax.set_ylabel("Movies/TV Shows -->")
ax.legend(["TV Shows", "Movies", "Total Shows"], loc="upper right")
fig.suptitle("Month-wise distribution")
plt.tight_layout()
plt.savefig("Question4b.png")
plt.show()
# %%    Question 5

