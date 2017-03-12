03/2017  
Dataquest : Data Analyst Path  
Step 4: Working With Data Sources  
SubStep :  SQL and Databases: Intermediate : Guided Project: Creating relations in SQLite  
dimanche, 12. mars 2017 12:36 


---
# 1: Introduction To The Data

So far in the SQL and Databases: Intermediate course, we explored how to modify existing data in a table and create our own schemas. In the Database Normalization and Relations mission, we then learned about the benefits of normalization and how to query an existing database on Academy Award nominations. In the previous guided project, we walked through how to clean and prepare the original CSV dataset on Academy Award nominations and export the data into a SQLite database as a single, denormalized table. In this guided project, we will walk through how to normalize our single table into multiple tables and how to create relations between them.  

If you're new to either our guided projects or Jupyter notebook in general, you can learn more here. You can find the solutions to this guided project here.  

As a quick refresher, the Academy Awards, also known as the Oscars, is an annual awards ceremony hosted to recognize the achievements in the film industry. There are many different awards categories and the members of the academy vote every year to decide which artist or film should get the award. Each row in our data represents a nomination for an award. Recall that our database file, nominations.db, contains just the nominations table. This table has the following schema:  

- Year - the year of the awards ceremony, integer type.
- Category - the category of award the nominee was nominated for, text type.
- Nominee - the person nominated for the award, text type.
- Movie - the movie the nominee participated in, text type.
- Character - the name of the character the nominee played, text type.
- Won - if this nominee won the award, integer type.

Let's now set up our enviroment and spend some time getting familiar with the data before we start normalizing it.   


#### Instructions :

 - Let's first get everything you need setup.
	- Import sqlite3 into the environment.
	- Connect to nominations.db and assign the Connection instance to conn.
 - Let's now write and run some queries to explore the data.
	- Return the schema using pragma table_info() and assign to schema.
	- Return the first 10 rows using the SELECT and LIMIT statements and assign to first_ten.
	- Since both schema and first_ten are lists, use a for loop to iterate over each element and print each element. This makes our output easier to understand.
 
```python
# 1: Introduction To The Data
import sqlite3
conn = sqlite3.connect("nominations.db")
infos = "pragma table_info(nominations);"
schema = conn.execute(infos).fetchall()
#print(schema)
print("------------")
first_ten = "select * from nominations limit 10"
first_ten = conn.execute(first_ten).fetchall()
#print(first_ten)
print("------------")
for row in schema:
    print(row )
print("------------")   
for row  in first_ten:
    print(row )
```  

#### Results :  

	------------
	------------
	(0, 'Year', 'INTEGER', 0, None, 0)
	(1, 'Category', 'TEXT', 0, None, 0)
	(2, 'Nominee', 'TEXT', 0, None, 0)
	(3, 'Won', 'INTEGER', 0, None, 0)
	(4, 'Movie', 'TEXT', 0, None, 0)
	(5, 'Character', 'TEXT', 0, None, 0)
	------------
	(2010, 'Actor -- Leading Role', 'Javier Bardem', 0, 'Biutiful', 'Uxbal')
	(2010, 'Actor -- Leading Role', 'Jeff Bridges', 0, 'True Grit', 'Rooster Cogburn')
	(2010, 'Actor -- Leading Role', 'Jesse Eisenberg', 0, 'The Social Network', 'Mark Zuckerberg')
	(2010, 'Actor -- Leading Role', 'Colin Firth', 1, "The King's Speech", 'King George VI')
	(2010, 'Actor -- Leading Role', 'James Franco', 0, '127 Hours', 'Aron Ralston')
	(2010, 'Actor -- Supporting Role', 'Christian Bale', 1, 'The Fighter', 'Dicky Eklund')
	(2010, 'Actor -- Supporting Role', 'John Hawkes', 0, "Winter's Bone", 'Teardrop')
	(2010, 'Actor -- Supporting Role', 'Jeremy Renner', 0, 'The Town', 'James Coughlin')
	(2010, 'Actor -- Supporting Role', 'Mark Ruffalo', 0, 'The Kids Are All Right', 'Paul')
	(2010, 'Actor -- Supporting Role', 'Geoffrey Rush', 0, "The King's Speech", 'Lionel Logue')

---
# 2: Creating The Ceremonies Table  

Let's now add information on the host for each awards ceremony. Instead of adding a Host column to the nominations table and having lots of redundant data, we'll create a separate table called ceremonies which contains data specific to the ceremony itself.  

Let's create a ceremonies table that contains the Year and Host for each ceremony and then set up a one-to-many relationship between ceremonies and nominations. In this screen, we'll focus on creating the ceremonies table and inserting the data we need and in the next guided step, we'll focus on setting up the one-to-many relationship.  

The ceremonies table will contain 3 fields:  

- id - unique identifier for each row, integer type.
- Year - the year of the awards ceremony, integer type.
- Host - the host of the awards ceremony, text type.

Before we can create and insert into the ceremonies table, we need to look up the host for each ceremony from 2000 to 2010. While we could represent each row as a tuple and write a SQL query with an INSERT statement to add each row to the ceremonies table, this is incredibly cumbersome.  

The Python sqlite3 library comes with an executemany method that let's us easily mass insert records into a table. The executemany method requires the records we want to insert to be represented as a list of tuples. We then just need to write a single INSERT query with placeholder elements and specify that we want the list of tuples to be dropped into the query.  

Let's first create the list of tuples representing the data we want inserted and then we'll walk through the placeholder query we need to write. We'll skip over creating the ceremonies table for now since we've explored how to create a table earlier in the course.  

Wikipedia lists the host(s) for each awards ceremony. Even though the 2010 ceremony had 2 hosts, we selected just the first host, Steve Martin, to keep things simple. Here's what the list of tuples looks like:  

```python
years_hosts = [(2010, "Steve Martin"),
               (2009, "Hugh Jackman"),
               (2008, "Jon Stewart"),
               (2007, "Ellen DeGeneres"),
               (2006, "Jon Stewart"),
               (2005, "Chris Rock"),
               (2004, "Billy Crystal"),
               (2003, "Steve Martin"),
               (2002, "Whoopi Goldberg"),
               (2001, "Steve Martin"),
               (2000, "Billy Crystal"),
            ]
```

We then need to write the INSERT query with placeholder values. Instead of having specific values in the query string, we use a question mark (?) to act as a placeholder in the values section of the query:  

```sql
insert_query = "INSERT INTO ceremonies (Year, Host) VALUES (?,?);"
```

Since the placeholder elements (?) will be replaced by the values in years_hosts, you need to make sure the number of question marks matches the length of each tuple in years_hosts. Since each tuple has 2 elements, we need to have 2 question marks as the placeholder elements. We don't need to specify values for the id column since it's a primary key column. When inserting values, recall that SQLite automatically creates a unique primary key for each row.  

We then call the executemany method and pass in insert_query as the first parameter and years_hosts as the second parameter:  

```python
conn.executemany(insert_query, years_hosts)
Python will iterate through years_hosts and replace the placeholder elements with the values in years_hosts to generate and execute the following query:
```

```sql
INSERT INTO ceremonies (Year, Host) VALUES
(2010, "Steve Martin"),
(2009, "Hugh Jackman"),
(2008, "Jon Stewart"),
(2007, "Ellen DeGeneres"),
(2006, "Jon Stewart"),
(2005, "Chris Rock"),
(2004, "Billy Crystal"),
(2003, "Steve Martin"),
(2002, "Whoopi Goldberg"),
(2001, "Steve Martin"),
(2000, "Billy Crystal")
;
```

Let's now create the ceremonies table and populate the table with the data on ceremonies.  


#### Instructions :

 - Create the ceremonies table with the following schema:
	- id: integer, primary key.
	- Year: integer.
	- Host: text.
 - Create the list of tuples, years_hosts, that contains the values for the rows we want to insert into the ceremonies table.
 - Use the Connection method executemany to insert the values into the ceremonies table.
 - To verify that the ceremonies table was created and populated correctly, run the following queries:
	- Return the first 10 rows using the SELECT and LIMIT statements.
	- Return the schema using pragma table_info().
 
