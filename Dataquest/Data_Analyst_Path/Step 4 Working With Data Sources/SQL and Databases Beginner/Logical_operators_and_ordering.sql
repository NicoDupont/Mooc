/*
03/2017
Dataquest : Data Analyst Path
Step 4: Working With Data Sources
SubStep : SQL and Databases: Beginner : Logical operators and ordering
*/

/*
1: Logical Operators

In the previous mission, we covered the basics of databases, SQL, and the SELECT statement.
In this mission, we'll explore how to express more complex filtering criteria.
We'll continue to work with the dataset, recent-grads.csv, which is loaded into the table recent_grads. Here's a preview of the dataset:

Rank 	Major_code 	Major 	Major_category 	Total 	Sample_size 	Men 	Women 	ShareWomen 	Employed
1 	2419 	PETROLEUM ENGINEERING 	Engineering 	2339 	36 	2057 	282 	0.120564 	1976
2 	2416 	MINING AND MINERAL ENGINEERING 	Engineering 	756 	7 	679 	77 	0.101852 	640
3 	2415 	METALLURGICAL ENGINEERING 	Engineering 	856 	3 	725 	131 	0.153037 	648
4 	2417 	NAVAL ARCHITECTURE AND MARINE ENGINEERING 	Engineering 	1258 	16 	1123 	135 	0.107313 	758
5 	2405 	CHEMICAL ENGINEERING 	Engineering 	32260 	289 	21239 	11021 	0.341631 	25694

We learned about the comparison operators in SQL in the last lesson:

    Less than: <
    Less than or equal to: <=
    Greater than: >
    Greater than or equal to: >=
    Equal to: =
    Not equal to: !=

which were useful for expressing our filtering criteria, or condition, in the WHERE statement.
What if we want to use multiple filtering criteria to specify the data we want from the database?

Logical operators are keywords you can use to combine filtering criteria to express more specific conditions. Here are the 2 basic logical operators you will often use:

    Condition1 or Condition2: OR
    Condition1 and Condition2: AND

*/


/*
2: And operator

The following is psuedo-code to help you conceptualize how the AND statement is used with a WHERE statement:

SELECT [column1, column2,...] FROM [table1]

WHERE [condition1] AND [condition2]

We can now write a SQL query that returns all majors that had women as the majority and more than 10000 people employed.

Let's see what that query would look like:

SELECT Major,ShareWomen,Employed FROM recent_grads

WHERE ShareWomen>0.5 AND Employed>10000;

We want the database to return all rows where both conditions are true:

    ShareWomen > 0.5
    Employed > 10000

Instructions

    Run the query above, which returns all majors that had women as the majority and more than 10000 people employed.

    Use the LIMIT statement to limit the results to just the first 10 results.

*/
SELECT Major,ShareWomen,Employed FROM recent_grads
WHERE ShareWomen>0.5 AND Employed>10000 LIMIT 10;
/*
Output
[["Major", "ShareWomen", "Employed"], ["COMPUTER SCIENCE", 0.578766338, 102087], ["NURSING", 0.896018988, 180903], ["COMPUTER AND INFORMATION SYSTEMS", 0.7077185020000001, 28459], ["INTERNATIONAL RELATIONS", 0.632986838, 21190], ["AGRICULTURE PRODUCTION AND MANAGEMENT", 0.59420765, 12323], ["CHEMISTRY", 0.5051405379999999, 48535], ["BUSINESS MANAGEMENT AND ADMINISTRATION", 0.580948004, 276234], ["BIOCHEMICAL SCIENCES", 0.515406449, 25678], ["HUMAN RESOURCES AND PERSONNEL MANAGEMENT", 0.672161443, 20760], ["MISCELLANEOUS HEALTH MEDICAL PROFESSIONS", 0.702020202, 10076]]
*/


