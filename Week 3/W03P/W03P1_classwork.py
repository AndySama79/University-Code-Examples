#%% imports
import numpy as np
import pandas as pd
#%%load data
df = pd.read_csv("ds_salaries.csv")
df.head()
df.describe()
# %%selecting columns
salary = df["salary_in_usd"]
experience = df["experience_level"]

salary_range = (salary.min(), salary.max())
experience_count = dict(experience.value_counts())

avg_salary_by_exp = dict(df.groupby("experience_level")["salary_in_usd"].agg(np.mean))
sd_salary_by_exp = dict(df.groupby("experience_level")["salary_in_usd"].agg(np.std))
avg_remote_ratio = dict(df.groupby("experience_level")["remote_ratio"].agg(np.mean))
#print(sd_salary_by_exp)
#print(avg_remote_ratio)
# %% Job titles with highest salary
highest_salary_dict = (df.groupby("job_title")["salary_in_usd"].agg(np.mean).nlargest(n=3))
highest_salary_titles = []
for key in highest_salary_dict.keys():
     highest_salary_titles.append(key)
# %% Economic recession
for idx, item in df["salary_in_usd"].iteritems():
    item = item - 0.1 * item
    df.loc[idx, "salary_in_usd"] = item
# %% Remove some entries
df.drop(df[(df["salary_in_usd"] < 100000) & (df["experience_level"] == "EX")].index, inplace=True)

# %%
