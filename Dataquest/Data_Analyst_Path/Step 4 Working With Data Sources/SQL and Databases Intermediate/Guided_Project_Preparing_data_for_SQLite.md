03/2017  
Dataquest : Data Analyst Path  
Step 4: Working With Data Sources  
SubStep :  SQL and Databases: Intermediate : Guided Project: Preparing data for SQLite  
samedi, 11. mars 2017 06:46 

---
# 1: Introduction To The Data  

So far, we've learned how to write SQL queries to interact with existing databases. In this guided project, you'll learn how to clean a CSV dataset and add it to a SQLite database. If you're new to either our guided projects or Jupyter notebook in general, you can learn more here. You can find the solutions to this guided project here.  

We'll work with data on Academy Award nominations, which can be downloaded here. The Academy Awards, also known as the Oscars, is an annual awards ceremony hosted to recognize the achievements in the film industry. There are many different awards categories and the members of the academy vote every year to decide which artist or film should get the award. The awards categories have changed over the years, and you can learn more about when categories were added on Wikipedia.  

Here are the columns in the dataset, academy_awards.csv:  

- Year - the year of the awards ceremony.
- Category - the category of award the nominee was nominated for.
- Nominee - the person nominated for the award.
- Additional Info - this column contains additional info like:
	- the movie the nominee participated in.
	- the character the nominee played (for acting awards).
- Won? - this column contains either YES or NO depending on if the nominee won the award.

Read in the dataset into a Dataframe and explore it to become more familiar with the data. Once you've cleaned the dataset, you'll use a Pandas helper method to export the data into a SQLite database.   


#### Instructions :

 - Import pandas and read the CSV file academy_awards.csv into a Dataframe using the read_csv method.
	- When reading the CSV, make sure to set the encoding to ISO-8859-1 so it can be parsed properly.
 - Start exploring the data in Pandas and look for data quality issues.
	- Use the head method to explore the first few rows in the Dataframe.
	- There are 6 unnamed columns at the end. Use the value_counts method to explore if any of them have valid values that we need.
	- You'll notice that the Additional Info column contains a few different formatting styles. Start brainstorming ways to clean this column up.
 
```python
import pandas as pd
academy_awards = pd.read_csv("academy_awards.csv",encoding="ISO-8859-1")
print(academy_awards.head())
unamed_liste = ["Unnamed: 5","Unnamed: 6","Unnamed: 7","Unnamed: 8","Unnamed: 9","Unnamed: 10"]
for col in unamed_liste:
    print(academy_awards[col].value_counts)
    print("--------")
```  


---
# 2: Filtering The Data  

The dataset is incredibly messy and you may have noticed many inconsistencies that make it hard to work with. Most columns don't have consistent formatting, which is incredibly important when we use SQL to query the data later on. Other columns vary in the information they convey based on the type of awards category that row corresponds to.  

In the SQL and Databases: Intermediate course, we worked with a subset of the same dataset. This subset contained only the nominations from years 2001 to 2010 and only the following awards categories:  

- Actor -- Leading Role
- Actor -- Supporting Role
- Actress -- Leading Role
- Actress -- Supporting Role

Let's filter our Dataframe to the same subset so it's more manageable.  


#### Instructions :

 - Before we filter the data, let's clean up the Year column by selecting just the first 4 digits in each value in the column, therefore excluding the value in parentheses:
 	- Use Pandas vectorized string methods to select just the first 4 elements in each string.
E.g. df["Year"].str[0:2] returns a Series containing just the first 2 characters for each element in the Year column.
 	- Assign this new Series to the Year column to overwrite the original column.
 	- Convert the Year column to the int64 data type using astype. Make sure to reassign the integer Series object back to the Year column in the Dataframe or the changes won't be reflected.
 - Use conditional filtering to select only the rows from the Dataframe where the Year column is larger than 2000. Assign the new filtered Dataframe to later_than_2000.
 - Use conditional filtering to select only the rows from later_than_2000 where the Category matches one of the 4 awards we're interested in.
	- Create a list of strings named award_categories with the following strings:
		- Actor -- Leading Role
		- Actor -- Supporting Role
		- Actress -- Leading Role
		- Actress -- Supporting Role
	- Use the isin method in the conditional filter to return all rows in a column that match any of the values in a list of strings.
		- Pass in award_categories to the isin method to return all rows : later_than_2000[later_than_2000["Category"].isin(award_categories)]
		- Assign the resulting Dataframe to nominations.
 
