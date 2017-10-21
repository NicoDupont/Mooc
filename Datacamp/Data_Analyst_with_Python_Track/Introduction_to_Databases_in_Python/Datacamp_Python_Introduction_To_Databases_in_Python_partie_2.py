# Datacamp - Introduction To Databases in Python
# partie 2 : Basics of Relational Databases
# Python 3.X


"""  
Connecting to a PostgreSQL Database
50xp

Before we jump into our filtering exercises, let's begin by connecting to a PostgreSQL database. You might recall from Chapter 1 that we use the create_engine and a connection string to connect to a database.

When connecting to a PostgreSQL database, many prefer to use the psycopg2 database driver, which you have to install before use, but that's outside of the scope of this class. Psycopg2 is preferred as it supports practically all of PostgreSQL's features efficiently and is the standard dialect for PostgreSQL in SQLAlchemy.

There are three components to the connection string in this exercise: the dialect and driver (postgresql+psycopg2://), followed by the username and password (student:datacamp), followed by the host and port (@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/), and finally, the database name (census).

In these exercises, you will be working with real databases hosted on the cloud via Amazon Web Services (AWS)!
Instructions

    Import the create_engine function from the sqlalchemy library.
    Create an engine to the census database on postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com. using port 5432 as the user named student with a password of datacamp.
    Use the table_names() method on the engine to print the table names.

"""
# Import create_engine function
from sqlalchemy import create_engine

# Create an engine to the census database
engine = create_engine("postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census")

# Use the 'table_names()' method on the engine to print the table names
print(engine.table_names())
""" sortie Ipython
<script.py> output:
    ['census', 'state_fact']

"""





"""  
Filter data selected from a Table - Simple
100xp

As mentioned in the video, a where() clause is used to filter the data that a statement returns. For example, to select all the records where the sex is Female we would do the following:

select([census]).where(census.columns.sex == 'F')

In addition to == we can use basically any python comparison operator (such as <=, !=, etc) in the where() clause.
Instructions

    Select all records from the census table.
    Append a where clause to return only the records with a state of New York.
    Execute the statement stmt and store the results as results.
    Iterate over results and print the age, sex and pop2008 columns from each record.

"""
# Create a select query: stmt
stmt = select([census])

# Add a where clause to filter the results to only those for New York
stmt = stmt.where(census.columns.state == 'New York')

# Execute the query to retrieve all the data returned: results
results = connection.execute(stmt).fetchall()

# Loop over the results and print the age, sex, and pop2008
for result in results:
    print(result.age, result.sex, result.pop2008)
