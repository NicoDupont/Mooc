"""
03/2017
Dataquest : Data Analyst Path
Step 4: Working With Data Sources
SubStep : SQL and Databases: Beginner : Querying SQLite from Python
"""


"""
1: Overview

In the past missions, we focused on exploring the SQL syntax for retrieving data from a database.
In this mission, we'll explore how to interact with a SQLite database in Python so you can start to incorporate databases in your data science workflow.
SQLite is a database that doesn't require a standalone server process and stores the entire database as a file on disk.
This makes it ideal for working with larger datasets that can fit on disk but not in memory.
Since the Pandas library loads the entire dataset we're working with into memory, this makes SQLite a compelling alternative option for working with datasets that are larger than 8 gigabytes (which is roughly the amount of memory modern computers contain).
In addition, since the entire database can be contained within a single file, some datasets are released online as a SQLite database file (using the extension .db).

You can interact with a SQLite database in two main ways:

    using the Sqlite Python module.
    using the SQLite shell.

In this mission, we'll focus on learning how to use the Sqlite Python module to interact with the database.
Next in this course is a guided project where we explore how to use the SQLite shell to interact with the database.
"""




"""
2: Introduction to the data

We'll continue to work with the dataset from the American Community Survey on college majors and job outcomes:
Rank 	Major_code 	Major 	Major_category 	Total 	Sample_size 	Men 	Women 	ShareWomen 	Employed
1 	2419 	PETROLEUM ENGINEERING 	Engineering 	2339 	36 	2057 	282 	0.120564 	1976
2 	2416 	MINING AND MINERAL ENGINEERING 	Engineering 	756 	7 	679 	77 	0.101852 	640
3 	2415 	METALLURGICAL ENGINEERING 	Engineering 	856 	3 	725 	131 	0.153037 	648
4 	2417 	NAVAL ARCHITECTURE AND MARINE ENGINEERING 	Engineering 	1258 	16 	1123 	135 	0.107313 	758
5 	2405 	CHEMICAL ENGINEERING 	Engineering 	32260 	289 	21239 	11021 	0.341631 	25694

The full table has many more columns, 21 to be specific, than the ones displayed above and they're explained in further detail on FiveThirtyEight's Github repo.

Here are the descriptions of the columns in the above snapshot:

    Rank - Rank by median earnings
    Major_code - Major code
    Major - Major description
    Major_category - Category of major
    Total - Total number of people with major
    Sample_size - Sample size (unweighted) of full-time
    Men - Male graduates
    Women - Female graduates
    ShareWomen - Women as share of total
    Employed - Number employed

We have loaded the data in for years 2010-2012 for just recent college grads into the table recent_grads.
The database file we'll be working with is called jobs.db.
"""




"""
3: Connect to the database

From Python 2.5 and onwards, the Sqlite module has come built-in to the Python language, which means we don't need to install any separate libraries to get started.
Specifically, we'll be working with the Sqlite3 Python module, which was developed to work with SQLite version 3.

We can import it into our environment using:

import sqlite3

Once imported, we connect to the database we want to query using the connect() function.
The connect() function has a single required parameter, the database we want to connect to.
Since the database we're working with is stored as a file on disk, we need to pass in the filename.
The connect() function returns a Connection instance, which maintains the connection to the database we want to work with.
When you're connected to a database, SQLite locks the database file and prevents any other process from connecting to the database simultaneously.
This was a design decision made by the SQLite team to keep the database lightweight and avoid the complexity that arises when multiple processes are interacting with the same database.
Instructions

    Import the Sqlite3 library into the environment.
    Then, use the Sqlite3 function connect() to connect to jobs.db and assign the returned Connection instance to conn.

"""
import sqlite3
conn = sqlite3.connect("jobs.db")




"""
4: Cursor object and tuples

Before we can execute a query, we need to express our SQL query as a string.
While we use the Connection class to represent the database we're working with, we use the Cursor class to:

    run a query against the database.
    parse the results from the database.
    convert the results to native Python objects.
    store the results within the Cursor instance as a local variable.

After running a query and converting the results to a list of tuples, the Cursor instance stores the list as a local variable.
Before diving into the syntax of querying the database, let's learn more about tuples.
"""





"""
5: Tuples

A tuple is a core Python data structure used to represent a sequence of values, similar to a list.
Unlike lists, tuples are immutable, which means they can't be modified after creation.
Each row is in the results set is represented as a tuple.

To create an empty tuple, assign a pair of empty parentheses to a variable:

t = ()

Tuples are indexed the same way as lists, from 0 to n-1, and you access values using bracket notation.

t = ('Apple', 'Banana')

apple = t[0]

banana = t[1]

Tuples are faster than lists, which is helpful when working with larger databases and larger results sets.
Let's now dive into how to use the Cursor instance to query the database.
"""