```python
# 2: Filtering The Data
academy_awards["Year"] = academy_awards["Year"].str[0:4]
academy_awards["Year"] = academy_awards["Year"].astype("int64")
academy_awards.head()

later_than_2000 = academy_awards[academy_awards["Year"] > 2000]
award_categories = ["Actor -- Leading Role","Actor -- Supporting Role",
              "Actress -- Leading Role","Actress -- Supporting Role"]
nominations = later_than_2000[later_than_2000["Category"].isin(award_categories)]
```  

---
# 3: Cleaning Up The Won? And Unnamed Columns  

Since SQLite uses the integers 0 and 1 to represent Boolean values, convert the Won? column to reflect this. Also rename the Won? column to Won so that it's consistent with the other column names. Finally, get rid of the 6 extra, unnamed columns, since they contain only null values in our filtered Dataframe nominations.   


#### Instructions :

 - Use the Series method map to replace all NO values with 0 and all YES values with 1.
	- Select the Won? column from nominations.
	- Then create a dictionary where each key is a value we want to replace and each value is the corresponding replacement value.
		- The following dictionary replace_dict = { True: 1, False: 0 } would replace all True values with 1 and all False values with 0.
	- Call the map function on the Series object and pass in the dictionary you created.
	- Finally, reassign the new Series object to the Won? column in nominations.
 - Create a new column Won that contains the values from the Won? column.
	- Select the Won? column and assign it to the Won column. Both columns should be in the Dataframe still.
 - Use the drop method to remove the extraneous columns.
	- As the required parameter, pass in a list of strings containing the following values:
		- Won?
		- Unnamed: 5
		- Unnamed: 6
		- Unnamed: 7
		- Unnamed: 8
		- Unnamed: 9
		- Unnamed: 10
	- Set the axis parameter to 1 when calling the drop method.
	- Assign the resulting Dataframe to final_nominations.
 
```python
# 3: Cleaning Up The Won? And Unnamed Columns
replace_dict = { "YES": 1, "NO": 0 }
nominations["Won?"] = nominations["Won?"].map(replace_dict)
nominations["Won"] = nominations["Won?"]
print(nominations["Won"].value_counts())
drop_list = ["Won?"
,"Unnamed: 5"
,"Unnamed: 6"
,"Unnamed: 7"
,"Unnamed: 8"
,"Unnamed: 9"
,"Unnamed: 10"]
final_nominations = nominations.drop(drop_list,axis=1)
final_nominations.columns
```  

#### Results :  

>0    160
>1     40
>Name: Won, dtype: int64
>Index(['Year', 'Category', 'Nominee', 'Additional Info', 'Won'], dtype='object')


---
# 4: Cleaning Up The Additional Info Column  

Now clean up the Additional Info column, whose values are formatted like so:  

	MOVIE {'CHARACTER'}

Here are some examples:  

 - Biutiful {'Uxbal'} - Biutiful is the movie and Uxbal is the character this nominee played.
 - True Grit {'Rooster Cogburn'} - True Grit is the movie and Rooster Cogburn is the character this nominee played.
 - The Social Network {'Mark Zuckerberg'} - The Social Network is the movie and Mark Zuckerberg is the character this nominee played.

The values in this column contain the movie name and the character the nominee played. Instead of keeping these values in 1 column, split them up into 2 different columns for easier querying.   


