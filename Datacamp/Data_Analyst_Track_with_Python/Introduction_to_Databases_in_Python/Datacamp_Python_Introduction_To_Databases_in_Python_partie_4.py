# Datacamp - Introduction To Databases in Python
# partie 4 : Advanced SQLAlchemy Queries
# Python 3.X


"""  
Creating Tables with SQLAlchemy
100xp
Previously, we used the Table object to reflect a table from an existing database, but what if we want to create a new table? We still use the Table object; however, we replace the autoload keyword arguments with Column objects. The Column object takes a name, a SQLAlchemy type with an optional format, and optional keyword arguments for different constraints. With the table defined, we're now ready to create the table in the database by using the create_all method on metadata and supplying the engine as the only parameter.

When building the table, recall how in the video we passed in 255 as the maximum length of a String, but there were no such constraints for other types.

Instructions
Import Table, Column, String, Integer, Float, Boolean from sqlalchemy.
Build a new table called data with a name (String), count (Integer), amount(Float), and valid (Boolean) columns.
Create the table in the database.
"""
# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import Table, Column,  String, Integer, Float, Boolean

# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255)),
             Column('count', Integer()),
             Column('amount', Float()),
             Column('valid', Boolean())
)

# Use the metadata to create the table
metadata.create_all(engine)

# Print table repr
print(repr(data))
""" sortie Ipython
<script.py> output:
    Table('data', MetaData(bind=None), Column('name', String(length=255), table=<data>), Column('count', Integer(), table=<data>), Column('amount', Float(), table=<data>), Column('valid', Boolean(), table=<data>), schema=None)
"""




"""  
Constraints and Data Defaults
100xp
Often, you need to make sure that a column is unique, nullable, a positive value, or related to a column in another table. These are called constraints. Many constraints are keywords on the column itself; however, they can also be passed directly to the Table object as well. In addition to constraints, you can also set a default value for the column if no data is passed to it via the default keyword on the column. There is also an onupdate keyword for setting the column value when the row is updated. This is extremely useful for keeping datetime stamps for auditing purposes.

Instructions
Import Table, Column, String, Integer, Float, Boolean from sqlalchemy.
Build a new table called data with a unique name (String), count (Integer) defaulted to 1, amount (Float), and valid (Boolean) defaulted to False.
Create the table in the database.
Print the table details for data from the metadata.tables dictionary with repr.
"""
# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import Table, Column,  String, Integer, Float, Boolean

# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255), unique=True),
             Column('count', Integer(), default=1),
             Column('amount', Float()),
             Column('valid', Boolean(), default=False)
)

# Use the metadata to create the table
metadata.create_all(engine)

# Print the table details
print(repr(metadata.tables['data']))
""" sortie Ipython
<script.py> output:
    Table('data', MetaData(bind=None), Column('name', String(length=255), table=<data>), Column('count', Integer(), table=<data>, default=ColumnDefault(1)), Column('amount', Float(), table=<data>), Column('valid', Boolean(), table=<data>, default=ColumnDefault(False)), schema=None)
"""




"""  
Inserting a single row with an insert() statement
100xp
There are several ways to perform an insert with SQLAlchemy; however, we are going to focus on the one that follows the same pattern as the select statement. It uses an insert statement where you specify the table as an argument, and supply the data you wish to insert into the value via the .values() method as keyword arguments.

Instructions
Import insert and select from the sqlalchemy module.
Build an insert statement for the data table to set name to Anna, count to 1, amount to 1000.00, and valid to True. Save the statement as stmt.
Execute stmt with the connection and store the results.
Print the results, rowcount attribute to see how many records were inserted.
Build a select statement to query for the record with the name of Anna.
Print the results of executing the select statement.
"""
# Import insert and select from sqlalchemy
from sqlalchemy import insert, select

# Build an insert statement to insert a record into the data table: stmt
stmt = insert(data).values(name="Anna", count=1, amount=1000.00, valid=True)

# Execute the statement via the connection: results
results = connection.execute(stmt)

# Print result rowcount
print(results.rowcount)

# Build a select statement to validate the insert
stmt = select([data]).where(data.columns.name == "Anna")

# Print the result of executing the query.
print(connection.execute(stmt).first())
""" sortie Ipython
<script.py> output:
    1
    ('Anna', 1, 1000.0, True)
"""




