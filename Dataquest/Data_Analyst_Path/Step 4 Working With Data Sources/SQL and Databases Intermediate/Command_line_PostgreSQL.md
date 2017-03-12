03/2017  
Dataquest : Data Analyst Path  
Step 4: Working With Data Sources  
SubStep :  SQL and Databases: Intermediate : Command line PostgreSQL  
dimanche, 12. mars 2017 02:29 


---
# 1: The Psql Tool  

In the last mission, we worked with PostgreSQL, or Postgres, databases and tables. In this mission, we'll learn how to work with the PostgreSQL command line tool, called psql.  

psql is similar to the sqlite3 command line tool in that it allows you to connect to and manage databases. psql connects to a running PostgreSQL server process, then enables you to:  

- Run queries.
- Manage users and permissions.
- Manage databases.
- See PostgreSQL system information.

By default, psql will connect to a PostgreSQL server running on the current computer, using port 5432. If you don't specify a user and database to connect to, it will use the defaults. By default, the name of the currently logged in system user will be used as both the PostgreSQL user name and database name.  

If you're logged in to a computer as the system user dq, then type psql, you will connect to the dq database as a PostgreSQL user called dq. We'll learn later on how to connect to different databases using different PostgreSQL users.  
  
After you're finished working with psql, you can exit using the \q command.  



#### Instructions :

 - Start the PostgreSQL command line tool by typing psql.
 - Exit psql by typing \q.

 
```shell
psql
\q
```  

#### Results :  

	/home/dq$ ls                                                                    
	/home/dq$ psql                                                                  
	psql (9.4.11)                                                                   
	Type "help" for help.                                                           
	                                                                                
	dq=# \q 

---
# 2: Running SQL Queries  

After starting the psql command line tool, we can run SQL queries. Any valid SQL query will be executed. Because the psql shell is about giving instant feedback, transactions don't apply, and each command we type is immediately executed. This allows us to quickly test out queries and get results.  

Since creating a database is one SQL query, we can do it via psql. You may recall that the syntax to create a database is like the following:  

```sql
CREATE DATABASE dbName;
```

Queries in psql must end with a semicolon (;), or they won't be performed.  

#### Instructions :

 - Start the psql command line tool.
 - Create a database called bank_accounts
 - Exit the psql command line tool.
 
```shell
psql
create database bank_accounts;
\q
```  

#### Results :  

	/home/dq$ psql                                                                  
	psql (9.4.11)                                                                   
	Type "help" for help.                                                           
	                                                                                
	dq=# create database bank_accounts;                                             
	CREATE DATABASE                                                                 
	dq=# \q


---
# 3: Special PostgreSQL Commands  

We can run several special commands using psql. These commands start with a backslash (\), and can perform a variety of functions, including:  

- Listing databases
- Listing tables
- Managing users

You can see a full list of all of the special functions by running \? after starting psql. You'll need to type q to exit the resulting help interface. You can also find the full list here.  

Two common functions to run are:  

- \l -- list all available databases.
- \dt -- list all tables in the current database.
- \du -- list users.

#### Instructions :

 - Start psql.
 - List all available databases.
 - Exit psql.
 
```shell
psql
\l
\q
```  

#### Results :  

	home/dq$ psql                                                                  
	psql (9.4.11)                                                                   
	Type "help" for help.                                                           
	                                                                                
	dq=# \l                                                                         
	dq=#                                                                            
	dq=# \q



---
# 4: Switching Databases  

When we're connected to a specific SQL database, we can only create tables within that database, and run queries on tables in that database. In the past few screens, we've been connected to the dq database. This prevents us from manipulating tables in the bank_accounts database.  

You can connect to a different database using the -d option of psql. If you wanted to connect to a database called dataquest, you could use the following command:  

```shell
psql -d dataquest
```

psql will start connected to the specified database, and you'll be able to create tables in the database.  



#### Instructions :

 - Start psql and connect to the bank_accounts database.
 - Create a table called deposits in bank_accounts with the following columns:
	- id, integer, primary key
	- name, text
	- amount, float
 - Use the \dt command to list all of the tables in bank_accounts.
 - Exit psql.
 
