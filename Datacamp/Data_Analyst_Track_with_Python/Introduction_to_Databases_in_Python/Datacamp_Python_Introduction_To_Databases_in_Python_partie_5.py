# Datacamp - Introduction To Databases in Python
# partie 5 : Putting it all together
# Python 3.X


"""  
Setup the Engine and MetaData
100xp
To do this, you need to leverage the create_engine method and MetaData object.

Instructions
Import create_engine and MetaData.
Create an engine to the sqlite:///chapter5.sqlite database.
Create a MetaData object as metadata.
"""
# Import create_engine, MetaData
from sqlalchemy import create_engine, MetaData

# Define an engine to connect to chapter5.sqlite: engine
engine = create_engine("sqlite:///chapter5.sqlite")

# Initialize MetaData: metadata
metadata = MetaData()
""" sortie Ipython

"""




"""  
Create the Table to the Database
100xp
Create the census table object and then create it in the database using MetaData and an engine

Instructions
Import Table, Column, String, and Integer.
Define a census table with the following columns:
state - String - 30 long
sex - String - 1 long
age - Integer
pop2000 - Integer
pop2008 - Integer
Create the table in the database with the metadata and engine.
"""
# Import Table, Column, String, and Integer
from sqlalchemy import Table, Column,  String, Integer

# Build a census table: census
census = Table('census', metadata,
               Column('state', String(30)),
               Column('sex', String(1)),
               Column('age', Integer()),
               Column('pop2000', Integer()),
               Column('pop2008', Integer()))

# Create the table in the database
metadata.create_all(engine)
""" sortie Ipython

"""





"""  
Reading the Data from the CSV
100xp
Leverage the Python CSV module from the standard library and load the data into a list of dictionaries.

Instructions
Create a list called values_list.
Iterate over the rows of csv_reader as row creating a dictionary of each row with the proper field names called data and append it to values_list. 
(NOTE: the columns are in the format of: state, sex, age, pop2000, pop2008)
"""
# Create an empty list: values_list
values_list = []

# Iterate over the rows
for row in csv_reader:
    # Create a dictionary with the values
    data = {'state': row[0], 'sex': row[1], 'age':row[2], 'pop2000': row[3],
            'pop2008': row[4]}
    # Append the dictionary to the values list
    values_list.append(data)
""" sortie Ipython

"""




"""  
Load Data from a list into the Table
100xp
Using the multiple insert pattern, load the data from the values_list into the table.

Instructions
Import insert.
Build an insert statement for the census table as: stmt.
Execute the insert statement with the values_list as results.
Print rowcount from results.
"""
# Import insert
from sqlalchemy import insert

# Build insert statement: stmt
stmt = insert(census)

# Use values_list to insert data: results
results = connection.execute(stmt, values_list)

# Print rowcount should be 8772
print(results.rowcount)
""" sortie Ipython
<script.py> output:
    8772

"""





"""  
Build a Query to Determine the Average Age by Population
100xp

Use the func.sum() and group_by() methods with the + and / operators to determine the average age weighted by population (NOTE: a weight average is calulated as the sum of all (weight*value) divided by the sum of all weights).
Instructions

    Import select.
    Build a statement to calculate the average ages weighted by population.
    Append group by sex.
    Label the average age calculation as average_age.
    Execute the query and store it as results.
    Print sex and average_age for each record.

"""
# Import select
from sqlalchemy import select

# Calculate weighted average age: stmt
stmt = select([census.columns.sex,
               (func.sum(census.columns.pop2008 * census.columns.age) /
                func.sum(census.columns.pop2008)).label('average_age')
               ])

# Group by sex
stmt = stmt.group_by(census.columns.sex)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the average age by sex
for row in results:
    print(row[0], row[1])
""" sortie Ipython
<script.py> output:
    F 38
    M 35
"""