```python
# 2: Creating The Ceremonies Table
years_hosts = [(2010, "Steve Martin"),
               (2009, "Hugh Jackman"),
               (2008, "Jon Stewart"),
               (2007, "Ellen DeGeneres"),
               (2006, "Jon Stewart"),
               (2005, "Chris Rock"),
               (2004, "Billy Crystal"),
               (2003, "Steve Martin"),
               (2002, "Whoopi Goldberg"),
               (2001, "Steve Martin"),
               (2000, "Billy Crystal"),
            ]
create_ceremonies = "create table ceremonies (id integer primary key, year integer, host text);"
conn.execute(create_ceremonies)
insert_query = "insert into ceremonies (Year, Host) values (?,?);"
conn.executemany(insert_query, years_hosts)
print(conn.execute("select * from ceremonies limit 10;").fetchall())
print("--------------------")
print(conn.execute("pragma table_info(ceremonies);").fetchall())
```  

#### Results :  

	[(1, 2010, 'Steve Martin'), (2, 2009, 'Hugh Jackman'), (3, 2008, 'Jon Stewart'), (4, 2007, 'Ellen DeGeneres'), (5, 2006, 'Jon Stewart'), (6, 2005, 'Chris Rock'), (7, 2004, 'Billy Crystal'), (8, 2003, 'Steve Martin'), (9, 2002, 'Whoopi Goldberg'), (10, 2001, 'Steve Martin')]
	--------------------
	[(0, 'id', 'integer', 0, None, 1), (1, 'year', 'integer', 0, None, 0), (2, 'host', 'text', 0, None, 0)]

---
# 3: Foreign Key Constraints

Since we'll be creating relations using foreign keys, we need to turn on foreign key constraints. By default, if you insert a row into a table that contains one or multiple foreign key columns, the record will be successfully inserted even if the foreign key reference is incorrect.  

For example, since the ceremonies table only contains the id values 1 to 10, inserting a row into nominations while specifying that the ceremony_id value be 11 will work and no error will be returned. This is problematic because if we try to actually join that row with the ceremonies table, the results set will be empty since the id value 11 doesn't map to any row in the ceremonies table. To prevent us from inserting rows with nonexisting foreign key values, we need to turn on foreign key constraints by running the following query:  

>PRAGMA foreign_keys = ON;

The above query needs to be run every time you connect to a database where you'll be inserting foreign keys. Whenever you try inserting a row into a table containing foreign key(s), SQLite will query the linked table to make sure that foreign key value exists. If it does, the transaction will continue as expected. If it doesn't, then an error will be returned and the transaction won't go through.  


#### Instructions :

 - Turn on foreign key constraints by writing and running the following query:
PRAGMA foreign_keys = ON;
 
```python
foreign_keys = "PRAGMA foreign_keys = ON;"
conn.execute(foreign_keys)
```  

---
# 4: Setting Up One-To-Many  

The next step is to remove the Year column from nominations and add a new column, ceremony_id, that contains the foreign key reference to the id column in the ceremonies table. Unfortunately, we can't remove columns from an existing table in SQLite or change its schema. The goal of SQLite is to create an incredibly lightweight, open source database that contains a common, but reduced, set of features. While this has allowed SQLite to become the most popular database in the world, SQLite doesn't have the ability to heavily modify an existing table to keep the code base lightweight.  

The only alterations we can make to an existing table are renaming it or adding a new column. This means that we can't just remove the Year column from nominations and add the ceremony_id column. We need to instead:  

- create a new table nominations_two with the schema we want,
- populate nominations_two with the records we want,
- delete the original nominations table,
- rename nominations_two to nominations.

For nominations_two, we want the following schema:  

- id: primary key, integer,
- category: text,
- nominee: text,
- movie: text,
- character: text,
- won: text,
- ceremony_id: foreign key reference to id column from ceremonies.

First, we need to select all the records from the original nominations table with the columns we want and use an INNER JOIN to add the id field from ceremonies for each row:  

```sql
SELECT nominations.category, nominations.nominee, nominations.movie, nominations.character, nominations.won, ceremonies.id
FROM nominations
INNER JOIN ceremonies ON
nominations.year == ceremonies.year
;
```

Then we can write the placeholder insert query we need to insert these records into nominations_two. Let's create and populate the nominations_two table in this screen and we'll work through the rest in the next screen.  


#### Instructions :

 - Write and run the query to create the nominations_two table with the schema specified above.
 - Write and run the query we discussed above that returns the records from the nominations table and assign the results set to joined_nominations.
 - Write a placeholder insert query that can insert values into nominations_two and assign this query to insert_nominations_two. Make sure the ordering of the columns matches the ordering from joined_nominations.
 - Use the Connection method executemany to insert the records in joined_nominations using the placeholder insert query insert_nominations_two.
 - Verify your work by returning the first 5 rows from nominations_two.
 
