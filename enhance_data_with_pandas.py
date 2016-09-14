from datetime import datetime
import pymongo 
import pandas as pd
import numpy as np

jobs = pd.read_csv('stackoverflow_jobs.csv')

# Salary 
jobs.salary = jobs.salary.fillna('')

# creating a new column for equity
jobs['equity'] = jobs['salary'].str.contains('Provides Equity')

# striping out equity part 
salary = jobs.salary 
salary = salary.map(lambda x: x.replace("Provides Equity","").replace("/","").strip())

salary = salary.str.extract('(?P<currency>[^\d]*)(?P<number_low>[\d,]+) - (?P<number_high>[\d,]+$)')
salary.number_low = salary.number_low.fillna(0)
salary.number_high = salary.number_high.fillna(0)
salary.currency = salary.currency.fillna('')

# adding new columns
jobs['currency'] = salary.currency
jobs['salary_low'] = salary.number_low
jobs['salary_high'] = salary.number_high
