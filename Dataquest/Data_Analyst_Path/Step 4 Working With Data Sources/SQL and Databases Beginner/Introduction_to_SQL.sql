/*
03/2017
Dataquest : Data Analyst Path
Step 4: Working With Data Sources
SubStep : SQL and Databases: Beginner : Introduction to SQL
*/


/*
1: Databases

In previous missions, we've worked extensively with datasets that are stored in a single file, usually a CSV file. While CSV files are easy to interface with, they have a lot of limitations.
As the data gets larger, it becomes more difficult to load the file into a computer's memory, which is how tools like Pandas work with data.
CSV files also fall short at providing strict security for production applications (imagine if companies like Google or Facebook used CSV files to store and access data) and are optimized for static representation.
If your data changes quickly, which is true for most technology companies, then you'll need to adopt a different method.

A database is a data store designed for storing, querying, and processing data.
Databases store the data we want and expose an interface for interacting with that data. M
ost technology companies use databases to structure the data coming into the system and later query specific subsets of the data to answer questions or update existing data.
Database systems also come with database management software with administrative controls, security and access controls, and a language to interface with the database.

In this course, we'll be focusing on a language called SQL, or Structured Query Language, which was designed to query, update, and modify data stored in a database.

SQL is the most common language for working with databases and is an important tool in any data professional's toolkit.
 While SQL is a language, it's quite different from languages like Python or R. SQL was built specifically for querying and interacting with databases and won't have much of the functionality you can expect in traditional programming languages.
 Since SQL is a declarative language, the user focuses on expressing what he or she wants and the computer focuses on figuring out how to perform the computation.

Before diving into SQL syntax, we'll introduce a few database concepts so you're aware of how the data is represented in a database and why SQL makes it easy to work with that data.
*/


/*
2: Tables, rows, & columns

A database is a collection of tables, where each table is made up of rows of data and each row has values for the same set of columns across the table.
A table is very similar to a DataFrame in Pandas or how a regular CSV file is structured. Both have rows of values with a consistent set of columns.

We'll be working with the data from the American Community Survey on college majors and job outcomes. Here's a preview of recent-grads.csv, the dataset we'll be working with:
Rank 	Major_code 	Major 	Major_category 	Total 	Sample_size 	Men 	Women 	ShareWomen 	Employed
1 	2419 	PETROLEUM ENGINEERING 	Engineering 	2339 	36 	2057 	282 	0.120564 	1976
2 	2416 	MINING AND MINERAL ENGINEERING 	Engineering 	756 	7 	679 	77 	0.101852 	640
3 	2415 	METALLURGICAL ENGINEERING 	Engineering 	856 	3 	725 	131 	0.153037 	648
4 	2417 	NAVAL ARCHITECTURE AND MARINE ENGINEERING 	Engineering 	1258 	16 	1123 	135 	0.107313 	758
5 	2405 	CHEMICAL ENGINEERING 	Engineering 	32260 	289 	21239 	11021 	0.341631 	25694

We have loaded the data in for years 2010-2012 for just recent college grads into a table named recent_grads in a database so we can explore how to query the data using SQL.
You'll notice that the table contains the same columns for each row of data, with each row representing a major in college.

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

Let's dive into how to use SQL to query this database, which contains just this one table.
*/




/*
3: Querying

Writing a SQL query is the primary way of interacting with a database. A SQL query has to adhere to a defined structure and vocabulary that we use to define what we want the database to do.
The SQL language has a set of general statements that you combine with specific logic to express the intent of that query.

The first and most basic statement in SQL is a SELECT statement.
To specify that we want 10 specific columns for all of the rows from a specific table, we use the SELECT keyword along with the names of the 10 columns we want the database to return.
You use a SELECT statement whenever you want to return specific data from the database without editing or modifying the values in the database.

Let's explore the basic syntax for the SELECT statement.

SELECT [columnA, columnB, ...]

FROM tableName;

The SQL syntax reads more like English than a programming language like Python.
The database converts your query to lower-level logic and returns the results back to you. Let's see what an actual SQL query looks like now.
The following query selects the Rank and Major columns from the table recent_grads, which represents the information from recent-grads.csv as a table in the database:

SELECT Rank,Major

FROM recent_grads;

The semi-colon (;) at the end of the query is required since it specifies where the query ends. This allow us to write a query either in one line or over multiple lines.
*/





