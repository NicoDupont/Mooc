# Datacamp - Introduction To Databases in Python
# partie 3 : Advanced SQLAlchemy Queries
# Python 3.X


"""  
Connecting to a MySQL Database
100xp
Before we jump into our calculation exercises, let's begin by connection to a MySQL database.

When connecting to a MySQL database, many prefer to use the pymysql database driver, which you have to install prior to use. This connection string is going to start with mysql+pymysql://, indicating which dialect and driver we are using to establish the connection. The dialect block is followed by the username:password combo. Next, we specify the host and port with the following @host:port/. Finally, we wrap up the connection string with the database_name. Now you'll practice connecting to a MySQL database: it will be the same census database that you have already been working with. One of the great things about SQLAlchemy is that, after connecting, it abstracts over the type of database it has connected to and you can write the same SQLAlchemy code, regardless.

Instructions
Import the create_engine function from the sqlalchemy library.
Create an engine to the census database on courses.csrrinzqubik.us-east-1.rds.amazonaws.com using port 3306 as the user named student with a password of datacamp.
Use the table_names() method on the engine to print the table names.
"""
# Import create_engine function
from sqlalchemy import create_engine

# Create an engine to the census database
engine = create_engine("mysql+pymysql://student:datacamp@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/census")

# Use the `tables_name()` method on the engine to print the table names
print(engine.table_names())
""" sortie Ipython
<script.py> output:
    ['census', 'state_fact']
"""




"""  
Calculating a Difference between Two Columns
100xp
Often, we need to perform math type operations as part of the query, such as the population change from 2000 to 2008. The operators work the same way for numbers in SQLAlchemy as they do in Python for math operations. We can perform addition +, subtraction -, multiplication *, division /, and modulus % via operators. Note: these operators behave differently when used with non-numeric column types. Let's find the top 5 states by population growth between 2000 and 2008.

Instructions
Define a select statement to return the state and calculate the population changes by population count from 2008 to 2000 labeled as pop_change stored as stmt.
Group the population differences by state.
Order the population changes (pop_change) in descending order.
Append limit to return only 5 records.
Use the connection to execute stmt and fetch all the records store as results.
The print statement has already been written for you. Hit 'Submit Answer' to view the results!
"""
# Build query to return state names by population difference from 2008 to 2000: stmt
stmt = select([census.columns.state, (census.columns.pop2008-census.columns.pop2000).label("pop_change")])

# Append group by for the state: stmt
stmt = stmt.group_by(census.columns.state)

# Append order by for pop_change descendingly: stmt
stmt = stmt.order_by(desc('pop_change'))

# Return only 5 results: stmt
stmt = stmt.limit(5)

# Use connection to execute the statement and fetch all results
results = connection.execute(stmt).fetchall()

# Print the state and population change for each record
for result in results:
    print('{}-{}'.format(result.state, result.pop_change))
""" sortie Ipython
<script.py> output:
    California-105705
    Florida-100984
    Texas-51901
    New York-47098
    Pennsylvania-42387
"""





"""  
Determining the Overall Percentage of Females
100xp

It's possible to combine functions and operators in a single select statement as well. These combinations can be exceptionally handy when we want to calculate percentages or averages, and we can also use the case() statement to operate on data that meets specific criteria while not affecting the query as a whole. The case() statement accepts a list of conditions to match and the column to return if the condition matches, followed by an else if none of the conditions match. We can wrap this entire expression in any function or math operation we like. Often when performing integer division, we want to get a float back. While some databases will do this automatically, you can use the cast statement to convert an expression to a particular type.
Instructions

    Import case, cast, and Float from sqlalchemy.
    Build an expression to calculate female population in 2000.
    Cast an expression to calculate total population in 2000 to Float.
    Build a query to calculate the percentage of females in 2000.
    Execute the query and store the scalar result as percent_female.
    Print percent_female.

"""
# import case, cast and Float from sqlalchemy
from sqlalchemy import case, cast, Float

# Build an expression to calculate female population in 2000
female_pop2000 = func.sum(
    case([
        (census.columns.sex == 'F', census.columns.pop2000)
    ], else_=0))

# Cast an expression to calculate total population in 2000 to Float
total_pop2000 = cast(func.sum(census.columns.pop2000), Float)