"""
6: Running a query

We need to use the Connection instance method cursor() to return a Cursor instance corresponding to the database we want to query.

cursor = conn.cursor()

In the following code block, we:

    write a basic select query that returns all of the values from the recent_grads table and store it as a string called query.
    use the Cursor method execute() to run the query against our database.
    return the full results set and store it as results.
    print the first 3 tuples in the list results.

# SQL Query as a string

query = "select * from recent_grads;"

# Execute the query, convert the results to tuples, and store as a local variable.

cursor.execute(query)

# Fetch the full results set, as a list of tuples.

results = cursor.fetchall()

# Display the first 3 results.

print(results[0:3])

Now it's your turn!
Instructions

    Write a query that returns all of the values in the Major column from the recent_grads table.
    Store the full results set (a list of tuples) in majors.
    Then, print the first 3 tuples in majors.

"""
import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "select * from recent_grads;"
cursor.execute(query)
results = cursor.fetchall()
print(results[0:2])

query = "select Major from recent_grads;"
cursor.execute(query)
majors = cursor.fetchall()
print(majors[0:3])
""" Console Outputs or Results
Output
[(0, 1, 2419, 'PETROLEUM ENGINEERING', 'Engineering', 2339, 36, 2057, 282, 0.120564344, 1976, 1849, 270, 1207, 37, 0.018380527, 110000, 95000, 125000, 1534, 364, 193), (1, 2, 2416, 'MINING AND MINERAL ENGINEERING', 'Engineering', 756, 7, 679, 77, 0.10185185199999999, 640, 556, 170, 388, 85, 0.117241379, 75000, 55000, 90000, 350, 257, 50)]
[('PETROLEUM ENGINEERING',), ('MINING AND MINERAL ENGINEERING',), ('METALLURGICAL ENGINEERING',)]

"""



"""
7: Shortcut for running a query

So far, we've been running queries by creating a Cursor instance and then calling the execute method on the instance.
The sqlite library actually allows us to skip creating a Cursor altogether by using the execute method within the Connection object itself.
Under the hood, a Cursor instance will be created for us and our query run against the database, but this shortcut allows us to skip a step.
Here's how that code looks like:

conn = sqlite3.connect("jobs.db")

query = "select * from recent_grads;"

conn.execute(query).fetchall()

In the above code, we didn't explicitly create a separate Cursor instance ourselves.
Let's now learn how to fetch a specific number of results after a query is run.
"""





"""
8: Fetching a specific number of results

To make it easier to work with large results sets, the Cursor class allows you to control the number of results you want to retrieve at any given time.
To return a single result (as a tuple), we use the Cursor method fetchone() and to return n results, we use the Cursor method fetchmany().

Each Cursor instance contains an internal counter which is updated every time you retrieve results.
When you call the fetchone() method, the Cursor instance will return a single result and then increment its internal counter by 1.
This means that if you call fetchone() again, the Cursor instance will actually return the second tuple in the results set (and increment by 1 again).

The fetchmany() method takes in an integer (n) and returns the corresponding results starting from the current position.
The fetchmany() method then increments the Cursor instance's counter by n.
In the following code, we return the first 2 results using the fetchone() method, then the next 5 results using the fetchmany() method.

first_result = cursor.fetchone()

second_result = cursor.fetchone()

next_five_results = cursor.fetchmany(5)

Instructions

    Write and run a query that returns the Major and Major_category columns from recent_grads.
    Then, fetch the first 5 results and store it as five_results.

"""
import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = ("select Major, Major_category from recent_grads;")
cursor.execute(query)
five_results = cursor.fetchmany(5)
print(five_results)
""" Console Outputs or Results
Output
[('PETROLEUM ENGINEERING', 'Engineering'), ('MINING AND MINERAL ENGINEERING', 'Engineering'), ('METALLURGICAL ENGINEERING', 'Engineering'), ('NAVAL ARCHITECTURE AND MARINE ENGINEERING', 'Engineering'), ('CHEMICAL ENGINEERING', 'Engineering')]

"""




"""
9: Closing the connection

Since SQLite restricts access to the database file when we're connected to a database, we need to close the connection when we're done working with it.
Closing the connection to the database allows other processes to access the database, which is important when you're in a production environment and working with other team members.
In addition, if we made any changes to the database, they are automatically saved and our changes are persisted in the database file upon closing.

To close a connection to a database, use the Connection instance method close().
When you're working with multiple databases and multiple Connection instances, you want to make sure you call the close() method on the correct instance.
After closing the connection, attempting to query the database using any linked Cursor instances will return the following error:

ProgrammingError: Cannot operate on a closed database.

Instructions

    Close the connection to the database using the Connection instance method close() method.

"""
conn = sqlite3.connect("jobs.db")
conn.close()
""" Console Outputs or Results
Variables
connConnection (<class 'sqlite3.Connection'>)
<sqlite3.Connection at 0x7f3c6b3f4730>
"""




"""
10: Practice

Let's now practice the entire workflow we've learned so far from start to finish.
Instructions

    Connect to the database jobs2.db, which contains the same data as jobs.db.
    Write and execute a query that returns all of the major names (Major) in reverse alphabetical order (Z to A).
    Assign the full result set to reverse_alphabetical.
    Finally, close the connection to the database.

"""
import sqlite3
conn = sqlite3.connect("jobs2.db")
cursor = conn.cursor()

query = ("select Major from recent_grads order by 1 desc;")
cursor.execute(query)
reverse_alphabetical = cursor.fetchall()

conn.close()





"""
11: Next steps

Next up in this course is a guided project where we walk through how to use the SQLite shell.
 The SQLite shell is similar to the IPython shell where you can write and run commands interactively.
"""
