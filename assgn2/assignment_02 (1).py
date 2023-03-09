#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import timeit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


from sklearn import preprocessing
from sklearn import decomposition
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer


# In[3]:


pd.set_option('display.max_columns', None)


# In[4]:


df = pd.read_excel('student_survey_semicleaned_20230226.xlsx')
df.head()


# In[5]:


len_cols = ['FaceWidth', 'HeadLen', 'RightHand', 'LeftHand']
str_cols = ['Play', 'Watch', 'Instrument']


# In[6]:


for col in str_cols:
    df.loc[:, col] = df[col].str.lower()
    idx = df.query(f'`{col}` in ["none", "na", "n/a"]')
    if len(idx) > 0:
        df.loc[col, idx] = np.nan


# In[7]:


df[str_cols].head()


# In[8]:


print('*' * 80, '\n', df)
print('*' * 80)


# In[9]:


regex = r'(?P<num>^\d*[.]?\d*)(?P<unit> *cms*| *inch| *inches)'
length = df['FaceWidth'].str.extract(regex, expand=True)
print(length)


# In[10]:


for col in len_cols:
    length = df[col].str.extract(regex, expand=True)
    length.loc[length.unit == np.nan, 'unit'] = ''
    df.loc[:, col] = length['num'].astype(float) * np.where(length.unit.str.startswith('in'), 2.54, 1.0)


# In[11]:


df.head()


# In[12]:


def is_float(string):
    if str(string).replace(".", "").isnumeric():
        return string
    else:
        return np.nan


# In[13]:


def is_alpha(string):
    if str(string).isalpha():
        return np.nan
    else:
        return string


# In[14]:


df['GPA'] = df['GPA'].apply(is_float).astype('float64')


# In[15]:


df['Sick'] = df['Sick'].apply(is_alpha).astype('float64')


# In[16]:


df['VideoGame'] = df['VideoGame'].apply(is_float).astype('float64')


# In[17]:


df['NoseLen'] = df['NoseLen'].apply(is_float).astype('float64')


# In[18]:


df.info()


# # Data type of the columns
# 
# **For each column, specify what type of data it is: nominal, ordinal, numeric, etc.**
# 
# - **ID** : Cardinal 
# - **Tstart** : Time-Series
# - **Tend** : Time-Series
# - **Gender** : Nominal 
# - **Age** : Numerical
# - **Height** : Numerical
# - **Play** : Nominal
# - **Watch** : Nominal
# - **Earlobes** : Nominal
# - **Hair** : Nominal
# - **VideoGame** : Numerical 
# - **Physical** : Numerical
# - **Extracurricular** : Numerical
# - **Sick** : Numerical
# - **GPA** : Numerical
# - **EduMother** : Ordinal
# - **City** : Ordinal
# - **NoseLen** : Numerical
# - **FaceWidth** : Numerical
# - **HeadLen** : Numerical
# - **RightHand** : Numerical
# - **LeftHand** : Numerical
# - **Instrument** : Nominal

# # Proximity measures
# 
# **Find ways to compute proximity between values of non-numeric data.  
# Write a function distance(p, q) to compute the distance between any two data
# points p and q in this dataset.**  
# 
# If the data is not numeric then it could be either nominal, ordinal or datetime.
# 
# To compute the proximity between values of non-numeric data, we need to first encode them into a numeric representation.  
# - 

# In[19]:


non_numeric_df = df.select_dtypes(exclude='number')
non_numeric_df.head()


# For measurring proximity meassure date time is not useful we will drop them

# In[20]:


city_ordinal_encoder = preprocessing.OrdinalEncoder(
    categories=[['village', 'Z tier city', 'Y tier city', 'X tier city']]
)


# In[21]:


city_ordinal_encoder.fit(non_numeric_df[['City']])


# In[22]:


non_numeric_df['City'] = city_ordinal_encoder.transform(non_numeric_df[['City']])


# In[23]:


EduMother_ordinal_encoder = preprocessing.OrdinalEncoder(
    categories=[['Primary School (4th or 5th)',  
                'Middle School (8th) ',
                'High School (12th)',
                'Bachelor',
                'Masters']]
)


# In[24]:


EduMother_ordinal_encoder.fit(non_numeric_df[['EduMother']])


# In[25]:


non_numeric_df['EduMother'] = EduMother_ordinal_encoder.transform(non_numeric_df[['EduMother']])


# In[26]:


non_numeric_df.head()


# In[27]:


non_numeric_df['Instrument'].fillna(value='Nothing', inplace=True)
df['Instrument'].fillna(value='Nothing', inplace=True)


# In[28]:


px.histogram(non_numeric_df['Watch'].str.strip())


# In[29]:


non_numeric_df.loc[18,'Watch'] = 'cricket'
df.loc[18,'Watch'] = 'cricket'


# In[30]:


non_numeric_df.head()


# In[31]:


pd.get_dummies(non_numeric_df, columns=['Gender', 'Play', 'Watch', 'Earlobes', 'Hair', 'Instrument']).head()


# In[32]:


numeric_df = df.select_dtypes(include='number')


# In[33]:


numeric_df.head()


# # Pipelining

# In[34]:


from sklearn.pipeline import Pipeline, make_pipeline


# In[35]:


missing_imputer = ColumnTransformer([
    ('median_imputer', SimpleImputer(strategy='median'),[11,14,15,16,17,18]),
    ('constant_num_imputer', SimpleImputer(strategy='constant',fill_value=0), [7,10]),
    ('most_freq_imputer', SimpleImputer(strategy='most_frequent'), [4]),
    ('conatant_cat_imputer', SimpleImputer(strategy='constant', fill_value='Nothing'),[19])
],
    remainder='passthrough'
)


# In[36]:


ordinal_encoder = ColumnTransformer([
    ('EduMother_ordinal', preprocessing.OrdinalEncoder(
        categories=[['Primary School (4th or 5th)',  
                'Middle School (8th) ',
                'High School (12th)',
                'Bachelor',
                'Masters']]),[18]),
    ('City_ordinal', preprocessing.OrdinalEncoder(
        categories=[['village', 
                     'Z tier city', 
                     'Y tier city', 
                     'X tier city']]
    ),[19] )
],remainder='passthrough')


# In[37]:


one_hot_encoder = ColumnTransformer([
    ('one_hot', preprocessing.OneHotEncoder(drop='first', sparse=False, handle_unknown='ignore'),[10,11,12,15,16,17])
],remainder='passthrough')


# In[38]:


scaling = ColumnTransformer([
    ('Min-max_scaling', preprocessing.MinMaxScaler(),slice(0,50))
],remainder='passthrough')


# In[39]:


pipe = Pipeline([
    ('imputation', missing_imputer),
    ('ordinal encoding', ordinal_encoder),
    ('one_hot_encoding', one_hot_encoder),
    ('scaling', scaling)
                ])


# In[40]:


df.iloc[:,3:].head()


# In[41]:


pipe.fit(df.iloc[:,3:])


# In[42]:


pd.DataFrame(pipe.transform(df.iloc[:,3:])).head()


# In[43]:


df.iloc[[0] , 3:]


# In[44]:


k = pipe.transform(df.iloc[[0], 3:])


# In[45]:


k


# # Proximity measures
# 
# We mainly have 3 types of data ordinal, nominal and numeric and we have different ways to find distances

# In[46]:


p = ['Man', 20, 174.00, 'football', 'football', 'Attached', 
     'Curly', 0.0, 7.0, 8.0, 1.0, 8.65, 'Primary School (4th or 5th)', 'X tier city', 
     10.16, 15.0, 20.0, 15.0, 15.0, 'flute']


# In[47]:


q = ['Man', 20, 174.00, 'cricket', 'football', 'Attached', 
     'Curly', 0.0, 7.0, 8.0, 1.0, 8.65, 'Primary School (4th or 5th)', 'Y tier city', 
     10.16, 15.0, 20.0, 15.0, 15.0, 'None']


# In[48]:


# q = ['Man', 20, 174.00, 'football', 'football', 'Attached', 
#      'Curly', 0.0, 7.0, 8.0, 1.0, 8.65, 'Primary School (4th or 5th)', 'X tier city', 
#      10.16, 15.0, 20.0, 15.0, 15.0, 'flute']


# In[49]:


def jacquard_cofficient(x, y):
    correct_matches = np.trace(pd.crosstab(x, y))
    total = pd.crosstab(x, y).sum().sum()
    
    return correct_matches/total


# In[50]:


def manhatten_distance(x, y):
    distance = 0
    for i in range(len(x)):
        distance += abs(x[i]-y[i])
        
    return distance


# In[51]:


def distance_1(p, q):
    p = pipe.transform([p])[0]
    q = pipe.transform([q])[0]
    print(p,q)
    # for numerical we have to find the manhatten distance 
    numerical_distace = manhatten_distance(p[36:], q[36:])
    
    # for nominal column we have to find jaquard cofficient
    nominal_similarity = jacquard_cofficient(p[:36], q[:36])
    
    
    print(f'The numerical distance is {numerical_distace}')
    print(f'The nominal similarity is {nominal_similarity}')
    return numerical_distace, nominal_similarity
    


# In[52]:


distance_1(p,q)


# In[53]:


def distance_2(p, q):
    p = pipe.transform([p])[0]
    q = pipe.transform([q])[0]
    print(p,q)
    # for nominal column we have to find jaquard cofficient
    nominal_similarity = jacquard_cofficient(p[:36], q[:36])
    
    print(f'The nominal similarity is {nominal_similarity}')
    return nominal_similarity


# In[54]:


distance_2(p,q)


# # Final

# In[ ]:





# In[ ]:





# In[55]:


ohe_1 = preprocessing.OneHotEncoder(handle_unknown='ignore', sparse=False, drop = 'first')
ohe_1.fit(non_numeric_df[['Gender', 'Play', 'Watch', 'Earlobes', 'Hair', 'Instrument']])


# In[56]:


city_ordinal_encoder.fit(df[['City']])


# In[57]:


EduMother_ordinal_encoder = preprocessing.OrdinalEncoder(
    categories=[['Primary School (4th or 5th)',  
                'Middle School (8th) ',
                'High School (12th)',
                'Bachelor',
                'Masters']]
)


# In[58]:


EduMother_ordinal_encoder.fit(df[['EduMother']])


# In[59]:


# in p and q you hace to enter the index of datapoints

def distance(p, q):
    p = df.iloc[p:p+1,:]
    q = df.iloc[q:q+1,:]
    nominal = ['Gender', 'Play', 'Watch', 'Earlobes', 'Hair', 'Instrument']
    ordinal = ['EduMother', 'City']
    
    # For ordinal
    p['City'] = city_ordinal_encoder.transform([p['City']])/3
    p['EduMother'] = EduMother_ordinal_encoder.transform([p['EduMother']])/4
    q['City'] = city_ordinal_encoder.transform([q['City']])/3
    q['EduMother'] = EduMother_ordinal_encoder.transform([q['EduMother']])/4
    
    distance = 0
    
    for i in ordinal:
        distance += abs(p[i]-q[i])
    
    # For nominal
    p = p.select_dtypes(exclude = 'number').drop(columns=['Tstart', 'Tend'],axis= True)
    q = q.select_dtypes(exclude = 'number').drop(columns=['Tstart', 'Tend'],axis= True)
    
    p1 = ohe_1.transform(p[nominal])
    q1 = ohe_1.transform(q[nominal])
    
    return jacquard_cofficient(p1,q1), distance


# In[60]:


distance(1, 1)


# # Principal Component Analysis

# ## Using only the numeric fields (consider GPA to be a numeric field for this exercise)

# In[61]:


numeric_df.head()


# ID column will not be of any use to us so we will not use it

# In[62]:


numeric_df.drop(columns=['ID'], inplace=True)


# Dealing with missing values

# In[63]:


# numpy array after removing the missing values
temp1 = SimpleImputer(strategy='median').fit_transform(numeric_df)


# Scaling

# In[64]:


# printing the numpy array in form of dataframe
temp2 = pd.DataFrame(preprocessing.MinMaxScaler().fit_transform(temp1))


# In[65]:


pca = decomposition.PCA()


# In[66]:


pca_numeric = pca.fit_transform(temp2)


# In[67]:


pd.DataFrame(pca_numeric)


# ## Where all fields have been converted to numeric values

# In[68]:


all_numeric = pd.DataFrame(pipe.transform(df.iloc[:,3:]))


# In[69]:


all_numeric.head()


# In[70]:


pca_all = pca.fit_transform(all_numeric)


# In[71]:


pd.DataFrame(pca_all)


# # Plot scatter matrices

# ## Using only the numeric fields (consider GPA to be a numeric field for this exercise)

# In[72]:


pd.DataFrame(pca_numeric).iloc[:,:3]


# In[73]:


px.scatter_matrix(pd.DataFrame(pca_numeric).iloc[:,:3], title="Scatter matrix plot for numeric fields", )


# ## Where all fields have been converted to numeric values

# In[74]:


pd.DataFrame(pca_all).iloc[:,:3]


# In[75]:


px.scatter_matrix(pd.DataFrame(pca_all).iloc[:,:3], title="Scatter matrix plot for all converted numeric fields")


# In[ ]:




