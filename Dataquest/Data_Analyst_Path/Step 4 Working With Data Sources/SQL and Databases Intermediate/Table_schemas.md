03/2017  
Dataquest : Data Analyst Path  
Step 4: Working With Data Sources  
SubStep :  SQL and Databases: Intermediate : Table schemas  
samedi, 11. mars 2017 05:31 

---
# 1: Table Schema  

In the last mission, we looked at a database called factbook.db, which contained information on each country in the world.  

We looked at the facts table inside factbook.db. Here are the first few rows of facts:  

see img/img11.png

In the last mission, we also looked at the columns for facts, and the corresponding datatypes. Here's an excerpt:  

see img/img12.png

This definition, which contains information like column names, data types, and which column is the primary key, is called a table schema.  

Table schemas let us create new tables to store data. What we store may change over time, so SQL also allows us to modify the schema of a table over time.  

---
# 2: Adding Columns  

Let's say we want to add a column called awesomeness to track how awesome all the countries in the facts table are. We would need to add a column to facts to track this.  

We can add a column with the ALTER TABLE statement:  

```sql
ALTER TABLE tableName
ADD columnName dataType;
```

Here's a concrete example:  

```sql
ALTER TABLE facts
ADD awesomeness integer;
```

The above code will add a column called awesomeness to the facts table. Let's break down what's happening:  

- ALTER TABLE -- indicates that we're making a change to the table schema.
- facts -- the table we're altering.
- ADD -- indicates that we're adding a column.
- awesomeness -- the name of the column we're adding.
- integer -- the data type of the column we're adding. We talked about data types in the last mission, and here's a full list.

When you add a column, all the values associated with it will be NULL to begin with.   

#### Instructions :

 - Write a SQL query that adds a column called leader to the facts table, with the data type text.
 

```sql
ALTER TABLE facts
ADD leader text;
```  

---
# 3: Removing Columns  

You can also use the ALTER TABLE statement to remove columns that are no longer needed:  

```sql
ALTER TABLE tableName
DROP COLUMN columnName;
```

Here's a concrete example:  

```sql
ALTER TABLE facts
DROP COLUMN awesomeness;
```

The above query would remove the column awesomeness from the table facts. This command is only possible in certain SQL versions, and isn't possible with the SQLite database engine, so we won't practice it right now.   


---
# 4 : Creating Tables  

We can create a new table in factbook.db using a new table schema. Let's say that we want to create a table that keeps track of leaders of countries. We would use the CREATE TABLE statement to do this:  

```sql
CREATE TABLE dbName.tableName(
   column1 dataType1 PRIMARY KEY,
   column2 dataType2,
   column3 dataType3,
   ...
);
```

Here's a concrete example:  

```sql
CREATE TABLE factbook.leaders(
   id integer PRIMARY KEY,
   name text,
   country text
);
```

Let's break down each piece of this example:   

- CREATE TABLE -- indicates that we want to create a table.
- factbook.leaders -- we're creating a table called leaders in the factbook database. The . separates the two.
- ( -- indicates that we're specifying the columns and data types inside.
- id integer PRIMARY KEY -- we're creating a column called id that has the data type integer, and is the primary key for the table. As we mentioned in the last mission, every table needs a primary key, and it's typical to make an integer column called id the primary key.
- name text -- we're creating a second column called name with the data type text.
- country text -- we're creating a third column called country with the data type text.
- ) -- indicates that we're done specifying columns.

When we run the above query, we'll end up with a new table called leaders that has three columns, id, name, and country. The columns will be in the order they are specified in the query.  

---
# 5: Relations Between Tables  

In the past screen, we created a table called leaders. Instead of directly referring to the row in the facts table that contained the country the leader was from, we had to create a country column in leaders that contains the full name of the country. Here's how the leaders table might look:  

see img/img13.png

As you can see, the country is just a string. Querying any leaders associated with a country requires us to specify the country name as a string:  

