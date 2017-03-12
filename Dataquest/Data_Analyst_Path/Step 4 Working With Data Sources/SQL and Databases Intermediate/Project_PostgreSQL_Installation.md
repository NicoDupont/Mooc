03/2017  
Dataquest : Data Analyst Path  
Step 4: Working With Data Sources  
SubStep :  SQL and Databases: Intermediate : Project: PostgreSQL Installation 
vendredi, 10. mars 2017 06:41 





---
# 1: Introduction  

So far, we've explored many database concepts using SQLite and PostgreSQL. In this project, we'll walk through how to install the PostgreSQL database system and the psycopg2 Python library for Windows, Mac, and Linux. We'll be focusing on installing and running PostgreSQL locally on your own machine instead of on a remote server.  


---
# 2: Installing PostgreSQL  

First things first, let's install PostgreSQL. During the setup process, you'll be asked to specify a default username and password. Select a username and password combination you'll remember since you're only installing PostgreSQL locally and don't need a highly secure combination.  

Also during installation, you may be asked to specify a port number. Even though PostgreSQL will be running on the same machine, other applications communciate with it through the port as if it were on a remote machine. Port number 5432 is the default for PostgreSQL.  

Here are the installation instructions for each operating system:

 - Mac:  

Download Postgres.app [here](http://postgresapp.com/) , move to the Applications folder, and double click to launch. This applications runs in the background and you'll need it to be running to connect to it from Python. By default, PostgreSQL will run on port 5432.  
Add the following line to the end of ~/.bash_profile:  

>export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/latest/bin

 - Windows:  


Download the latest Windows installer [here](http://www.bigsql.org/postgresql/installers.jsp), double click the installer, and go through the installation wizard.  
When asked for a port number, use 5432.  

 - Linux:  

Read the installation directions for your specific flavor of Linux from [the official documentation](https://www.postgresql.org/download/linux/) .  
If asked for a port number, use 5432.  
To test your installation, open your command line application, type psql, and you should be in the PostgreSQL shell.  


---
# 3: Psycopg2  

Now let's install the psycopg2 Python library:  

 - Mac & Linux:  

Install using Anaconda:  

>conda install psycopg2.

 - Windows:  

Run the code from here for the corresponding version of Python on your machine. Run python -version to return the version of Python if you're unsure.  


---
# 4: Connecting To PostgreSQL From Psycopg2  

Launch your Python shell and import the psycopg2 library. Then, run the following code to connect to PostgreSQL and test that everything works as expected:  

```python
import psycopg2
conn = psycopg2.connect(dbname="postgres", user="postgres")
cursor = conn.cursor()
cursor.execute("CREATE TABLE notes(id integer PRIMARY KEY, body text, title text)")
conn.close()
```

If no errors were returned, then you're setup is good to go! If you run into any issues, use Google, StackOverflow, and the Dataquest member-only Slack community to get help.  