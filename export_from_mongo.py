import pymongo
import datetime
import pandas as pd

def export_jobs(year, weeknum): 
    df = pd.DataFrame(list(jobs.find({ "weeknum": weeknum}))) 
    
    # Dropping _id column
    df = df.drop('_id', 1)

    out_path = "./export/jobs_export_" + str(year) + "_w" + str(weeknum)  + ".csv"
    print "Exporting " + out_path + " with " + str(len(df.index)) + " rows."
    
    df.to_csv(out_path, index = False, encoding='utf-8')


# mongo information 
client = pymongo.MongoClient('localhost', 27017)
db = client['stackoverflow']
jobs = db['jobs']

# week of year and year needed for export
t = datetime.date.today()
weeknum = t.isocalendar()[1] 
year = t.isocalendar()[0] 

    
# this week 
export_jobs(year, weeknum)

# previous week
export_jobs(year, weeknum-1)