```shell
psql -d bank_accounts
create table deposits(id integer primary key,name text, amount float);
\dt
\q
```  

#### Results :  

	/home/dq$ psql -d bank_accounts                                                 
	psql (9.4.11)                                                                   
	Type "help" for help.                                                           
	                                                                                
	bank_accounts=#                                                                 
	create table deposits(id integer primary key,name text, amount float);          
	CREATE TABLE                                                                    
	bank_accounts=# \dt                                                             
	         List of relations                                                      
	 Schema |   Name   | Type  | Owner                                              
	--------+----------+-------+-------                                             
	 public | deposits | table | dq                                                 
	(1 row)                                                                         
	                                                                                
	bank_accounts=# \q 

---
# 5: Creating Users  

In order to manage access to different databases, you can also create users. Users will be able to log into a PostgreSQL database and run queries. You can create a user with the CREATE ROLE statement. Here's how the statement looks:  

```sql
CREATE ROLE userName;
```

By default, the user isn't allowed to login to PostgreSQL and run queries. You can fix this by adding the WITH and LOGIN statements:  

```sql
CREATE ROLE userName WITH LOGIN;
```

If you run the pseudo-code above with a real username, you may be unable to login as that user. Depending on the configuration of your PostgreSQL instance, you may either be unable to login entirely, or will only be able to login when your system user name is the same as the PostgreSQL user name you want to login as. You can get around this by creating a password -- you'll then be able to login using the password. We'll cover PostgreSQL authentication and login methods in more depth in a later mission.  

You can create a password using the WITH PASSWORD statement like this:  

```sql
CREATE ROLE userName WITH LOGIN PASSWORD `password`;
```

If the user needs to be able to create databases, you can add that ability in with the CREATEDB statement:

```sql
CREATE ROLE userName WITH CREATEDB LOGIN PASSWORD 'password';
```

As you may be able to tell from above, we can keep modifying how the user is created by adding statements after the WITH statement. Some other statements we can add are:

- CREATEROLE -- allows the user to create other users.
- SUPERUSER -- makes the user a superuser. We'll cover what a superuser is later on.

For a full list of statements that can be added, see here.  

#### Instructions :

- Start psql.
- Create a user called sec with the following modifying statements:
	- LOGIN
	- PASSWORD 'test'
	- CREATEDB
- List all the users using \du.
- Exit psql.

 
```shell
psql
CREATE ROLE sec WITH CREATEDB LOGIN PASSWORD 'test';
\du
\q
```  

#### Results :  

	/home/dq$ psql                                                                  
	psql (9.4.11)                                                                   
	Type "help" for help.                                                           
	                                                                                
	dq=# CREATE ROLE sec WITH CREATEDB LOGIN PASSWORD 'test';                       
	CREATE ROLE                                                                     
	dq=# \du                                                                        
	                             List of roles                                      
	 Role name |                   Attributes                   | Member of         
	-----------+------------------------------------------------+-----------        
	 dq        | Superuser, Create role, Create DB, Replication | {}                
	 sec       | Create DB                                      | {}                
	                                                                                
	dq=# \q

---
# 6: Adding Permissions  

When users are created, they don't have any ability, or permissions, to access tables in existing databases. This is done for security reasons, so that all permissions are issued explicitly instead of being unexpected. You can issue permissions to a user using the GRANT statement. The GRANT statement will issue permissions to access certain tables in a database to a certain user. You can allow a user to perform SELECT queries on a given table like this:  

```shell
GRANT SELECT ON tableName TO userName;
```

If you want to grant different types of permissions, you can separate them with commas. The below query will allow a given user to query data from a table, update rows in the table, insert rows into the table, and delete rows from the table:  

```shell
GRANT SELECT, INSERT, UPDATE, DELETE ON tableName TO userName;
```

A shortcut for this is to use the ALL PRIVILEGES statement:  

```shell
GRANT ALL PRIVILEGES ON tableName TO userName;
```

You can use the psql \dp command to find out what privileges have been granted to users for a specific table:  

```shell
\dp tableName
```


#### Instructions :

- Start psql and connect to the bank_accounts database.
- Grant all privileges on the table deposits to the user sec.
- List all the privileges for deposits using \dp.
- Exit psql.

 
```shell
psql -d bank_accounts
GRANT ALL PRIVILEGES ON deposits TO sec;
\dp deposits
\q
```  

