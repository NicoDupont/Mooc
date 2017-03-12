"""
03/2017
Dataquest : Data Analyst Path
Step 4: Working With Data Sources
SubStep : SQL and Databases: SQL Summary Statistics
"""


"""
1: Counting In Python
In this mission, we'll be working on computing summary statistics using SQL. There have been many cases in the past few missions when we've needed to count the number of records that match a particular SQL query. So far, we've been able to do this by:

Performing a SQL query with Python.
Retrieving the results and storing into a list.
Finding the length of the list.
This approach works, but also requires quite a bit of code and is fairly slow. As we go through this mission, we'll learn how to count records and more using only SQL.

We'll be working with factbook.db, a SQLite database that contains information about each country in the world. We'll use a table in the file called facts. Each row in facts represents a single country, and contains several columns, including:

name -- the name of the country.
area -- the total land and sea area of the country.
population -- the population of the country.
birth_rate -- the birth rate of the country.
created_at -- the date the record was created.
updated_at -- the date the record was updated.
Here are the first few rows of facts:

id	code	name	area	area_land	area_water	population	population_growth	birth_rate	death_rate	migration_rate	created_at	updated_at
1	af	Afghanistan	652230	652230	0	32564342	2.32	38.57	13.89	1.51	2015-11-01 13:19:49.461734	2015-11-01 13:19:49.461734
2	al	Albania	28748	27398	1350	3029278	0.3	12.92	6.58	3.3	2015-11-01 13:19:54.431082	2015-11-01 13:19:54.431082
3	ag	Algeria	2381741	2381741	0	39542166	1.84	23.67	4.31	0.92	2015-11-01 13:19:59.961286	2015-11-01 13:19:59.961286

Instructions
Import sqlite3.
Initialize a connection to factbook.db using the connect() method, and store it in the variable conn.
Use conn, the execute() method, and the fetchall() method to fetch all the records in the facts table. Assign the result to the facts variable.
Print out the facts variable.
Count the number of items in facts, and assign the result to facts_count.
"""
import sqlite3
conn = sqlite3.connect('factbook.db')
c = conn.cursor()
c.execute('SELECT * FROM facts;')
facts = c.fetchall()
#print(facts)
facts_count = len(facts)
print(facts_count)
""" Console Outputs or Results
Output
261
"""


"""
2: Counting In SQL
Counting up the number of records in a table is a common operation, and it feels like it should be more efficient than the code we just wrote in the last screen.
Thankfully, SQL includes the COUNT aggregation function, which allows us to count the number of records in a table.
It's called an aggregation function because it works across many rows to compute an aggregate value. Here's an example:


sELECT COUNT(*) FROM facts;
The query above will count the number of rows in the facts table of factbook.db. If we instead want to count the number of non-null values in a single column, we can use the following syntax:


sELECT COUNT(area_water)
FROM facts;
Note that the above query will only count the total number of non-null values in the area_water column, and so can return different counts than COUNT(*).

Each of the queries above will return a list with a single tuple when executed in Python. It will look like this:


[(243,)]
In order to get the integer count from the result, you'll need to extract the first element in the first tuple in the results.

This style not only saves typing, it's also much faster for larger datasets, because we can do the counting inside the database, and not have to pull all the data into the Python environment first. In general, operations done within a SQL database engine will be faster than the equivalent operations done after pulling the data into a programming environment. This is because SQL database engines are optimized specifically for querying.

Instructions
Use the COUNT aggregation function to count the number of non-null values in the birth_rate column of the facts table
Extract the integer value from the result, and assign to birth_rate_count.
Print out birth_rate_count.
"""
import sqlite3
onn = sqlite3.connect("factbook.db")
c = conn.cursor()
c.execute('SELECT count(birth_rate) FROM facts where birth_rate is not null;')
birth_rate_count = c.fetchall()
print(birth_rate_count)

#or
birth_rate_tuple = conn.execute("SELECT COUNT(birth_rate) FROM facts;").fetchall()
birth_rate_count = birth_rate_tuple[0][0]
print(birth_rate_count)
""" Console Outputs or Results
Output
228
"""



