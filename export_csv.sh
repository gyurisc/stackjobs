mongoexport --db stackoverflow --collection jobs --type csv --fields jobid,title,employer,location,salary,description,tags,url,date,weeknum --out stackoverflow_jobs.csv
mongoexport --db stackoverflow --collection jobs --type json --fields jobid,title,employer,location,salary,description,tags,url,date,weeknum --out stackoverflow_jobs.json
