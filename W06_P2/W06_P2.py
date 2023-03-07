#%% imports
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering, DBSCAN, KMeans, BisectingKMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from kneed import KneeLocator

#%% load data
basedir = '/home/schecter/Code/university/Semester4/DMPR/assignments/W06_P2/data/'
fname = 'student_survey_semicleaned_20230226.xlsx'
df = pd.read_excel(os.path.join(basedir, fname))
# %%    keep only the numeric columns
df = df[['VideoGame', 'Sick', 'GPA', 'Extracurricular',
'Physical', 'NoseLen', 'FaceWidth', 'Height', 'HeadLen',
'RightHand', 'LeftHand']].copy()

print(df.columns)
len_cols = ['FaceWidth', 'HeadLen', 'RightHand', 'LeftHand']
# %%    regex magic to cleanup units
regex = r'(?P<num>^\d*[.]?\d*)(?P<unit> *cms*| *inch| *inches)'
for col in len_cols:
    length = df[col].str.extract(regex, expand=True)
    length.loc[length.unit == np.nan, 'unit'] = ''
    df.loc[:, col] = length['num'].astype(float) * np.where(length.unit.str.startswith('in'), 2.54, 1.0)

# %%    Try to convert each column into numeric-donverting entries to 'float'
for col in df.columns:
    df.loc[:, col] = pd.to_numeric(df[col], errors='coerce', downcast='float')

# %% impute missing values by mean
da = SimpleImputer(missing_values=np.nan, strategy='mean').fit_transform(df)
# %%    scale the features for 0 mean and 1 variance
da = StandardScaler().fit_transform(da)

# %%    Single kmeans clustering
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=None)
kmeans_fit = kmeans.fit(da)
inertia = kmeans_fit.inertia_
cluster_centers = kmeans_fit.cluster_centers_
labels = kmeans_fit.labels_

df['cluster'] = labels
#%%
print(df)
#%%
print(inertia)
#%%
print(cluster_centers)
#%%
print(labels)
# %%    series of kmeans clustering with k=1 to 10
inertias = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=None)
    kmeans_fit = kmeans.fit(da)
    inertias.append(kmeans_fit.inertia_)

#%% Now plot the inertia against the number of clusters
fig, ax = plt.subplots()
ax.plot(np.arange(1, 11), inertias)
ax.set_ylabel('Inertia')
ax.set_xlabel('Clusters')
fig.suptitle('Inertia v/s Cluster')
plt.savefig('Q7.png')
plt.show()

#%% Use the KneeLocator class from the kneed module to find the elbow
kl = KneeLocator(np.arange(1, 11), inertias, curve='convex', direction='decreasing')
print(kl.knee)

#%% Now carry out PCA to project the data into 3 dimensions and create a scatter matrix of the pariwis components
pca = PCA(n_components=3)
ret = pca.fit(da)
transform = pca.transform(da)
transform_df = pd.DataFrame(transform, columns=['pca1', 'pca2', 'pca3'])
axes = pd.plotting.scatter_matrix(transform_df, c=df['cluster'])
print(axes)
#%% Indicate the cluster of each point by overlaying a marker with a different color