```python
# 4: Setting Up One-To-Many

nominations_two = "create table nominations_two (id integer primary key, category text, nominee text, movie text, character text, won text,ceremony_id integer,foreign key(ceremony_id) references ceremonies(id));"

nom_query = '''
select ceremonies.id as ceremony_id, nominations.category as category, 
nominations.nominee as nominee, nominations.movie as movie, 
nominations.character as character, nominations.won as won
from nominations
inner join ceremonies 
on nominations.year == ceremonies.year
;
'''

joined_nominations = conn.execute(nom_query).fetchall()

#conn.execute(nominations_two)

insert_nominations_two = '''insert into nominations_two (ceremony_id, category, nominee, movie, character, won) 
values (?,?,?,?,?,?);
'''

conn.executemany(insert_nominations_two, joined_nominations)
first_five = conn.execute("select * from nominations_two limit 5;").fetchall()

for row in first_five:
    print(row)
```

#### Results :  

	(1, 'Actor -- Leading Role', 'Javier Bardem', 'Biutiful', 'Uxbal', '0', 1)
	(2, 'Actor -- Leading Role', 'Jeff Bridges', 'True Grit', 'Rooster Cogburn', '0', 1)
	(3, 'Actor -- Leading Role', 'Jesse Eisenberg', 'The Social Network', 'Mark Zuckerberg', '0', 1)
	(4, 'Actor -- Leading Role', 'Colin Firth', "The King's Speech", 'King George VI', '1', 1)
	(5, 'Actor -- Leading Role', 'James Franco', '127 Hours', 'Aron Ralston', '0', 1)

---
# 5: Deleting And Renaming Tables  

We now need to delete the nominations table since we'll be using the nominations_two table moving forward. We can use the DROP TABLE statement to drop the original nominations table.  

Once we drop this table, we can use the ALTER TABLE statement to rename nominations_two to nominations. Here's what the syntax looks like for that statement:  


	ALTER TABLE [current_table_name]
	RENAME TO [future_table_name]  


#### Instructions :

 - Write and run the query that deletes the nominations table from the database.
 - Write and run the query that renames nominations_two to nominations.
 
```python
# 5: Deleting And Renaming Tables
delete_nominations = "drop table nominations;"
conn.execute(delete_nominations)

rename_nom_two = "alter table nominations_two rename to nominations;"
conn.execute(rename_nom_two)
```  


---
# 6: Creating A Join Table  

In the Database Normalization and Relations mission, we learned how to query the tables involved in the many-to-many relation between movies and actors.  

Here's a preview of what those tables look like:  

see img/img26.png  

Creating a join table is no different than creating a regular one. To create the movies_actors join table we need to declare both of the foreign key references when specifying the schema:  

```sql
CREATE TABLE movies_actors (
id INTEGER PRIMARY KEY,
movie_id INTEGER REFERENCES movies(id), 
actor_id INTEGER REFERENCES actors(id)
);
```

In this screen, you'll create the 3 tables we need.  


#### Instructions :

 - Create the 3 tables we need to model the relationship between movies and actors. You need to create the movies and actors tables before creating the movies_actors table for the foreign key references to work.
 - Create the movies table using the following schema:
	- id: primary key, integer type.
	- movie: movie name, text type.
 - Create the actors table using the following schema:
	- id: primary key, integer type.
	- actor: actor's full name, text type.
 - Create the movies_actors join table using the following schema:
	- id: primary key, integer type.
	- movie_id: foreign key reference to movies.id column.
	- actor_id: foreign key reference to actors.id column.
 
```python
# 6: Creating A Join Table
movies = "create table movies (id integer primary key,movie text);"
actors = "create table actors (id integer primary key,actor text);"
movies_actors = '''create table movies_actors (id INTEGER PRIMARY KEY,
movie_id INTEGER references movies(id), actor_id INTEGER references actors(id));
'''

create_list = [movies,actors,movies_actors]

for table in create_list:
    conn.execute(table)
```  


---
# 7: Next Steps

In this guided project, you explored how to create relations and set up a join table. That's it for the guided steps but we encourage you to keep exploring! Here are some ideas:  

What other datasets can we add to the database?
Based on what you know, brainstorm how you would populate the join table and the linked tables using data from nominations.  