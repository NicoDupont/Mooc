"""
03/2017
Dataquest : Data Analyst Path
Step 4: Working With Data Sources
SubStep : SQL and Databases: Beginner : Guided Project: Working with a SQLite database
"""


"""
1: The dataset

In this project, you'll be working with the CIA World Factbook, a compendium of country facts. The Factbook contains demographic information for each country in the world, including:

    population -- the population as of 2015.
    population_growth -- the annual population growth rate, as a percentage.
    area -- the total land and water area.

You can download the Factbook as a SQLite database here if you want to work with it on your own computer. In this guided project, you'll be working with Python and the SQLite command line tool, to connect to the database, extract data, and perform analysis.
Instructions

For now, just hit "Next" to get started with the project!
"""



"""
2: The SQLite Command Shell

SQLite is a relational database management system that enables you to create databases and query them using SQL syntax. SQLite is simpler than full database systems like MySQL and PostgreSQL. SQLite is good for cases where ease of use is more important than performance. Each SQLite database is stored as a single file, making it easy to transport.

The Factbook database is stored in the file factbook.db. db is a file extension that is short for database.

If you're in the same folder as factbook.db, and you type sqlite3 factbook.db on the command line, you'll open the Factbook database in the SQLite Command Shell. This enables you to manage the database and run SQL queries.
Instructions

Use the SQLite Shell to explore factbook.db.

    Connect to factbook.db using the SQLite shell.
    Type .help into the shell to see a list of commands you can run in the shell.
    Type .tables to see a list of the tables in the database.

    If you type .header on, you'll see the column headers when you run queries.

    If you type an incomplete command (missing ending ; for example), your command won't be executed and you'll be instead taken to an indented line. Type ; in the indented line (and press Enter) to exit the indentation and run the command. Here's an example:

Imgur

When you're done with the Command Shell, you can type .quit to quit. Don't quit the shell just yet since you'll be using it in the next step.
"""

""" Console Outputs or Results
ls
factbook.db  query.py
/home/dq/scripts$ sqlite3 factbook.db
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .help
.backup ?DB? FILE      Backup DB (default "main") to FILE
.bail ON|OFF           Stop after hitting an error.  Default OFF
.databases             List names and files of attached databases
.dump ?TABLE? ...      Dump the database in an SQL text format
                         If TABLE specified, only dump tables matching
                         LIKE pattern TABLE.
.echo ON|OFF           Turn command echo on or off
.exit                  Exit this program
.explain ?ON|OFF?      Turn output mode suitable for EXPLAIN on or off.
                         With no args, it turns EXPLAIN on.
.header(s) ON|OFF      Turn display of headers on or off
.help                  Show this message
.import FILE TABLE     Import data from FILE into TABLE
.indices ?TABLE?       Show names of all indices
                         If TABLE specified, only show indices for tables
                         matching LIKE pattern TABLE.
.load FILE ?ENTRY?     Load an extension library
.log FILE|off          Turn logging on or off.  FILE can be stderr/stdout
.mode MODE ?TABLE?     Set output mode where MODE is one of:
                         csv      Comma-separated values
                         column   Left-aligned columns.  (See .width)
                         html     HTML <table> code
                         insert   SQL insert statements for TABLE
                        line     One value per line
                         list     Values delimited by .separator string
                         tabs     Tab-separated values
                         tcl      TCL list elements
.nullvalue STRING      Use STRING in place of NULL values
.open ?FILENAME?       Close existing database and reopen FILENAME
.output FILENAME       Send output to FILENAME
.output stdout         Send output to the screen
.print STRING...       Print literal STRING
.prompt MAIN CONTINUE  Replace the standard prompts
.quit                  Exit this program
.read FILENAME         Execute SQL in FILENAME
.restore ?DB? FILE     Restore content of DB (default "main") from FILE
.schema ?TABLE?        Show the CREATE statements
                        If TABLE specified, only show tables matching
                        lIKE pattern TABLE.
.separator STRING      Change separator used by output mode and .import
.show                  Show the current values for various settings
.stats oN|OFF          Turn stats on or off
.tables ?TABLE?        List names of tables
                         If TABLE specified, only list tables matching
                         liKE pattern TABLE.
.timeout MS            Try opening locked tables for MS milliseconds
.trace FILE|off        Output each SQL statement as it is run
.vfsname ?AUX?         Print the name of the VFS stack
.width NUM1 NUM2 ...   set column widths for "column" mode
.timer ON|OFF          Turn the CPU timer measurement on or off
sqlite> ^C.tables
facts
sqlite> .header on
sqlite> select * from facts limit 10
   ...> ;
id|code|name|area|area_land|area_water|population|population_growth|birth_rate|d
eath_rate|migration_rate|created_at|updated_at
1|af|Afghanistan|652230|652230|0|32564342|2.32|38.57|13.89|1.51|2015-11-01 13:19
:49.461734|2015-11-01 13:19:49.461734
2|al|Albania|28748|27398|1350|3029278|0.3|12.92|6.58|3.3|2015-11-01 13:19:54.431
082|2015-11-01 13:19:54.431082
3|ag|Algeria|2381741|2381741|0|39542166|1.84|23.67|4.31|0.92|2015-11-01 13:19:59
.961286|2015-11-01 13:19:59.961286
4|an|Andorra|468|468|0|85580|0.12|8.13|6.96|0.0|2015-11-01 13:20:03.659945|2015-
11-01 13:20:03.659945
5|ao|Angola|1246700|1246700|0|19625353|2.78|38.78|11.49|0.46|2015-11-01 13:20:08
.625072|2015-11-01 13:20:08.625072
6|ac|Antigua and Barbuda|442|442|0|92436|1.24|15.85|5.69|2.21|2015-11-01 13:20:1
3.049627|2015-11-01 13:20:13.049627
7|ar|Argentina|2780400|2736690|43710|43431886|0.93|16.64|7.33|0.0|2015-11-01 13:
20:18.233063|2015-11-01 13:20:18.233063
8|am|Armenia|29743|28203|1540|3056382|0.15|13.61|9.34|5.8|2015-11-01 13:20:23.04
8753|2015-11-01 13:20:23.048753
9|as|Australia|7741220|7682300|58920|22751014|1.07|12.15|7.14|5.65|2015-11-01 13
:20:28.186341|2015-11-01 13:20:28.186341
10|au|Austria|83871|82445|1426|8665550|0.55|9.41|9.42|5.56|2015-11-01 13:20:33.0
93597|2015-11-01 13:20:33.093597
sqlite> .quit
"""