"""  
Build a Query to Determine the Percentage of Population by Gender by State
100xp

Use the func.sum(), case(), cast() and group_by() methods with the / operator to determine the percentage of females by state.
Instructions

    Import case, cast and Float.
    Build a query with a case statement to calculate the percentage of females.
    Append group by state.
    Remember to cast the divisor to Float and label the column as percent_female.
    Execute the query and store it as results.
    Print state and percent_female for each record.

"""
# import case, cast and Float from sqlalchemy
from sqlalchemy import case, cast, Float

# Build a query to calculate the percentage of females in 2000: stmt
stmt = select([census.columns.state,
    (func.sum(
        case([
            (census.columns.sex == 'F', census.columns.pop2000)
        ], else_=0)) /
     cast(func.sum(census.columns.pop2000), Float) * 100).label('percent_female')
])

# Group By state
stmt = stmt.group_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the percentage
for result in results:
    print(result[0], result[1])
""" sortie Ipython
<script.py> output:
    Alabama 51.8324077702
    Alaska 49.3014978935
    Arizona 50.2236130306
    Arkansas 51.2699284622
    California 50.3523321490
    Colorado 49.8476706030
    Connecticut 51.6681650713
    Delaware 51.6110973356
    District of Columbia 53.1296261417
    Florida 51.3648800117
    Georgia 51.1140835034
    Hawaii 51.1180118369
    Idaho 49.9897262390
    Illinois 51.1122423480
    Indiana 50.9548031330
    Iowa 50.9503983425
    Kansas 50.8218641078
    Kentucky 51.3268703693
    Louisiana 51.7535159655
    Maine 51.5057081342
    Maryland 51.9357554997
    Massachusetts 51.8430235713
    Michigan 50.9724651832
    Minnesota 50.4933294430
    Mississippi 51.9222948179
    Missouri 51.4688860264
    Montana 50.3220269073
    Nebraska 50.8584549336
    Nevada 49.3673636138
    New Hampshire 50.8580198450
    New Jersey 51.5171395613
    New Mexico 51.0471720798
    New York 51.8345386515
    North Carolina 51.4822623221
    North Dakota 50.5006936323
    Ohio 51.4655035002
    Oklahoma 51.1136245708
    Oregon 50.4294670362
    Pennsylvania 51.7404347305
    Rhode Island 52.0734339190
    South Carolina 51.7307212977
    South Dakota 50.5258358137
    Tennessee 51.4306896994
    Texas 50.5157216642
    Utah 49.9729527511
    Vermont 51.0185732099
    Virginia 51.6572524472
    Washington 50.5185650872
    West Virginia 51.4004231809
    Wisconsin 50.6148645265
    Wyoming 49.9459554265
"""





"""  
Build a Query to Determine the Difference by State from the 2000 and 2008 Censuses
100xp

Use the func.sum(), order_by(), group_by() and limit() methods with the - operator to calculate the population change for the top 10 states in descending order by change.
Instructions

    Define a select statement to return the state name and calculate the population changes by population count from 2008 to 2000, labeled as pop_change, stored as stmt.
    Group by state_fact.
    Order by population change (in descending order).
    Limited to the top 10 states.
    Use the connection to execute stmt and fetch all the records store as results.
    Print the state and the population change separated by a - for each result.

"""
# Build query to return state name and population difference from 2008 to 2000
stmt = select([census.columns.state,
     (census.columns.pop2008-census.columns.pop2000).label('pop_change')
])

# Group by State
stmt = stmt.group_by(census.columns.state)

# Order by Population Change
stmt = stmt.order_by(desc('pop_change'))

# Limit to top 10
stmt = stmt.limit(10)

# Use connection to execute the statement and fetch all results
results = connection.execute(stmt).fetchall()

# Print the state and population change for each record
for result in results:
    print('{}-{}'.format(result[0], result[1]))
""" sortie Ipython
<script.py> output:
    California-105705
    Florida-100984
    Texas-51901
    New York-47098
    Pennsylvania-42387
    Arizona-29509
    Ohio-29392
    Illinois-26221
    Michigan-25126
    North Carolina-24108
"""


