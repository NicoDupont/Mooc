03/2017  
Dataquest : Data Analyst Path  
Step 4: Working With Data Sources  
SubStep :  SQL and Databases: Intermediate : Using PostgreSQL  
dimanche, 12. mars 2017 01:09 



---
# 1: SQLite Vs PostgreSQL

So far, we've been using a database engine called SQLite. SQLite is one of the most common database engines, and has many advantages:  

- The database is stored in a single file, making it portable.
- You can use a SQLite database directly from Python, and don't need a separate program running.
- It implements most SQL commands, enabling you to use most of the statements you're familiar with.

However, particularly when developing larger applications, SQLite has a few downsides that make other database engines more attractive:  

 - Only one process at a time can write to the database. When you have a complex web application, you may have multiple processes updating information in the database at the same time. For example, on Facebook, one process might handle updating user information, and another might handle generating the news feed.
 - You can't take advantage of performance features, such as caching. Because a SQLite database is a single file, and it doesn't require a special program to run, it can't have performance optimizations like caching. When running a site like Facebook that has a ton of traffic, it's important to be able to lookup data quickly.
 - SQLite doesn't have any built-in security. With a production website, it's common to want some people to be able to modify tables in a database (write), and others to only be able to make SELECT queries to tables in the database (read). This is because giving someone write access to the database can be a security risk, in that they can update or overwrite data. SQLite doesn't allow for restricting access to a database in this way.
 
In general, SQLite is good in cases where having a small and simple database engine is important. SQLite is used extensively in embedded applications, such as Android and iOS applications.  

In cases where there will be multiple users or performance is important, PostgreSQL is the most commonly used database engine. PostgreSQL is open source, and is free to download and use.  

In this mission, we'll look at the basics of PostgreSQL, then dive into creating a database, querying data, and some advanced features.  


---
# 2: PostgreSQL Overview

PostgreSQL, also known as Postgres, is an extremely powerful database engine. At a high level, PostgreSQL consists of two pieces, a server and clients. The server is a program that manages databases and handles queries. Clients communicate back and forth to the server. Only the server ever directly accesses the databases -- the clients can only make requests to the server. If you've gone through the APIs and Web Scraping course, the communication process is very similar to making requests to a remote API.  

One of the advantages of this model is that multiple clients can communicate with the server at the same time. This allows multiple processes to write to a database at the same time.  

It's possible to run a PostgreSQL server either remotely or locally. If it's remote, you connect to it via the internet. If it's local, you connect to it on your own machine. In both cases, you'll be connecting to PostgreSQL via a system port.  

One way to think of ports is to think of receiving mail at an apartment building. Let's say 5 people live in an apartment building, but they only have a single address. All incoming mail will come to the address, then have to be sorted out and given to each person:  

see img/img27.png

All incoming mail is merged into a single pile, because the whole apartment building only has one address. Each apartment occupant then has to sort through the pile to find their mail. Not only is this inefficient, it also results in some apartments getting mail that isn't theirs by accident.  

We can make life easier for everyone by giving each apartment its own address:  

see img/img28.png

Now, nobody has to sort mail, and it's unlikely that someone will accidentally get a message that isn't theirs.  

Every computer runs dozens to hundreds of programs. Many of these programs can accept incoming connections from the internet. For instance, web servers, such as the servers that run Dataquest, run on ordinary computers and accept connections from people all over the world. Once the connections are created, data is sent along the connections.  

If every program received data in the same stream, you'd have a similar situation to all of the apartments only having one address. Each program would be responsible for figuring out which messages were for it, and many messages would be sent to the wrong program. It would be impossible to know which program you were communicating with when you connected to the computer.  

One way to avoid this is for each program to have its own address. A system port is similar to an apartment number in that a port on a computer can only be used by one server at a time. For example, web servers run on port 80. Any incoming messages on this computer port are automatically sent to the program.  

By default, PostgreSQL uses port 5432 to communicate with the outside world. If you start a PostgreSQL server, it will listen for incoming connections on port 5432. Clients will be able to connect to the server using this port. If you start a client, you'll have to specify which server to connect to, along with the port to connect to.  

---
# 3: Psycopg2  

There are many clients for PostgreSQL, including graphical clients. The most common Python client for PostgreSQL is called psycopg2. Connecting to a PostgreSQL database using psycopg2 is similar to connecting to a SQLite database using the sqlite3 libary. psycopg2 also uses Connection and Cursor objects.  

We'd connect to a database using psycopg2 like this:  

```python
import psycopg2
conn = psycopg2.connect("dbname=postgres user=postgres")
cur = conn.cursor()
```

You may notice that we have to specify both a database name and a user name. A PostgreSQL server can have multiple databases and multiple users, so we need to specify which user we're connecting as, and which database we're connecting to.  

