mongoexport --db stackoverflow --collection jobs --type csv --fields jobid,title,employer,location,salary,description,tags,url,date,weeknum --out data/stackoverflow_jobs.csv
mongoexport --db stackoverflow --collection jobs --type json --fields jobid,title,employer,location,salary,description,tags,url,date,weeknum --out data/stackoverflow_jobs.json