"""3: Running Queries
The SQLite Command Shell also allows you to run any valid SQL query. For example, you could run the following:


Loading editor...
This will show you all the rows in the facts table.

Instructions
Run some queries in the SQLite Command Shell. Make sure to turn headers on with .header on to see headers for each column.
You should think of your own queries, but here are some examples:
sELECT * FROM facts ORDER BY population DESC LIMIT 10;
sELECT * FROM facts ORDER BY area_land ASC LIMIT 10;
You may notice that these queries will show you some strange results, such as Ethiopia having the least land area. The queries also include non-national entities like the European Union and Akrotiri.
The data is fairly messy, and some values in the area_land column are missing. Add WHERE area_land != "" to the query before the ORDER BY clause to remove the invalid rows. You may also need to try additional filtering.
When you're done exploring, you can quit the SQLite Command Shell with .quit."""

""" Console Outputs or Results

"""



"""
4: Using Python With SQLite
The sqlite3 library, which comes default in Python, allows us to connect to SQLite databases. *To do this, we open a database connection, then create an object that can run queries.

For example, this will let us connect to factbook.db, and select all of the rows:

import sqlite3
"""
#conn = sqlite3.connect('factbook.db')
​"""
c = conn.cursor()
"""
#c.execute('sELECT * FROM facts;')
​"""
print(c.fetchall())
The code above creates a Connection object. We then create a Cursor instance, which can execute queries. Finally, we execute a query and display the results using the print function.
For more depth, read the package documentation here.

Instructions
Write code in query.py that will select the 10 countries with the least population from the facts table, and then print the results.
Execute query.py from the command line by running python query.py.
"""
import sqlite3
conn = sqlite3.connect('factbook.db')

c = conn.cursor()
c.execute('sELECT name FROM facts ORDER BY population DESC LIMIT 10;')

print(c.fetchall())
""" Console Outputs or Results

"""



