# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 11:54:35 2022

@author: AndySama
"""

#%% Imports
import numpy as np
import pandas as pd
#%% Load Data
df = pd.read_csv("ds_salaries.csv")
(df.head())
(df.describe())
#%% Selecting Columns
salary = df["salary_in_usd"]
experience = df["experience_level"]
print(salary)
print(experience)
#%% Finding Some Information
salary_range = (salary.min(), salary.max())
experience_count = experience.value_counts()
print(salary_range)
print(experience_count)
#%% Compute some statistics
avg_salary_by_exp = dict(df.groupby("experience_level")["salary_in_usd"].agg(np.mean))
sd_salary_by_experience = dict(df.groupby("experience_level")["salary_in_usd"].agg(np.std))
avg_remote_ratio = dict(df.groupby("experience_level")["remote_ratio"].agg(np.mean))

print(avg_salary_by_exp)
print(sd_salary_by_experience)
print(avg_remote_ratio)
#%% Job Titles with highest salary
highest_salary_titles = list(df.groupby("job_title")["salary_in_usd"].agg(np.mean).nlargest(n=3))
print(highest_salary_titles)
#%% Economic recession
for idx, item in df["salary_in_usd"].iteritems():
    item = item - 0.1 * item
    df.loc[idx, "salary_in_usd"] = item
#%% Remove some entries
df.drop(df[df["salary"] < 100000].index, inplace=True)
#%%