""" sortie Ipython
<script.py> output:
    0 M 128088
    1 M 125649
    2 M 121615
    3 M 120580
    4 M 122482
    5 M 121205
    6 M 120089
    7 M 122355
    8 M 118653
    9 M 117369
    10 M 118810
    11 M 121121
    12 M 126338
    13 M 128713
    14 M 129812
    15 M 134463
    16 M 136569
    17 M 140114
    18 M 156892
    19 M 147556
    20 M 146611
    21 M 141932
    22 M 138557
    23 M 136150
    24 M 132383
    25 M 141850
    26 M 129603
    27 M 131419
    28 M 127224
    29 M 122449
    30 M 126404
    31 M 126124
    32 M 123362
    33 M 126486
    34 M 120030
    35 M 123017
    36 M 127076
    37 M 136270
    38 M 144715
    39 M 135027
    40 M 135355
    41 M 132905
    42 M 140025
    43 M 151555
    44 M 149030
    45 M 148147
    46 M 146692
    47 M 147648
    48 M 155155
    49 M 144287
    50 M 143466
    51 M 139630
    52 M 133939
    53 M 136723
    54 M 125953
    55 M 122478
    56 M 118070
    57 M 115823
    58 M 117177
    59 M 108293
    60 M 106825
    61 M 113681
    62 M 83763
    63 M 81226
    64 M 76961
    65 M 82242
    66 M 70423
    67 M 64117
    68 M 63657
    69 M 58801
    70 M 57609
    71 M 53231
    72 M 51132
    73 M 50696
    74 M 44822
    75 M 43592
    76 M 41900
    77 M 40417
    78 M 40241
    79 M 35941
    80 M 34659
    81 M 32022
    82 M 28890
    83 M 27217
    84 M 23879
    85 M 124478
    0 F 122194
    1 F 119661
    2 F 116413
    3 F 114877
    4 F 116936
    5 F 116051
    6 F 115186
    7 F 116951
    8 F 113279
    9 F 111919
    10 F 113891
    11 F 115607
    12 F 120156
    13 F 123797
    14 F 124343
    15 F 127635
    16 F 130769
    17 F 134311
    18 F 150772
    19 F 142871
    20 F 141831
    21 F 142302
    22 F 138703
    23 F 138084
    24 F 135339
    25 F 141601
    26 F 130002
    27 F 129600
    28 F 129868
    29 F 119821
    30 F 125047
    31 F 127486
    32 F 123742
    33 F 126908
    34 F 121824
    35 F 124485
    36 F 130377
    37 F 140890
    38 F 148408
    39 F 137936
    40 F 138561
    41 F 139720
    42 F 145307
    43 F 154437
    44 F 154805
    45 F 153651
    46 F 151107
    47 F 154997
    48 F 158855
    49 F 151022
    50 F 149883
    51 F 146988
    52 F 142566
    53 F 144121
    54 F 135180
    55 F 132338
    56 F 127500
    57 F 126450
    58 F 128713
    59 F 121743
    60 F 119540
    61 F 126847
    62 F 96462
    63 F 94667
    64 F 90185
    65 F 97321
    66 F 83336
    67 F 77404
    68 F 77802
    69 F 71850
    70 F 71451
    71 F 66625
    72 F 65037
    73 F 65719
    74 F 58818
    75 F 58722
    76 F 57584
    77 F 56907
    78 F 58456
    79 F 54136
    80 F 52932
    81 F 50693
    82 F 48206
    83 F 47777
    84 F 43454
    85 F 273476
"""




"""  
Filter data selected from a Table - Expressions
100xp

In addition to standard Python comparators, we can also use methods such as in_() to create more powerful where clauses. You can see a full list of expressions in the SQLAlchemy Documentation.

We've already created a list of some of the most densely populated states.
Instructions

    Select all records from the census table.
    Append a where clause to return all the records with a state in the states list.
    Loop over the ResultProxy and print the state and pop2000 columns from each record.

"""
# Create a query for the census table: stmt
stmt = select([census])

# Append a where clause to match all the states in_ the list states
stmt = stmt.where(census.columns.state.in_(states))

# Loop over the ResultProxy and print the state and its population in 2000
for result in connection.execute(stmt):
    print(result.state, result.pop2000)
""" sortie Ipython

"""





"""  
Filter data selected from a Table - Advanced
100xp

SQLAlchemy allows users to use conjunctions such as and_(), or_(), and not_() to build more complex filtering. For example, we can get a set of records for people in New York who are 21 or 37 years old with the following code:

stmt([census]).where(
  and_(census.columns.state == 'New York',
       or_(census.columns.age == 21,
          census.columns.age == 37
         )
      )
  )

Instructions

    Import and_ from the sqlalchemy module.
    Select all records from the census table.
    Append a where clause to return all the records whose state is California, and whose sex is not M.
    Iterate over the ResultProxy and print the age and sex columns from each record.

"""
# Import and_
from sqlalchemy import and_

# Build a query for the census table: stmt
stmt = select([census])

# Append a where clause to select only non-male records from California using and_
stmt = stmt.where(
    # The state of California with a non-male sex
    and_(census.columns.state == "California",
         census.columns.sex != "M"
         )
)

# Loop over the ResultProxy printing the age and sex
for result in connection.execute(stmt):
    print(result.age, result.sex)