#### Instructions :

 - Use vectorized string methods to clean up the Additional Info column:
	- Select the Additional Info column and strip the single quote and closing brace ("'}") using the rstrip method. Assign the resulting Series object to additional_info_one.
	- Split additional_info_one on the string, " {', using the split method and assign to additional_info_two. Each value in this Series object should be a list containing the movie name first then the character name.
	- Access the first element from each list in additional_info_two using vectorized string methods and assign to movie_names. Here's what the code looks like: additional_info_two.str[0]
	- Access the second element from each list in additional_info_two using vectorized string methods and assign to characters.
 - Assign the Series movie_names to the Movie column in the final_nominations Dataframe.
 - Assign the Series characters to the Character column in the final_nominations Dataframe.
 - Use the head method to preview the first few rows to make sure the values in the Character and Movie columns resemble the Additional Info column.
 - Drop the Additional Info column using the drop method.

Your Dataframe should look like:  

![](https://dq-content.s3.amazonaws.com/bknJGXc.png) 
 
```python
# 4: Cleaning Up The Additional Info Column
additional_info_one = final_nominations["Additional Info"].str.rstrip("'}")
additional_info_two = additional_info_one.str.split(" {'")
print(additional_info_one[0:2])
print("------------------")
print(additional_info_two[0:2])
print("------------------")
movie_names = additional_info_two.str[0]
characters = additional_info_two.str[1]
final_nominations["Movie"] = movie_names
final_nominations["Character"] = characters
final_nominations = final_nominations.drop("Additional Info", axis=1)
final_nominations.head()

```  

#### Results :  

	0               Biutiful {'Uxbal
	1    True Grit {'Rooster Cogburn
	Name: Additional Info, dtype: object
	------------------
	0               [Biutiful, Uxbal]
	1    [True Grit, Rooster Cogburn]
	Name: Additional Info, dtype: object
	------------------
	Out[18]:
	Year	Category	Nominee	Won	Movie	Character
	0	2010	Actor -- Leading Role	Javier Bardem	0	Biutiful	Uxbal
	1	2010	Actor -- Leading Role	Jeff Bridges	0	True Grit	Rooster Cogburn
	2	2010	Actor -- Leading Role	Jesse Eisenberg	0	The Social Network	Mark Zuckerberg
	3	2010	Actor -- Leading Role	Colin Firth	1	The King's Speech	King George VI
	4	2010	Actor -- Leading Role	James Franco	0	127 Hours	Aron Ralston

---
# 5: Exporting To SQLite  

Now that our Dataframe is cleaned up, let's write these records to a SQL database. We can use the Pandas Dataframe method to_sql to create a new table in a database we specify. This method has 2 required parameters:  

 - name - string corresponding to the name of the table we want created. The rows from our Dataframe will be added to this table after it's created.
 - conn: the Connection instance representing the database we want to add to.
 
Behind the scenes, Pandas creates a table and uses the first parameter to name it. Pandas uses the data types of each of the columns in the Dataframe to create a SQLite schema for this table. Since SQLite uses integer values to represent Booleans, it was important to convert the Won column to the integer values 0 and 1. We also converted the Year column to the integer data type, so that this column will have the appropriate type in our table. Here's the mapping for our columns from the Pandas data type to the SQLite data type:  

see img/img25.png

After creating the table, Pandas creates a large INSERT query and runs it to insert the values into the table. We can customize the behavior of the to_sql method using its parameters. For example, if we wanted to append rows to an existing SQLite table instead of creating a new one, we can set the if_exists parameter to "append". By default, if_exists is set to "fail" and no rows will be inserted if we specify a table name that already exists. If we're inserting a large number of records into SQLite and we want to break up the inserting of records into chunks, we can use the chunksize parameter to set the number of rows we want inserted each time.  

Since we're creating a database from scratch, we need to create a database file first so we can connect to it and export our data. To create a new database file, we use the sqlite3 library to connect to a file path that doesn't exist yet. If Python can't find the file we specified, it will create it for us and treat it as a SQLite database file.  

SQLite doesn't have a special file format and you can use any file extension you'd like when creating a SQLite database. We generally use the .db extension, which isn't a file extension that's generally used for other applications.  
 
#### Instructions :

 - Create the SQLite database nominations.db and connect to it.
	- Import sqlite3 into the environment.
	- Use the sqlite3 method connect to connect to the database file nominations.db.
		- Since it doesn't exist in our current directory, it will be automatically created.
		- Assign the returned Connection instance to conn.
 - Use the Dataframe method to_sql to export final_nominations to nominations.db.
	- For the first parameter, set the table name to "nominations".
	- For the second parameter, pass in the Connection instance.
	- Set the index parameter to False.
 
```python
# 5: Exporting To SQLite
import sqlite3
conn = sqlite3.connect("nominations.db")
final_nominations.to_sql("nominations", conn, index=False)
```  


---
# 6: Verifying In SQL  

Let's now query the database to make sure everything worked as expected.   


#### Instructions :

 - Import sqlite3 into the environment.
 - Create a Connection instance using the sqlite3 method connect to connect to your database file.
 - Explore the database to make sure the nominations table matches our Dataframe.
	- Return and print the schema using pragma table_info(). The following schema should be returned:
		- Year: Integer.
		- Category: Text.
		- Nominee: Text.
		- Won: Text.
		- Movie: Text.
		- Character: Text.
	- Return and print the first 10 rows using the SELECT and LIMIT statements.
 - Once you're done, use the Connection method close to close the connection to the database.
 
```python
#6: Verifying In SQL
info = "pragma table_info(nominations);"
ligne = "select * from nominations limit 10;"
print(conn.execute(info).fetchall())
print("-----------------")
print(conn.execute(ligne).fetchall())
conn.close()
```  

#### Results :  


	[(0, 'Year', 'INTEGER', 0, None, 0), (1, 'Category', 'TEXT', 0, None, 0), (2, 'Nominee', 'TEXT', 0, None, 0), (3, 'Won', 'INTEGER', 0, None, 0), (4, 'Movie', 'TEXT', 0, None, 0), (5, 'Character', 'TEXT', 0, None, 0)]
	-----------------
	[(2010, 'Actor -- Leading Role', 'Javier Bardem', 0, 'Biutiful', 'Uxbal'), (2010, 'Actor -- Leading Role', 'Jeff Bridges', 0, 'True Grit', 'Rooster Cogburn'), (2010, 'Actor -- Leading Role', 'Jesse Eisenberg', 0, 'The Social Network', 'Mark Zuckerberg'), (2010, 'Actor -- Leading Role', 'Colin Firth', 1, "The King's Speech", 'King George VI'), (2010, 'Actor -- Leading Role', 'James Franco', 0, '127 Hours', 'Aron Ralston'), (2010, 'Actor -- Supporting Role', 'Christian Bale', 1, 'The Fighter', 'Dicky Eklund'), (2010, 'Actor -- Supporting Role', 'John Hawkes', 0, "Winter's Bone", 'Teardrop'), (2010, 'Actor -- Supporting Role', 'Jeremy Renner', 0, 'The Town', 'James Coughlin'), (2010, 'Actor -- Supporting Role', 'Mark Ruffalo', 0, 'The Kids Are All Right', 'Paul'), (2010, 'Actor -- Supporting Role', 'Geoffrey Rush', 0, "The King's Speech", 'Lionel Logue')]


---
# 7: Next Steps  

In this guided project, you used Pandas to clean a CSV dataset and export it to a SQLite database. As a data scientist, it's important to learn many tools and how to use them together to accomplish what you need to. As you do more guided projects, you'll become more familiar with the strengths and weaknesses of each tool. For example, you probably have noticed that data cleaning is much easier in Pandas than in SQL.  

- For next steps, explore the rest of our original dataset academy_awards.csv and brainstorm how to fix the rest of the dataset:
	- The awards categories in older ceremonies were different than the ones we have today. What relevant information should we keep from older ceremonies?
	- What are all the different formatting styles that the Additional Info column contains. Can we use tools like regular expressions to capture these patterns and clean them up?
		- The nominations for the Art Direction category have lengthy values for Additional Info. What information is useful and how do we extract it?
		- Many values in Additional Info don't contain the character name the actor or actress played. Should we toss out character name altogether as we expand our data? What tradeoffs do we make by doing so?
	- What's the best way to handle awards ceremonies that included movies from 2 years?
		- E.g. see 1927/28 (1st) in the Year column.

Next up is a guided project where we'll continue down the path we started and explore how to normalize our data into multiple tables using relations.  