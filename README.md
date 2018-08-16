## PROJECT: LOG ANALYSIS

### UDACITY FSND

### PROJECT OVERVIEW
The objective of the project is to create a reporting tool that prints out query results in plain text based on the data in the given database.

## REQUIRED RESOURCES
[Python3](https://www.python.org/)
[Vagrant](https://www.vagrantup.com/)
[VirtualBox](https://www.virtualbox.org/)

#### RUNNING THE PROGRAM
  1. Install Vagrant and VirtualBox
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download the [news data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
  2. Load the database using `psql -d news -f newsdata.sql`.
  3. Connect to the database using `psql -d news`.
  4. Create VIEWS
  Views for question 3:
  ```sql
  CREATE VIEW logs AS
  SELECT to_char(time, 'DD-MON-YYYY') AS Date, count(*) as LogCount
  FROM log
  GROUP BY Date;
  ```
  ```sql
  CREATE VIEW errorlogs AS
  SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as ErrorCount
  FROM log
  WHERE STATUS = '404 NOT FOUND'
  GROUP BY Date;
  ```
  5. Exit `psql`.
  6. Execute the Python file - `python log.py`.

### PROJECT REVIEW
The project sets up a mock PostgreSQL database for a fictional news company, and the Python script uses the psycopg2 library to send queries to the database and to produce answers to these three questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?


### DATABASE OUTLINE
  The project uses a database of a newspaper company, which has 3 tables:
  articles - articles posted in the newspaper to date.
  authors - List of authors who have published their articles in the newspaper.
  log - log of every request sent to the newspaper server.
