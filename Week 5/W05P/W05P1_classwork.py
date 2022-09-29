# %% imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %% load data
df = pd.read_csv('salaries-by-college-type.csv')

# %% Convert strings with $ and , to numbers
df['starting'] = df['Starting Median Salary'].str.replace('[$,]', '', regex=True).astype(float)
df['mid'] = df['Mid-Career Median Salary'].str.replace('[$,]', '', regex=True).astype(float)
df['mid10'] = df['Mid-Career 10th Percentile Salary'].str.replace('[$,]', '', regex=True).astype(float)
df['mid25'] = df['Mid-Career 25th Percentile Salary'].str.replace('[$,]', '', regex=True).astype(float)
df['mid75'] = df['Mid-Career 75th Percentile Salary'].str.replace('[$,]', '', regex=True).astype(float)
df['mid90'] = df['Mid-Career 90th Percentile Salary'].str.replace('[$,]', '', regex=True).astype(float)

# %% Rename columns to something shorter
df.rename(columns={'School Name': 'sname', 'School Type': 'stype'}, inplace=True)

# %% Rename columns to something shorter
df.drop(columns=['Starting Median Salary',
                'Mid-Career Median Salary',
                'Mid-Career 10th Percentile Salary',
                'Mid-Career 25th Percentile Salary', 
                'Mid-Career 75th Percentile Salary',
                'Mid-Career 90th Percentile Salary'], inplace=True)
# See what columns we got now
print(df.columns)
# Print the head of the dataframe
print(df.head())
# %% Create a random number sequence
rng = np.random.default_rng(0)
y = rng.random(10)

# %% Create a random number sequence
fig, ax = plt.subplots()
ax.plot(y)
ax.set_ylabel('random number sequence')
ax.legend(['random'])
fig.suptitle("Random Number Sequence Plotter")
ax.set_xlim(-1, 12)
ax.set_yticks((0.1, 0.3, 0.5, 0.7))
fig.savefig('line_plot.png')

# %% Pie Chart and bar plot with titles and labels
fig, ax = plt.subplots(1, 2)
counts = df.groupby('stype').agg('count')
ax[0].pie(counts['sname'], labels=counts.index, autopct='%1.1f')
ax[0].set_title("School Types")

counts = df.groupby('stype').agg(np.mean)
ax[1].bar(counts.index, counts['starting'])
ax[1].set_ylabel('Average Median Salary')
ax[1].tick_params(axis='x', rotation=90)
fig.tight_layout()
fig.savefig('pie_bar_plot.png')

# %% Bar chart with error bars
fig, ax = plt.subplots()
sem = df.groupby('stype').agg('sem')
ax.bar(counts.index, counts['starting'], yerr=sem['starting'])
ax.set_ylabel('Average Median Salary')
fig.tight_layout()
fig.savefig('error_bar_plot.png')

# %% Box Plot the mid career salaries
fig, ax = plt.subplots()

mid = df.groupby('stype')
values = mid.groups.values()
stypes = mid.groups.keys()

ax.boxplot(values, labels=stypes)
fig.savefig('box_plot.png')
# %%
