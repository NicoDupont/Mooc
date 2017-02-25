"""
02/2017
Dataquest : Data Analyst Path
Step 2: Intermediate Python And Pandas
SubStep : Data Analysis With Pandas Intermediate : Pandas Internals: Series
"""




"""
1: Data Structures
Over the next two missions, we'll dive into some of pandas' internals to better understand how it does things under the hood.

The three key data structures in pandas are:

Series objects (collections of values)
DataFrames (collections of Series objects)
Panels (collections of DataFrame objects)
We'll focus on the Series object in this mission.

Series objects use NumPy arrays for fast computation, but add valuable features to them for analyzing data. While NumPy arrays use an integer index, for example, Series objects can use other index types, such as a string index. Series objects also allow for mixed data types, and use the NaN Python value for handling missing values.

A Series object can hold many data types, including:

float - For float values
int - For integer values
bool - For Boolean values
datetime64[ns] - For date & time, without time zone
datetime64[ns, tz] - For date & time, with time zone
timedelta[ns] - For representing differences in dates & times (seconds, minutes, etc.)
category - For categorical values
object - For string values
Before we go into further depth, let's introduce the data set we'll be working with. The FiveThirtyEight team recently released a data set containing scores for all movies that have substantive user and critic reviews on IMDB, Rotten Tomatoes, Metacritic, and Fandango. We'll be working with the file fandango_score_comparison.csv, which you can download from their Github repository. Here are some of the columns in the data set:

FILM - Film name
RottenTomatoes - Average critic score on Rotten Tomatoes
RottenTomatoes_User - Average user score on Rotten Tomatoes
RT_norm - Average critic score on Rotten Tomatoes (normalized to a 0 to 5-point system)
RT_user-norm - Average user score on Rotten Tomatoes (normalized to a 0 to 5-point system)
Metacritic - Average critic score on Metacritic
Metacritic_User - Average user score on Metacritic
The full list of columns, along with their descriptions, is available on the Github repository.
https://github.com/fivethirtyeight/data/tree/master/fandango

Instructions
Use the pd.read_csv() function to read "fandango_score_comparison.csv" into a DataFrame object called fandango.
Then, use the .head() method to print the first two rows.
"""
import pandas as pd
fandango = pd.read_csv("fandango_score_comparison.csv")
print(fandango.head(2))
""" Console Output or Results
Output
                             FILM  RottenTomatoes  RottenTomatoes_User  \
0  Avengers: Age of Ultron (2015)              74                   86   
1               Cinderella (2015)              85                   80   

   Metacritic  Metacritic_User  IMDB  Fandango_Stars  Fandango_Ratingvalue  \
0          66              7.1   7.8             5.0                   4.5   
1          67              7.5   7.1             5.0                   4.5   

   RT_norm  RT_user_norm         ...           IMDB_norm  RT_norm_round  \
0     3.70           4.3         ...                3.90            3.5   
1     4.25           4.0         ...                3.55            4.5   

   RT_user_norm_round  Metacritic_norm_round  Metacritic_user_norm_round  \
0                 4.5                    3.5                         3.5   
1                 4.0                    3.5                         4.0   

   IMDB_norm_round  Metacritic_user_vote_count  IMDB_user_vote_count  \
0              4.0                        1330                271107   
1              3.5                         249                 65709   

   Fandango_votes  Fandango_Difference  
0           14846                  0.5  
1           12640                  0.5  

[2 rows x 22 columns]
"""



"""
2: Integer Indexes
DataFrames use Series objects to represent columns. 
When we select a single column from a DataFrame, pandas will return the Series object representing that column. 
By default, pandas indexes each individual Series object in a DataFrame with the integer data type. Each value in the Series has a unique integer index, or position. 
Like most Python data structures, the Series object uses 0-indexing. The indexing ranges from 0 to n-1, where n is the number of rows. We can use an integer index to select an individual value in a Series if we know its position.

With both NumPy arrays and Series objects, we can pass integer indexes into bracket notation to slice and select values. 
With Series objects, however, we can also specify custom indexes.

To explore this idea further, let's use two Series objects representing the film names and Rotten Tomatoes scores.

Instructions
Select the FILM column, assign it to the variable series_film, and print the first five values.
Then, select the RottenTomatoes column, assign it to the variable series_rt, and print the first five values.
"""
fandango = pd.read_csv('fandango_score_comparison.csv')
series_film = fandango["FILM"]
print(series_film[0:5])
print("----------------")
series_rt = fandango["RottenTomatoes"]
print(series_rt[0:5])
""" Console Output or Results
Output
0    Avengers: Age of Ultron (2015)
1                 Cinderella (2015)
2                    Ant-Man (2015)
3            Do You Believe? (2015)
4     Hot Tub Time Machine 2 (2015)
Name: FILM, dtype: object
----------------
0    74
1    85
2    80
3    18
4    14
Name: RottenTomatoes, dtype: int64
"""



