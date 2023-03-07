#%% imports
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
#%% read data and convert to csv
datadir = '/home/schecter/Code/University/Semester4/DMPR/assignments/W05_P2/data'
fname = 'student_data.xlsx'
df = pd.read_excel(os.path.join(datadir, fname))
df.to_csv(os.path.join(datadir, 'student_data.csv'))
df.head()
# %%
fname_clean = 'student_data_clean.xlsx'
df_clean = pd.read_excel(os.path.join(datadir, fname_clean))
df_clean.to_csv(os.path.join(datadir, 'student_data_clean.csv'))
df_clean.head()

# %%
df_clean.info()
# %%
hola = pd.read_csv(os.path.join(datadir, 'hola.csv'))
hola.head()
# %% Q3)B)
def jaccard_similarity(obj1, obj2):
    if len(obj1) == 0 or len(obj2) == 0:
        return 0
    intersection = len(obj1.intersection(obj2))
    union = len(obj1.union(obj2))
    return intersection / union

#%% Q3)C)
instruments = ["guitar", "keyboard", "drums", "mouth organ", "piano", "ukelele"]
dataset = []
guitar = hola["Guitar"].to_numpy()
keyboard = hola["Keyboard"].to_numpy()
drums = hola["Drums"].to_numpy()
mouth_organ = hola["Mouth Organ"].to_numpy()
piano = hola["Piano"].to_numpy()
ukelele = hola["Ukelele"].to_numpy()
temp = []
for i in range(len(hola)):
    if guitar[i] == 1:
        temp.append("guitar")
    if keyboard[i] == 1:
        temp.append("keyboard")
    if drums[i] == 1:
        temp.append("drums")
    if mouth_organ[i] == 1:
        temp.append("mouth_organ")
    if piano[i] == 1:
        temp.append("piano")
    if ukelele[i] == 1:
        temp.append("ukelele")

    dataset.append(set(temp))
    temp = []
print(dataset)

#%% 
similarity_scores = []
for i in range(len(dataset)):
    for j in range(len(dataset)):
        if i < j:
            jaccard_score = jaccard_similarity(dataset[i], dataset[j])
            similarity_scores.append((i, j, jaccard_score))

similarity_scores.sort(reverse=True)

#   print the pairs with the lowest Jaccard similarity scores
for i, j, score in similarity_scores:
    print(f'ID {i} and {j} have a Jaccard similarity score of {score}')
#%%
scores = np.array(similarity_scores)
min = np.min(scores[np.where(scores[2] > 0)])
most_vary = scores[np.where(scores[2] == min)]
most_vary

#%%
new_df = pd.DataFrame({'Height': df_clean['Height'], 'Nose Length': df_clean['The length of you nose is (from bridge to tip)\n'], 'Seconds': df_clean['Time in seconds']})
rows = len(new_df)
#%%
def manhattan(u, v):
    dist = 0
    for i in range(len(u)):
        dist += abs(u[i] - v[i])
    return dist

minX, minD = 0, 0
v = [178.0, 2.4, 480.0]

#%%
for x in range(1, rows):
    d = manhattan(new_df.iloc[x], v)
    if x == 1:
        minD = d
        minX = x
    else:
        if d < minD:
            minD = d
            minX = x
print(minD, minX)
new_df.iloc[10]

# %%
lr = LinearRegression()
df[['Distance between your thumb and your little finger on your right hand', 
   'Distance between your thumb and your little finger on your left hand']]

x = df[['Distance between your thumb and your little finger on your right hand']]
y = df['Distance between your thumb and your little finger on your left hand']

lr.fit(x, y)
print("Coefficient:", lr.coef_)
print("Intercept:", lr.intercept_)
#%%
fig, ax = plt.subplots()
ax.scatter(x, y)
ax.plot(np.arange(12, 26), np.arange(12, 26) * lr.coef_ + lr.intercept_, color='r')
ax.set_xlabel('Distance between your thumb and your little finger on your right hand')
ax.set_ylabel('Distance between your thumb and your little finger on your left hand')
plt.savefig('Linear_Regression.png')
plt.show()
# %%
fig, ax = plt.subplots()
ax.boxplot(df,'Distance between your thumb and your little finger on your right hand')
plt.savefig("Box_1.png")
plt.show()

#%%
fig, ax = plt.subplots()
ax.boxplot(df,'Distance between your thumb and your little finger on your left hand')
plt.savefig("Box_2.png")
plt.show()