/*
4: SQLite

We'll be working with SQLite, a lightweight database that's ideal for exploring and learning SQL.
We'll dive more into how SQLite specifically works in a later mission, but for now we have taken care of setting up and loading the data into the database on our end.

Writing and running SQL queries in our interface is similar to writing and running Python code.
Write the query in the code cell and then click check to execute the query against the database.
The results are returned as a list of lists, where each inner list represents the values in a row.
If you write multiple queries in a code cell, only the last query's results will be displayed.

Here's a preview of the results that SQLite returns:

[[1, "PETROLEUM ENGINEERING"], [2, "MINING AND MINERAL ENGINEERING"], [3, "METALLURGICAL ENGINEERING"], [4, "NAVAL ARCHITECTURE AND MARINE ENGINEERING"], [5, "CHEMICAL ENGINEERING"],...

Let's now practice writing and running a SQL query.

Instructions

    Use the query from the previous step that returns the Rank and Major columns from the table recent_grads.
    Click check to see the results of the query.

*/
select Rank, Major from recent_grads;
/* Console Ouputs or Results
Output
[["Rank", "Major"], [1, "PETROLEUM ENGINEERING"], [2, "MINING AND MINERAL ENGINEERING"], [3, "METALLURGICAL ENGINEERING"], [4, "NAVAL ARCHITECTURE AND MARINE ENGINEERING"], [5, "CHEMICAL ENGINEERING"], [6, "NUCLEAR ENGINEERING"], [7, "ACTUARIAL SCIENCE"], [8, "ASTRONOMY AND ASTROPHYSICS"], [9, "MECHANICAL ENGINEERING"], [10, "ELECTRICAL ENGINEERING"], [11, "COMPUTER ENGINEERING"], [12, "AEROSPACE ENGINEERING"], [13, "BIOMEDICAL ENGINEERING"], [14, "MATERIALS SCIENCE"], [15, "ENGINEERING MECHANICS PHYSICS AND SCIENCE"], [16, "BIOLOGICAL ENGINEERING"], [17, "INDUSTRIAL AND MANUFACTURING ENGINEERING"], [18, "GENERAL ENGINEERING"], [19, "ARCHITECTURAL ENGINEERING"], [20, "COURT REPORTING"], [21, "COMPUTER SCIENCE"], [22, "FOOD SCIENCE"], [23, "ELECTRICAL ENGINEERING TECHNOLOGY"], [24, "MATERIALS ENGINEERING AND MATERIALS SCIENCE"], [25, "MANAGEMENT INFORMATION SYSTEMS AND STATISTICS"], [26, "CIVIL ENGINEERING"], [27, "CONSTRUCTION SERVICES"], [28, "OPERATIONS LOGISTICS AND E-COMMERCE"], [29, "MISCELLANEOUS ENGINEERING"], [30, "PUBLIC POLICY"], [31, "ENVIRONMENTAL ENGINEERING"], [32, "ENGINEERING TECHNOLOGIES"], [33, "MISCELLANEOUS FINE ARTS"], [34, "GEOLOGICAL AND GEOPHYSICAL ENGINEERING"], [35, "NURSING"], [36, "FINANCE"], [37, "ECONOMICS"], [38, "BUSINESS ECONOMICS"], [39, "INDUSTRIAL PRODUCTION TECHNOLOGIES"], [40, "NUCLEAR, INDUSTRIAL RADIOLOGY, AND BIOLOGICAL TECHNOLOGIES"], [41, "ACCOUNTING"], [42, "MATHEMATICS"], [43, "COMPUTER AND INFORMATION SYSTEMS"], [44, "PHYSICS"], [45, "MEDICAL TECHNOLOGIES TECHNICIANS"], [46, "INFORMATION SCIENCES"], [47, "STATISTICS AND DECISION SCIENCE"], [48, "APPLIED MATHEMATICS"], [49, "PHARMACOLOGY"], [50, "OCEANOGRAPHY"], [51, "ENGINEERING AND INDUSTRIAL MANAGEMENT"], [52, "MEDICAL ASSISTING SERVICES"], [53, "MATHEMATICS AND COMPUTER SCIENCE"], [54, "COMPUTER PROGRAMMING AND DATA PROCESSING"], [55, "COGNITIVE SCIENCE AND BIOPSYCHOLOGY"], [56, "SCHOOL STUDENT COUNSELING"], [57, "INTERNATIONAL RELATIONS"], [58, "GENERAL BUSINESS"], [59, "ARCHITECTURE"], [60, "INTERNATIONAL BUSINESS"], [61, "PHARMACY PHARMACEUTICAL SCIENCES AND ADMINISTRATION"], [62, "MOLECULAR BIOLOGY"], [63, "MISCELLANEOUS BUSINESS & MEDICAL ADMINISTRATION"], [64, "AGRICULTURE PRODUCTION AND MANAGEMENT"], [65, "GENERAL AGRICULTURE"], [66, "MISCELLANEOUS ENGINEERING TECHNOLOGIES"], [67, "MECHANICAL ENGINEERING RELATED TECHNOLOGIES"], [68, "GENETICS"], [69, "MISCELLANEOUS SOCIAL SCIENCES"], [70, "UNITED STATES HISTORY"], [71, "INDUSTRIAL AND ORGANIZATIONAL PSYCHOLOGY"], [72, "AGRICULTURAL ECONOMICS"], [73, "PHYSICAL SCIENCES"], [74, "MILITARY TECHNOLOGIES"], [75, "CHEMISTRY"], [76, "ELECTRICAL, MECHANICAL, AND PRECISION TECHNOLOGIES AND PRODUCTION"], [77, "BUSINESS MANAGEMENT AND ADMINISTRATION"], [78, "MARKETING AND MARKETING RESEARCH"], [79, "POLITICAL SCIENCE AND GOVERNMENT"], [80, "GEOGRAPHY"], [81, "MICROBIOLOGY"], [82, "COMPUTER ADMINISTRATION MANAGEMENT AND SECURITY"], [83, "BIOCHEMICAL SCIENCES"], [84, "BOTANY"], [85, "COMPUTER NETWORKING AND TELECOMMUNICATIONS"], [86, "GEOLOGY AND EARTH SCIENCE"], [87, "HUMAN RESOURCES AND PERSONNEL MANAGEMENT"], [88, "PRE-LAW AND LEGAL STUDIES"], [89, "MISCELLANEOUS HEALTH MEDICAL PROFESSIONS"], [90, "PUBLIC ADMINISTRATION"], [91, "GEOSCIENCES"], [92, "SOCIAL PSYCHOLOGY"], [93, "ENVIRONMENTAL SCIENCE"], [94, "COMMUNICATIONS"], [95, "CRIMINAL JUSTICE AND FIRE PROTECTION"], [96, "COMMERCIAL ART AND GRAPHIC DESIGN"], [97,
*/




/*
5: Specifying column order

SQL allows us to specify the order of columns in the returned results in the SELECT statement.
Try swapping the order of the columns we specified in the previous query and click check to see the results.
Instructions

Modify the SQL query from the previous step so:

    The Major value for each row is first,
    The Rank value for each row is second,

*/
select Major,Rank from recent_grads;




/*
6: Practice: Select

When we used Major,Rank instead of Rank,Major in the SELECT statement from the previous step, you'll notice that the first value in each list was the major while the second value was the rank.

Now it's your turn to write a SQL query from scratch.
Instructions

Write a query that returns the following 5 columns in the order specified from recent_grads:

    Rank
    Major_code
    Major
    Major_category
    Total

*/
select Rank,Major_code,Major,Major_category,Total from recent_grads;




/*
7: Where

So far, we've been writing queries that return every row from the table but constrained to specific columns.
If we wanted to figure out which majors had more female graduates than male graduates (when ShareWomen is larger than 0.5), we need a way to constrain the rows that are returned.

To filter rows by specific criteria, we need to use the WHERE statement. The WHERE statement requires 3 things:

    The column we want the database to filter on: ShareWomen
    A comparison operator to specify how we want a value in a column to be compared: >
    The comparison value we want the database to compare each value to: 0.5

In the below query, we:

    Use SELECT to specify the column filtering criteria: Major and ShareWomen
    Use FROM to specify the table we want to query: recent_grads
    Use WHERE to specify the row filtering criteria: ShareWomen > 0.5

SELECT Major,ShareWomen

FROM recent_grads

WHERE ShareWomen > 0.5;

Here are the comparison operators we can use:

    Less than: <
    Less than or equal to: <=
    Greater than: >
    Greater than or equal to: >=
    Equal to: =
    Not equal to: !=

The comparison value after the operator must either be text or a number depending on the field. ShareWomen is a numeric column, we don't need to wrap the number 0.5 with quotes.
Lastly, most database systems require that the SELECT and FROM statements come first before any WHERE or other statements.
Instructions

Run the query that we explored above that returns the Major and ShareWomen values for all rows where ShareWomen exceeded 0.5.

    Ensure that all of the values for ShareWomen (the second value in each inner list) are greater than 0.5.

*/
SELECT Major,ShareWomen
FROM recent_grads
WHERE ShareWomen > 0.5;




/*
8: Practice: Where

Now it's your turn to writing a SQL query that uses the WHERE statement to filter the results.
Instructions

Write a SQL query that returns all majors that have more than 10000 people employed with that background.

    In the SELECT statement, specify that we only want the values from the Major and Employed columns (in that order).

*/
SELECT Major,Employed
FROM recent_grads
WHERE Employed > 10000;




/*
9: Limit

Many queries return a large number of results, which can be cumbersome to work with.
SQL comes with a statement called LIMIT that allows us to specify how many results we'd like the database to return.

To use the LIMIT statement, we need to specify the number of results that are returned as an integer value.
The following query returns the first 5 values in the Major column:

SELECT Major FROM recent_grads LIMIT 5;

Here's the result of that query:

[["PETROLEUM ENGINEERING"], ["MINING AND MINERAL ENGINEERING"], ["METALLURGICAL ENGINEERING"], ["NAVAL ARCHITECTURE AND MARINE ENGINEERING"], ["CHEMICAL ENGINEERING"]]

Instructions

Write a query that returns:

    the Major column
    where Employed exceeds 10000
    only the first 10 results

*/
SELECT Major FROM recent_grads where Employed > 10000  LIMIT 10;



/*
10: Next steps

We covered the basics of databases and SQL syntax in this lesson and have seen that SQL is an expressive language for working with data.
In the next lesson, we'll learn about how to combine multiple filtering criteria together to express more complex logic in SQL
*/
