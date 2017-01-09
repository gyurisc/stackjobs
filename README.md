# stackjobs
Very simple scrapy scraper to get stackoverflow jobs using mongodb as store and pandas to enhance data.

Articles written related to this project: 

- [Scraping Stackoverflow Careers for Fun and Profit - Part 1](http://littlebigtomatoes.com/2016/07/scraping-stackoverflow-careers-for-fun-and-profit/). Started writing a parser. Showing how to parse udsing xpath expressions.
- [Scraping Stackoverflow Careers for Fun and Profit - Part 2](http://littlebigtomatoes.com/2016/08/scraping-stackoverflow-careers-for-fun-and-profit-part-2/). Added mongodb support to the parser and saving the items to the database.  
- [Playing with Pandas - Part 3](http://littlebigtomatoes.com/2016/09/playing-with-pandas/). Manipulating and enhancing the data using python pandas and jupyter notebooks.

Workflow steps 

The steps should be ran in the following order: 

- run the scraper 
- export from mongodb (export_from_mongo.py)
- merge exported jobs (merge_exported_jobs.py)
- enhance data (enhance_data_with_pandas.py)
