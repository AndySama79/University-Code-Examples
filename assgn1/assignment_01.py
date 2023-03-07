#%% imports
import os
import timeit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#%% set paths and file names
datadir = '/home/schecter/Code/University/Semester4/DMPR/data'
fname = 'vehicles.csv'

#%% measure the time take to read the CSV file
t_csv_read = timeit.timeit('pd.read_csv(os.path.join(datadir, fname))', number=3, globals=globals())
print(t_csv_read)
# %%
df = pd.read_csv(os.path.join(datadir, fname))
df_clean = df.drop(['url', 'region_url', 'image_url', 'description'], axis=1)
df_clean.info()

#%%
types = ['xml', 'csv', 'json', 'excel', 'pickle', 'hdf', 'parquet', 'feather']
read_time = []
write_time = []
size = []
#%%
df.to_xml('vehicles.xml')
read_time.append(timeit.timeit("pd.read_xml('vehicles.xml')", number=3, globals=globals()))
write_time.append(timeit.timeit("df.to_xml('vehicles.xml')", number=3, globals=globals()))
size.append(os.path.getsize('vehicles.xml'))
#%%
df.to_csv('vehicles.csv')
read_time.append(timeit.timeit("pd.read_csv('vehicles.csv')", number=3, globals=globals()))
write_time.append(timeit.timeit("df.to_csv('vehicles.csv')", number=3, globals=globals()))
size.append(os.path.getsize('vehicles.csv'))
#%%
df.to_json('vehicles.json')
read_time.append(timeit.timeit("pd.read_json('vehicles.json')", number=3, globals=globals()))
write_time.append(timeit.timeit("df.to_json('vehicles.json')", number=3, globals=globals()))
size.append(os.path.getsize('vehicles.json'))
#%%
df.to_excel('vehicles.xlsx')
read_time.append(timeit.timeit("pd.read_excel('vehicles.xlsx')", number=3, globals=globals()))
write_time.append(timeit.timeit("df.to_excel('vehicles.xlsx')", number=3, globals=globals()))
size.append(os.path.getsize('vehicles.xlsx'))
#%%
df.to_pickle('vehicles.pkl')
read_time.append(timeit.timeit("pd.read_pickle('vehicles.pkl')", number=3, globals=globals()))
write_time.append(timeit.timeit("df.to_pickle('vehicles.pkl')", number=3, globals=globals()))
size.append(os.path.getsize('vehicles.pkl'))
#%%
df.to_hdf('vehicles.h5', key='df')
read_time.append(timeit.timeit("pd.read_hdf('vehicles.h5')", number=3, globals=globals()))
write_time.append(timeit.timeit("df.to_hdf('vehicles.h5', key='df')", number=3, globals=globals()))
size.append(os.path.getsize('vehicles.h5'))
#%%
df.to_parquet('vehicles.parquet')
read_time.append(timeit.timeit("pd.read_parquet('vehicles.parquet')", number=3, globals=globals()))
write_time.append(timeit.timeit("df.to_parquet('vehicles.parquet')", number=3, globals=globals()))
size.append(os.path.getsize('vehicles.parquet'))
#%%
df.to_feather('vehicles.feather')
read_time.append(timeit.timeit("pd.read_feather('vehicles.feather')", number=3, globals=globals()))
write_time.append(timeit.timeit("df.to_feather('vehicles.feather')", number=3, globals=globals()))
size.append(os.path.getsize('vehicles.feather'))
#%%
read_csv = []
write_csv = []
for idx in range(len(types)):
  read_csv.append([types[idx], read_time[idx]])
  write_csv.append([types[idx], write_time[idx], size[idx]])

read_df = pd.DataFrame(read_csv, index=None, columns=["format", "time"])
print(read_df)
write_df = pd.DataFrame(write_csv, index=None, columns=["format", "time", "size"])
print(write_df)

read_df.to_csv('read_time.csv')
write_df.to_csv('write_time.csv')
#%%
read_time = read_df['time'].to_numpy()
write_time = write_df['time'].to_numpy()
size = write_df['size'].to_numpy()

fig, ax = plt.subplots()
ax.bar(types, read_time)
ax.set_xlabel('Format')
ax.set_ylabel('Read Time')
fig.suptitle('Read Time of Formats')
fig.savefig('read.png')
plt.show()

fig, ax = plt.subplots()
ax.bar(types, write_time)
ax.set_xlabel('Format')
ax.set_ylabel('Write Time')
fig.suptitle('Write Time of Formats')
fig.savefig('write.png')
plt.show()

fig, ax = plt.subplots()
ax.bar(types, size)
ax.set_xlabel('Format')
ax.set_ylabel('Size')
fig.suptitle('Size of Formats')
fig.savefig('size.png')
plt.show()
#%%
df.columns
# %%    8) Extract some info about the dropped columns
df_clean['desc_len'] = df['description'].str.len()
df_clean['has_image'] = ~df['image_url'].isnull()

# %%    9) Scatter matrix to understand relationships
sample = df_clean.sample(1000)
# sample.columns
sample = sample.select_dtypes(exclude=['object'])
sample.drop(['id', 'has_image', 'desc_len', 'county'], axis=1, inplace=True)
sample.columns
# df.info()
pd.plotting.scatter_matrix(sample)
# %%    10) Age vs Price
df_clean['posting_date'] = pd.to_datetime(df['posting_date'], utc=True)
df_clean['age'] = df_clean['posting_date'].dt.year - df_clean['year']
# %%
fig, ax = plt.subplots()
ax.scatter(df_clean['age'], df_clean['price'])
ax.set_xlabel('Age')
ax.set_ylabel('Price')
fig.suptitle('Age v/s Price')
fig.savefig('Q10.png')
plt.show()
# %%
data = df_clean[['age', 'price']].dropna()
regr = LinearRegression()
regr.fit(data[['age']], data[['price']])
coef = regr.coef_
intercept = regr.intercept_

X = np.arange(130)
y = np.arange(130) * coef + intercept

print(X.shape)
print(y.shape)

fig, ax = plt.subplots()
ax.scatter(df_clean['age'], df_clean['price'])
ax.plot(X, np.transpose(y), color='red')
ax.set_xlabel('Age')
ax.set_ylabel('Price')
fig.suptitle(f'coefficient:{coef}, intercept:{intercept}')
fig.savefig('Q10.png')
plt.show()
# %%
import sqlite3
con = sqlite3.connect('vehicles.db')
#%%
print(timeit.timeit('df_clean.to_sql("data", con, if_exists="append")', number=1, globals=globals()))
print(os.path.getsize('vehicles.db'))
print(timeit.timeit('pd.read_sql("select * from data", con)', number=1, globals=globals()))
# %%  12) find the number of rows in df_clean
prius_data = df_clean[df_clean['model'].str.contains('prius') == True]
prius_data.query('condition == "excellent" and posting_date.dt.year >= 2021')
#%%
print(timeit.timeit("prius_data.query('model == \"prius\" and condition == \"excellent\" and posting_date.dt.year >= 2021')", number=3, globals=globals()))

# %%
query = "select * from data where condition == \'excellent\' and model like \'%prius%\' and posting_date >= \'2021-01-01\'"
pd.read_sql_query(query, con)
#%%
print(timeit.timeit("pd.read_sql_query(query, con)", number=3, globals=globals()))
# %%
con.close()

# %%