```sql
SELECT * from leaders
WHERE country="United States";
```
It also makes querying the country associated with a particular leader difficult. We first need to extract the country column as a string from the leaders table, then we need to query the facts table with the string:  

```sql
SELECT * from facts
WHERE name="United States";
```

There's no way to combine both sets of records with this table schema, or query them more efficiently.

Fortunately, SQL databases are commonly known as relational databases because they support relations between tables. These relations enable us to efficiently query across multiple tables.

The most common type of relation is known as a foreign key. A SQL foreign key points from a record in one table to a record in another table. Here's an example of creating a table that contains a foreign key:

```sql
CREATE TABLE factbook.leaders(
   id integer PRIMARY KEY,
   name text,
   country integer,
   worth float,
   FOREIGN KEY(country) REFERENCES facts(id)
);
```

We've seen the CREATE TABLE statement before, but here are the main changes:  

- country is now an integer column, because it "points" to the id column of the facts table.
- FOREIGN KEY -- specifies that we're setting one column in our table schema to be a foreign key to another table.
- (country) -- specifies the column that is a foreign key.
- REFERENCES -- indicates the table and column we're referencing with the foreign key.
- facts -- the table that we're referencing with the foreign key.
- (id) -- the column in facts that we're referencing with our foreign key.

After setting up this table, the country column of leaders can only be assigned integer values that exist in the id column of facts. This will point to a row in the facts table, and indicate that a particular leader represents a particular country.  

Here's a diagram that may help you visualize what's happening:  

see img/img14.png

The above diagram shows how the integer value in the country column of leaders "points" to the corresponding value in the id column of facts, and thus associates a row in leaders with a row in facts.  


---
# 6: Creating A Table With Relations  

Now that we understand foreign keys and relations, we can create a table that contains a foreign key.  


#### Instructions :

Write a SQL query that creates a table called states in the factbook database that will contain information on each state in a country. It should have the following columns:  

- id -- integer data type, should be a primary key.
- name -- text data type.
- area -- integer data type.
- country -- integer foreign key to the id column of the facts table.
 

```sql

CREATE TABLE factbook.states(
    id integer PRIMARY KEY,
    name text,
    area integer,
    country integer,
    FOREIGN KEY(country) REFERENCES facts(id)
);
```  

---
# 7: Querying Across Foreign Keys  

We can use the INNER JOIN statement to make querying across foreign key relationships easier:  

```sql
SELECT [column1, column2, ...] from tableName1
INNER JOIN tableName2
ON tableName1.column3 == tableName2.column4;
```

Here's a concrete example:  

```sql
SELECT * from states
INNER JOIN facts
ON states.country == facts.id;
```

We've seen the basic SELECT statement before, so here's what's new:  

- INNER JOIN -- indicates that we're combining data from two tables into one query.
- facts -- specifies the table we're joining with states.
- ON -- indicate how SQL matches a record in states with a record in facts.
- facts.id -- specifies that the id column in the facts table will be used to join.
- states.country -- specifies that the country column in the states table will be used to join.

You may recall from a previous screen that the country column of states "points" to the id column of facts. Therefore, we're saying that we're finding the associated row in facts for each row in states.  

We'll get back each row of states, but with information from facts added in. This enables us to get all the information we need in one place, without having to resort to multiple queries.   



#### Instructions :

Write a SQL query that:  

 - Uses the SELECT statement to query all the columns of the landmarks table.
 - Uses INNER JOIN to combine data from the landmarks table with data from the facts table.
	 - Uses the id column from facts and the country column of landmarks to perform the join.
 
```sql
SELECT * from landmarks
INNER JOIN facts
ON landmarks.country == facts.id;
```  


