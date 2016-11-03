# Ad-hoc fixing of mongo database 
from datetime import datetime
import pymongo 

client = pymongo.MongoClient('localhost', 27017)
db = client['stackoverflow']
jobs = db['jobs']

# total jobs
total_jobs = jobs.count()
print "Total jobs: %s" % total_jobs

print "=== Fixing Date Stamp ==="
date_stamp = datetime(2016, 6, 1, 7, 01, 01)

jobs.update_many({ "date" : { "$exists" : False}}, {"$set" : {"date" : date_stamp}})
count = 0
for job in jobs.find( { "date" : { "$exists" : False}}):
    count = count + 1
    # print(job)

print "=== Fixing Date Stamp ==="
print "Number of jobs with no date is %s." % count

count = 0
for job in jobs.find( { "date" : date_stamp}):
    count = count + 1
    # print(job)

print "Number of jobs with default date is %s." % count

# Week number 
print "=== Fixing Week Number ==="
wkcount = jobs.find( {"weeknum" : {"$exists" : True}}).count()

print "Week number exists with %s and missing for %s jobs." % (wkcount, total_jobs - wkcount)

for job in jobs.find({"weeknum" : {"$exists": False}}):
    d = datetime.strptime(job["date"], '%Y-%m-%d')
    wk = d.isocalendar()[1]
    jobs.update({"_id" : job["_id"]}, {"$set" : {"weeknum" : wk}})

# Employee and Location Whitespace 
print "=== Fixing Employee & Location ==="
print "Striping strings from white space in employer and location strings"
for job in jobs.find():    
    _emp = job["employer"].strip()
    _loc = job["location"].strip()  
    jobs.update({"_id" : job["_id"]}, {"$set" : {"employer" : _emp, "location" : _loc}})
    
print "Stripping strings from whitespace where salary exists"
for job in jobs.find({ "salary" : { "$exists" : True }}):    
    _salary = job["salary"].strip()
    jobs.update({"_id" : job["_id"]}, {"$set" : {"salary" : _salary}})