When PostgreSQL is first installed, the default user account is called postgres, with an associated database called postgres.  

You may also notice that we didn't specify a server to connect to, or a port to connect using. psycopg2 will default to connecting to port 5432 on the current computer.  

When you're done with a Connection object, you should close it to avoid issues where one connection prevents another from executing a query. You can close a connection like this:  

```python
conn.close()
```

Closing a connection will terminate the client's connection with the PostgreSQL server. It's a good idea to close a connection whenever you're done executing your queries.  

We've automatically started a PostgreSQL server, and created a database called dq, with an associated user called dq.  


#### Instructions :

 - Import the psycopg2 library.
 - Connect to the dq database with the user dq.
 - Initialize a Cursor object from the connection.
 - Use the print function to display the Cursor object.
 - Close the Connection using the close method.
 
```python
import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
print(cur)
conn.close()
```  

#### Results :  

	Output
	<cursor object at 0x7fcde58258b8; closed: 0>

---
# 4: Creating A Table  

Once we've connected to a database, we can create a table inside that database. You may recall the CREATE TABLE statement from an earlier mission:  

```sql
CREATE TABLE tableName(
   column1 dataType1 PRIMARY KEY,
   column2 dataType2,
   column3 dataType3,
   ...
);
```

We can use the same syntax to create a table in the dq database. In order to execute the query, we can use the execute method of the Cursor object:  

```python
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("SELECT * FROM notes;")
```

The above code will connect to the database dq, then execute a query. The syntax above should look familiar to you from using the sqlite3 library, as all the methods are the same.  


#### Instructions :

 - Connect to the dq database as the user dq
 - Write a SQL query that creates a table called notes in the dq database, with the following columns and data types:
	- id -- integer data type, and is a primary key.
	- body -- text data type.
	- title -- text data type.
 - Execute the query using the execute method.
 - Close the Connection using the close method.
 
```python
import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute('''CREATE TABLE notes(id integer PRIMARY KEY,body text,title text);''')
conn.close()
```  

#### Results :  

	Variables
	 connconnection (<class 'psycopg2._psycopg.connection'>)
	<connection object at 0x7fa4ca7147b8; dsn: 'dbname=dq user=dq', closed: 1>
	 curcursor (<class 'psycopg2._psycopg.cursor'>)
	<cursor object at 0x7fa4ca7457c8; closed: 0>

---
# 5: SQL Transactions  

If you checked the database dq now, you would notice that there actually isn't a notes table inside it. This isn't a bug -- it's because of a concept called SQL transations. With SQLite, every query we made that modified the data was immediately executed, and immediately changed the database.  

With PostgreSQL, we're dealing with multiple users who could be changing the database at the same time. Let's imagine a simple scenario where we're keeping track of accounts for different customers of a bank. We could write a simple query to create a table for this:  

```sql
CREATE TABLE accounts(
   id integer PRIMARY KEY,
   name text,
   balance float
);
```

Let's say we have the following two rows in the table:  


	id    name    balance
	1     Jim     100
	2     Sue     200
	
Let's say Sue gives 100 dollars to Jim. We could model this with two queries:  

```sql
UPDATE accounts SET balance=200 WHERE name="Jim";
​
UPDATE accounts SET balance=100 WHERE name="Sue";
```

In the above example, we remove 100 dollars from Sue, and add 100 dollars to Jim. Let's say either the second UPDATE statement has an error in it, the database fails, or another user has a conflicting query. The first query would run properly, but the second would fail. That would result in the following:  

Jim would be credited 100 dollars, but 100 dollars would not be removed from Sue. This would cause the bank to lose money.  

Transactions prevent this type of behavior by ensuring that all the queries in a transaction block are executed at the same time. If any of the transactions fail, the whole group fails, and no changes are made to the database at all.  

Whenever we open a Connection in psycopg2, a new transaction will automatically be created. All queries run up until the commit method is called will be placed into the same transaction block. When commit is called, the PostgreSQL engine will run all the queries at once.  

If we don't want to apply the changes in the transaction block, we can call the rollback method to remove the transaction. Not calling either commit or rollback will cause the transaction to stay in a pending state, and will result in the changes not being applied to the database.  


#### Instructions :

 - Connect to the dq database as the user dq.
 - Write a SQL query that creates a table called notes in the dq database, with the following columns and data types:
	- id -- integer data type, and is a primary key.
	- body -- text data type.
	- title -- text data type.
 - Execute the query using the execute method.
 - Use the commit method on the Connection object to apply the changes in the transaction to the database.
 - Close the Connection.
 
```python
import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute('''CREATE TABLE notes(id integer PRIMARY KEY,body text,title text);''')
conn.commit()
conn.close()
```  