"""  
Inserting Multiple Records at Once
100xp
Often we want to insert more than just one record. In that case, we'll want to build a list of dictionaries that represents our data we want to insert and pair that with an insert statement in the execute method of the connection. To do that we build an insert statement without the values and pass the list of data dictionaries as the second argument to the execute method.

Instructions
Build a list of dictionaries called values_list with two dictionaries. In the first dictionary set name to 'Anna', count to 1, amount to 1000.00, and valid to True. In the second dictionary of the list, set name to 'Taylor', count to 1, amount to 750.00, and valid to False.
Build an insert statement for the data table for a multiple insert, save it as stmt.
Execute stmt with the values_list via connection and store the results.
Print the rowcount of the results.
"""
# Build a list of dictionaries: values_list
values_list = [
    {'name': "Anna", 'count': 1, 'amount': 1000.00, 'valid': True},
    {'name': "Taylor", 'count': 1, 'amount': 750.00, 'valid': False}
]

# Build an insert statement for the data table: stmt
stmt = insert(data)

# Execute stmt with the values_list: results
results = connection.execute(stmt, values_list)

# Print rowcount
print(results.rowcount)
""" sortie Ipython
<script.py> output:
    2
"""




"""  
Loading a CSV into a Table
100xp
We can load the contents of a CSV file into a table by using the multiple insert from the prior exercise and the python csv module. Here we are using a csv_reader that has already been setup for you. The csv_reader returns a list that represents in line from the CSV file. We can loop over the csv_reader to handle the results one at a time. The enumerate function can be used with a csv_reader to return the line number and the data as a tuple starting from line 0.

Instructions
Create a statement for bulk insert into the census table and save it as stmt.
Create a list called values_list, create a variable called total_rowcount set to 0.
Enumerate the rows of csv_reader as idx and row. Create a dictionary of each row called data and append it to values_list (NOTE: the columns are in the format of: state , sex, age, pop2000, pop2008).
If 51 will cleanly divide into the current idx (NOTE: use the % operator and make sure it is 0), Execute stmt with the values_list. Save the result as results. Add the results rowcount to total_rowcount, and set values_list back to an empty list.
Print total_rowcount when done with all the records.
"""
# Create a insert statement for census: stmt
stmt = insert(census)

# Create an empty list and zeroed row count: values_list, total_rowcount
values_list = []
total_rowcount = 0

# Enumerate the rows of csv_reader
for idx, row in enumerate(csv_reader):
    print(row)
    #create data and append to values_list
    data = {'state': row[0], 'sex': row[1], 'age': row[2], 'pop2000': row[3],
            'pop2008': row[4]}
    values_list.append(data)

    # Check to see if divisible by 51
    if idx % 51 == 0:
        results = connection.execute(stmt, values_list)
        total_rowcount += results.rowcount
        values_list = []

# Print total rowcount
print(total_rowcount)
""" sortie Ipython

"""




"""  
Updating individual records
100xp
The update statement is very similar to an insert statement, except that it also typically uses a where clause to help us determine what data to update. We'll be using the FIPS state code using here, which is appropriated by the U.S. government to identify U.S. states and certain other associated areas.

For your convenience, the names of the tables and columns of interest in this exercise are: state_fact (Table), name (Column), and fips_state (Column).

Instructions
Build a statement to view the current fips_state code for New York records and assign it to select_stmt.
Print the results of executing the Select statement.
Build an update statement to change the fips_state column code to 36, save it as stmt.
Append a where cause to target states with the name of New York in the state_fact table.
Execute stmt via the connection and save the output as results.
Print rowcount of the results.
Print the results of executing the Select statement to verify the fips_state code is now 36.
"""
# Build a statement to view the current fips_state code for New York: select_stmt
select_stmt = select([state_fact]).where(state_fact.columns.name == 'New York')

# Print the results of executing the select_stmt
print(connection.execute(select_stmt).fetchall())

# Build a statement to update the fips_state to 36: stmt
stmt = update(state_fact).values(fips_state=36)

# Append a where clause to limit it to records for New York state
stmt = stmt.where(state_fact.columns.name == "New York")

# Execute the statement: results
results = connection.execute(stmt)

# Print rowcount
print(results.rowcount)

# Execute the select_stmt again to view the changes
print(connection.execute(select_stmt).fetchall())
""" sortie Ipython
<script.py> output:
    [('32', 'New York', 'NY', 'USA', 'state', '10', 'current', 'occupied', '', '0', 'N.Y.', 'II', '1', 'Northeast', '2', 'Mid-Atlantic', '2')]
    1
    [('32', 'New York', 'NY', 'USA', 'state', '10', 'current', 'occupied', '', '36', 'N.Y.', 'II', '1', 'Northeast', '2', 'Mid-Atlantic', '2')]
"""




