03/2017  
Dataquest : Data Analyst Path  
Step 4: Working With Data Sources  
SubStep :  SQL and Databases: Intermediate : Modifying data  
samedi, 11. mars 2017 04:49 



---
# 1: Modifying Data In Tables  

There are many times when we don't just want to query data from SQL tables, and instead we want to modify the existing data or add new data. Modifying data in SQL tables is possible through 3 statements:  

- INSERT -- adds new data.
- UPDATE -- changes the values of some columns in existing data.
- DELETE -- removes existing data.

In this mission, we'll cover these 3 statements. As we do so, we'll be working with factbook.db, a SQLite database that contains information about each country in the world. We'll be working with a table in the file called facts. Each row in facts represents a single country, and contains several columns, including:  

- name -- the name of the country.
- area -- the total land and sea area of the country.
- population -- the population of the country.
- birth_rate -- the birth rate of the country.
- created_at -- the date the record was created.
- updated_at -- the date the record was updated.

Here are the first few rows of facts:  

see img/img7.png


---
# 2: Working With Dates In SQL  

Dates are an extremely important part of querying and analyzing data. Some common use cases are segmenting records by date, figuring out how many events occurred on each date, and finding all the dates on which a particular event occurred.  

Because of how common it is to use dates when querying data, SQL has built-in support for handling dates. It makes it easy to query based on date and time ranges. We can query a date range from the facts table using the following syntax:  


>SELECT * FROM facts WHERE created_at < "2015-11-01" AND created_at > "2015-10-30";

Here's what's happening in this query:  

- SQL is comparing the created_at column in facts to 2015-11-01, and selecting any rows where created_at is less.
- SQL is comparing the created_at column in facts to 2015-10-30, and selecting any rows where created_at is greater.

You may recognize that this looks exactly like some of the WHERE statements you used in previous missions. The only caveat is to put the date you want to compare in quotes so SQL parses the date properly. Dates have a natural ordering, and SQL automatically uses this ordering. For example, 2015-11-01 is greater than 2015-10-30, because it comes afterwards.  

We can also query based on times using the following syntax:  

```sql
SELECT [columnA, columnB, ...]
FROM tableName
WHERE dateColumn < "date1"
AND dateColumn > "date2";
Here's a concrete example:
```
```sql
SELECT * FROM facts 
WHERE created_at < "2015-11-01 14:00"
AND created_at > "2015-10-30 12:00";
```

The above SQL query selects any rows in facts that were created between 12pm on October 30th, 2015, and 2pm on November 1st, 2015. If you're not familiar with the time notation, it's military time, a 24-hour clock which starts at 0:00 (midnight), and ends at 24:00. 9:00 military time is 9am, and 17:00 military time is 5pm. The primary advantage of military time is that we don't need to specify am or pm.   



#### Instructions :

 - Select any rows from facts where updated_at is greater than October 30th, 2015 at 4pm, and updated_at is less than November 2nd, 2015 at 3pm.
 

```sql
 select * from facts where updated_at > "2015-10-30 16:00" and updated_at < "2015-11-02 15:00";
```  


---
# 3: Data Types  

In Python, variables can have data types, such as string, float, or integer. Whereas these data types don't have to be specified upfront in Python, each column in a SQL table has to have a data type specified when the table is created. This helps SQL store and search the data efficiently. Every SQL database engine has slightly different names for data types. Some of the common data types for SQLite are:  

- INTEGER -- similar to the integer type in Python.
- REAL -- similar to the float type in Python.
- FLOAT -- similar to the float type in Python.
- TEXT -- similar to the string type in Python.
- VARCHAR(255) -- similar to the string type in Python.

The reason why SQLite has so many names for similar data types is to provide compatibility with other databases, some of which will only allow one or the other (REAL or FLOAT, for example).  

To see the data types of each column in a table, you can use the PRAGMA statement:  

>PRAGMA table_info(tableName);

Here's a concrete example:  

>PRAGMA table_info(table);

We'll cover the PRAGMA statement in more depth later on, but for now it's enough to know that it shows information about a SQL database.  

#### Instructions :

 - Write a SQL query that returns the data type of each column in facts
 

```sql
 PRAGMA table_info(facts);
```  

#### Results :  

	Output
	[["cid", "name", "type", "notnull", "dflt_value", "pk"], [0, "id", "INTEGER", 1, null, 1], [1, "code", "varchar(255)", 1, null, 0], [2, "name", "varchar(255)", 1, null, 0], [3, "area", "integer", 0, null, 0], [4, "area_land", "integer", 0, null, 0], [5, "area_water", "integer", 0, null, 0], [6, "population", "integer", 0, null, 0], [7, "population_growth", "float", 0, null, 0], [8, "birth_rate", "float", 0, null, 0], [9, "death_rate", "float", 0, null, 0], [10, "migration_rate", "float", 0, null, 0], [11, "created_at", "datetime", 0, null, 0], [12, "updated_at", "datetime", 0, null, 0]]

---
# 4: Primary Keys
Every SQL table has a primary key. A primary key is a column or combination of columns that are unique for each row in the table. The primary key is how SQL uniquely identifies each row. Most tables have an integer column called id by default, which is the primary key.

If you look back on the output of the PRAGMA statement in the last screen, you'll see something like this:

see img/img8.png

There's a column called pk, which is an integer. It's set to 1 (or True) for the first row, and 0 (or False) for the others. So the first column in the facts table, id, is the primary key.

The most common name for the primary key column in a SQL table is id, although it doesn't have to be.  


#### Instructions :

 - Write a SQL query that uses the ORDER BY and LIMIT statements to select the entire row that has the highest id
 

