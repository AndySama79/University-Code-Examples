#%% imports
import os
import timeit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%    sklearn imports
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering, DBSCAN, KMeans, BisectingKMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
#%% read data and cleanup
df = pd.read_excel('student_survey_semicleaned_20230226.xlsx')
print(df)

# %%    cleanup data programmatically
len_cols = ['FaceWidth', 'HeadLen', 'RightHand', 'LeftHand']
str_cols = ['Play', 'Watch', 'Instrument']

#   convert all string columns to lowercase
for col in str_cols:
    df.loc[:, col] = df[col].str.lower()
    idx = df.query(f'`{col}` in ["none", "na", "n/a"]')
    if len(idx) > 0:
        df.loc[col, idx] = np.nan

print('*' * 80, '\n', df)
print('*' * 80)

# %%    regex magic to cleanup units
regex = r'(?P<num>^\d*[.]?\d*)(?P<unit> *cms*| *inch| *inches)'
length = df['FaceWidth'].str.extract(regex, expand=True)
print(length)

for col in len_cols:
    length = df[col].str.extract(regex, expand=True)
    length.loc[length.unit == np.nan, 'unit'] = ''
    df.loc[:, col] = length['num'].astype(float) * np.where(length.unit.str.startswith('in'), 2.54, 1.0)
# %%    data type of columns
print(df.info())
print(df.columns)

# %%


# %%    PCA using only the numeric fields
num_fields = ['Age', 'Height', 'VideoGame', 'Physical', 'Extracurricular', 'Sick', 'GPA', 'NoseLen', 'FaceWidth', 'HeadLen', 'RightHand', 'LeftHand']
non_num_fields = list(set(df.columns) - set(num_fields))
fields = num_fields + non_num_fields

df_num = df[num_fields]

for col in num_fields:
    df_num[col] = pd.to_numeric(df_num[col], errors='coerce')

df_num = SimpleImputer(missing_values=np.nan, strategy='median').fit_transform(df_num)
df_num = StandardScaler().fit_transform(df_num)

pca = PCA(copy=True, n_components=3)
ret = pca.fit(df_num)

print('Components:', ret.components_)
print('Explained variance:', ret.explained_variance_)
# %%    PCA using all fields
df_non_num = pd.get_dummies(df[non_num_fields])
df_final = pd.merge(df_num, df_non_num)
df_final

# %%