# Build a query to calculate the percentage of females in 2000: stmt
stmt = select([female_pop2000 / total_pop2000* 100])

# Execute the query and store the scalar result: percent_female
percent_female = connection.execute(stmt).scalar()

# Print the percentage
print(percent_female)
""" sortie Ipython
<script.py> output:
    51.0946743229
"""





"""  
Automatic Joins with an Established Relationship
100xp

If we have two tables that already have an established relationship, we can automatically use that relationship by just adding the columns we want from each table to the select statement.
Instructions

    Build a statement to select the pop2008 column from the census table while joining it to the state_fact table and selecting the abbreviation column from it.
    Execute the statement to get the first result and save it as result.
    Loop over the keys of the result object, and print the key and value for each one. You can use (key, getattr(result, key)) to print the key and value of result.keys().

"""
# Build a statement to join census and state_fact tables: stmt
stmt = select([census.columns.pop2008, state_fact.columns.abbreviation])

# Execute the statement and get the first result: result
result = connection.execute(stmt).first()

# Loop over the keys in the result object and print the key and value
for key in result.keys():
    print(key, getattr(result, key))
""" sortie Ipython
In [4]: print(key)
95012

In [5]: print(result)
(95012, 'IL')

In [6]: result.keys()
Out[6]: ['pop2008', 'abbreviation']

<script.py> output:
    pop2008 95012
    abbreviation IL
"""





"""  
Joins
100xp
If we aren't selecting columns from both tables or the two tables don't have a defined relationship, we can still use the join() method on a table to join it with another table and get extra data related to our query. The join() takes the table object we want to join in as the first argument and a condition that indicates how the tables are related to the second argument. Finally, we use the select_from() method on the select statement to wrap the join clause.

Instructions
Build a statement to select all the columns from the census and state_fact tables.
Append a select_from to join the census table to the state_fact table by the state column in census and the name column in the state_fact table.
Execute the statement to get the first result and save it as result.
Loop over the keys of the result object, and print the key and value for each one.
"""
# Build a statement to select the census and state_fact tables: stmt
stmt = select([census, state_fact])

# Add a select_from clause that wraps a join for the census and state_fact
# tables where the census state column and state_fact name column match
stmt = stmt.select_from(
    census.join(state_fact, census.columns.state == state_fact.columns.name))

# Execute the statement and get the first result: result
result = connection.execute(stmt).first()

# Loop over the keys in the result object and print the key and value
for key in result.keys():
    print(key, getattr(result, key))
""" sortie Ipython
In [3]: stmt = stmt.select_from(
...     census.join(state_fact, census.columns.state == state_fact.columns.name))

<script.py> output:
    state Illinois
    sex M
    age 0
    pop2000 89600
    pop2008 95012
    id 13
    name Illinois
    abbreviation IL
    country USA
    type state
    sort 10
    status current
    occupied occupied
    notes 
    fips_state 17
    assoc_press Ill.
    standard_federal_region V
    census_region 2
    census_region_name Midwest
    census_division 3
    census_division_name East North Central
    circuit_court 7
"""






"""  
More Practice with Joins
100xp
We can use the same select statement we built in the last exercise, however, let's add a twist and only return a few columns and use the other table in a group_by clause.

Instructions
Build a statement to select the state, sum of 2008 population (pop2008) and census division name (census_division_name): stmt
Append a select from to join the census and state_fact tables by the census state and state_fact name columns.
Append a group by for the state_fact name columns.
Execute the statement to get all the records and save it as results.
Loop over the results object and print each record.
"""
# Build a statement to select the state, sum of 2008 population and census
# division name: stmt
stmt = select([
    census.columns.state,
    func.sum(census.columns.pop2008),
    state_fact.columns.census_division_name
])

# Append select_from to join the census and state_fact tables by the census state and state_fact name columns
stmt = stmt.select_from(
    census.join(state_fact, census.columns.state == state_fact.columns.name)
)

# Append a group by for the state_fact name column
stmt = stmt.group_by(state_fact.columns.name)

# Execute the statement and get the results: results
results = connection.execute(stmt).fetchall()

# Loop over the results object and print each record.
for record in results:
    print(record)
