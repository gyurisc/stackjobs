import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import time 

jobs = pd.read_csv('data/stackoverflow_jobs_enhanced.csv', thousands=',')

# filtering out most important columns
tmp = jobs.loc[:,['jobid', 'city', 'state', 'country', 'tags', 'weeknum', 'salary', 'salary_low', 'salary_high', 'currency', 'equity']]

tag_split = lambda x: pd.Series([i for i in x[1:-1].split(',')])
tag_splitted = tmp['tags'].apply(tag_split)

tag_splitted = tag_splitted.fillna('')

t = []

for i in range(0, len(tmp)):    
    num_tags = len(tag_splitted.iloc[i])
    for j in range(0,num_tags):
        tech = tag_splitted.iloc[i][j]        
        if tech == '': break
        # creating new row 
        new_row = {}
        new_row['jobid'] = tmp.iloc[i]['jobid']
        new_row['city'] = tmp.iloc[i]['city']
        new_row['state'] = tmp.iloc[i]['state']
        new_row['country'] = tmp.iloc[i]['country']
        new_row['weeknum'] = tmp.iloc[i]['weeknum']
        new_row['salary_low'] = tmp.iloc[i]['salary_low']
        new_row['salary_high'] = tmp.iloc[i]['salary_high']
        new_row['equity'] = tmp.iloc[i]['equity']
        new_row['currency'] = tmp.iloc[i]['currency']            
        new_row['tech'] = tech
        # adding 
        t.append(new_row)
        
technologies = pd.DataFrame(t)   

#  removing spaces from the beginning and ending
technologies.tech = technologies.tech.str.lstrip(' ')
technologies.tech = technologies.tech.str.rstrip(' ')

technologies.tech = technologies.tech.str.rstrip('"')
technologies.tech = technologies.tech.str.lstrip('"')

# getting the mean figure for salary
technologies['salary_mean'] = technologies[['salary_high','salary_low']].mean(axis=1)

technologies.fillna('', inplace=True)

# saving the result to csv 
technologies.to_csv('../data/technologies.csv', index = False)