#### Results :  

	Output
	[["id", "name", "country", "id", "code", "name", "area", "area_land", "area_water", "population", "population_growth", "birth_rate", "death_rate", "migration_rate", "created_at", "updated_at", "leader"], [1, "Statue of Liberty", 186, 186, "us", "United States", 9826675, 9161966, 664709, 321368864, 0.78, 12.49, 8.15, 3.86, "2015-11-01 13:35:14.898271", "2015-11-01 13:35:14.898271", null], [2, "Golden Gate Bridge", 186, 186, "us", "United States", 9826675, 9161966, 664709, 321368864, 0.78, 12.49, 8.15, 3.86, "2015-11-01 13:35:14.898271", "2015-11-01 13:35:14.898271", null], [3, "Washington Monument", 186, 186, "us", "United States", 9826675, 9161966, 664709, 321368864, 0.78, 12.49, 8.15, 3.86, "2015-11-01 13:35:14.898271", "2015-11-01 13:35:14.898271", null]]

---
# 8: Types Of Joins  

There are a few different types of joins. Before diving into them, it's helpful to know that each table in a JOIN statement has a side:  

```sql
SELECT * from landmarks
INNER JOIN facts
ON landmarks.country == facts.id;
```

In the above JOIN statement, landmarks is the left side table, and facts is the right side table. The table that is specified first is the left table, and the second is the right side table. Values come from the left and right sides when the JOIN is performed:  

see img/img15.png

In the above table, id, name, and country come from landmarks. id_1, code, name_1, area, and the rest of the columns come from facts. The _1 suffixes are because some columns from the tables have the same names, so the suffixes are to disambiguate. The records are combined via the JOIN when country from the landmarks table matches id_1 from the facts table.  

Given that, here are the types of joins:  

 - INNER JOIN -- only displays rows where there is a match for the ON condition in both tables. Any rows that aren't matched are excluded.
 - LEFT OUTER JOIN -- if there is no match for a row from the table on the left side of the ON condition, it is shown with NULL values for all the right side values.  
 - RIGHT OUTER JOIN -- if there is no match for a row from the table on the right side of the ON condition, it is shown with NULL values for all the left side values.  
 
 INNER JOIN is the most common type of join, but LEFT OUTER JOIN is also occassionally used. It's very uncommon to use RIGHT OUTER JOIN, and SQLite doesn't support it.  

From a syntax points of view, using the statements is the exact same, you just swap out INNER JOIN for LEFT OUTER JOIN.  

#### Instructions :

Write a SQL query that:  

 - Uses the SELECT statement to query all the columns of the landmarks table.
 - Uses LEFT OUTER JOIN to combine data from the landmarks table with data from the facts table.
	- Uses the id column from facts and the country column of landmarks to perform the join.
 

```sql
SELECT * from landmarks
LEFT OUTER JOIN facts
ON landmarks.country == facts.id;
```  


#### Results :  

	Output
	[["id", "name", "country", "id", "code", "name", "area", "area_land", "area_water", "population", "population_growth", "birth_rate", "death_rate", "migration_rate", "created_at", "updated_at", "leader"], [1, "Statue of Liberty", 186, 186, "us", "United States", 9826675, 9161966, 664709, 321368864, 0.78, 12.49, 8.15, 3.86, "2015-11-01 13:35:14.898271", "2015-11-01 13:35:14.898271", null], [2, "Golden Gate Bridge", 186, 186, "us", "United States", 9826675, 9161966, 664709, 321368864, 0.78, 12.49, 8.15, 3.86, "2015-11-01 13:35:14.898271", "2015-11-01 13:35:14.898271", null], [3, "Washington Monument", 186, 186, "us", "United States", 9826675, 9161966, 664709, 321368864, 0.78, 12.49, 8.15, 3.86, "2015-11-01 13:35:14.898271", "2015-11-01 13:35:14.898271", null]]


---
# 9: Next Steps  

In this mission, we covered the basics of modifying table schema, creating tables, and defining relations. Relations allow us to harness the full power of SQL, and query more efficiently. In the next few missions, we'll cover relations in more depth, and talk about optimizing table performance.  