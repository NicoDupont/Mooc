# Datacamp - Introduction To Databases in Python
# partie 1 : Basics of Relational Databases
# Python 3.X


"""  question réponse :4
Relational Model
50xp

Which of the following is not part of the relational model?
Possible Answers

    Tables
    1
    Columns
    2
    Rows
    3
    Dimensions
    4
    Relationships
    5
"""







"""  
Engines and Connection Strings
100xp

Earlier, we used the connection string of 'sqlite:///:memory:'. In this string, sqlite is the vendor, and :memory: is the path to the file that represents memory (RAM). We can also connect to SQLite files by providing a relative or full path to the file just as we would from the shell prompt. For example, sqlite:///demographics.db would connect to a SQLite file named demographics.db in the local directory. You can learn a lot more about connection strings in the SQLAlchemy documentation.

Now, create another engine that connects to a local SQLite file named census.sqlite and print the names of the tables it contains using the table_names() method. Note that when you just want to print the table names, you do not need to use engine.connect() after creating the engine.
Instructions

    Import create_engine from the sqlalchemy module.
    Create an engine for the census.sqlite file.
    Print the output from the table_names() method on the engine.

"""
# Import create_engine
from sqlalchemy import create_engine

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite')

# Print table names
print(engine.table_names())
""" sortie Ipython
<script.py> output:
    ['census', 'state_fact']
"""







"""  
Autoloading Tables from a Database
100xp

SQLAlchemy can be used to automatically load tables from a database using something called reflection. Reflection is the process of reading the database and building the metadata based on that information. It's the opposite of creating a Table by hand and is very useful for working with existing databases. To perform reflection, we need to import the Table object from the SQLAlchemy package. Then we use the Table object to read our table from the engine and autoload the columns. Using the Table object in this manner looks like we are using a function.

Try to reflect the census table available on your engine into the census variable. The metadata has already been loaded for you.
Instructions

    Import the Table object from sqlalchemy.
    Use the Table object with the arguments: the name of the table, metadata, whether autoload is True, and the engine to autoload from.
    Print the repr of the census object.

"""
# Import Table
from sqlalchemy import Table

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True,autoload_with=engine)

# Print repr
print(repr(census))
""" sortie Ipython
<script.py> output:
    Table('census', MetaData(bind=None), Column('state', VARCHAR(length=30), table=<census>), Column('sex', VARCHAR(length=1), table=<census>), Column('age', INTEGER(), table=<census>), Column('pop2000', INTEGER(), table=<census>), Column('pop2008', INTEGER(), table=<census>), schema=None)
"""






"""  
Viewing Table Details
100xp

With our table reflected, we can begin to learn more about the columns and structure of our table. It is important to get an understanding of our database by examining the column names. This can be done by using the columns attribute and accessing the keys() method. For example, census.columns.keys() would return a list of column names on the census table.

Following this, we can use the metadata container to find out more details about the reflected table such as the columns and their types. For example, we can get the metadata of our census table on the metadata.tables dictionary with metadata.tables['census']. This output should match the details from print(repr(census)) in the previous exercise.
Instructions

    Reflect the census table.
    Print a list of column names on the census table.
    Print the repr of the census table metadata.

"""
# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True,autoload_with=engine)

# Print columns names
print(census.columns.keys())

# Print full table metadata
print(repr(metadata.tables['census']))
""" sortie Ipython
<script.py> output:
    ['state', 'sex', 'age', 'pop2000', 'pop2008']
    Table('census', MetaData(bind=None), Column('state', VARCHAR(length=30), table=<census>), Column('sex', VARCHAR(length=1), table=<census>), Column('age', INTEGER(), table=<census>), Column('pop2000', INTEGER(), table=<census>), Column('pop2008', INTEGER(), table=<census>), schema=None)
"""





"""  
Selecting data from a Table: raw SQL
100xp

Using what we just learned about SQL and applying the execute() method on our connection, we can leverage a raw SQL query to query all the records in our census table. Then we use the fetchall() method on execute() to get our results.

In this exercise, you will use a traditional SQL query. In the next exercise, you will move to SQLAlchemy and begin to understand its advantages.
Instructions

    Build a SQL statement to query all the columns from census and store it in stmt.
    Use the execute() and fetchall() methods on our connection and store the result in results. Remember that execute() comes before fetchall().
    Print results.

"""
# Build select statement for census table: stmt
stmt = "select * from census"

# Execute the statement and print the results
results = connection.execute(stmt).fetchall()

# Print Results
print(results)
""" sortie Ipython

"""






"""  
Selecting data from a Table with SQLAlchemy
100xp

You might have noticed in the previous exercise that SQLAlchemy provides a nice abstraction from the complexities that can occur when using traditional SQL. It also provides a nice "Pythonic" way of interacting with databases. This is one of the key benefits of using SQLAlchemy over traditional SQL: Rather than dealing with the differences between specific dialects of traditional SQL such as MySQL or PostgreSQL, we can leverage the Pythonic framework of SQLAlchemy to streamline our workflow and more efficiently query our data. For this reason, it is worth learning SQLAlchemy even if you may be familiar with traditional SQL.

Let's write another select statement; however, this time using the select() statement from the sqlalchemy module to get all the records from our census table. The SQLAlchemy select() statements expects a list of tables or columns as the only required argument.

Table and MetaData have already been imported.
Instructions

    Import select from the sqlalchemy module.
    Reflect the census table using the Table() object and the metadata.
    Create a query using the select() statement to retrieve the census table.
    Print stmt to see the actual SQL query being created.
    Print all the records from the census table using the execute() method on the connection and use fetchall() to get the results.

"""
# Import select
from sqlalchemy import select

# Reflect census table via engine: census
census = Table('census', metadata, autoload=True,autoload_with=engine)

# Build select statement for census table: stmt
stmt = select([census])

# Print the emitted statement to see the SQL emitted
print(stmt)

# Execute the statement and print the results
print(connection.execute(stmt).fetchall())








"""  
Handling a ResultSet
100xp

Recall the differences between a ResultProxy and a ResultSet:

    ResultProxy: The object returned by the execute() method. It can be used in a variety of ways to get the data returned by the query.
    ResultSet: The actual data asked for in the query when using a fetch method such as fetchall() on a ResultProxy.

This separation between the ResultSet and ResultProxy allows us to fetch as much or as little data as we desire.

A query returns a ResultSet when a fetch method such as fetchall() is called on an executed query, and we can use Python to access all the data within it by column name and by list style indexes. For example, you can get the first row of the results by using results[0]. With that first row, you can then get data from the first column by either using first_row[0] or by column name such as first_row['column_name'].
Instructions

    Using the ResultProxy results, save the first row as first_row and print it.
    Print the value of the first column in first_row.
    Print the value of the state column in first_row.

"""
# Get the first row of the results by using an index: first_row
first_row = results[0]

# Print the first row of the results
print(first_row)

# Print the first column of the row by using an index
print(first_row[0])

# Print the state column of the row by using its name
print(first_row['state'])
""" sortie Ipython
<script.py> output:
    ('Illinois', 'M', 0, 89600, 95012)
    Illinois
    Illinois
"""