/*
3: Or operator

We used the AND operator to specify that our filter needs to pass 2 Boolean conditions, both of which had to evaluate to True for the record to be included in the result set.
If we instead want to specify a filter that met either of the conditions, we would use the OR operator.

SELECT [column1, column2,...] FROM [table1]

WHERE [condition1] OR [condition2]

We'll dive straight into a practice problem since the OR and AND operators are used in similar ways.
Instructions

Write a SQL query that will return the first 20 majors that either:

    had a Median salary greater than or equal to 10,000 or
    less than or equal to 1,000 Unemployed people.

We only want to include the following columns in the results with the following order:

    Major
    Median
    Unemployed

*/
select Major, median, Unemployed from recent_grads where Median >= 10000 or Unemployed <= 1000 LIMIT 20

/*
Output
[["Major", "Median", "Unemployed"], ["PETROLEUM ENGINEERING", 110000, 37], ["MINING AND MINERAL ENGINEERING", 75000, 85], ["METALLURGICAL ENGINEERING", 73000, 16], ["NAVAL ARCHITECTURE AND MARINE ENGINEERING", 70000, 40], ["CHEMICAL ENGINEERING", 65000, 1672], ["NUCLEAR ENGINEERING", 65000, 400], ["ACTUARIAL SCIENCE", 62000, 308], ["ASTRONOMY AND ASTROPHYSICS", 62000, 33], ["MECHANICAL ENGINEERING", 60000, 4650], ["ELECTRICAL ENGINEERING", 60000, 3895], ["COMPUTER ENGINEERING", 60000, 2275], ["AEROSPACE ENGINEERING", 60000, 794], ["BIOMEDICAL ENGINEERING", 60000, 1019], ["MATERIALS SCIENCE", 60000, 78], ["ENGINEERING MECHANICS PHYSICS AND SCIENCE", 58000, 23], ["BIOLOGICAL ENGINEERING", 57100, 589], ["INDUSTRIAL AND MANUFACTURING ENGINEERING", 57000, 699], ["GENERAL ENGINEERING", 56000, 2859], ["ARCHITECTURAL ENGINEERING", 54000, 170], ["COURT REPORTING", 54000, 11]]
*/


/*
4: Grouping operators

There is a certain class of questions that can't be answered using just the techniques we've learned so far.
If we wanted to write a query that returned all Engineering majors that either had majority women or an unemployment rate below the August 2015 unemployment rate of 5.1%, we'll need to use parentheses to express this more complex logic.

The 3 raw conditions we'll need:

Major_category = 'Engineering'

ShareWomen >= 0.5

Unemployment_rate < 0.051

How the SQL query looks like using parantheses:

select Major, Major_category, ShareWomen, Unemployment_rate

from recent_grads

where (Major_category = 'Engineering') and (ShareWomen > 0.5 or Unemployment_rate < 0.051);

The first thing you may notice is that we didn't capitalize any of the operators or statements in the query.
SQL is case-insensitive with its built-in keywords which means we don't have to capitalize operators like AND or statements like SELECT.

The second thing you may notice is how we grouped logic we wanted to be evaluated together in parentheses.
This is very similar to how we group calculations in math together with a particular order.
The parentheses makes it explictly clear to the database that we want all the rows where both the expressions in the statements evaluate to True:

(Major_category = 'Engineering' and ShareWomen > 0.5) -> True or False

(ShareWomen > 0.5 or Unemployment_rate < 0.051) -> True or False

If we had written the where statement without any parentheses, the database would guess what our intentions are and will actually execute the following query instead:

where (Major_category = 'Engineering' and ShareWomen > 0.5) or (Unemployment_rate < 0.051)

Leaving parentheses out implies that we want the calculation to happen from left to right in the order the logic is written and wouldn't return us the data we want.
 Let's now run our intended query and see the results!
Instructions

    Run the query we explored above, which returns all Engineering majors that:
        either had majority women,
        or had an unemployment rate below 5.1%, the August 2015 unemployment rate.
    We're interested in returning the Major, Major_category, ShareWomen, and Unemployment_rate columns.

*/
select Major, Major_category, ShareWomen, Unemployment_rate
from recent_grads
where (Major_category = 'Engineering') and (ShareWomen > 0.5 or Unemployment_rate < 0.051);
/*
Output
[["Major", "Major_category", "ShareWomen", "Unemployment_rate"], ["PETROLEUM ENGINEERING", "Engineering", 0.120564344, 0.018380527], ["METALLURGICAL ENGINEERING", "Engineering", 0.153037383, 0.024096386], ["NAVAL ARCHITECTURE AND MARINE ENGINEERING", "Engineering", 0.107313196, 0.050125313], ["MATERIALS SCIENCE", "Engineering", 0.310820285, 0.023042836], ["ENGINEERING MECHANICS PHYSICS AND SCIENCE", "Engineering", 0.183985189, 0.006334343], ["INDUSTRIAL AND MANUFACTURING ENGINEERING", "Engineering", 0.34347321799999997, 0.042875544], ["MATERIALS ENGINEERING AND MATERIALS SCIENCE", "Engineering", 0.292607004, 0.027788805], ["ENVIRONMENTAL ENGINEERING", "Engineering", 0.558548009, 0.093588575], ["INDUSTRIAL PRODUCTION TECHNOLOGIES", "Engineering", 0.75047259, 0.028308097], ["ENGINEERING AND INDUSTRIAL MANAGEMENT", "Engineering", 0.174122505, 0.03365166]]

*/



/*
5: Practice grouping operators

In this step, you'll practice grouping operators to express more complex logic.
Instructions

Find all majors that meet the following criteria:

    Major_category of Business or Arts or Health

and

    Employed students greater than 20,000 or Unemployment_rate below 5.1%

We're only interested in the following columns (in the following order):

    Major
    Major_category
    Employed
    Unemployment_rate

Return all the results (no limit).
*/
select
    Major
    ,Major_category
    ,Employed
    ,Unemployment_rate
from recent_grads
where Major_category in ("Business","Arts","Health")
and (Employed > 20000 or Unemployment_rate < 0.051);



/*
6: Order by

The database has been returning all results ordered by the Rank column because that's how the original dataset was ordered.
Since this may not make sense for all queries, SQL comes with a statement, ORDER BY, that allows us to specify how we want the results ordered.
To use the ORDER BY statement, we need to specify the column we'd like the database to use to order the results by and whether we want them ordered in ascending (low to high) or descending order.

SELECT [column1, column2,...] FROM [table1]

WHERE [conditions]..

ORDER BY column1 [ASC or DESC]

We use ASC to order from low to high and DESC to order from high to low. SQL uses the standard methods of ordering -- alphabetically for text fields and numerically for numeric fields.
This means that if you order by a text field in descending order, the results will be reverse alphabetical order.

The following code selects the Employed column, ordered in ascending order (low to high), and limits the results to the first 10:

select Employed

from recent_grads

order by Employed asc

limit 10;

This query returns the lowest 10 values in the Employed column.
The values in Employed are ordered in ascending order first then the first 10 values under the new ordering are returned.

Instructions

    Return the first 10 values in the Major column in reverse alphabetical order.

*/
select Major from recent_grads order by Major desc limit 10;


/*
7: Order using multiple columns

SQL also allows us to specify multiple columns in the ORDER BY statement if we'd like the database to order the results of the query first using the first column, then the second one, and so forth.
The database will order the results by the first column and then will order by the second column specified if multiple rows have the same values for the first column.
Here's how the relevant psuedocode looks like:

select [column1, column2..]

from table_name

order by column1 (asc or desc), column2 (asc or desc)

Ordering by multiple columns is especially useful when working with people's names, where the database will have separate columns for First Name and Last Name and you want the results to be ordered, or alphabetized in this case, by Last Name first then First Name.
After alphabetizing all last names, the database will alphabetize by First Name for all rows containing the same values for Last Name.
Last Name	First Name
Khan	Sal
Khan	Tony
Prescot	Pete
Prescot	Russ

Now it's your turn!
Instructions

Write a query that orders the majors by Major in ascending order then by Median salary in descending order. We're interested in selecting only these columns in the following order:

    Major_category
    Median
    Major

Limit the query to just the first 20 results.
*/
select
    Major_category
    ,Median
    ,Major
from recent_grads
order by 3 asc, 2 desc
limit 20;


/*
8: Next steps

Now that you've had some practice writing and running SQL queries, it's time to complete a challenge.
The next mission in this course is a challenge that will let you apply what you've learned so far.
*/