"""  
Updating Multiple Records
100xp
By using a where clause that would select more records, we can update Multiple records at once.

For your convenience, the names of the tables and columns of interest in this exercise are: state_fact (Table), notes (Column), and census_region_name (Column).

Instructions
Build an update statement to update the notes column in the state_fact table to The Wild West. Save it as stmt.
Append a where clause to match the West census region records.
Execute stmt via the connection and save the output as results.
Print rowcount of the results.
"""
# Build a statement to update the notes to 'The Wild West': stmt
stmt = update(state_fact).values(notes='The Wild West')

# Append a where clause to match the West census region records
stmt = stmt.where(state_fact.columns.census_region_name == "West")

# Execute the statement: results
results = connection.execute(stmt)

# Print rowcount
print(results.rowcount)
""" sortie Ipython
<script.py> output:
    13
"""




"""  
Correlated Updates
100xp
We can also update records with data from a select statement which is called a correlated update. It works by defining a select statement that returns the value we want to update the record with and assigning that as the value in an update statement. We'll be using a flat_census in this exercise as the target of our correlated update. The flat_census table is a summarized copy of our census table.

Instructions
Build a statement to select name from state_fact. Save the statement as fips_stmt.
Append a where clause that matches fips_state from the state_fact table with fips_code in the flat_census table.
Build an update statement to set the state_name in flat_census to fips_stmt, save the statement as update_stmt.
Execute the connection and store the results.
Print rowcount from results.
"""
# Build a statement to select name from state_fact: stmt
fips_stmt = select([state_fact.columns.name])

# Append a where clause to Match the fips_state to flat_census fips_code
fips_stmt = fips_stmt.where(
    state_fact.columns.fips_state == flat_census.columns.fips_code)

# Build an update statement to set the name to fips_stmt: update_stmt
update_stmt = update(flat_census).values(state_name=fips_stmt)

# Execute update_stmt: results
results = connection.execute(update_stmt)

# Print rowcount
print(results.rowcount)
""" sortie Ipython
<script.py> output:
    51
"""




"""  
Deleting all the records from a table
100xp

Often, we need to empty a table of all of its records so we can reload the data. We do this with a delete statement with just the table as an argument.
Instructions

    Import delete and select from sqlalchemy.
    Build a delete statement to remove all the data from the census table; saved it as stmt.
    Execute stmt via the connection and save the results.
    Print rowcount from the results.

"""
# Import delete, select
from sqlalchemy import delete, select

# Build a statement to empty the census table: stmt
stmt = delete(census)

# Execute the statement: results
results = connection.execute(stmt)

# Print affected rowcount
print(results.rowcount)

# Build a statement to select all records from the census table
stmt = select([census])

# Print the results of executing the statement to verify there are no rows
print(connection.execute(stmt).fetchall())
""" sortie Ipython
<script.py> output:
    8772
    []
"""




"""  
Deleting specific records
100xp

By using a where() clause we can target the delete statement to remove only certain records.
Instructions

    Build a statement to count records using the sex column for Men (M) whose age is 36.
    Build a delete statement to remove data from the census table; save it as stmt.
    Execute stmt via the connection; save the results.
    Print rowcount from the results, as well as to_delete, which returns the number of rows that should be deleted. These should match.
"""
# Build a statement to count records using the sex column for Men (M) age 36: stmt
stmt = select([func.count(census.columns.sex)]).where(
    and_(census.columns.sex == "M",
         census.columns.age == 36)
)

# Execute the select statement and use the scalar() fetch method to save the record count
to_delete = connection.execute(stmt).scalar()

# Build a statement to delete records for Men (M) age 36: stmt
stmt_del = delete(census)

# Append a where clause to target man age 36
stmt_del = stmt_del.where(
    and_(census.columns.sex == "M",
         census.columns.age == 36)
)

# Execute the statement: results
results = connection.execute(stmt_del)

# Print affected rowcount and to_delete record count, make sure they match
print(results.rowcount, to_delete)
""" sortie Ipython
<script.py> output:
    51 51
"""




"""  
Deleting a Table Completely
100xp

We can delete a table from the database by using the drop() method found on the table object. We can also drop all the tables by using a drop_all() method on the metadata object. Finally, we can check to see if a table exists with the exists() method of that table. All of these methods take an engine as the argument. Supplying the engine allows it to know which database to target. (NOTE: these operations affect the database, and will not remove the python references to the objects)
Instructions

    Drop the state_fact table.
    Check to see if state_fact exists via print.
    Drop all the tables via the metadata.
    Check to see if census exists via print.

"""
# Drop the state_fact table
state_fact.drop(engine)

# Check to see if state_fact exists
print(state_fact.exists(engine))

# Drop all tables
metadata.drop_all(engine)

# Check to see if census exists
print(census.exists(engine))
""" sortie Ipython
<script.py> output:
    False
    False
"""