```sql
 select * from facts order by id desc limit 1;
```  

#### Results :  

	Output
	[["id", "code", "name", "area", "area_land", "area_water", "population", "population_growth", "birth_rate", "death_rate", "migration_rate", "created_at", "updated_at"], [261, "xx", "World", null, null, null, 7256490011, 1.08, 18.6, 7.8, null, "2015-11-01 13:39:09.910721", "2015-11-01 13:39:09.910721"]]


---
# 5: Inserting Data Into A Table  

Sometimes, we'll receive new rows that we want to add to a SQL table. We can insert a row into a table using the INSERT SQL statement. Here's an example INSERT statement:  

```sql
INSERT INTO tableName
VALUES (value1, value2, ...);
```

Here's a concrete example:  

```sql
INSERT INTO facts
VALUES (262, "dq", "DataquestLand", 60000, 40000, 20000, 500000, 100, 50, 10, 20, "2016-02-25 12:00:00", "2016-02-25 12:00:00");
```

There's quite a bit happening, so let's unpack each part:  

- INSERT INTO -- this indicates that we're adding a row to a particular table.
- facts -- the table we're inserting the row into.
- VALUES -- this indicates that we're specifying which values to insert.
	- 262 -- the primary key -- this is one higher than the current maximum primary key.
	- The other values we're inserting are comma separated, and match the column order in facts.
	- Date and text fields are in quotes, but integer and float fields aren't.
	- Dates must be in the yyyy-mm-dd HH:MM:SS format.

After the above query runs, we'll have a new row in facts that we can work with like any other row.  



#### Instructions :

 - Write a SQL query that inserts a row into facts with the following values:
 
 see img/img9.png
 
```sql
 INSERT INTO facts
VALUES (262, "dq", "DataquestLand", 60000, 40000, 20000, 500000, 100, 50, 10, 20, "2016-02-25 12:00:00", "2016-02-25 12:00:00");
```  

---
# 6: Missing Values  

We've worked with data sets that have missing values before. Because it's so common for data to be missing, SQL has explicit support for handling missing, or NULL, values. You can retrieve any rows where a specific column is NULL by using the following syntax:  

```sql
SELECT * from tableName
WHERE columnName IS NULL;
```

Here's a concrete example:  

```sql
SELECT * FROM facts 
WHERE area IS NULL;
```

If a value in a row is missing when you add it, you can also use NULL with the INSERT INTO statement:  

```sql
INSERT INTO facts
VALUES (262, "dq", "DataquestLand", NULL, 40000, 20000, 500000, 100, 50, 10, 20, "2016-02-25 12:00:00", "2016-02-25 12:00:00");
```
Some columns may specify a NOT NULL constraint, which specifies that they can't contain any missing values. If you try to insert a NULL value into one of these columns, you'll get an error.  


#### Instructions :

 - Write a SQL query that inserts a row into facts with the following values:
 

```sql
 INSERT INTO facts
VALUES (263, "dq", "DataquestLand", NULL, NULL, 20000, 500000, 100, 50, 10, 20, "2016-02-25 12:00:00", "2016-02-25 12:00:00");
```  

---
# 7: Updating Rows  

Let's say we wanted to simulate a takeover of Australia by New Zealand and rename Australia. You can use the UPDATE statement for this:  

```sql
UPDATE tableName
SET column1=value1, column2=value2, ...
WHERE column1=value3, column2=value4, ...
```

Here's a concrete example:  

```sql
UPDATE facts
SET name="New Zealand", code="nz"
WHERE name="Australia"
```

The above will rename any rows where name equals Australia to New Zealand. Let's break down what's happening:

- UPDATE -- indicates that we're updating rows in the table.
- facts -- the table we're updating.
- SET -- indicates which columns we're going to update.
- name="New Zealand" -- set the values in the name column to the value New Zealand.
- code="nz" -- set the values in the code column to the value nz.
- WHERE -- specifies which rows to update.
- name="Australia" -- only update rows where the name column equals Australia.

The above query updates two columns, name, and code, but we could easily update one column or more columns. We can also use AND and OR in the WHERE statement to provide complex logic around which rows to update.  

It's very important to specify a WHERE clause when running an UPDATE statement -- if you don't, all rows will be updated.   



#### Instructions :

 - Write a SQL query that uses the UPDATE statement to update any rows where name is United States to DataquestLand.
 

```sql
 UPDATE facts
SET name="DataquestLand"
WHERE name="United States";
```  


---
# 8: Deleting Rows  

Let's say we wanted to remove any rows associated with the United States. We'd have to use the DELETE statement like this:  

```sql
DELETE FROM tableName
WHERE column1=value1, column2=value2, ...;
```

Here's a concrete example:  

```sql
DELETE FROM facts
WHERE name="United States";
```

The above query will delete any rows where name equals United States. Here's a breakdown of what's happening:  

- DELETE FROM -- indicates that we're deleting rows.
- facts -- the table we're deleting rows from.
- WHERE -- specifies which rows to delete.
- name="United States" -- only delete rows where name equals United States.

It's very important to specify a WHERE clause for the DELETE statement -- if you don't, all rows will be deleted.   



#### Instructions :

 - Write a SQL query that removes all the rows in facts where name equals Canada.
 

```sql
 DELETE FROM facts
WHERE name="Canada";
```  


---
# 9: Conclusion  

In this mission, we covered how to modify data in SQL tables, using the INSERT, UPDATE, and DELETE statements. In the next mission, we'll dive into how to setup and modify SQL tables, including changing which columns are in the table.  