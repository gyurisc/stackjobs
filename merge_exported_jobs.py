import pandas as pd
import numpy as np 
import glob
import datetime 
import time

allFiles = glob.glob("./export/*.csv")

dataframes = []
for file in allFiles: 
    df = pd.read_csv(file, index_col='jobid', header=0)
    dataframes.append(df)
    
merged_jobs = pd.concat(dataframes)
    
# Dropping duplicates

print "Before de-deuplication count is " + str(len(merged_jobs.index))
merged_jobs.drop_duplicates(keep='last', inplace=True)
print "After de-deuplication count is " + str(len(merged_jobs.index))

timestr = time.strftime("%Y%m%d")
out_path = "./data/jobs_merged_" + timestr + "_" + str(len(merged_jobs.index))  + ".csv"

# writing it out 
merged_jobs.to_csv(out_path,mode='w')    