#### Results :  

	/home/dq$ psql -d bank_accounts                                                 
	psql (9.4.11)                                                                   
	Type "help" for help.                                                           
	                                                                                
	bank_accounts=# GRANT ALL PRIVILEGES ON deposits TO sec;                        
	GRANT                                                                           
	bank_accounts=# \dp deposits                                                    
	                            Access privileges                                   
	 Schema |   Name   | Type  | Access privileges | Column access privileges       
	--------+----------+-------+-------------------+--------------------------      
	 public | deposits | table | dq=arwdDxt/dq    +|                                
	        |          |       | sec=arwdDxt/dq    |                                
	(1 row)                                                                         
	                                                                                
	bank_accounts=# \q


---
# 7: Removing Permissions  

There are times when you'll want to remove permissions that you granted to a user previously. Permissions can be removed using the REVOKE statement. The REVOKE statement enables you to take back any permissions given via the GRANT statement. You can revoke the ability for a user to run queries:  

```sql
REVOKE SELECT ON tableName FROM userName;
```

If you want to revoke different types of permissions, you can separate them with commas. The below query will revoke permissions for a given user to query data from a table, update rows in the table, insert rows into the table, and delete rows from the table:  

```sql
REVOKE SELECT, INSERT, UPDATE, DELETE ON tableName FROM userName;
```

A shortcut for this is to use the ALL PRIVILEGES statement:  

```sql
REVOKE ALL PRIVILEGES ON tableName FROM userName;
```

The above syntax likely looks very similar to the GRANT syntax from the last screen. This is by design, and both are as similar as possible to make adding and removing permissions straightforward.  



#### Instructions :

- Start psql and connect to the bank_accounts database.
- Revoke all privileges on the table deposits from the user sec.
- List all the privileges for deposits using \dp.
- Exit psql.
 
```shell
psql -d bank_accounts
REVOKE ALL PRIVILEGES ON deposits FROM sec;
\dp deposits
\q
```  

#### Results :  

	/home/dq$ psql -d bank_accounts                                                 
	psql (9.4.11)                                                                   
	Type "help" for help.                                                           
	                                                                                
	bank_accounts=# REVOKE ALL PRIVILEGES ON deposits FROM sec;                     
	REVOKE                                                                          
	bank_accounts=# \dp deposits                                                    
	                            Access privileges                                   
	 Schema |   Name   | Type  | Access privileges | Column access privileges       
	--------+----------+-------+-------------------+--------------------------      
	 public | deposits | table | dq=arwdDxt/dq     |                                
	(1 row)                                                                         
	                                                                                
	bank_accounts=# \q



---
# 8: Superusers  

A superuser is a special type of user that overrides all access restrictions. Superusers can perform any function in a database, and a user should only be made a superuser in special cases. Adding the SUPERUSER statement to a CREATE ROLE statement will make a user a superuser:  

```sql
CREATE ROLE userName WITH SUPERUSER;
```

You can also setup login and a password for the superuser:  

```sql
CREATE ROLE userName WITH LOGIN PASSWORD 'password' SUPERUSER;
```


#### Instructions :

- Start psql.
- Create a user called aig with the following modifying statements:
	- LOGIN
	- PASSWORD 'test'
	- SUPERUSER
- List all the users using \du.
- Exit psql.
 
```shell
psql
CREATE ROLE aig WITH LOGIN PASSWORD 'test' SUPERUSER;
 \du
 \q
```  

#### Results :  

	/home/dq$ psql                                                                  
	psql (9.4.11)                                                                   
	Type "help" for help.                                                           
	                                                                                
	dq=# CREATE ROLE aig WITH LOGIN PASSWORD 'test' SUPERUSER;                      
	CREATE ROLE                                                                     
	dq=# \du                                                                        
	                             List of roles                                      
	 Role name |                   Attributes                   | Member of         
	-----------+------------------------------------------------+-----------        
	 aig       | Superuser                                      | {}                
	 dq        | Superuser, Create role, Create DB, Replication | {}                
	 sec       | Create DB                                      | {}                
	                                                                                
	dq=# \q