""" sortie Ipython
<script.py> output:
    0 F
    1 F
    2 F
    3 F
    4 F
    5 F
    6 F
    7 F
    8 F
    9 F
    10 F
    11 F
    12 F
    13 F
    14 F
    15 F
    16 F
    17 F
    18 F
    19 F
    20 F
    21 F
    22 F
    23 F
    24 F
    25 F
    26 F
    27 F
    28 F
    29 F
    30 F
    31 F
    32 F
    33 F
    34 F
    35 F
    36 F
    37 F
    38 F
    39 F
    40 F
    41 F
    42 F
    43 F
    44 F
    45 F
    46 F
    47 F
    48 F
    49 F
    50 F
    51 F
    52 F
    53 F
    54 F
    55 F
    56 F
    57 F
    58 F
    59 F
    60 F
    61 F
    62 F
    63 F
    64 F
    65 F
    66 F
    67 F
    68 F
    69 F
    70 F
    71 F
    72 F
    73 F
    74 F
    75 F
    76 F
    77 F
    78 F
    79 F
    80 F
    81 F
    82 F
    83 F
    84 F
    85 F
"""




"""  
Ordering by a Single Column
100xp

To sort result output by a field, we use the order_by() method. By default, the order_by() method sorts from lowest to highest on the supplied column. You just have to pass in the name of the column you want sorted to order_by.
Instructions

    Build a select statement to return all the state records in the census table.
    Append an order_by() on census.columns.state and store that statement as stmt.
    Execute stmt using the connection to get all the rows and store the results as results.
    Print the first 10 rows of results.

"""
# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Append an order_by state
stmt = stmt.order_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the first 10 result
print(results[:10])
""" sortie Ipython
<script.py> output:
    [('Alabama',), ('Alabama',), ('Alabama',), ('Alabama',), ('Alabama',), ('Alabama',), ('Alabama',), ('Alabama',), ('Alabama',), ('Alabama',)]
"""





"""  
Ordering in Descending Order by a Single Column
100xp

We can also use order_by to sort from highest to lowest by wrapping a column in the desc() function. Although you haven't seen this function in action, it generalizes what you have already learned. All you have to just pass in desc inside an order_by with the name of the column you want to sort by. For instance, stmt.order_by(desc(table.columns.column_name)) sorts column_name in descending order.
Instructions

    Import desc from the sqlalchemy module.
    Build a select statement to return all the state records in the census. table and store that statement as rev_stmt.
    Append an order_by() descending census.state.
    Execute rev_stmt using the connection to get all the rows and store the results as rev_results.
    Print the first 10 rows of rev_results.

"""
# Import desc
from sqlalchemy import desc

# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Append order_by descending state: rev_stmt
rev_stmt = stmt.order_by(desc(census.columns.state))

# Execute the query and store the results: rev_results
rev_results = connection.execute(rev_stmt).fetchall()

# Print the first 10 rev_results
print(rev_results[:10])
""" sortie Ipython
<script.py> output:
    [('Wyoming',), ('Wyoming',), ('Wyoming',), ('Wyoming',), ('Wyoming',), ('Wyoming',), ('Wyoming',), ('Wyoming',), ('Wyoming',), ('Wyoming',)]
"""




"""  
Ordering by Multiple Columns
100xp

We can pass multiple arguments to the order_by() method to order by multiple columns. In fact, we can also sort in ascending or descending order for each individual column. Each column in the order_by statement is fully sorted from left to right. This means that the first column is completely sorted, and then within each matching group of values in the first column, it's sorted by the next column in the order_by() method. This process is repeated until all the columns in the order_by() are sorted.
Instructions

    Build a select statement to get the state and age columns from the census table and store it as stmt.
    Append an order_by for the state in ascending order and age in descending order. (NOTE: desc() is already imported).
    Execute stmt using the connection to get all the rows and store the results as results.
    Print the first 20 results.

"""
# Build a query to select state and age: stmt
stmt = select([census.columns.state, census.columns.age])

# Append order by to ascend by state and descend by age
stmt = stmt.order_by(census.columns.state, desc(census.columns.age))

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print the first 20 results
print(results[:20])
""" sortie Ipython
<script.py> output:
    [('Alabama', 85), ('Alabama', 85), ('Alabama', 84), ('Alabama', 84), ('Alabama', 83), ('Alabama', 83), ('Alabama', 82), ('Alabama', 82), ('Alabama', 81), ('Alabama', 81), ('Alabama', 80), ('Alabama', 80), ('Alabama', 79), ('Alabama', 79), ('Alabama', 78), ('Alabama', 78), ('Alabama', 77), ('Alabama', 77), ('Alabama', 76), ('Alabama', 76)]
"""