""" sortie Ipython
<script.py> output:
    ('Alabama', 4649367)
    ('Alaska', 664546)
    ('Arizona', 6480767)
    ('Arkansas', 2848432)
    ('California', 36609002)
    ('Colorado', 4912947)
    ('Connecticut', 3493783)
    ('Delaware', 869221)
    ('Florida', 18257662)
    ('Georgia', 9622508)
    ('Hawaii', 1250676)
    ('Idaho', 1518914)
    ('Illinois', 12867077)
    ('Indiana', 6373299)
    ('Iowa', 3000490)
    ('Kansas', 2782245)
    ('Kentucky', 4254964)
    ('Louisiana', 4395797)
    ('Maine', 1312972)
    ('Maryland', 5604174)
    ('Massachusetts', 6492024)
    ('Michigan', 9998854)
    ('Minnesota', 5215815)
    ('Mississippi', 2922355)
    ('Missouri', 5891974)
    ('Montana', 963802)
    ('Nebraska', 1776757)
    ('Nevada', 2579387)
    ('New Hampshire', 1314533)
    ('New Jersey', 8670204)
    ('New Mexico', 1974993)
    ('New York', 19465159)
    ('North Carolina', 9121606)
    ('North Dakota', 634282)
    ('Ohio', 11476782)
    ('Oklahoma', 3620620)
    ('Oregon', 3786824)
    ('Pennsylvania', 12440129)
    ('Rhode Island', 1046535)
    ('South Carolina', 4438870)
    ('South Dakota', 800997)
    ('Tennessee', 6202407)
    ('Texas', 24214127)
    ('Utah', 2730919)
    ('Vermont', 620602)
    ('Virginia', 7648902)
    ('Washington', 6502019)
    ('West Virginia', 1812879)
    ('Wisconsin', 5625013)
    ('Wyoming', 529490)

In [11]: state_fact
Out[11]: Table('state_fact', MetaData(bind=None), Column('id', VARCHAR(length=256), table=<state_fact>), Column('name', VARCHAR(length=256), table=<state_fact>), Column('abbreviation', VARCHAR(length=256), table=<state_fact>), Column('country', VARCHAR(length=256), table=<state_fact>), Column('type', VARCHAR(length=256), table=<state_fact>), Column('sort', VARCHAR(length=256), table=<state_fact>), Column('status', VARCHAR(length=256), table=<state_fact>), Column('occupied', VARCHAR(length=256), table=<state_fact>), Column('notes', VARCHAR(length=256), table=<state_fact>), Column('fips_state', VARCHAR(length=256), table=<state_fact>), Column('assoc_press', VARCHAR(length=256), table=<state_fact>), Column('standard_federal_region', VARCHAR(length=256), table=<state_fact>), Column('census_region', VARCHAR(length=256), table=<state_fact>), Column('census_region_name', VARCHAR(length=256), table=<state_fact>), Column('census_division', VARCHAR(length=256), table=<state_fact>), Column('census_division_name', VARCHAR(length=256), table=<state_fact>), Column('circuit_court', VARCHAR(length=256), table=<state_fact>), schema=None)

"""





"""  
Using alias to handle same table joined queries
100xp
Often, we will have tables that contain hierarchical data, such as employees and managers who are also employees. The alias() method helps us accomplish this task, and because it's the same table, we only need a where clause to specify the join condition. Let's use the alias() method to build a query to join the employees table against itself to determine to whom everyone reports.

Instructions
Save an alias of the employees table as managers.
Build a query to select the employee name and their manager's name. You can use label to label the name column of managers and employees as manager and employee respectively.
Append a clause to match where the mgr field on the employee is the manager's id.
Order by the manager's name.
Execute the statement and store all the results.
Print the names of the managers and all their reports.
"""
# Make an alias of the employees table: managers
managers = employees.alias()

# Build a query to select manager's and their employees names: stmt
stmt = select(
    [managers.columns.name.label("manager"),
     employees.columns.name.label("employee")]
)

# Append where to match manager ids with employees managers: stmt
stmt = stmt.where(managers.columns.id == employees.columns.mgr)

# Append order by managers name: stmt
stmt = stmt.order_by(managers.columns.name)

# Execute statement: results
results = connection.execute(stmt).fetchall()

# print manager
for record in results:
    print(record)
