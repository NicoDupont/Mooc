03/2017  
Dataquest : Data Analyst Path  
Step 4: Working With Data Sources  
SubStep :  SQL and Databases: Intermediate : Database Normalization and Relations  
samedi, 11. mars 2017 06:00 




---
# 1: Introduction  

In the previous mission, we learned how to create a foreign key to reference a table in another record and how to use joins to query across tables using the foreign key. In this mission, we'll dive more deeply into relations between tables, learn about data normalization, and how we can take advantage of them to perform more complex joins.  

In this mission, we'll work with data on Academy Award nominations from 2001 to 2010 for just the lead and supporting acting roles. The Academy Awards, also known as the Oscars, is an annual awards ceremony hosted to recognize the achievements in the film industry. There are many different awards categories and the members of the academy vote every year to decide which artist or film should get the award. The full dataset, containing data on all award categories from years 1927 to 2010, can be found here. We've cleaned and transformed the data and created academy_awards.db.  

The database file academy_awards.db contains 2 tables:  

- nominations, where each row describes an individual actor's nomination.
- ceremonies, where each row describes an individual Academy Awards ceremony.  

The nominations table has the following schema:  

- id - integer field, primary key for uniquely identifying rows.
- ceremony_id - integer field, foreign key reference to the id column from the ceremonies table.
- category: text field, award category. Can only be one of the following 4 values:
	- Actor -- Leading Role.
	- Actor -- Supporting Role.
	- Actress -- Leading Role.
	- Actress -- Supporting Role.
- nominee: text field, name of the actor or actress.
- movie: text field, name of the movie the actor or actresses was nominated for.
- character: text field, name of the character this actor or actress played.
- won: Boolean field, if the actor or actress won the award (either 0 or 1).
The won column is specified as Boolean in the schema but since SQLite doesn't have a Boolean type, SQLite uses the integer data type instead. The integer 0 represents False while the integer 1 represents True.

Here's what the first 10 rows in the nominations table look like:  

see img/img16.png

Since awards are only given to one winner, 4 nominees for each award lose and 1 nominee wins. You'll notice that among the nominees for each award, there was 1 nominee with a value of 1 for won and 4 nominees with a value of 0 for won. You may have also noticed that the movie The King's Speech shows up twice. This is because separate actors were nominated for different roles in the same movie.
  
The ceremonies table has the following schema:  

- id - integer field, primary key for uniquely identify rows.
- year - integer field, the year of the ceremony.
- host - text field, the host for that ceremony.

Here's what the entire ceremonies table, which only contains 11 rows, looks like:  

see img/img17.png

Let's now explore the data to become more familiar with it.  


---
# 2: Database Normalization  

The ceremonies table contains just the information on the actual awards ceremony while the nominations table contains just the information on individual nominations. If we had instead stored the year and host values as columns within the nominations table and avoided using a ceremonies table altogether, our nominations table would look like this:  

see img/img18.png

While this representation is easier to query, since you don't have to do a join each time you want to get the year or host information, it has a few problems:  

 - it contains a lot of redundant data, which means the database will take up more disk space and cost more to store.
 - if we want to update or remove a value in the year or host columns, we need to update every row that contains that same value. This is cumbersome to remember and can cause human error.
 - updating or removing many rows can be slow for larger databases. As your data grows bigger, which is often the case with databases used in production, the update and removal speeds become significantly worse.
 
We instead chose to normalize the data, which involves separating data into smaller tables with less redundant information and creating relations between the appropriate tables. By having the year and host columns in a separate ceremonies table, we get the following benefits:  

 - much less data redundancy since the actual values for year and host are only stored in 1 row in ceremonies, instead of replicated for each relevant row in nominations.
 - separation of concerns and ease of updating.
 