"""  
Counting Distinct Data
100xp
As mentioned in the video, SQLAlchemy's func module provides access to built-in SQL functions that can make sure like counting and summing faster than getting all the results and performing the calculation in Python. These functions are typically found in the column list or where clause of statements. You should always import the func module, as importing the methods in the func module (such as sum) directly can cause problems and confusion with Python’s built-in sum function. To use the count method, you would wrap the column in func.count().

Also in a statement, we can use the distinct() method on a column to get only the unique values in it.

So far, we've seen fetchall() and first() used on a ResultProxy to get the results. However, the ResultProxy also has a method called scalar() for getting just the value of a query that returns only one row and column. This can be very useful when you are querying for just a count or sum.

Instructions
Build a select statement to count the distinct values in the state field of the census table and store it as stmt.
Execute stmt using the connection to get the count and store the results as distinct_state_count (Use the scalar() method).
Print the value of distinct_state_count.
"""
# Build a query to count the distinct states values: stmt
stmt = select([func.count(census.columns.state.distinct())])

# Execute the query and store the scalar result: distinct_state_count
distinct_state_count = connection.execute(stmt).scalar()

# Print the distinct_state_count
print(distinct_state_count)

""" sortie Ipython
<script.py> output:
    51
"""





"""  
Count of Records by State
100xp
Often, we want to get a count for each record with a particular value in another column. The group_by() method helps answer this type of query. You can pass a column to the group_by() method and use in a aggregate function like sum() or count(). Much like the order_by() method, group_by() can take multiple columns as arguments.

Instructions
Import the func module from the sqlalchemy.sql module.
Build a select statement to get the value of the state field and a count of the values in the age field, and store it as stmt.
Append a group by for the state from the census table.
Execute stmt using the connection to get the count and store the results as results.
Print results.
Print results[0].keys(), the keys/column names of the results returned.
"""
# Import func
from sqlalchemy.sql import func

# Build a query to select the state and count of ages by state: stmt
stmt = select([census.columns.state, func.count(census.columns.age)])

# Append group by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())
""" sortie Ipython
<script.py> output:
    [('Alabama', 172), ('Alaska', 172), ('Arizona', 172), ('Arkansas', 172), ('California', 172), ('Colorado', 172), ('Connecticut', 172), ('Delaware', 172), ('District of Columbia', 172), ('Florida', 172), ('Georgia', 172), ('Hawaii', 172), ('Idaho', 172), ('Illinois', 172), ('Indiana', 172), ('Iowa', 172), ('Kansas', 172), ('Kentucky', 172), ('Louisiana', 172), ('Maine', 172), ('Maryland', 172), ('Massachusetts', 172), ('Michigan', 172), ('Minnesota', 172), ('Mississippi', 172), ('Missouri', 172), ('Montana', 172), ('Nebraska', 172), ('Nevada', 172), ('New Hampshire', 172), ('New Jersey', 172), ('New Mexico', 172), ('New York', 172), ('North Carolina', 172), ('North Dakota', 172), ('Ohio', 172), ('Oklahoma', 172), ('Oregon', 172), ('Pennsylvania', 172), ('Rhode Island', 172), ('South Carolina', 172), ('South Dakota', 172), ('Tennessee', 172), ('Texas', 172), ('Utah', 172), ('Vermont', 172), ('Virginia', 172), ('Washington', 172), ('West Virginia', 172), ('Wisconsin', 172), ('Wyoming', 172)]
    ['state', 'count_1']

"""





