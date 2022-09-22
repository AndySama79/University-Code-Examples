#%% 1: Startup

import numpy as np

#%% 2: Array creation and indexing

array2d = np.arange(0, 20).reshape(4, 5)
print(array2d)

#%% 3: Creating a random array and replacing certain rows and columns

rng = np.random.default_rng(0)
print(rng.random())

rand_array = rng.random((5, 4))

array2d[1, :] = rand_array[:, 2]
# array2d[0, :] += rand_array[:, 3]
array2d = array2d.astype(dtype=float)
array2d[:, 0] += rand_array[3, :]

#%% 4: Stats on arrays

value_range = (array2d.min(), array2d.max())
std = np.std(array2d)
mean_rows = np.mean(array2d, axis=1)
sum_cols = np.sum(array2d, axis=0)
matrix_product = np.matmul(array2d, rand_array)

#%% 5: Transpose

array2d_T = array2d.transpose()
print('transpose:\n', array2d_T)

#%% 6: Concatenation

concated = np.concatenate((array2d_T, rand_array), axis=1)

# ? concated_2 = np.concatenate((array2d, rand_array))
# the above statement raises a ValueError
# all the input array dimensions for the concatenation axis
# must match exactly, but along dimension 1, the array at
# index 0 has size 5 and the array at index 1 has size 4

#%% 7: Stacking

stacked = np.stack((array2d_T, rand_array), axis=0)

#%% 8: Another way of stacking

stacked2 = np.stack((array2d_T, rand_array), axis=-1)

#%% 9: Flip the array elements

print(rand_array)
flipped = np.flip(rand_array, axis=1)

#%% 10: Structured array

names = [
    'Tokyo',
    'Jakarta',
    'Delhi',
    'Manila',
    'Sao Paulo',
    'Seoul',
    'Mumbai',
    'Shanghai',
    'Mexico City',
    'Guangzhou',
    'Cairo',
    'Beijing',
    'New York',
    'Kolkata',
    'Moscow',
    'Bangkok',
    'Dhaka',
    'Buenos Aires'
]

lats = [
    35.6839, 
    -6.2146, 
    28.6667, 
    14.6, 
    -23.5504, 
    37.56, 
    19.0758, 
    31.1667, 
    19.4333, 
    23.1288, 
    30.0444, 
    39.904, 
    40.6943, 
    22.5727, 
    55.7558, 
    13.75, 
    23.7289, 
    -34.5997
]

longs = [
    139.7744, 
    106.8451, 
    77.2167, 
    120.9833, 
    -46.6339, 
    126.99, 
    72.8775, 
    121.4667, 
    -99.1333, 
    113.259, 
    31.2358, 
    116.4075, 
    -73.9249,
    88.3639,
    37.6178, 
    100.5167, 
    90.3944,
    -58.3819
]

city_loc_type = np.dtype([("name", "U16"), ("lat", "f4"), ("long", "f4")])
city_loc = np.array([(names[i], lats[i], longs[i]) for i in range(0, len(names))], dtype=city_loc_type)

# %% 11: Query the structured array

#   11.1: Southern hemisphere cities

southern = city_loc[city_loc['lat'] < 0]
my_southern = ['Jakarta', 'Sao Paulo', 'Buenos Aires']

#   11.2: Cities in southern and western hemisphere

southwest = city_loc[(city_loc['lat'] < 0) & (city_loc['long'] < 0)]
# %%