"""
3: Min And Max In SQL
SQL contains other aggregation functions besides COUNT. MIN and MAX are two aggregation functions that allow us to find the maximum and minimum values in columns.
Whereas we could use the COUNT function with any column, we can only use MAX and MIN with numeric columns.


sELECT MAX(birth_rate)
FROM facts;
The above query will again return a list with a single tuple:


[(45.45,)]
45.45 is the highest value in the birth_rate column of the facts table.

Instructions
Use the MIN function to find the minimum value in the population_growth column.
Extract the numeric result and assign it to min_population_growth.
Print min_population_growth.
Use the MAX function to find the maximum value in the death_rate column.
Extract the numeric result and assign it to max_death_rate.
Print max_death_rate.
"""
conn = sqlite3.connect("factbook.db")
min_population_growth_tuple = conn.execute("SELECT min(population_growth) FROM facts;").fetchall()
min_population_growth = min_population_growth_tuple[0][0]
print(min_population_growth)

max_death_rate_tuple = conn.execute("SELECT max(death_rate) FROM facts;").fetchall()
max_death_rate = max_death_rate_tuple[0][0]
print(max_death_rate)
""" Console Outputs or Results
Output
0.0
14.89
"""



"""
4: Sum And Average In SQL
The final two aggregation functions that we'll look at are SUM and AVG. SUM finds the total of all the values in a numeric column:


sELECT SUM(birth_rate)
FROM facts;
This will again return a list with a single tuple:


[(4406.909999999998,)]
AVG finds the mean of all the non-null values in a column:


sELECT AVG(birth_rate)
FROM facts;
The result of the above query is:


[(19.32855263157894,)]
Instructions
Use the SUM function to find the sum of the area_land column.
Extract the numeric result and assign it to total_land_area.
Print total_land_area.
Use the AVG function to find the mean of the area_water column.
Extract the numeric result and assign it to avg_water_area.
Print avg_water_area.

"""
conn = sqlite3.connect("factbook.db")

total_land_area_tuple = conn.execute("SELECT sum(area_land) FROM facts;").fetchall()
total_land_area = total_land_area_tuple[0][0]
print(total_land_area)

avg_water_area_tuple = conn.execute("SELECT avg(area_water) FROM facts;").fetchall()
avg_water_area = avg_water_area_tuple[0][0]
print(avg_water_area)
""" Console Outputs or Results
Output
128584834
19067.59259259259
"""



"""
5: Multiple Aggregation Functions
If we wanted to use the SUM, AVG, and MAX functions on a column, it would be inefficient to write three different queries to retrieve the information.
You may recall that we can query multiple columns by separating the names with a comma:


sELECT birth_rate, death_rate, population_growth
FROM facts;
We can apply the sample principle to use multiple aggregation functions in one query:


sELECT COUNT(*), SUM(death_rate), AVG(population_growth)
FROM facts;
Because there are three aggregation functions specified in the query, it will return a list containing a tuple with three elements:


[(261, 1783.2500000000002, 1.2009745762711865)]
The order of the aggregation functions in the query corresponds to the order of the results.
So the first element in the tuple is the count of all the rows, the second is the sum of the death_rate column, and the third is the mean of the population_growth column.

Instructions
Write a single query that calculates the following statistics about the facts table, in order:
The mean of the population column.
The sum of the population column.
The maximum value in the birth_rate column.
Assign the result of the query to facts_stats.
Print facts_stats.

"""
conn = sqlite3.connect("factbook.db")
facts_stats_tuple = conn.execute("SELECT avg(population),sum(population),max(birth_rate) FROM facts;").fetchall()
facts_stats = facts_stats_tuple
print(facts_stats)
""" Console Outputs or Results
Output
[(62094928.32231405, 15026972654, 45.45)]
"""



"""
6: Conditional Aggregation
As you may recall from earlier, we can use the WHERE statement to only query certain rows in a SQL table:


sELECT population
FROM facts
WHERE birth_rate > 10;
The above query will select any values in the population column where the birth_rate is higher than 10.
We can also use WHERE statements with aggregation functions to only calculate statistics for a certain subset of rows:


sELECT COUNT(*)
FROM facts
WHERE population > 5000000;
The query above will count the number of rows where population is greater than 5000000.

Instructions
Calculate the mean population_growth for countries with a population greater than 10000000.
Extract the numeric result and assign it to population_growth.
Print population_growth.
"""
conn = sqlite3.connect("factbook.db")
population_growth_tuple = conn.execute("SELECT avg(population_growth) FROM facts where population > 10000000;").fetchall()
population_growth = population_growth_tuple[0][0]
print(population_growth)
""" Console Outputs or Results
Output
1.4572222222222226
"""