""" sortie Ipython
In [1]: employees
Out[1]: Table('employees', MetaData(bind=None), Column('id', INTEGER(), table=<employees>, primary_key=True, nullable=False), Column('name', VARCHAR(length=20), table=<employees>), Column('job', VARCHAR(length=20), table=<employees>), Column('mgr', INTEGER(), table=<employees>), Column('hiredate', DATETIME(), table=<employees>), Column('sal', NUMERIC(precision=7, scale=2), table=<employees>), Column('comm', NUMERIC(precision=7, scale=2), table=<employees>), Column('dept', INTEGER(), table=<employees>), schema=None)

In [2]: managers = employees.alias()

In [3]: stmt = select(
...     [managers.columns.name,
...      employees.columns.name]
... )

In [4]: stmt = select(
...     [managers.columns.name.label("manager"),
...      employees.columns.name.label("employee")]
... )

<script.py> output:
    ('FILLMORE', 'GRANT')
    ('FILLMORE', 'ADAMS')
    ('FILLMORE', 'MONROE')
    ('GARFIELD', 'JOHNSON')
    ('GARFIELD', 'LINCOLN')
    ('GARFIELD', 'POLK')
    ('GARFIELD', 'WASHINGTON')
    ('HARDING', 'TAFT')
    ('HARDING', 'HOOVER')
    ('JACKSON', 'HARDING')
    ('JACKSON', 'GARFIELD')
    ('JACKSON', 'FILLMORE')
    ('JACKSON', 'ROOSEVELT')
"""





"""  
Leveraging Functions and Group_bys with Hierarchical Data
100xp
It's also common to want to roll up data which is in a hierarchical table. Rolling up data requires making sure we are careful which alias we use to perform the group_bys and which table we use for the function. Let's get a count of employees for each manager.

Instructions
Save an alias of the employees table as managers.
Build a query to select the manager's name and count their direct reports.
Append a where clause that ensures the manager id and employee mgr are equal.
Use a group_by() clause to group the query by the names of the managers.
Execute the statement and store all the results.
Print the names of the managers and all their reports.
"""
# Make an alias of the employees table: managers
managers = employees.alias()

# Build a query to select manager's and their employees names: stmt
stmt = select(
    [managers.columns.name,
     func.count(employees.columns.id)]
)

# Append a where clause that ensures the manager id and employee mgr are equal
stmt = stmt.where(managers.columns.id == employees.columns.mgr)

# Group by Managers Name
stmt = stmt.group_by(managers.columns.name)

# Execute statement: results
results = connection.execute(stmt).fetchall()

# print manager
for record in results:
    print(record)
""" sortie Ipython
<script.py> output:
    ('FILLMORE', 3)
    ('GARFIELD', 4)
    ('HARDING', 2)
    ('JACKSON', 4)
"""






"""  
Working on Blocks of Records
100xp
Occasionally, we have the need to work on a large ResultProxy, and don't have the memory to load all the results at once. To work around that issue, we can get blocks of rows from the ResultProxy with the fetchmany() method. With fetchmany(), give it an argument of the number of records we want. When we reach an empty list, there are no more rows left to fetch, and we have processed all the results of the query. Then you need to use the close() method to close out the connection to the database.

We already built a query with a results_proxy.

Instructions
Use a while loop that checks if there are more_results.
Inside the loop fetchmany() on results_proxy to get 50 records at a time and store those records as partial_results.
After fetching the records, if partial_results is an empty list set more_results to False.
Loop over the partial_results,
If the row.state is in the state_count dictionary, increment state_count[row.state] by 1 otherwise set state_count[row.state] to 1.
After the while loop, close the ResultProxy results_proxy.
Hit 'Submit' to print state_count.
"""
# Start a while loop checking for more results
while more_results:
    # Fetch the first 50 results from the ResultProxy: partial_results
    partial_results = results_proxy.fetchmany(50)

    # if empty list, set more_results to False
    if partial_results == []:
        more_results = False

    # Loop over the fetched records and increment the count for the state: state_count
    for row in partial_results:
        if row.state in state_count:
            state_count[row.state] += 1
        else:
            state_count[row.state] = 1

# Close the ResultProxy, and thus the connection
results_proxy.close()

# Print the count by state
print(state_count)
""" sortie Ipython
<script.py> output:
    {'Maryland': 49, 'New Jersey': 172, 'District of Columbia': 172, 'Florida': 172, 'North Dakota': 75, 'Illinois': 172, 'Idaho': 172, 'Massachusetts': 16}

"""