"""
3: Custom Indexes
Both of these Series objects use the same integer indexes. 
This means that the value at index 5, for example, would describe the same film in both Series objects (The Water Diviner (2015)). 
To look up information about a specific movie, we would need to know its integer index.

If we only had these two Series objects and wanted to look up the Rotten Tomatoes scores for Minions (2015) and Leviathan (2014), we'd have to:

Find the integer index corresponding to Minions (2015) in series_film
Look up the value at that integer index from series_rt
Find the integer index corresponding to Leviathan (2014) in series_film
Look up the value at that integer index from series_rt
This becomes especially cumbersome as we scale up the problem to look for a larger number of movies. 
What we really want is a way to retrieve the Rotten Tomatoes scores for many movies at the same time with just one command (and one Series object). 
To accomplish this, we need to move away from using integer indexes, and use string indexes corresponding to the film names instead. 
Then we can pass in a list of strings matching the film names to retrieve the scores, like so:

series_custom[['Minions (2015)', 'Leviathan (2014)']]
Instructions
Create a new Series object named series_custom that has a string index (based on the values from film_names), and contains all of the Rotten Tomatoes scores from series_rt.
To create a new Series object:
Import Series from pandas.
Instantiate a new Series object, which takes in a data parameter and an index parameter. 
See the documentation for help.
Both of these parameters need to be lists.
"""
# Import the Series object from pandas
from pandas import Series

film_names = series_film.values
rt_scores = series_rt.values
series_custom = pandas.Series(data=rt_scores, index=film_names)
# 1 column and 1 Index
print(series_custom[0:5])
""" Console Output or Results
Output
Avengers: Age of Ultron (2015)    74
Cinderella (2015)                 85
Ant-Man (2015)                    80
Do You Believe? (2015)            18
Hot Tub Time Machine 2 (2015)     14
dtype: int64
"""





"""
4: Integer Index Preservation
Even though we specified that the Series object uses a custom string index, the object still has an internal integer index that we can use for selection. 
When it comes to indexes, Series objects act like both dictionaries and lists. We can access values with our custom index (like the keys in a dictionary), or the integer index (like the index in a list).

Instructions
Assign the values in series_custom at indexes 5 through 10 to the variable fiveten. 
Then, print fiveten to verify that you can still use integer values for selection.
"""
series_custom = Series(rt_scores , index=film_names)
series_custom[['Minions (2015)', 'Leviathan (2014)']]
fiveten = series_custom[5:10]
print("--------------")
print(fiveten)
""" Console Output or Results
Output
--------------
The Water Diviner (2015)        63
Irrational Man (2015)           42
Top Five (2014)                 86
Shaun the Sheep Movie (2015)    99
Love & Mercy (2015)             89
dtype: int64
"""



"""
5: Reindexing
Reindexing is the pandas way of modifying the alignment between labels (indexes) and the data (values). 
The reindex() method allows us to specify a different order for the labels (indexes) in a Series object. 
This method takes in a list of strings corresponding to the order we'd like for that Series object.

We can use the reindex() method to sort series_custom alphabetically by film. To accomplish this, we need to:

Return a list representation of the current index using tolist().
Sort the index with sorted().
Use reindex() to set the newly-ordered index.
The following code cell contains the logic for accomplishing the first task. We'll leave it up to you to finish the rest.

Instructions
The list original_index contains the original index. 
Sort this index using the Python 3 core method sorted(), then pass the result in to the Series method reindex().
Store the result in a variable named sorted_by_index.
"""
original_index = series_custom.index.tolist()
print(series_custom[0:5])
print("----------------")
sorted_by_index = series_custom.reindex(sorted(original_index))
print(sorted_by_index [0:5])
""" Console Output or Results
Output
Avengers: Age of Ultron (2015)    74
Cinderella (2015)                 85
Ant-Man (2015)                    80
Do You Believe? (2015)            18
Hot Tub Time Machine 2 (2015)     14
dtype: int64
----------------
'71 (2015)                    97
5 Flights Up (2015)           52
A Little Chaos (2015)         40
A Most Violent Year (2014)    90
About Elly (2015)             97
dtype: int64
"""



