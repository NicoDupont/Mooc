"""
02/2017
Dataquest : Data Analyst Path
Step 2: Intermediate Python And Pandas
SubStep : Data Analysis With Pandas Intermediate : Pandas Internals: Dataframes
"""




"""
1: Shared Indexes
Dataframe objects can easily query and interact with many columns. 
They represent each of these columns as a Series object. We discussed how Series objects work in the previous mission. 
In this mission, we'll learn how dataframes build on Series objects to provide a powerful data analysis toolkit.

Series objects maintain data alignment between values and their index labels. 
Because dataframes are basically collections of Series objects, they maintain alignment along both columns and rows.

Pandas dataframe share a row index across columns. 
By default, this is an integer index. 
Pandas enforces this shared row index by throwing an error if we read in a CSV file with columns that contain a different number of elements.

Whenever you call a method that returns or prints a dataframe, the index values (such as a sequence of integers) appear in the leftmost column. 
You can also use the index attribute to access the index values directly. For this mission, we'll continue to work with the data set containing average user and critic ratings from the major film review sites. FiveThirtyEight compiled the data set and made it available in their Github repository.
https://github.com/fivethirtyeight/data/tree/master/fandango
Instructions
Read fandango_score_comparison.csv into a dataframe named fandango.
Use the head method to return the first two rows in the dataframe, then display them with the print function.
Use the index attribute to return the index of the dataframe, and display it with the print function.
"""
import pandas as pd
fandango = pd.read_csv("fandango_score_comparison.csv")
print(fandango.head(2))
print("-----------")
print(fandango.index)
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
-----------
RangeIndex(start=0, stop=146, step=1)
None
"""



"""
2: Using Integer Indexes To Select Rows
In the previous cell, we explored the default integer index that pandas uses for the dataframe. 
With Series, each unique index value refers to a data value. 
With dataframes, however, each index value refers to an entire row. 
We can use the integer index to select rows in a few different ways:


# First five rows
fandango[0:5]
# From row at 140 and higher
fandango[140:]
# Just row at index 50
fandango.iloc[50]
# Just row at index 45 and 90
fandango.iloc[[45,90]]
We use bracket notation to select a slice (continuous sequence) of rows, just as we would for a list. 
To select an individual row, however, we'll need to use the iloc[] method. This method accepts the following objects for selection:

An integer
A list of integers
A slice object
A Boolean array
When selecting an individual row, pandas will return a Series object. 
When selecting multiple rows, it will return a subset of the original dataframe as a new dataframe.

Instructions
Return a dataframe containing just the first and last rows, and assign it to first_last.
"""
fandango = pd.read_csv('fandango_score_comparison.csv')
first_last = fandango.iloc[[0,-1]]
print(first_last)
""" Console Output or Results
Output
                                   FILM  RottenTomatoes  RottenTomatoes_User  \
0        Avengers: Age of Ultron (2015)              74                   86   
145  Kumiko, The Treasure Hunter (2015)              87                   63   

     Metacritic  Metacritic_User  IMDB  Fandango_Stars  Fandango_Ratingvalue  \
0            66              7.1   7.8             5.0                   4.5   
145          68              6.4   6.7             3.5                   3.5   

     RT_norm  RT_user_norm         ...           IMDB_norm  RT_norm_round  \
0       3.70          4.30         ...                3.90            3.5   
145     4.35          3.15         ...                3.35            4.5   

     RT_user_norm_round  Metacritic_norm_round  Metacritic_user_norm_round  \
0                   4.5                    3.5                         3.5   
145                 3.0                    3.5                         3.0   

     IMDB_norm_round  Metacritic_user_vote_count  IMDB_user_vote_count  \
0                4.0                        1330                271107   
145              3.5                          19                  5289   

     Fandango_votes  Fandango_Difference  
0             14846                  0.5  
145              41                  0.0  

[2 rows x 22 columns]
"""



"""
3: Using Custom Indexes
The dataframe object has a set_index() method that allows us to pass in the name of the column we want pandas to use as the Dataframe index. 
By default, pandas will create a new dataframe, index it by the values in the column we specify, then drop that column. 
The set_index() method has a few parameters that allow us to tweak this behavior:

inplace: If set to True, this parameter will set the index for the current, "live" dataframe, instead of returning a new dataframe.
drop: If set to False, this parameter will keep the column we specified as the index, instead of dropping it.
Instructions
Use the pandas dataframe method set_index to assign the FILM column as the custom index for the dataframe. 
Also, specify that we don't want to drop the FILM column from the dataframe. We want to keep the original dataframe, so assign the new one to fandango_films.
Display the index for fandango_films using the index attribute and the print function.
"""
fandango = pd.read_csv('fandango_score_comparison.csv')
fandango_films = fandango.set_index("FILM",inplace=False,drop=False)
print(fandango.index)
print("------------")
print(fandango_films.index)
""" Console Output or Results
Output
RangeIndex(start=0, stop=146, step=1)
------------
Index(['Avengers: Age of Ultron (2015)', 'Cinderella (2015)', 'Ant-Man (2015)',
       'Do You Believe? (2015)', 'Hot Tub Time Machine 2 (2015)',
       'The Water Diviner (2015)', 'Irrational Man (2015)', 'Top Five (2014)',
       'Shaun the Sheep Movie (2015)', 'Love & Mercy (2015)',
       ...
       'The Woman In Black 2 Angel of Death (2015)', 'Danny Collins (2015)',
       'Spare Parts (2015)', 'Serena (2015)', 'Inside Out (2015)',
       'Mr. Holmes (2015)', ''71 (2015)', 'Two Days, One Night (2014)',
       'Gett: The Trial of Viviane Amsalem (2015)',
       'Kumiko, The Treasure Hunter (2015)'],
      dtype='object', name='FILM', length=146)
"""




"""
4: Using A Custom Index For Selection
Now that we have a custom index, we can select a row by film name instead of row number (which is the default integer index). 
We can select rows using the custom index by either:

Using the loc[] method (the same way we would the iloc[] method)
Creating a slice using bracket notation

