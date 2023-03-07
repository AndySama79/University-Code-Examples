#%% import libraries
import numpy as np
from scipy import signal as sig
import h5py as h5
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA

#%% dummy data (inspired by the nature article)
data = pd.DataFrame(data=[[9.0, 10.0, 5.0, 6.0, 11.0, 12.0],
                           [9.5, 9.0, 6.0, 7.0, 10.0, 11.0],
                           [10.0, 11.0, 7.0, 5.0, 10.0, 9.0],
                           [7.0, 6.0, 10.0, 11.0, 12.0, 10.5],
                           [6.0, 7.0, 11.0, 10.0, 12.0, 11.0],
                           [4.0, 3.0, 8.0, 7.6, 9.0, 8.6],
                           [8.0, 8.7, 9.0, 4.3, 5.0, 4.8],
                           [10.0, 9.6, 10.2, 6.3, 5.9, 5.3],
                           [7.5, 8.0, 7.7, 2.4, 3.0, 3.1]],
                    index=['u1', 'u2', 'u3', 'v1', 'v2', 'v3',
                                    'w1', 'w2', 'w3'],
                    columns=['a', 'b', 'c', 'd', 'e', 'f'])

# %%    display the data
data.T.plot.line(subplots=True, figsize=(8, 12))
# %%    Do PCA
pca = PCA(copy=True)
ret = pca.fit(data)

print('Components:', ret.components_)
print('Explained variance:', ret.explained_variance_)

cum_exp_var = np.cumsum(ret.explained_variance_) / np.sum(ret.explained_variance_)
fig, ax = plt.subplots()
ax.plot(['pc1', 'pc2', 'pc3', 'pc4', 'pc5', 'pc6'] ,cum_exp_var)
ax.set_xlabel('Principal Component')
ax.set_ylabel('Explained Variance')
fig.suptitle('Cumulative Explained Variance')
ax.legend(['n_components=none'])
plt.savefig('Q6a.png')
plt.show()
# %%    another PCA n_components=3
pca = PCA(copy=True, n_components=3)
ret = pca.fit(data)

print('Components:', ret.components_)
print('Explained variance:', ret.explained_variance_)

# %%    plot: explined variance by principal components 
cum_exp_var = np.cumsum(ret.explained_variance_) / np.sum(ret.explained_variance_)
fig, ax = plt.subplots()
ax.plot(['pc1', 'pc2', 'pc3'], cum_exp_var)
ax.set_xlabel('Principal Component')
ax.set_ylabel('Explained Variance')
fig.suptitle('Cumulative Explained Variance')
ax.legend(['n_components=3'])
plt.savefig('Q6b.png')
plt.show()
# %%    Transform to PC axes
transformed = pca.transform(data)
print(data.shape, transformed.shape)
fig, axes = plt.subplots(nrows=transformed.shape[0], ncols=1)
for ii in range(transformed.shape[0]):
    axes[ii].plot(transformed[ii])
# %%    Scatter plot: first two PCs
df = pd.DataFrame(transformed)
fig, ax = plt.subplots()
ax.scatter(df[0], df[1], c=[0.3, 0.3, 0.3, 0.6, 0.6, 0.6, 0.9, 0.9, 0.9])
fig.suptitle('PC2 vs PC1')
plt.savefig('Q8.png')
plt.show()
# %%    Inverse transform
ori = pca.inverse_transform(transformed)
ori = pd.DataFrame(ori, index=['u1', 'u2', 'u3', 'v1', 'v2', 'v3',
                                    'w1', 'w2', 'w3'],
                    columns=['a', 'b', 'c', 'd', 'e', 'f'])

fig, axes = plt.subplots(nrows=ori.shape[0], ncols=1, figsize=(8, 12))
for ii in range(ori.shape[0]):
    axes[ii].plot(data.iloc[ii])
    axes[ii].plot(ori.iloc[ii])
    axes[ii].legend(['old', 'new'])
fig.savefig('Q9.png')
# %%    compute errors
error = data - ori
sq_error = np.mean(np.sum(error ** 2, axis=1))
print(sq_error)
print(np.sum(error ** 2, axis=1))
# %%