"""
6: Sorting
We just learned how to sort a Series object by the index using the reindex() method. 
This can be cumbersome if we just want to do some quick exploratory data analysis, or reorder by rating instead of film name.

To make sorting easier, pandas comes with a sort_index() method that sorts a Series by index, and a sort_values() method that sorts a Series by its values. 
Since the values representing the Rotten Tomatoes scores are integers, sorting by values will return the data in numerically ascending order (low to high).

In both cases, pandas preserves the link between each element's index (film name) and value (score). 
We call this data alignment, which is a key tenet of pandas that's incredibly important when analyzing data. 
Pandas allows us to assume the linking will be preserved, unless we specifically change a value or an index.

Instructions
Sort series_custom by index using sort_index(), and assign the result to the variable sc2.
Sort series_custom by values, and assign the result to the variable sc3.
Finally, print the first 10 values in sc2 and the first 10 values in sc3.
"""
sc2 = series_custom.sort_index()
sc3 = series_custom.sort_values()
print(sc2[0:10])
print("-----------")
print(sc3[0:10])
""" Console Output or Results
Output
'71 (2015)                    97
5 Flights Up (2015)           52
A Little Chaos (2015)         40
A Most Violent Year (2014)    90
About Elly (2015)             97
Aloha (2015)                  19
American Sniper (2015)        72
American Ultra (2015)         46
Amy (2015)                    97
Annie (2014)                  27
dtype: int64
-----------
Paul Blart: Mall Cop 2 (2015)     5
Hitman: Agent 47 (2015)           7
Hot Pursuit (2015)                8
Fantastic Four (2015)             9
Taken 3 (2015)                    9
The Boy Next Door (2015)         10
The Loft (2015)                  11
Unfinished Business (2015)       11
Mortdecai (2015)                 12
Seventh Son (2015)               12
dtype: int64
"""





"""
7: Transforming Columns With Vectorized Operations
A column is really a vector of values. For this reason, we often want to transform an entire column in a data set. 
Series objects offer robust support for vectorized operations, which enable us to run computations over an entire column very quickly.

Since pandas builds on NumPy, it takes advantage of NumPy's vectorizaton capabilities. 
These capabilities generate incredibly optimized, low level code in the C programming language to loop over the values. 
Using a traditional for loop would be much slower, especially for large data sets.

We can use any of the standard Python arithmetic operators (+, -, *, and /) to transform each of the values in a Series object. 
If we wanted to transform the Rotten Tomatoes scores from a 100-point scale to a 10-point scale, for example, we could use the Python division operator (/) to divide the Series by 10:


series_custom/10
This will return a new Series object where each value is 1/10 of the original value. 
We can even use NumPy functions to transform and run calculations over Series objects:


# Add each value with each other
np.add(series_custom, series_custom)
# Apply sine function to each value
np.sin(series_custom)
# Return the highest value (will return a single value, not a Series)
np.max(series_custom)
The values in a Series object are part of an ndarray, the core data type in NumPy. 
Applying some NumPy functions to a Series object will return a new Series object, while other functions will return a single value. 
NumPy's documentation gives us a good sense of the return value for each function. 
If a particular NumPy function usually returns an ndarray, it will return a Series object instead when we apply it to a Series.

The original DataFrame contains the column RT_norm, which represents a normalized score (from 0 to 5) of the Rotten Tomatoes average critic score. 
Let's use vectorized operations to normalize series_custom back to the 0-5 scale.

Instructions
Normalize series_custom (which is currently on a 0 to 100-point scale) to a 0 to 5-point scale by dividing each value by 20.
Assign the new normalized Series object to series_normalized.
"""
series_normalized = series_custom / 20
print(series_custom[0:5])
print("-----------")
print(series_normalized[0:5])
""" Console Output or Results
Output
Avengers: Age of Ultron (2015)    74
Cinderella (2015)                 85
Ant-Man (2015)                    80
Do You Believe? (2015)            18
Hot Tub Time Machine 2 (2015)     14
dtype: int64
-----------
Avengers: Age of Ultron (2015)    3.70
Cinderella (2015)                 4.25
Ant-Man (2015)                    4.00
Do You Believe? (2015)            0.90
Hot Tub Time Machine 2 (2015)     0.70
dtype: float64
"""



