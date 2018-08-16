#! /usr/bin/env python3

# Project: Log Analysis | Udacity Full Stack Nanodegree

# Import PostgresSQL library
import psycopg2

BETA = "news"

query_1 = """
        SELECT title, count(*) AS views
        FROM articles
        JOIN log
        ON concat('/article/', articles.slug) = log.path
        WHERE log.status LIKE '%200%'
        GROUP BY log.path, articles.title
        ORDER BY views DESC
        LIMIT 3;
        """

query_2 = """
        SELECT authors.name, count(*) AS views
        FROM articles JOIN authors
        ON articles.author = authors.id JOIN log
        ON articles.slug = substring(log.path, 10)
        WHERE log.status LIKE '200 OK'
        GROUP BY authors.name ORDER BY views DESC;
        """

query_3 = """
        SELECT errorlogs.date, round(100.0*errorcount/logcount,2) AS percent
        FROM logs, errorlogs
        WHERE logs.date = errorlogs.date
        AND errorcount > logcount/100;
        """


def connect(query):
    # Connect to database
    db = psycopg2.connect(database=BETA)
    c = db.cursor()
    # Execute queries
    c.execute(query)
    # Fetch results
    results = c.fetchall()
    db.close()
    return results


# 1. The most popular three articles of all time
def top_articles(query):
    results = connect(query)
    print('\n Three most popular articles of all time:\n')
    for i in results:
            print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')
            print(" ")


# 2. The most popular article authors of all time
def top_authors(query):
    results = connect(query)
    print('\n The most popular authors of all time:\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')
        print(" ")


# 3. Days when more than 1% of requests lead to errors
def error(query):
    results = connect(query)
    print('\n The days when more than 1% of requests led to error:\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' %' + ' errors')
        print(" ")


if __name__ == '__main__':
    # Print results
    top_articles(query_1)
    top_authors(query_2)
    error(query_3)