"""  
Determining the Population Sum by State
100xp
To avoid confusion with query result column names like count_1, we can use the label() method to provide a name for the resulting column. This gets appended to the function method we are using, and its argument is the name we want to use.

We can pair func.sum() with group_by() to get a sum of the population by State and use the label() method to name the output.

We can also create the func.sum() expression before using it in the select statement. We do it the same way we would inside the select statement and store it in a variable. Then we use that variable in the select statement where the func.sum() would normally be.

Instructions
Import the func module from the sqlalchemy.sql module.
Build an expression to calculate the sum of the values in the pop2008 field labeled as population.
Build a select statement to get the value of the state field, and store it asstmt.
Append a grouped by the state from the census table.
Execute stmt using the connection to get the count and store the results as results.
Print results.
Print results.keys().
"""
# Import func
from sqlalchemy.sql import func

# Build an expression to calculate the sum of pop2008 labeled as population
pop2008_sum = func.sum(census.columns.pop2008).label("population")

# Build a query to select the state and sum of pop2008 as population grouped by state: stmt
stmt = select([census.columns.state, pop2008_sum])

# Append group by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())
""" sortie Ipython
<script.py> output:
    [('Alabama', 4649367), ('Alaska', 664546), ('Arizona', 6480767), ('Arkansas', 2848432), ('California', 36609002), ('Colorado', 4912947), ('Connecticut', 3493783), ('Delaware', 869221), ('District of Columbia', 588910), ('Florida', 18257662), ('Georgia', 9622508), ('Hawaii', 1250676), ('Idaho', 1518914), ('Illinois', 12867077), ('Indiana', 6373299), ('Iowa', 3000490), ('Kansas', 2782245), ('Kentucky', 4254964), ('Louisiana', 4395797), ('Maine', 1312972), ('Maryland', 5604174), ('Massachusetts', 6492024), ('Michigan', 9998854), ('Minnesota', 5215815), ('Mississippi', 2922355), ('Missouri', 5891974), ('Montana', 963802), ('Nebraska', 1776757), ('Nevada', 2579387), ('New Hampshire', 1314533), ('New Jersey', 8670204), ('New Mexico', 1974993), ('New York', 19465159), ('North Carolina', 9121606), ('North Dakota', 634282), ('Ohio', 11476782), ('Oklahoma', 3620620), ('Oregon', 3786824), ('Pennsylvania', 12440129), ('Rhode Island', 1046535), ('South Carolina', 4438870), ('South Dakota', 800997), ('Tennessee', 6202407), ('Texas', 24214127), ('Utah', 2730919), ('Vermont', 620602), ('Virginia', 7648902), ('Washington', 6502019), ('West Virginia', 1812879), ('Wisconsin', 5625013), ('Wyoming', 529490)]
    ['state', 'population']
"""





"""  
SQLAlchemy ResultsProxy and Pandas Dataframes
100xp
We can directly feed a result proxy to a Pandas DataFrame, and use the DataFrame as you would normally. In this exercise, you'll turn a ResultProxy into a DataFrame, the workhorse of many Data Scientists in PythonLand.

Instructions
Import pandas as pd.
Create a DataFrame using the provided results object as df.
Set the columns of the DataFrame to the Columns from the first result object.
Print the DataFrame.
"""
# import pandas
import pandas as pd

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set column names
df.columns = results[0].keys()

# Print the Dataframe
print(df)
""" sortie Ipython
<script.py> output:
            state  population
    0  California    36609002
    1       Texas    24214127
    2    New York    19465159
    3     Florida    18257662
    4    Illinois    12867077
"""





"""  
From SQLAlchemy results to a Graph
100xp
We can also take advantage of Pandas and MatPlotLib to build figures of our data. Remember that data visualization is essential for both exploratory data analysis and communication of your data!

Instructions
Import pyplot as plt from matplotlib.
Create a DataFrame using the provided results object as df.
Set the columns of the DataFrame to the Columns from the first result object.
Print the DataFrame.
Use the plot.bar() method on the dataframe to graph the results.
"""
# Import Pyplot as plt from matplotlib
import matplotlib.pyplot as plt

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set Column names
df.columns = results[0].keys()

# Print the DataFrame
print(df)

# Plot the DataFrame
df.plot.bar()
plt.show()

""" sortie Ipython
<script.py> output:
            state  population
    0  California    36609002
    1       Texas    24214127
    2    New York    19465159
    3     Florida    18257662
    4    Illinois    12867077
"""