"""
8: Comparing And Filtering
Pandas uses vectorized operations for many tasks, such as filtering values within a single Series object and comparing two different Series objects. 
For example, to find all films with an average critic rating of 50 or above on Rotten Tomatoes, running:


series_custom > 50
will actually return a Series object with a Boolean value for each film. 
That's because pandas applies the filter (> 50) to each value in the Series object. 
To retrieve the actual film names, we need to pass this Boolean series into the original Series object.


series_greater_than_50 = series_custom[series_custom > 50]
Pandas returns Boolean Series objects that serve as intermediate representations of the logic. 
These objects make it easier to separate complex logic into modular pieces. 
We can specify filtering criteria in different variables, then chain them together with the and operator (&) or the or operator (|). 
Finally, we can use a Series object's bracket notation to pass in an expression representing a Boolean Series object and get back the filtered data set.

Instructions
In the following code cell, the criteria_one and criteria_two statements return Boolean Series objects.
Return a filtered Series object named both_criteria that only contains the values where both criteria are true. 
Use bracket notation and the & operator to obtain this Series object.
"""
criteria_one = series_custom > 50
criteria_two = series_custom < 75
both_criteria = series_custom[criteria_one & criteria_two]
print(criteria_one[0:5])
print("-----------")
print(criteria_two[0:5])
print("-----------")
print(both_criteria[0:5])
""" Console Output or Results
Output
Avengers: Age of Ultron (2015)     True
Cinderella (2015)                  True
Ant-Man (2015)                     True
Do You Believe? (2015)            False
Hot Tub Time Machine 2 (2015)     False
dtype: bool
-----------
Avengers: Age of Ultron (2015)     True
Cinderella (2015)                 False
Ant-Man (2015)                    False
Do You Believe? (2015)             True
Hot Tub Time Machine 2 (2015)      True
dtype: bool
-----------
Avengers: Age of Ultron (2015)    74
The Water Diviner (2015)          63
Unbroken (2014)                   51
Southpaw (2015)                   59
Insidious: Chapter 3 (2015)       59
dtype: int64
"""



"""
9: Alignment
One of pandas' core tenets is data alignment. Series objects align along indices, and DataFrame objects align along both indices and columns. 
With Series objects, pandas implicitly preserves the link between the index labels and the values across operations and transformations, unless we explicitly break it. 
With DataFrame objects, the values link to the index labels and the column labels. Pandas also preserves these links, unless we explicitly break them (by reassigning or editing a column or index label, for example).

This core tenet allows us to use pandas effectively when working with data, and offers a big advantage over using NumPy objects. For Series objects in particular, this means we can use the standard Python arithmetic operators (+, -, *, and /) to add, subtract, multiply, and divide the values at each index label for two different Series objects.

Let's use this functionality to calculate the mean ratings from both critics and users on Rotten Tomatoes.

Instructions
rt_critics and rt_users are Series objects containing the average ratings from critics and users for each film.
Both Series objects use the same custom string index, which they base on the film names. 
Use the Python arithmetic operators to return a new Series object, rt_mean, that contains the mean ratings from both critics and users for each film.
"""
rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])
rt_mean = (rt_users + rt_critics) / 2
print(rt_mean[0:5])
""" Console Output or Results
Output
FILM
Avengers: Age of Ultron (2015)    80.0
Cinderella (2015)                 82.5
Ant-Man (2015)                    85.0
Do You Believe? (2015)            51.0
Hot Tub Time Machine 2 (2015)     21.0
dtype: float64
"""