"""
5: Computing Projected Population
You can read the results of a SQL query into a Pandas Dataframe using the read_sql_query function, which is documented here.
The read_sql_query function takes a SQL query string and a connection object, and returns a Dataframe containing all the rows and columns from the query.

When Pandas reads in columns this way, it sets the type of the column to be the type of the column in the database. Some columns, like area_land, which had blank entries in the database, will have NaN values in a DataFrame, corresponding to "Not a Number". This is because Pandas can't have blanks in numeric columns, and uses NaN as a way to signify an invalid or missing value.
"""
"""
See this Pandas documentation on how to work with missing data. The best way to deal with it for now is to just use the dropna method, with the axis=0 argument, which will drop any rows that have NaN values in them.
"""
"""
Instructions
Read the facts table into Pandas, and then compute the projected population for each country in 2050. Here are the rough steps:
Create a script called growth.py.
Read facts into a Pandas Dataframe using read_sql_query.
Filter out any rows with invalid data, such as the area_land column being 0.
Write a function that takes in the initial population and the growth rate of a country, and outputs the final population. The annual population growth (expressed as a percentage) for each country is in the population_growth column. The initial population is in the population column.
The formula for compound annual population growth is N=N0e(rt)N=N0e(rt), where NN is the final population, N0N0 is the initial population, ee is a constant value you can access with math.e, rr is the rate of annual change, expressed as a decimal (so 1.5 percent should be .015), and tt is the number of years to calculate for. Assume that you'll be starting in January 2015, and you'll be ending in January 2050, or 35 years.
Let's say you have a country with 5000 people, and a 4 percent annual growth rate. The formula would look like N=5000∗e(.04∗35)N=5000∗e(.04∗35).
Use the apply method on Pandas Dataframes to compute the population in 2050 for each row in the data.
Use the Dataframe sort_values method to sort on the 2050 population in descending order.
Print the 10 countries that will have the highest projected populations in 2050.
"""
import sqlite3
conn = sqlite3.connect('factbook.db')

import pandas as pd

facts = pd.read_sql_query("select * from facts",conn)
print(facts.info())

facts = facts.dropna(axis=0)
print("-------------")
print("-------------")
print(facts.info())

import math

def estimpop(df):
    estpop = df["population"]*(math.e**((df["population_growth"]/100)*35))
    return round(estpop,0)

facts["estimated_pop"] = facts.apply(estimpop,axis=1)
facts = facts.sort_values("estimated_pop",ascending=False)
print(facts[["name","estimated_pop","population"]][0:10])
""" Console Outputs or Results
                                 name  estimated_pop    population
76                               India   1.918415e+09  1.251696e+09
36                               China   1.600752e+09  1.367485e+09
128                            Nigeria   4.279890e+08  1.815621e+08
185                      United States   4.222466e+08  3.213689e+08
77                           Indonesia   3.532418e+08  2.559937e+08
131                           Pakistan   3.318676e+08  1.990858e+08
13                          Bangladesh   2.957897e+08  1.689577e+08
23                              Brazil   2.674393e+08  2.042598e+08
39   Congo, Democratic Republic of the   1.871078e+08  7.937514e+07
113                             Mexico   1.839863e+08  1.217368e+08
"""


"""
6: Computing Total Area
You can compute totals of a column using the SUM function in SQL queries. For example, you can select the total population with:


sELECT SUM(population) from facts;
You can also add a WHERE clause:


sELECT SUM(population) from facts WHERE area_land != "";
Instructions
Use SQL and Python to compute the ratio of how much land area countries claim as their territory versus how much water area they claim. Here are the rough steps:
Make a script called area.py.
Query to get the total of the area_land column.
Query to get the total of the area_water column`.
Divide area_land by area_water, and print the result.
"""
import sqlite3
conn = sqlite3.connect('factbook.db')

c = conn.cursor()
c.execute('SELECT sum(area_land),sum(area_water),sum(area_land)/sum(area_water) as rt FROM facts;')

print(c.fetchall())
""" Console Outputs or Results
/home/dq/scripts$ python area.py
[(128584834, 4633425, 27)]
"""



"""
7: Next Steps
That's all for the guided steps, but feel free to keep going through the data and answering questions.
We encourage you to think of your own questions, and to be creative in exploring the dataset!

Some interesting questions to get you started:

Which countries will lose population over the next 35 years?
Which countries have the lowest/highest population density?
Which countries receive the most immigrants? Which countries lose the most emigrants?
You can write scripts and explore here, or download the code to your computer using the download icon to the right:

Imgur

We hope this guided project has been a good experience, and please email us at hello@dataquest.io if you want to share your work -- we'd love to see it!
"""
