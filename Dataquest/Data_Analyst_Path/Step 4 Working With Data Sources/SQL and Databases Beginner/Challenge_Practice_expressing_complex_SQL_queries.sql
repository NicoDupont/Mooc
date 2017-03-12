/*
03/2017
Dataquest : Data Analyst Path
Step 4: Working With Data Sources
SubStep : SQL and Databases: Beginner : Practice expressing complex SQL queries
*/

/*
1: Introduction

In the last 2 missions, we've covered the basics of SQL and have explored how to use it to retrieve relevant rows from a database table.
In this challenge, you'll practice writing your own SQL queries from scratch.

We'll continue to work with the data from the American Community Survey on college majors and job outcomes.
Here's a preview of recent-grads.csv, the dataset we'll be working with:

Rank 	Major_code 	Major 	Major_category 	Total 	Sample_size 	Men 	Women 	ShareWomen 	Employed
1 	2419 	PETROLEUM ENGINEERING 	Engineering 	2339 	36 	2057 	282 	0.120564 	1976
2 	2416 	MINING AND MINERAL ENGINEERING 	Engineering 	756 	7 	679 	77 	0.101852 	640
3 	2415 	METALLURGICAL ENGINEERING 	Engineering 	856 	3 	725 	131 	0.153037 	648
4 	2417 	NAVAL ARCHITECTURE AND MARINE ENGINEERING 	Engineering 	1258 	16 	1123 	135 	0.107313 	758
5 	2405 	CHEMICAL ENGINEERING 	Engineering 	32260 	289 	21239 	11021 	0.341631 	25694

We have loaded the data in for years 2010-2012 for just recent college grads into a table named recent_grads.
The full table has many more columns, 21 to be specific, than the ones displayed above and they're explained in further detail on FiveThirtyEight's Github repo.

Here are the descriptions of the columns in the above snapshot:

    Rank - Rank by median earnings.
    Major_code - Major code.
    Major - Major description.
    Major_category - Category of major.
    Total - Total number of people with major.
    Sample_size - Sample size (unweighted) of full-time.
    Men - Male graduates.
    Women - Female graduates.
    ShareWomen - Women as share of total.
    Employed - Number employed.

*/


/*
2: Select and Limit

In this step, you'll practice using the SELECT and LIMIT statements.
Instructions

Write a query that retrieves the first 20 rows in the table, with only the following columns in the following order:

    College_jobs
    Median
    Unemployment_rate

*/
select
    College_jobs
    ,Median
    ,Unemployment_rate
from recent_grads
limit 20;


/*
3: Where

In this step, you'll practice using the WHERE SQL statement to express row filtering criteria.
Instructions

    Write a query that returns the first 5 Arts majors (only include the Major column).

*/
select Major from recent_grads where Major_category = "Arts" limit 5;


/*
4: Operators

In this step, you'll practice using the logical operators in SQL to express complex criteria.
Instructions

Return all non-engineering majors:

    with a median salary less than or equal to 50,000
    or an unemployment rate higher than 6.5%.

Return only these columns in the following order:

    Major
    Total
    Median
    Unemployment_rate

*/
select
    Major
    ,Total
    ,Median
    ,Unemployment_rate
from recent_grads
where Major_category != "Engineering" and (Median <= 50000 or Unemployment_rate > 0.065);

/*
5: Ordering

Lastly, in this step you'll practice using the ORDER BY statement to customize the ordering of a query's results.
Instructions

Return the first 20 non-engineering majors in reverse alphabetical order.

    We're only interested in the major names in the results.

*/
select
    Major
from recent_grads
where Major_category != "Engineering"
order by 1 desc
limit 20;


/*
6: Next steps

In the next mission, we'll walk through how to query a SQLite database from Python.
Most companies in industry use a SQL database of some kind to store their data.
Learning how to interface with SQL databases from Python will allow you to incorporate more data sources in your data science workflow.
*/
