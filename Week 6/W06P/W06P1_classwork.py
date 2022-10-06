# %% imports
import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt

# %% load data
data = datasets.load_iris(as_frame=True)
df = data.data.copy()
# Print the column names
print('Original columns', df.columns.values)
# Rename columns (creating a new df)
df = df.rename(columns={'sepal length (cm)': 'slength',
                        'sepal width (cm)': 'swidth',
                        'petal length (cm)': 'plength',
                        'petal width (cm)': 'pwidth'})
print('After renaming', df.columns.values)

# %% Scatter plot with pandas
df.plot.scatter(x='slength', y='plength')
fname = 'slen_plen_pandas.png'
plt.savefig(fname)
fname

# %% Scatter plot with matplotlib
fig, ax = plt.subplots()
ax.scatter(df.slength, df.plength)
ax.set_xlabel('Sepal length')
ax.set_ylabel('Petal length')
fname = 'slen_plen_mpt.png'
plt.savefig(fname)
fname

# %% Petal width vs. Sepal width
fig, ax = plt.subplots()
ax.scatter(df.swidth, df.pwidth, marker="^", s=3, color="orange")
ax.set_xlabel('Sepal width')
ax.set_ylabel('Petal width')
fname = 'swidth_pwidth_plot.png'
plt.savefig(fname)

# %% Scatterplot matrix
pd.plotting.scatter_matrix(df)
fname = 'iris_scatter_matrix.png'
plt.savefig(fname)

## the diagonal entries represent the histogram of each variable

# %% 3D plotting
fig, ax = plt.figure(), plt.axes(projection='3d')

ax.scatter(df.slength, df.swidth, df.plength, marker="^", color="blue", s=3)
ax.scatter(df.slength, df.swidth, df.pwidth, marker="o", color="orange", s=3)

ax.set_xlabel("Sepal length")
ax.set_ylabel("Sepal width")
ax.set_zlabel("Petal length/width")
fig.tight_layout()

ax.legend(["Petal length", "Petal width"])
plt.savefig("iris_3d.png")

# %% Visualizing with color maps
x = np.arange(-5, 25)
y = np.arange(5, 20)
X, Y = np.meshgrid(x, y)
Z = np.cos(X / np.pi) - np.sin(Y / np.pi)

fig, ax = plt.subplots()
s = ax.pcolormesh(X, Y, Z, cmap='viridis')
fig.colorbar(s, ax=ax)

fname = 'colormesh_plot.png'
plt.savefig(fname)
