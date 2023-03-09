# %% imports
import os
import timeit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%    sklearn imports
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering, DBSCAN, KMeans, BisectingKMeans
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
# %%    
df = pd.read_excel('student_survey_semicleaned_20230226.xlsx')
print(df)
df.to_csv('student_survey_cleaned.csv')

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
# %%    proximity measures
def isFloat(string):
    if str(string).replace(".", "").isnumeric():
        return string
    return np.nan

def isAlpha(string):
    if str(string).isalpha():
        return np.nan
    return string

df['GPA'] = df['GPA'].apply(isFloat).astype('float64')
df['Sick'] = df['Sick'].apply(isAlpha).astype('float64')
df['VideoGame'] = df['VideoGame'].apply(isFloat).astype('float64')
df['NoseLen'] = df['NoseLen'].apply(isFloat).astype('float64')

df.info()

ord_encode_city = preprocessing.OrdinalEncoder(
    categories=[['village', 
                'Z tier city', 
                'Y tier city', 
                'X tier city']])
ord_encode_edu = preprocessing.OrdinalEncoder(
    categories=[['Primary School (4th or 5th)',  
                'Middle School (8th) ',
                'High School (12th)',
                'Bachelor',
                'Masters']])

df_non_numeric = df.select_dtypes(exclude='number')
one_hot_encode = preprocessing.OneHotEncoder(handle_unknown='ignore', sparse=False, drop='first')
one_hot_encode.fit(df_non_numeric[['Gender', 'Play', 'Watch', 'Earlobes', 'Hair', 'Instrument']])

ord_encode_city.fit(df[['City']])
ord_encode_edu.fit(df[['EduMother']])

def jacquard_coeff(x, y):
    matches = np.trace(pd.crosstab(x, y))
    total = pd.crosstab(x, y).sum().sum()

    return matches/total

def distance(p, q):
    p = df.iloc[p:p+1, :]
    q = df.iloc[q:q+1, :]

    nominal = ['Gender', 'Play', 'Watch', 'Earlobes', 'Hair', 'Instrument']
    ordinal = ['EduMother', 'City']

    p['City'] = ord_encode_city.transform([p['City']])/3
    q['City'] = ord_encode_city.transform([q['City']])/3
    
    p['EduMother'] = ord_encode_city.transform([p['EduMother']])/4
    q['EduMother'] = ord_encode_city.transform([q['EduMother']])/4

    ord_dist = 0

    for ord in ordinal:
        ord_dist += abs(float(p[ord] - q[ord]))
    
    p = p.select_dtypes(exclude = 'number').drop(columns=['Tstart', 'Tend'],axis= True)
    q = q.select_dtypes(exclude = 'number').drop(columns=['Tstart', 'Tend'],axis= True)
    
    p1 = one_hot_encode.transform(p[nominal])
    q1 = one_hot_encode.transform(q[nominal])
    
    print(jacquard_coeff(p1,q1)) 
    print(ord_dist)

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
ret1 = pca.fit(df_num)

print('Components:', ret1.components_)
print('Explained variance:', ret1.explained_variance_)
# %%    PCA using all fields
columns = ['Gender', 'Age', 'Height', 'Play', 'Watch',
       'Earlobes', 'Hair', 'VideoGame', 'Physical', 'Extracurricular', 'Sick',
       'GPA', 'EduMother', 'City', 'NoseLen', 'FaceWidth', 'HeadLen',
       'RightHand', 'LeftHand', 'Instrument']
df = pd.get_dummies(df[columns])
df = SimpleImputer(missing_values=np.nan, strategy='median').fit_transform(df)
df = MinMaxScaler().fit_transform(df)

ret2 = pca.fit(df)

print('Components: ', ret2.components_)
print('Explained Variance: ', ret2.explained_variance_)
# %%    Plot scatter matrices (only numeric values)
pd.plotting.scatter_matrix(pd.DataFrame(pca.fit_transform(df_num)))
plt.suptitle('Scatter Matrix of the first 3 components of only numeric data')
plt.savefig('Q6a.png')
plt.show()
# %%    Plot scatter matrices (all fields converted)
pd.plotting.scatter_matrix(pd.DataFrame(pca.fit_transform(df)))
plt.suptitle('Scatter Matrix of the first 3 components of all fields converted')
plt.savefig('Q6b.png')
plt.show()

# %%