You can read more about the benefits of database normalization [here](https://en.wikipedia.org/wiki/Database_normalization#Objectives) .  


---
# 3: Types Of Relations  

There are many types of relations you can create between tables to represent the links between columns. In this mission, we'll focus on the 2 most common relations:  

- one-to-many.
- many-to-many.

A one-to-many relation exists whenever many rows in one table need to relate to one row in the other table. The relation between ceremonies and nominations is a one-to-many relation since many rows in the nominations table can be linked to an individual row in the ceremonies table. A row in the ceremonies table contains no reference to the nominations table. However, many rows in the nominations table contain a reference to the ceremonies table using the ceremony_id foreign key.  

Below is a diagram that demonstrates how multiple rows in the nominations table, that share the same ceremony_id of 10, relate to the row in the ceremonies table whose id is 10:  

see img/img19.png

An important thing to remember in a one-to-many relation is that the reference is one-sided. The nominations table contains a foreign key reference to the id column in ceremonies but the ceremonies table contains no references to values in the nominations table.  

Here are some other examples of one-to-many relations:  

- a car insurance policy can have multiple people on it, but each person can only belong to one policy.
- a mother can have many children, but each child can only have one birth mother.
- a reporter can have many articles but each article can only have one associated reporter.

---
# 4: Querying A Normalized Database  

As with many things in software development, there is a tradeoff to database normalization. We need to write longer queries sometimes and use joins more often to grab information from multiple tables. Many companies have databases with hundreds or thousands of tables with many relations in between, so this can get complicated quickly! As you become more familiar with querying normalized databases, you'll be able to overcome the added complexity much more easily.  

To write a query that involves 2 tables that are in a one-to-many relation, you need to join on the foreign key column that the "many" side uses to reference the "one" side. When using the WHERE statement to express filtering criteria, we can use columns from both tables. For example, to return all of the movies that won an award in 2010, we'd need to write the following query:  

```sql
SELECT movie FROM nominations 
INNER JOIN ceremonies
ON nominations.ceremony_id == ceremonies.id
WHERE ceremonies.year == 2010 AND nominations.won == 1;
```

In the WHERE statement, we expressed that we were only interested in rows where the year value was 2010 from the ceremonies table and where the won value was 1 from the nominations table.  

When joining 2 tables, you can be more explicit about which columns you want returned from which tables using dot notation -- e.g. nominations.movie. In the following query, we modified the earlier query to select the year and host columns from ceremonies and the movie and nominee columns from nominations:  

```sql
SELECT ceremonies.year, ceremonies.host, nominations.movie, nominations.nominee FROM nominations 
INNER JOIN ceremonies
ON nominations.ceremony_id == ceremonies.id
WHERE ceremonies.year == 2010;
```

In the denormalized schema, which had the year and host columns in nominations itself, we'd only need to write the following query to accomplish the same result:  

```sql
SELECT movie FROM nominations
WHERE nominations.year == 2010;
```

Let's practice using joins further to query tables in a one-to-many relation.   

#### Instructions :

 - We've imported the sqlite3 library for you already and connected to the academy_awards.db database. The Connection instance is named conn.
 - Write a query that returns all of the years that the actress Natalie Portman was nominated for an award.
	- Only return the year column from ceremonies and the movie column from nominations.
	- Run the query and assign the full results list to the variable portman_movies.
	- Then display portman_movies using the print function.
 

```python
nomi = "Select ceremonies.year, nominations.movie from nominations INNER JOIN ceremonies ON nominations.ceremony_id == ceremonies.id where nominations.nominee == 'Natalie Portman'"

portman_movies = conn.execute(nomi).fetchall()
```  

#### Results :  

	Variables
	 portman_movieslist (<class 'list'>)
	[(2010, 'Black Swan'), (2004, 'Closer')]

---
# 5: Many-To-Many Relation  

If we wanted to extend our analysis to study how Academy Awards affect a nominee's career, we'd need to first add more data on which movies each actor starred in. We need a way to represent the relation between actors and movies. Our first instinct might be to use a movies table, an actors table, and specify a one-to-many relationship between them. The movies table could contain an actor_id field that acts as a foreign key reference to the id column from the actors table.  

We immediately run into a road block. Each movie contains many actors and since the actor_id column would be an integer field, we have no way to reference multiple rows from the actors table. We could have a separate row in movies where each row contains a different value for actor_id and cover all the actors in the movie that way. This unfortunately means a large amount of data duplication, since the rest of the columns describing that movie probably won't be different.  
 
What if we had a list data type where we could store multiple values:   

see img/img20.png  

SQLite unfortunately doesn't contain a list data type, so we can't simply store the list of actor names. While some other databases do contain a list data type, this is still a poor design for our data. While searching for a movie by name would be a simple SELECT query, searching by actors would be incredibly cumbersome and slow.  

You may have noticed that the actress Amy Adams stars in all 3 of the movies above. If we wanted to write a query that searched every element in the actors list for every row in movies, the query would take a long time to return as our table starts to hold more than a few thousand movies. We can't use a one-to-many relation since SQLite, and many databases, don't contain a list data type and it would be inefficient to query.  

The right way to model actors and movies is to use a many-to-many relation. A many-to-many relation allows us to flexibly represent both:  

- the actors in a movie and
- the movies an actor has starred in.

To represent a many-to-many relation, we need to use an intermediate table called a join table, which we'll learn more about in the next screen.  

---
# 6: Join Table

To model a many-to-many relationship, we need to create a separate table that contains the foreign keys to each of the tables that we're creating a many-to-many relationship between. This table is called a join table, but is often referenced by many other names. The rows in the join table contain the foreign keys to the 2 other tables. Here's what a join table representing the many-to-many relationship between movies and actors would look:  

see img/img21.png  

 In a many-to-many relation, we separate the data contained within the rows with the actual relation between the rows. This means we can, for example, edit a movie's name without touching the many actor records that are related to that movie. Each table above has it's own id column:  

- the movies.id column is used as a foreign key reference by the movies_actors.movie_id column.
- the actors.id column is used as a foreign key reference by the movies_actors.actor_id column.
- the movies_actors.id column is used just to uniquely identify each row in movies_actors.

The movies_actors table is no different than any other table in our database and it's role as a join table between movies and actors is a design pattern. For example, we can add more columns to the movies_actors table just like with any other table. We could take advantage of this to add attributes that are specific to that movie-actor combination (e.g. Salary or Awards Nominated).  

Creating a join table is similar to creating a regular table except that there need to be 2 foreign columns that reference the 2 tables in the many-to-many relationship:  

```sql
CREATE table movies_actors (
id INTEGER PRIMARY KEY,
movie_id INTEGER REFERENCES movies(id),
actor_id INTEGER REFERENCES actors(id) 
);
```

Let's explore the data in these tables we just discussed a bit further. We've added information about all of the actors and movies from the nominations table to the movies, actors, and movies_actors tables. This will enable us to practice using many-to-many relations

#### Instructions :

- Write a query that returns the first 5 rows in movies_actors and assign the results to five_join_table.
- Write a query that returns the first 5 rows in actors and assign the results to five_actors.
- Write a query that returns the first 5 rows in movies and assign the results to five_movies.
- Then use the print function to display five_join_table, five_actors, and five_movies.

 
```python
movies_actors = "Select * from movies_actors limit 5"
five_join_table = conn.execute(movies_actors).fetchall()

movies = "Select * from movies limit 5"
five_movies = conn.execute(movies).fetchall()

actors = "Select * from actors limit 5"
five_actors = conn.execute(actors).fetchall()

print(five_join_table)
print("---------------")
print(five_movies)
print("---------------")
print(five_actors)
print("---------------")
```  

#### Results :  

	Output
	[(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5)]
	---------------
	[(1, 'Biutiful'), (2, 'True Grit'), (3, 'The Social Network'), (4, "The King's Speech"), (5, '127 Hours')]
	---------------
	[(1, 'Javier Bardem'), (2, 'Jeff Bridges'), (3, 'Jesse Eisenberg'), (4, 'Colin Firth'), (5, 'James Franco')]
	---------------


---
# 7: Querying A Many-To-Many Relation  

Recall that the values in our join table, movies_actors, are all just integer id values that refer to different rows in the movies and actors tables. If we wanted to know the actors who starred in The Fighter that were nominated for an Academy Award between 2001 and 2010, we'd have to use multiple joins in our query across all 3 tables.  

Let's first join the movies table with the movies_actors table:  

```sql
SELECT * FROM movies
INNER JOIN movies_actors ON movies.id == movies_actors.movie_id
```

Here's a preview of the results of that query. Note that in the column names, we use dot notation to connect the table name with the column name (e.g. movies.id refers to the id column from the movies table):  

see img/img22.png

You may have noticed that the movies_actors.id column skips from 5 to 10. We wanted to demonstrate that there's not just one row in the result for each movie in movies since the movie, The King's Speech shows up twice in the sample results. The results of the query so far are really just the cross join of all the rows in the movies table with all the rows in the movies_actors table.  

We then need to join these results with the actors columns. To do this, add another JOIN statement in our query:  

```sql
SELECT * FROM movies
INNER JOIN movies_actors ON movies.id == movies_actors.movie_id
INNER JOIN actors ON movies_actors.actor_id == actors.id
```

Here's a preview of the results of this query:  

see img/img23.png

We now have a row for each actor in actors that played in each movie in movies. However, if you go back to the original problem, you'll notice that we were only interested in actors that starred in The Fighter. To accomplish this, we can modify the columns returned in the SELECT statement and add filtering criteria using the WHERE statement:  

```sql
SELECT actors.actor FROM movies
INNER JOIN movies_actors ON movies.id == movies_actors.movie_id
INNER JOIN actors ON movies_actors.actor_id == actors.id
WHERE movies.movie == "The Fighter";
```

We'll get back just the 3 actors in our database that starred in The Fighter:  

see img/img24.png

You may have noticed that we used dot notation to specify the column name in the query above:  

- movies.movie in the WHERE statement.
- actors.actor in the SELECTstatement.

While this dot notation is required in the JOIN statement, it's optional in the SELECT and WHERE statements. It's a good habit, however, to write out the full name (instead of just movie or actor) of the column using dot notation. Besides the id column, you'll often work with multiple tables that contain the same column names and using dot notation helps us and the database system know what exactly we're referring to.  

In the query above,  

- we started with the movies table (in our select),
- joined with the movies_actors table,
- and then finally joined with the actors table.

We could have actually accomplished the same thing by:  

- starting with the actors table,
- joining with the movies_actors table, and then joining with the movies table

since the filtering criteria is still the same (WHERE movies.movie == "The Fighter").  

Here's a good summary of the steps you need to do when querying tables that are in a many-to-many relation:  

 - first, state the question you want answered:
	- we want all of the actors that starred in The Fighter. Information on The Fighter is in the movies table and there's a join table we'll need to use to get the related information from the actors table.
 - then, understand what joins you need and the filtering criteria you need:
	- we need to join the movies table with the movies_actors table, then join the results with the actors table.
	- our filtering criteria is that we only want the row from movies corresponding to The Fighter.
 - finally, write the query you need based on the joins, columns, and filtering criteria you need.

Writing multiple joins to query tables in a many-to-many relation can be overwhelming at first but it's nothing that practice can't help you overcome. As you practice more, you'll find yourself skipping right to writing the query itself as this kind of querying becomes second nature to you.  

#### Instructions :

 - Modify the query we wrote earlier to instead return all the actors that starred in The King's Speech.
	- We're interested in both the actor name as well as the movie name this time (in that order).
 - Run the query and assign the results list to kings_actors.
 - Then, use the print function to display kings_actors.
 

```python
query = '''SELECT actors.actor,movies.movie FROM movies INNER JOIN movies_actors ON movies.id == movies_actors.movie_id INNER JOIN actors ON movies_actors.actor_id == actors.id WHERE movies.movie == "The King's Speech"'''

kings_actors = conn.e
```  

#### Results :  

	Output
	[('Colin Firth', "The King's Speech"), ('Geoffrey Rush', "The King's Speech"), ('Helena Bonham Carter', "The King's Speech")]



---
# 8: Practice: Querying A Many-To-Many Relation  

In this step, you'll synthesize the concepts learned in this mission by writing a query from scratch that pulls information from 3 tables. 

#### Instructions :

 - Write a query that returns all of the movies that "Natalie Portman" played in.
	- We want to return only the movie name (from the movies table) and the actor name (from the actors table).
	- You need to first join the movies table with the movies_actors table.
	- Then, you need to join the movies_actors table with the actors table.
	- Finally, you need to add a where statement that limits the results to just where actors.actor is equal to Natalie Portman.
 - Run the query and assign the full results list to portman_joins.
 - Use the print function to display portman_joins.
 

```python
query = "select movies.movie, actors.actor from movies inner join movies_actors on movies.id == movies_actors.movie_id inner join actors on actors.id == movies_actors.actor_id where actors.actor == 'Natalie Portman';"

portman_joins = conn.execute(query).fetchall()
print(portman_joins)
```  

#### Results :  

	Output
	[('Black Swan', 'Natalie Portman'), ('Closer', 'Natalie Portman')]



---
# 9: Caveats

While normalization helps reduce data redundancy and allows us to decouple related columns into separate tables, too much normalization can do more harm than good. A highly normalized database means that even some basic queries can involve joining multiple tables together.  

You may have wondered why we didn't try to separate out the actors (nominee column) and the movie names (movie column) in the nominations table. We could have replaced these columns with foreign key references to the actors and movies tables instead. This is because we probably wouldn't have realized the gains of normalization by replacing the actual values with foreign key references.  

If we think that we'll almost always be accessing the movies and actors names when we're querying the nominations table, then forcing the user to do multiple joins to get the relevant information is quite cumbersome. In addition, we know that once an awards ceremony has finished, the movies and nominees are not going to change. This means that another benefit of normalization, easy updating and editing of related values, probably won't be realized.  

When we represented the year and host columns in a separate table from the nominations table, we made the assumption that we don't always need to access both columns every single time when querying the nominations table. We preferred having less data redundancy and writing a join when we needed to.  

Lastly, it's important to remember that the schema isn't set in stone. In many cases, it's best to start out with a denormalized representation of your data with one, or a few, giant tables. As your data grows and your use cases change, you can rethink your schema and restructure your data accordingly. When structuring your data and writing a schema, it's important to remember the tradeoffs that come with normalization.   

---
# 10: Next Steps

In this mission, we learned about 2 different kinds of relations, how to query tables in a database with these kinds of relations, and the paradigm of database normalization. Next up is a guided project where we'll explore how to create a schema and and the relations we learned about in this mission.  