"""
7: Selecting Unique Rows
There are cases when we'll only want to select the unique values in a column or database, and not get each individual row. One example is if our facts table had duplicate entries for each country:

id	code	name	area	area_land	area_water	population	population_growth	birth_rate	death_rate	migration_rate	created_at	updated_at
1	af	Afghanistan	652230	652230	0	32564342	2.32	38.57	13.89	1.51	2015-11-01 13:19:49.461734	2015-11-01 13:19:49.461734
2	af	Afghanistan	652230	652230	0	32564342	2.32	38.57	13.89	1.51	2015-11-01 13:19:49.461734	2015-11-01 13:19:49.461734
If we want to get a list of all the countries in the world, we'll need to remove these duplicate rows, so countries appear twice. We can do this with the DISTINCT statement:


sELECT DISTINCT name
FROM facts;
The above query will return all of the unique values in the name column of facts. It won't return any values twice.

The DISTINCT statement can also be used with multiple columns, in which case, it will return unique groups of those columns:


sELECT DISTINCT name, population
FROM facts;
The above query will select unique pairs of population and name values from facts.

Instructions
Select all the distinct values in the birth_rate column of the facts table, and assign the result to the unique_birth_rates.
Print unique_birth_rates.
"""
conn = sqlite3.connect("factbook.db")
unique_birth_rates = conn.execute("SELECT distinct birth_rate  FROM facts;").fetchall()
print(unique_birth_rates)
""" Console Outputs or Results
Output
[(38.57,), (12.92,), (23.67,), (8.13,), (38.78,), (15.85,), (16.64,), (13.61,), (12.15,), (9.41,), (15.5,), (13.66,), (21.14,), (11.87,), (10.7,), (11.41,), (24.68,), (36.02,), (17.78,), (22.76,), (8.87,), (20.96,), (14.46,), (17.32,), (8.92,), (42.03,), (18.39,), (42.01,), (23.83,), (36.17,), (10.28,), (20.33,), (35.08,), (36.6,), (13.83,), (12.49,), (16.47,), (27.84,), (34.88,), (35.85,), (15.91,), (28.67,), (9.45,), (9.9,), (9.63,), (10.27,), (23.65,), (15.41,), (18.73,), (18.51,), (22.9,), (16.46,), (33.31,), (30.0,), (10.51,), (37.27,), (19.43,), (10.72,), (12.38,), (34.49,), (30.86,), (12.74,), (8.47,), (31.09,), (8.66,), (16.03,), (24.89,), (35.74,), (33.38,), (15.59,), (22.31,), (23.14,), (9.16,), (13.91,), (19.55,), (16.72,), (17.99,), (31.45,), (14.84,), (18.48,), (8.74,), (18.16,), (7.93,), (25.37,), (19.15,), (26.4,), (21.46,), (14.52,), (8.19,), (None,), (19.91,), (22.98,), (24.25,), (10.0,), (14.59,), (25.47,), (34.41,), (18.03,), (10.45,), (10.1,), (11.37,), (11.55,), (32.61,), (41.56,), (19.71,), (15.75,), (44.99,), (10.18,), (25.6,), (31.34,), (13.29,), (18.78,), (20.54,), (12.0,), (6.65,), (20.25,), (10.42,), (18.2,), (38.58,), (19.8,), (24.95,), (20.64,), (10.83,), (13.33,), (45.45,), (37.64,), (12.14,), (24.44,), (22.58,), (11.05,), (18.32,), (24.38,), (16.37,), (18.28,), (24.27,), (9.74,), (9.27,), (9.84,), (9.14,), (11.6,), (33.75,), (13.5,), (13.7,), (13.57,), (20.87,), (8.63,), (34.23,), (34.52,), (9.08,), (14.19,), (37.03,), (8.27,), (9.91,), (8.42,), (25.77,), (40.45,), (20.75,), (36.91,), (9.64,), (29.19,), (16.34,), (24.67,), (11.99,), (10.5,), (22.17,), (36.39,), (11.19,), (34.16,), (34.13,), (23.0,), (13.46,), (16.33,), (19.4,), (23.74,), (43.79,), (15.43,), (12.17,), (13.07,), (17.0,), (25.04,), (19.16,), (15.96,), (29.98,), (42.13,), (32.26,), (10.2,), (9.23,), (8.88,), (13.77,), (14.48,), (15.22,), (15.33,), (7.42,), (13.45,), (12.56,), (13.8,), (13.0,), (14.33,), (12.67,), (11.33,), (10.91,), (12.11,), (10.9,), (14.08,), (11.91,), (11.1,), (11.26,), (9.88,), (16.13,), (22.89,), (16.82,), (10.86,), (10.31,), (31.11,), (22.99,), (30.24,), (18.6,)]
"""


"""
8: Distinct Aggregations
If we wanted to count the number of unique items in the population column, we could use the COUNT aggregation function along with the DISTINCT statement. Here's how it would work:


sELECT COUNT(DISTINCT population)
FROM facts;
The above query will count all the distinct values in the population column. We can also use other aggregation functions along with the DISTINCT statement:


sELECT AVG(DISTINCT birth_rate)
FROM facts;
The above query will find the mean of all the distinct values in the birth_rate column.

Instructions
Find the average of all the distinct values in the birth_rate column when population is greater than 20000000.
Extract the numeric result, and assign to average_birth_rate.
Print average_birth_rate.
Find the sum of all the distinct values in the population column when area_land is greater than 1000000.
Extract the numeric result, and assign to sum_population.
Print sum_population.
"""
conn = sqlite3.connect("factbook.db")
average_birth_rate_tuple = conn.execute("SELECT avg(DISTINCT birth_rate) FROM facts where population > 20000000;").fetchall()
average_birth_rate = average_birth_rate_tuple[0][0]
print(average_birth_rate)

sum_population_tuple = conn.execute("SELECT sum(DISTINCT population) FROM facts where area_land > 1000000;").fetchall()
sum_population = sum_population_tuple[0][0]
print(sum_population)
""" Console Outputs or Results
Output
20.43473684210527
4233873015
"""



"""
9: Arithmetic In SQL
There are times when we'll want to do some arithmetic on columns in a SQL table.
One example is making the counts in the population column easier to understand by expressing them in terms of millions.
Instead of a number like 9766442, we'd want to display 9.766442.
We could do this in Python, but it would be cumbersome to pull all the data into the Python environment, then manipulate it.
Instead, we can perform the math inside the SQL database engine:


sELECT population / 1000000
FROM facts;
The above query will divide every value in the population column by 1000000, and return the result.
Because the population column contains integers, and we specified an integer to divide by, the results will be integers as well.
If we want to retain precision, we can specify a float instead:

sELECT population / 1000000.0
FROM facts;
The above query will return a series of floats, instead of rounding the values to integers. Here's the rules for what an arithmetic operation will return:

Two floats -- returns a float (ex. sELECT birth_rate / 1000000.0 FROM facts;)
A float and an integer -- returns a float (ex. sELECT population / 1000000.0 FROM facts;)
Two integers -- returns an integer (ex. sELECT population / 1000000 FROM facts;)
Instructions
Use arithmetic operators in a SQL query to express population_growth in terms of millions. Ensure that you divide by a float so that the result is also a float.
Assign the result of the query to population_growth_millions.
Print population_growth_millions
"""
conn = sqlite3.connect("factbook.db")
population_growth_millions_tuple = conn.execute("SELECT population_growth / 1000000.0  FROM facts;").fetchall()
population_growth_millions = population_growth_millions_tuple
print(population_growth_millions)
""" Console Outputs or Results

"""



"""
10: Arithmetic Between Columns
A few screens ago, we learned how to apply aggregation functions to columns after the sELECT statement:


sELECT AVG(birth_rate), SUM(population)
FROM facts;
This modified the values of the columns before they were returned.
SQL lets us perform many different kinds of manipulations on the columns we select.
If we wanted to calculate the ratio between births and deaths for each country, we could divide the birth_rate column by the death_rate column. Here's how we could do it:


sELECT birth_rate / death_rate
FROM facts;
The above query will divide each value in the birth_rate column by its corresponding value in the death_rate column.

We can also perform more complex queries, such as finding the ratio of birth_rate plus migration_rate to death_rate, which will help us discover if the population is increasing or decreasing:


sELECT (birth_rate + migration_rate) / death_rate
FROM facts;
The above query will add together the birth_rate and migration_rate columns, then divide by the death_rate column.
Arithmetic in SQL respects the order of operations and parentheses, so the addition step happens before the division step.

Instructions
Use a SQL query to compute the population of each country a year from now.
Multiply the population and population_growth columns, then add the population column to the result.
Assign the result of the query to next_year_population.
Print next_year_population.
"""
conn = sqlite3.connect("factbook.db")
next_year_population = conn.execute("SELECT (1 + (population_growth/100)) * population FROM facts;").fetchall()
print(next_year_population)
""" Console Outputs or Results

"""



"""
11: Next Steps
In this mission, we covered computing summary statistics in SQL.
It's often advantageous to do these computations in the SQL database versus in a Python environment because it's faster to code up and execute.
In the next mission, we'll cover computing more advanced statistics in SQL with the GROUP BY statement.
"""
