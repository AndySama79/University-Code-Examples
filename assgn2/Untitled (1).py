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


print('*' * 80, '\n', df)
print('*' * 80)


# In[8]:


regex = r'(?P<num>^\d*[.]?\d*)(?P<unit> *cms*| *inch| *inches)'
length = df['FaceWidth'].str.extract(regex, expand=True)


# In[9]:


for col in len_cols:
    length = df[col].str.extract(regex, expand=True)
    length.loc[length.unit == np.nan, 'unit'] = ''
    df.loc[:, col] = length['num'].astype(float) * np.where(length.unit.str.startswith('in'), 2.54, 1.0)


# In[10]:


def is_float(string):
    if str(string).replace(".", "").isnumeric():
        return string
    else:
        return np.nan


# In[11]:


def is_alpha(string):
    if str(string).isalpha():
        return np.nan
    else:
        return string


# In[12]:


df['GPA'] = df['GPA'].apply(is_float).astype('float64')
df['Sick'] = df['Sick'].apply(is_alpha).astype('float64')
df['VideoGame'] = df['VideoGame'].apply(is_float).astype('float64')
df['NoseLen'] = df['NoseLen'].apply(is_float).astype('float64')


# In[13]:


df.info()


# In[15]:


df_non_num = df.select_dtypes(exclude='number')
df_non_num.head()


# In[16]:


city_ordinal_encoder = preprocessing.OrdinalEncoder(
    categories=[['village', 
                 'Z tier city', 
                 'Y tier city', 
                 'X tier city']]
)


# In[17]:


EduMother_ordinal_encoder = preprocessing.OrdinalEncoder(
    categories=[['Primary School (4th or 5th)',  
                'Middle School (8th) ',
                'High School (12th)',
                'Bachelor',
                'Masters']]
)


# In[18]:


one_hot = preprocessing.OneHotEncoder(handle_unknown='ignore', sparse=False, drop = 'first')
one_hot.fit(non_numeric_df[['Gender', 'Play', 'Watch', 'Earlobes', 'Hair', 'Instrument']])


# In[19]:


city_ordinal_encoder.fit(df[['City']])


# In[20]:


EduMother_ordinal_encoder.fit(df[['EduMother']])


# In[21]:


def jacquard_cofficient(x, y):
    correct_matches = np.trace(pd.crosstab(x, y))
    total = pd.crosstab(x, y).sum().sum()
    
    return correct_matches/total


# In[62]:


def distance(p, q):
    p = df.iloc[p:p+1,:]
    q = df.iloc[q:q+1,:]
    
    nominal = ['Gender', 'Play', 'Watch', 'Earlobes', 'Hair', 'Instrument']
    ordinal = ['EduMother', 'City']
    
    p['City'] = city_ordinal_encoder.transform([p['City']])/3
    q['City'] = city_ordinal_encoder.transform([q['City']])/3
    
    p['EduMother'] = EduMother_ordinal_encoder.transform([p['EduMother']])/4
    q['EduMother'] = EduMother_ordinal_encoder.transform([q['EduMother']])/4
    
    ordinal_distance = 0
    
    for i in ordinal:
        ordinal_distance += abs(float(p[i])-float(q[i]))
    
    p = p.select_dtypes(exclude = 'number').drop(columns=['Tstart', 'Tend'],axis= True)
    q = q.select_dtypes(exclude = 'number').drop(columns=['Tstart', 'Tend'],axis= True)
    
    p1 = one_hot.transform(p[nominal])
    q1 = one_hot.transform(q[nominal])
    
    print(jacquard_cofficient(p1,q1)) 
    print(ordinal_distance)


# In[63]:


distance(1, 2)


# In[ ]:





# In[ ]:




