/*
03/2017
Dataquest : Data Analyst Path
Step 4: Working With Data Sources
SubStep : SQL and Databases : Beginner : Group Summary Statistics
*/


/*
1: Statistics By Group
In the last mission, we computed summary statistics across columns using SQL.
In many cases, though, we want to drill down even more, and compute summary statistics per-group.
In this mission, we'll explore how to calculate more granular summary statistics.
We'll switch back to writing SQL queries directly instead of using Python so we can focus more on the SQL syntax.

We'll be working with a dataset on jobs that's stored in the recent_grads table of jobs.db.
Each row represents a single college major, and contains information about post-graduation employment of students who had the major.
You can find out more about the dataset here. Here are descriptions of a few of the columns (the whole dataset has 21 columns):

Rank - The numerical rank of the major by post-graduation median earnings.
Major_code - The numerical code of the major.
Major - The description of the major.
Major_category - The category of the major.
Total - The total number of people who studied the major.
Men - The number of men who studied the major.
Women - The number of women who studied the major.
ShareWomen - The share of women (from 0 to 1) who studied the major.
Employed - The number of people who studied the major and were employed post-graduation.
Here are the first few rows and columns in the dataset:

Rank	Major_code	Major	Major_category	Total	Sample_size	Men	Women	ShareWomen	Employed
1	2419	PETROLEUM ENGINEERING	Engineering	2339	36	2057	282	0.120564	1976
2	2416	MINING AND MINERAL ENGINEERING	Engineering	756	7	679	77	0.101852	640
3	2415	METALLURGICAL ENGINEERING	Engineering	856	3	725	131	0.153037	648
4	2417	NAVAL ARCHITECTURE AND MARINE ENGINEERING	Engineering	1258	16	1123	135	0.107313	758
5	2405	CHEMICAL ENGINEERING	Engineering	32260	289	21239	11021	0.341631	25694
As we go through this mission, we'll drill down and compute summary statistics by group, and answer questions like:

What's the share of women in each major category?
What major categories are the most likely to be employed post-graduation?
What percentage of people in each major category get a low wage job?
First, let's explore the data.

Instructions
Write a SQL query that displays all of the columns and the first 5 rows of the recent_grads table.
*/
SELECT * FROM recent_grads limit 5;
/* Console Outputs or results
Output
[["index", "Rank", "Major_code", "Major", "Major_category", "Total", "Sample_size", "Men", "Women", "ShareWomen", "Employed", "Full_time", "Part_time", "Full_time_year_round", "Unemployed", "Unemployment_rate", "Median", "P25th", "P75th", "College_jobs", "Non_college_jobs", "Low_wage_jobs"], [0, 1, 2419, "PETROLEUM ENGINEERING", "Engineering", 2339, 36, 2057, 282, 0.120564344, 1976, 1849, 270, 1207, 37, 0.018380527, 110000, 95000, 125000, 1534, 364, 193], [1, 2, 2416, "MINING AND MINERAL ENGINEERING", "Engineering", 756, 7, 679, 77, 0.10185185199999999, 640, 556, 170, 388, 85, 0.117241379, 75000, 55000, 90000, 350, 257, 50], [2, 3, 2415, "METALLURGICAL ENGINEERING", "Engineering", 856, 3, 725, 131, 0.153037383, 648, 558, 133, 340, 16, 0.024096386, 73000, 50000, 105000, 456, 176, 0], [3, 4, 2417, "NAVAL ARCHITECTURE AND MARINE ENGINEERING", "Engineering", 1258, 16, 1123, 135, 0.107313196, 758, 1069, 150, 692, 40, 0.050125313, 70000, 43000, 80000, 529, 102, 0], [4, 5, 2405, "CHEMICAL ENGINEERING", "Engineering", 32260, 289, 21239, 11021, 0.341630502, 25694, 23170, 5180, 16697, 1672, 0.061097712, 65000, 50000, 75000, 18314, 4440, 972]]
*/




/*
2: The GROUP BY Statement
The GROUP BY SQL statement allows us to compute summary statistics for each group in a dataset.
Groups are defined by the unique values in a column or set of columns.
The unique values are equivalent to using the DISTINCT statement.
To illustrate, we can figure out the total number of people employed in each major category with the following query:

SELECT Major_category, SUM(Employed)
FROM recent_grads
GROUP BY Major_category;
This results in more clear output:

This will give us the count of total people employed for each major category (output is truncated for length):

see img/img1.png

The above displays aggregate counts of the Employed column for each Major_category.
Unfortunately, the above doesn't have any indication of which major category each row refers to.
We can fix this by selecting the Major_category column as well:

SELECT SUM(Employed)
FROM recent_grads
GROUP BY Major_category;

This results in more clear output:

see img/img2.png

This works because the GROUP BY statement splits each category into groups, then figures out what values to display.
Here's a diagram of how GROUP BY splits the data into groups, using a small sample from the recent_grads table:

see img/img3.png

For each group, the GROUP BY statement queries each column and aggregation function mentioned after the SELECT statement:

see img/img4.png

If a column is selected, the SQL engine will use the last value for that column in the group.
If an aggregation function is selected, the SQL engine will compute the value for that aggregation function across the group.

For the query in the diagram, we end up with the following result:

see img/img5.png

Instructions
Use the SELECT statement to select the following columns and aggregates in a query:
Major_category
AVG(ShareWomen)
Use the GROUP BY statement to group the query by the Major_category column.

*/
select Major_category
,AVG(ShareWomen)
from recent_grads
group by 1;
/* Console Outputs or results
Output
[["Major_category", "AVG(ShareWomen)"], ["Agriculture & Natural Resources", 0.6179384232], ["Arts", 0.56185119575], ["Biology & Life Science", 0.584518475857143],
["Business", 0.4050631853076923], ["Communications & Journalism", 0.64383484025], ["Computers & Mathematics", 0.5127519954545455], ["Education", 0.6749855163125],
["Engineering", 0.2571578951034483], ["Health", 0.6168565694166667], ["Humanities & Liberal Arts", 0.6761934042], ["Industrial Arts & Consumer Services", 0.4493512688571429],
["Interdisciplinary", 0.495397153], ["Law & Public Policy", 0.3359896912], ["Physical Sciences", 0.5087494197], ["Psychology & Social Work", 0.7777631628888888], ["Social Science", 0.5390672957777778]]
*/



/*
3: The AS Statement
You may have noticed that in the last screen, specifying AVG(ShareWomen) caused the column to show up with that name in the results.
This can often be unintuitive, and make it hard to work with the results of SQL queries.
n order to help with this, when we select columns, we can rename them using the AS statement. Here's an example:


SELECT AVG(ShareWomen) AS average_female_share
FROM recent_grads;
This query will result in the following output:

average_female_share
0.5225502029537575

Instructions
Write a query that selects the following items, in order, and renames them with AS:
SUM(Men) as total_men.
SUM(Women) as total_women.
*/
select
SUM(Men) as total_men,
SUM(Women) as total_women
from recent_grads;
/* Console Outputs or results
Output
[["total_men", "total_women"], [2878263, 3897752]]
*/



/*
4: Practice: Using GROUP BY
Now that we understand the GROUP BY statement better, let's practice with it to compute some summary statistics by group in the recent_grads table.

Instructions
Find the percentage of graduates that are employed in each major category.
Use the SELECT statement to select the following columns and aggregates in a query:
Major_category
AVG(Employed) / AVG(Total) as share_employed
Use the GROUP BY statement to group the query by the Major_category column.
*/
select
Major_category,
AVG(Employed) / AVG(Total) as share_employed
from recent_grads
group by 1;
/* Console Outputs or results
Output
[["Major_category", "share_employed"], ["Agriculture & Natural Resources", 0.8369862842425075],
["Arts", 0.8067482429367457], ["Biology & Life Science", 0.6671565365683841], ["Business", 0.8359659576036412],
["Communications & Journalism", 0.8422291333949735], ["Computers & Mathematics", 0.7956108197773972], ["Education", 0.858190149321534],
["Engineering", 0.7819666916550562], ["Health", 0.8033741337996244], ["Humanities & Liberal Arts", 0.7626382682895378],
["Industrial Arts & Consumer Services", 0.8226700668430581], ["Interdisciplinary", 0.7987150292778139],
["Law & Public Policy", 0.8083994483744353], ["Physical Sciences", 0.7506564085422069], ["Psychology & Social Work", 0.790724459311403], ["Social Science", 0.7575825619001975]]
*/



/*
5: The HAVING Statement
Sometimes, we'll want to select a subset of rows after we perform a GROUP BY query.
For instance, in the last screen, we may have only wanted to select rows where share_employed is greater than .8.
We can't use the WHERE clause to do this, because share_employed isn't a column in recent_grads.
Instead, it's a virtual column that's generated by the GROUP BY statement.

In cases like this, where we want to filter on a generated column, we can use the HAVING statement. Here's an example:


SELECT Major_category, AVG(Employed) / AVG(Total) AS share_employed
FROM recent_grads
GROUP BY Major_category
HAVING share_employed > .8;

Note how we're able to use the same column name in the HAVING statement that we specified using the AS statement.
SQL allows us to use custom column names in subsequent statements, including HAVING and WHERE.
The above statement will result in the following output:

Major_category	share_employed
Agriculture & Natural Resources	0.8369862842425075
Arts	0.8067482429367457
Business	0.8359659576036412
Communications & Journalism	0.8422291333949735
Note how only categories where share_employed is greater than .8 are shown above. This is because the HAVING statement filters out the other rows.

Instructions
Find all the major categories where the share of graduates with low wage jobs is greater than .1.
Use the SELECT statement to select the following columns and aggregates in a query:
Major_category
AVG(Low_wage_jobs) / AVG(Total) as share_low_wage
Use the GROUP BY statement to group the query by the Major_category column.
Use the HAVING statement to only select rows where share_low_wage is greater than .1.
*/
select
Major_category,
AVG(Low_wage_jobs) / AVG(Total) as share_low_wage
from recent_grads
group by 1
having share_low_wage > 0.1
/* Console Outputs or results
Output
[["Major_category", "share_low_wage"], ["Arts", 0.16833085991095678], ["Communications & Journalism", 0.1263241815481876],
["Humanities & Liberal Arts", 0.13208721344194835], ["Industrial Arts & Consumer Services", 0.11571334076033978],
["Law & Public Policy", 0.11568503743572278], ["Psychology & Social Work", 0.11693384919554187], ["Social Science", 0.10223297343603174]]
*/



/*
6: The ROUND Function
In the last screen, the percentages we got as results were very long and hard to read -- they looked like 0.16833085991095678. We can use the SQL ROUND function to round values when we query them.


SELECT Major_category, ROUND(ShareWomen, 2) AS rounded_share_women
FROM recent_grads;
The above SQL query will round the ShareWomen column to 2 decimal places, and display the results. Here's a truncated view of the results:

Major_category	rounded_share_women
Engineering	0.12
Engineering	0.1
By specifying different values to the ROUND function, such as ROUND(ShareWomen, 3), we can round to different numbers of decimal places.

Instructions
Write a SQL query that returns the following columns of recent_grads, in the specified order:
ShareWomen rounded to 4 decimal places.
Major_category
Limit the results to 10 rows.
*/
select
ROUND(ShareWomen, 4),
Major_category
from recent_grads
limit 10;
/* Console Outputs or results
Output
[["ROUND(ShareWomen, 4)", "Major_category"], [0.1206, "Engineering"], [0.1019, "Engineering"], [0.153, "Engineering"],
[0.1073, "Engineering"], [0.3416, "Engineering"], [0.145, "Engineering"], [0.5357, "Business"], [0.4414, "Physical Sciences"],
[0.1398, "Engineering"], [0.4378, "Engineering"]]
*/



/*
7: Nesting Functions
In a previous screen, we used the following query:


SELECT Major_category, AVG(Employed) / AVG(Total) AS share_employed
FROM recent_grads
GROUP BY Major_category
HAVING share_employed > .8;
This displayed very long fractional values for share_employed. We can update this with the ROUND function to round the results to 3 decimal places:


SELECT Major_category, ROUND(AVG(Employed) / AVG(Total), 3) AS share_employed
FROM recent_grads
GROUP BY Major_category
HAVING share_employed > .8;
This will result in the following:

Major_category	share_employed
Agriculture & Natural Resources	0.837
Arts	0.807

Instructions
Use the SELECT statement to select the following columns and aggregates in a query:
Major_category
AVG(College_jobs) / AVG(Total) as share_degree_jobs
Use the ROUND function to round share_degree_jobs to 3 decimal places.
Group the query by the Major_category column.
Only select rows where share_degree_jobs is less than .3.
*/
select
Major_category,
ROUND(AVG(College_jobs) / AVG(Total),3) as share_degree_jobs
from recent_grads
group by 1
having share_degree_jobs < 0.3
/* Console Outputs or results
Output
[["Major_category", "share_degree_jobs"], ["Agriculture & Natural Resources", 0.248], ["Arts", 0.265], ["Business", 0.114],
["Communications & Journalism", 0.22], ["Humanities & Liberal Arts", 0.27], ["Industrial Arts & Consumer Services", 0.249],
["Law & Public Policy", 0.163], ["Social Science", 0.215]]
*/



/*
8: Next Steps
In this mission, we covered the GROUP BY and HAVING statements.
With these statements, we can calculate powerful summary statistics in SQL quickly.
In the next few missions, we'll learn more about working with SQL tables, and inserting and modifying data.
*/