---
# 6: Autocommitting  

There are cases when you won't want to manage a transaction, and you'll instead want changes right away. This is most common when you're making changes to the database that you want to be guaranteed to happen immediately.  

Some changes also have such widespread effects that they can't be wrapped inside of a transaction. One example of this is creating a database. When creating a database, we'll need to activate autocommit mode first.  

To activate autocommit mode, we'll need to set the autocommit property of the Connection object to True.  

```python
conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE TABLE notes(id integer PRIMARY KEY, body text, title text)")
```

The above command will create a table called notes without having to explicitly commit the transaction. We'll then be able to use the notes table right away.  


#### Instructions :

 - Connect to the dq database as the user dq.
 - Set the autocommit property of the Connection object to True.
 - Write a SQL query that creates a table called facts in the dq database, with the following columns and data types:
	- id -- integer data type, and is a primary key.
	- country -- text data type.
	- value -- integer data type.
 - Execute the query using the execute method.
 - Close the Connection.
 
```python
import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute('''CREATE TABLE facts(id integer PRIMARY KEY,country text,value integer);''')
conn.close()
```  

---
# 7: Executing Queries  

We can issue SELECT queries against a database using the execute method, along with the fetchall and fetchone methods to retrieve results:  

```python
cur.execute("SELECT * FROM notes;")
rows = cur.fetchall()
print(rows)
```

The above code will select all of the rows in the notes table, then print them all out.  

Of course, we don't have any rows in our table yet. You may recall how to insert rows from a previous mission:  

```sql
INSERT INTO tableName
VALUES (value1, value2, ...);
```

The below query will insert a row into the notes table:  

```sql
INSERT INTO notes
VALUES (1, 'This is my note text.', 'Test note');
```

#### Instructions :

 - Connect to the dq database as the user dq.
 - Execute a SQL query that inserts a row into the notes table with the following values:
	- id -- 1
	- body -- 'Do more missions on Dataquest.'
	- title -- 'Dataquest reminder'.
 - Execute a SQL query that selects all of the rows from the notes table.
 - Fetch all of the results and print them out.
 - Close the Connection.
 
```python
import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute('''INSERT INTO notes VALUES (1, 'Do more missions on Dataquest.', 'Dataquest reminder');''')
cur.execute('''select * from notes;''')
row = cur.fetchall()
print(row)
conn.close()
```  

#### Results :  

	Output
	[(1, 'Do more missions on Dataquest.', 'Dataquest reminder')]

---
# 8: Creating A Database  

One of the most powerful aspects of PostgreSQL is that it enables you to create multiple databases. Different databases are generally used to hold information about different applications. For instance, if you have the following three datasets and applications:  

- An application that enables you to add and remove friends in your neighborhood.
- A dataset on household income worldwide.
- An application that allows you to store and share notes.

You could in theory make different tables for each of these in an existing database. But eventually, you'll reach a point where each application has multiple tables, due to foreign keys and joins. It will get messy to manage all the tables for each application separately. By storing data for a single application in a single database, we encapsulate that application, and make it easier to manage and alter the data for it.  

We can create a database using the CREATE DATABASE SQL statement:  

```sql
CREATE DATABASE dbName;
```

Here's a concrete example:

```sql
CREATE DATABASE notes;
```

The above SQL command will create a database called notes. We can specify the user who will own the database when we create it as well, using the OWNER statement:  

```sql
CREATE DATABASE notes OWNER postgres;
```

The above statement will create a database called notes with the default postgres user as the owner. The owner of a database is the only one that can access and modify a database, unless they give permission to other users. An exception is superusers, who we'll cover in a later mission, who can perform any action on any database without being given permission.  


#### Instructions :

- Connect to the dq database with the user dq.
- Set the connection to autocommit mode.
- Create a database called income where the owner is the user dq.
- Close the Connection.
 
```python
import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute('''create database income;''')
conn.close()
```  


---
# 9: Deleting A Database

We can delete a database using the DROP DATABASE statement. The DROP DATABASE statement will immediately remove a database, provided the user executing the query has the right permissions. It should be used with caution when working with real data.  

```sql
DROP DATABASE dbName;
```

Here's a more concrete example:  

```sql
DROP DATABASE income;
```

The above statement will remove the database called income, along with any tables it contains.  


#### Instructions :

- Connect to the dq database with the user dq.
- Set the connection to autocommit mode.
- Drop the income database.
- Close the Connection.
 
```python
import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute('''drop database income;''')
conn.close()
```  

---
# 10: Next Steps  

In this mission, we covered the basics of PostgreSQL, along with transactions and working with databases. In the next mission, we'll look at managing databases, users, and permissions in PostgreSQL.  