# Slice using either bracket notation or loc[]
fandango_films["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]
fandango_films.loc["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]
​
# Specific movie
fandango_films.loc['Kumiko, The Treasure Hunter (2015)']
​
# Selecting list of movies
movies = ['Kumiko, The Treasure Hunter (2015)', 'Do You Believe? (2015)', 'Ant-Man (2015)']
fandango_films.loc[movies]
When we select multiple rows, pandas returns a dataframe. 
When we select an individual row, however, it returns a Series object instead. 
Either way, pandas will maintain the original integer index, even if we specify a custom index. 
That means we can still select by row number.

Instructions
Select the following movies from fandango_films (in the order in which they appear), and assign them to best_movies_ever:
"The Lazarus Effect (2015)"
"Gett: The Trial of Viviane Amsalem (2015)"
"Mr. Holmes (2015)"
"""
best_movies_ever = fandango_films.loc[['The Lazarus Effect (2015)','Gett: The Trial of Viviane Amsalem (2015)','Mr. Holmes (2015)']]
""" Console Output or Results
Variables
 best_movies_everDataFrame (<class 'pandas.core.frame.DataFrame'>)
"""





"""
5: Apply() Logic Over The Columns In A Dataframe
Recall that a dataframe object represents both rows and columns as Series objects. 
The apply() method in pandas allows us to specify Python logic that we want to evaluate over the Series objects in a dataframe. 
Here are some examples of what we can accomplish using the apply() method:

Calculate the standard deviations for each numeric column
Lowercase all film names in the FILM column
The apply() method requires us to pass in the vectorized operation we want to apply over each Series object. 
The method runs over the dataframe's columns by default, but we can use the axis parameter to change this (which we'll do later). 
If the vectorized operation usually returns a single value (such as the NumPy std() function), it will return a Series object containing the computed value for each column. 
If it usually returns a value for each element (such as multiplying or dividing by 2), it will transform all of the values and return them as a dataframe.

In the following code cell, we select only the float columns, and assign the dataframe containing them to float_df. 
Then, we pass in the NumPy function std() as a lambda function to the dataframe method apply() in order to calculate the standard deviation of each column. Under the hood, pandas uses vectorized operations to apply the NumPy function for each iteration of the apply() method. It then returns a final Series object containing the standard deviations for each column (i.e., the film ratings).

Instructions
This step is a demo. Play around with code or advance to the next step.
"""
import numpy as np

# returns the data types as a Series
types = fandango_films.dtypes
# filter data types to just floats, index attributes returns just column names
float_columns = types[types.values == 'float64'].index
# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]

# `x` is a Series object representing a column
deviations = float_df.apply(lambda x: np.std(x))

print(deviations)
""" Console Output or Results
Output
Metacritic_User               1.505529
IMDB                          0.955447
Fandango_Stars                0.538532
Fandango_Ratingvalue          0.501106
RT_norm                       1.503265
RT_user_norm                  0.997787
Metacritic_norm               0.972522
Metacritic_user_nom           0.752765
IMDB_norm                     0.477723
RT_norm_round                 1.509404
RT_user_norm_round            1.003559
Metacritic_norm_round         0.987561
Metacritic_user_norm_round    0.785412
IMDB_norm_round               0.501043
Fandango_Difference           0.152141
dtype: float64
"""



"""
6: Apply() Logic Over Columns: Practice
Recall that the NumPy std() method returns a single computed value when we apply it over a Series. 
In the previous code cell, the apply() method returned a single value for each column for this reason.

If we use a NumPy function that returns a value for each element in a Series, we can transform all of the values in each column and return a dataframe with those new values instead. 

Here's an example:

float_df.apply(lambda x: x*2)

This will double each of the ratings in the float columns and return a new dataframe, instead of modifying the object in place.

Instructions
Use the apply() method on float_df to halve each value, and assign the result to halved_df. Then, print the first row.
"""
double_df = float_df.apply(lambda x: x*2)
print(double_df.head(1))
halved_df = float_df.apply(lambda x: x/2)
print("--------------------")
print(halved_df.head(1))
""" Console Output or Results
Output
                                Metacritic_User  IMDB  Fandango_Stars  \
FILM                                                                    
Avengers: Age of Ultron (2015)             14.2  15.6            10.0   

                                Fandango_Ratingvalue  RT_norm  RT_user_norm  \
FILM                                                                          
Avengers: Age of Ultron (2015)                   9.0      7.4           8.6   

                                Metacritic_norm  Metacritic_user_nom  \
FILM                                                                   
Avengers: Age of Ultron (2015)              6.6                  7.1   

                                IMDB_norm  RT_norm_round  RT_user_norm_round  \
FILM                                                                           
Avengers: Age of Ultron (2015)        7.8            7.0                 9.0   

                                Metacritic_norm_round  \
FILM                                                    
Avengers: Age of Ultron (2015)                    7.0   

                                Metacritic_user_norm_round  IMDB_norm_round  \
FILM                                                                          
Avengers: Age of Ultron (2015)                         7.0              8.0   

                                Fandango_Difference  
FILM                                                 
Avengers: Age of Ultron (2015)                  1.0  
--------------------
                                Metacritic_User  IMDB  Fandango_Stars  \
FILM                                                                    
Avengers: Age of Ultron (2015)             3.55   3.9             2.5   

                                Fandango_Ratingvalue  RT_norm  RT_user_norm  \
FILM                                                                          
Avengers: Age of Ultron (2015)                  2.25     1.85          2.15   

                                Metacritic_norm  Metacritic_user_nom  \
FILM                                                                   
Avengers: Age of Ultron (2015)             1.65                1.775   

                                IMDB_norm  RT_norm_round  RT_user_norm_round  \
FILM                                                                           
Avengers: Age of Ultron (2015)       1.95           1.75                2.25   

                                Metacritic_norm_round  \
FILM                                                    
Avengers: Age of Ultron (2015)                   1.75   

                                Metacritic_user_norm_round  IMDB_norm_round  \
FILM                                                                          
Avengers: Age of Ultron (2015)                        1.75              2.0   

                                Fandango_Difference  
FILM                                                 
Avengers: Age of Ultron (2015)                 0.25 
"""



"""
7: Apply() Over Dataframe Rows
So far we've used the default behavior of the apply() method, which operates over the columns in a Datframe. 
To apply a function over the rows in a dataframe (which pandas treats as Series objects), we need to set the axis parameter to 1. 
Applying over the rows allows us to do things like calculate the standard deviation of multiple column values for each movie:


rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_user.apply(lambda x: np.std(x), axis=1)
The code above filters the dataframe down to the two columns we want. 
Because std() returns a value for each iteration, it then returns a Series object containing the standard deviation of each movie's ratings from RT_user_norm and Metacritic_user_nom.

Instructions
Use the apply() method to calculate the average of each movie's values for RT_user_norm and Metacritic_user_nom, and assign the result to the variable rt_mt_means.
Display the first five values in rt_mt_means.
"""
rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
print(rt_mt_user[0:5])
print("-------------------")
print("-------------------")
rt_mt_deviations = rt_mt_user.apply(lambda x: np.std(x), axis=1)
print(rt_mt_deviations[0:5])
print("-------------------")
print("-------------------")
rt_mt_means = rt_mt_user.apply(lambda x: np.mean(x), axis=1)
print(rt_mt_means[0:5])
""" Console Output or Results
Output
                                RT_user_norm  Metacritic_user_nom
FILM                                                             
Avengers: Age of Ultron (2015)           4.3                 3.55
Cinderella (2015)                        4.0                 3.75
Ant-Man (2015)                           4.5                 4.05
Do You Believe? (2015)                   4.2                 2.35
Hot Tub Time Machine 2 (2015)            1.4                 1.70
-------------------
-------------------
FILM
Avengers: Age of Ultron (2015)    0.375
Cinderella (2015)                 0.125
Ant-Man (2015)                    0.225
Do You Believe? (2015)            0.925
Hot Tub Time Machine 2 (2015)     0.150
dtype: float64
-------------------
-------------------
FILM
Avengers: Age of Ultron (2015)    3.925
Cinderella (2015)                 3.875
Ant-Man (2015)                    4.275
Do You Believe? (2015)            3.275
Hot Tub Time Machine 2 (2015)     1.550
dtype: float64
"""