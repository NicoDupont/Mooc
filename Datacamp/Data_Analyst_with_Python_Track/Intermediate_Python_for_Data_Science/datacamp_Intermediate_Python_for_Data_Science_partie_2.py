# Datacamp Intermediate Python for Data Science
# partie 2 : Dictionaries & Pandas

"""
Motivation for dictionaries
100xp
To see why dictionaries are useful, have a look at the two lists defined on the right. countries contains the names of some European countries. capitals lists the corresponding names of their capital.

Instructions
Use the index() method on countries to find the index of 'germany'. Store this index as ind_ger.
Use ind_ger to access the capital of Germany from the capitals list. Print it out.
"""
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])
""" sortie ipython
In [1]: countries = ['spain', 'france', 'germany', 'norway']
... capitals = ['madrid', 'paris', 'berlin', 'oslo']

In [2]: ind_ger = countries.index('germany')

In [3]: print(ind_ger)
2

In [4]: print(capitals[2])
berlin

In [5]: print(capitals[ind_ger])
berlin

<script.py> output:
    berlin
"""




"""
Create dictionary
100xp
The countries and capitals lists are again available in the script. It's your job to convert this data to a dictionary where the country names are the keys and the capitals are the corresponding values. As a refresher, here is a recipe for creating a dictionary:

my_dict = {
   "key1":"value1",
   "key2":"value2",
}
In this recipe, both the keys and the values are strings. This will also be the case for this exercise.

Instructions
With the strings in countries and capitals, create a dictionary called europe with 4 key:value pairs. Beware of capitalization! Make sure you use lowercase characters everywhere.
Print out europe to see if the result is what you expected.
"""
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {countries[0]:capitals[0],countries[1]:capitals[1],countries[2]:capitals[2],countries[3]:capitals[3]}

# Print europe
print(europe)
""" sortie ipython
In [1]: countries = ['spain', 'france', 'germany', 'norway']
... capitals = ['madrid', 'paris', 'berlin', 'oslo']

In [2]: europe = {countries[0]:capitals[0],countries[1]:capitals[1],countries[2]:capitals[2],countries[3]:capitals[3]}

In [3]: print(europe)
{'france': 'paris', 'spain': 'madrid', 'germany': 'berlin', 'norway': 'oslo'}

In [4]: europe = {countries[0].lower():capitals[0],countries[1]:capitals[1],countries[2]:capitals[2],countries[3]:capitals[3]}

"""




"""
Access dictionary
100xp
If the keys of a dictionary are chosen wisely, accessing the values in a dictionary is easy and intuitive. For example, to get the capital for France from europe you can use:

europe['france']
Here, 'france' is the key and 'paris' the value is returned.

Instructions
Check out which keys are in europe by calling the keys() method on europe. Print out the result.
Print out the value that belongs to the key 'norway'.
"""
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])
""" sortie ipython
In [1]: europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

In [2]: print(europe.keys())
dict_keys(['france', 'spain', 'germany', 'norway'])

In [3]: print(europe['norway'])
oslo

<script.py> output:
    dict_keys(['france', 'spain', 'germany', 'norway'])
    oslo
"""




"""
Dictionary Manipulation (1)
100xp
If you know how to access a dictionary, you can also assign a new value to it. To add a new key-value pair to europe you can use something like this:

europe['iceland'] = 'reykjavik'
Instructions
Add the key 'italy' with the value 'rome' to europe.
To assert that 'italy' is now a key in europe, print out 'italy' in europe.
Add another key:value pair to europe: 'poland' is the key, 'warsaw' is the corresponding value.
Print out europe.
"""
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'
# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)
""" sortie ipython
In [1]: europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

In [2]: europe += {'italy':'rome'}

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    europe += {'italy':'rome'}
TypeError: unsupported operand type(s) for +=: 'dict' and 'dict'


In [3]: print(europe)
{'france': 'paris', 'germany': 'berlin', 'spain': 'madrid', 'norway': 'oslo'}

In [4]: europe['italy'] = 'rome'

In [5]: print(europe)
{'france': 'paris', 'italy': 'rome', 'germany': 'berlin', 'spain': 'madrid', 'norway': 'oslo'}

In [6]: print(europe['italy'])
rome

In [7]: europe['poland'] = 'warsaw'

In [8]: print(europe)
{'poland': 'warsaw', 'germany': 'berlin', 'spain': 'madrid', 'france': 'paris', 'italy': 'rome', 'norway': 'oslo'}

<script.py> output:
    rome
    {'poland': 'warsaw', 'germany': 'berlin', 'spain': 'madrid', 'france': 'paris', 'italy': 'rome', 'norway': 'oslo'}

In [9]: print('italy' in europe)
True

<script.py> output:
    True
    {'poland': 'warsaw', 'germany': 'berlin', 'spain': 'madrid', 'france': 'paris', 'italy': 'rome', 'norway': 'oslo'}
"""




"""
Dictionary Manipulation (2)
100xp
Somebody thought it would be funny to mess with your accurately generated dictionary. An adapted version of the europe dictionary is available in the script on the right.

Can you clean up? Do not do this by adapting the definition of europe, but by adding Python commands to the script to update and remove key:value pairs.

Instructions
The capital of Germany is not 'bonn'; it's 'berlin'. Update its value.
Australia is not in Europe, Austria is! Remove they key 'australia' from europe.
Print out europe to see if your cleaning work paid off.
"""
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn', 
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)
""" sortie ipython
In [1]: europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn', 
...           'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 
...           'australia':'vienna' }
... 

In [2]: europe['germany'] = 'berlin'

In [3]: print(europe)
{'poland': 'warsaw', 'australia': 'vienna', 'germany': 'berlin', 'spain': 'madrid', 'france': 'paris', 'italy': 'rome', 'norway': 'oslo'}

In [4]: del(europe['australia'])

In [5]: print(europe)
{'poland': 'warsaw', 'germany': 'berlin', 'spain': 'madrid', 'france': 'paris', 'italy': 'rome', 'norway': 'oslo'}

In [6]: print(europe)
<script.py> output:
    {'poland': 'warsaw', 'germany': 'berlin', 'spain': 'madrid', 'france': 'paris', 'italy': 'rome', 'norway': 'oslo'}
"""



"""
Dictionariception
100xp
Remember lists? They could contain anything, even other lists. Well, for dictionaries the same holds. Dictionaries can contain key:value pairs where the values are again dictionaries.

As an example, have a look at the script where another version of europe - the dictionary you've been working with all along - is coded. The keys are still the country names, but the values are dictionaries that contain more information than just the capital.

It's perfectly possible to chain square brackets to select elements. To fetch the population for spain from europe, for example, you need:

europe['spain']['population']
Instructions
Use chained square brackets to select and print out the capital of France.
Create a dictionary, named data, with the keys capital and population. Set them to 'rome' and 59.83, respectively.
Add a new key-value pair to europe: the key is 'italy' and the value is data, the dictionary you just built.
"""
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }
           
           
# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital':'rome','population':59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)
""" sortie ipython
In [1]: europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
...            'france': { 'capital':'paris', 'population':66.03 },
...            'germany': { 'capital':'berlin', 'population':80.62 },
...            'norway': { 'capital':'oslo', 'population':5.084 } }

In [2]: print(europe['france']['capital'])
paris

In [3]: data = {'capital':'rome','population':59.83}

In [4]: europe['italy'] = data

In [5]: print(europe)
{'france': {'population': 66.03, 'capital': 'paris'}, 'italy': {'population': 59.83, 'capital': 'rome'}, 'germany': {'population': 80.62, 'capital': 'berlin'}, 'spain': {'population': 46.77, 'capital': 'madrid'}, 'norway': {'population': 5.084, 'capital': 'oslo'}}

<script.py> output:
    paris
    {'france': {'population': 66.03, 'capital': 'paris'}, 'italy': {'population': 59.83, 'capital': 'rome'}, 'germany': {'population': 80.62, 'capital': 'berlin'}, 'spain': {'population': 46.77, 'capital': 'madrid'}, 'norway': {'population': 5.084, 'capital': 'oslo'}}
"""



# PANDAS

"""
Dictionary to DataFrame (1)
100xp
Pandas is an open source library, providing high-performance, easy-to-use data structures and data analysis tools for Python. Sounds promising!

The DataFrame is one of Pandas' most important data structures. It's basically a way to store tabular data, where you can label the rows and the columns. One way to build a DataFrame is from a dictionary.

In the exercises that follow you will be working with vehicle data in different countries. Each observation corresponds to a country and the columns give information about the number of vehicles per capita, whether people drive left or right, and so on.

Three lists are defined in the script: - names, containing the country names for which data is available. - dr, a list with booleans that tells whether people drive left or right in the corresponding country. - cpc, the number of motor vehicles per 1000 people in the corresponding country.

Each dictionary key is a column label and each value is a list which contains the column elements.

Instructions
Import pandas as pd.
Use the pre-defined lists to create dictionary, called my_dict. There should be three key value pairs:
key 'country' and value names.
key 'drives_right' and value dr.
key 'cars_per_cap' and value cpc.
Use pd.DataFrame() to turn your dict into a DataFrame called cars.
Print out cars and see how beautiful it is.
"""
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names,'drives_right':dr,'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)
""" sortie ipython
In [1]: names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
... dr =  [True, False, False, False, True, True, True]
... cpc = [809, 731, 588, 18, 200, 70, 45]

In [2]: import pandas as pd

In [3]: my_dict = {'country':names,'drives_right':dr,'cars_per_cap',cpc}

  File "<stdin>", line 1
    my_dict = {'country':names,'drives_right':dr,'cars_per_cap',cpc}
                                                               ^
SyntaxError: invalid syntax


In [4]: my_dict = {'country':names,'drives_right':dr,'cars_per_cap':cpc}

In [5]: cars = pd.DataFrame(my_dict)

In [6]: print(cars)
   cars_per_cap        country drives_right
0           809  United States         True
1           731      Australia        False
2           588          Japan        False
3            18          India        False
4           200         Russia         True
5            70        Morocco         True
6            45          Egypt         True

<script.py> output:
       cars_per_cap        country drives_right
    0           809  United States         True
    1           731      Australia        False
    2           588          Japan        False
    3            18          India        False
    4           200         Russia         True
    5            70        Morocco         True
    6            45          Egypt         True
"""





"""
Dictionary to DataFrame (2)
100xp
The Python code that solves the previous exercise is included on the right. Have you noticed that the row labels (so the labels for the different observations) where automatically set to integers from 0 up to 6?

To solve this a list row_labels has been created. You can use it to specify the row labels of the cars DataFrame. You do this by setting the index attribute of cars, that you can access as cars.index.

Instructions
Hit Submit Answer to see that, indeed, the row labels are not correctly set.
Specify the row labels by setting cars.index equal to row_labels.
Print out cars again and check if the row labels are correct this time.
"""
import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)
""" sortie ipython
In [1]: import pandas as pd
... 
... # Build cars DataFrame
... names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
... dr =  [True, False, False, False, True, True, True]
... cpc = [809, 731, 588, 18, 200, 70, 45]
... dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
... cars = pd.DataFrame(dict)
... print(cars)
   cars_per_cap        country drives_right
0           809  United States         True
1           731      Australia        False
2           588          Japan        False
3            18          India        False
4           200         Russia         True
5            70        Morocco         True
6            45          Egypt         True

In [2]: row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

In [3]: cars.index = row_labels

In [4]: print(cars)
     cars_per_cap        country drives_right
US            809  United States         True
AUS           731      Australia        False
JAP           588          Japan        False
IN             18          India        False
RU            200         Russia         True
MOR            70        Morocco         True
EG             45          Egypt         True

<script.py> output:
       cars_per_cap        country drives_right
    0           809  United States         True
    1           731      Australia        False
    2           588          Japan        False
    3            18          India        False
    4           200         Russia         True
    5            70        Morocco         True
    6            45          Egypt         True
         cars_per_cap        country drives_right
    US            809  United States         True
    AUS           731      Australia        False
    JAP           588          Japan        False
    IN             18          India        False
    RU            200         Russia         True
    MOR            70        Morocco         True
    EG             45          Egypt         True
"""





"""
CSV to DataFrame (1)
100xp
Putting data in a dictionary and then building a DataFrame works, but it's not very efficient. What if you're dealing with millions of observations? In those cases, the data is typically available as files with a regular structure. One of those file types is the CSV file, which is short for "comma-separated values".

To import CSV data into Python as a Pandas DataFrame you can use read_csv().

Let's explore this function with the same cars data from the previous exercises. This time, however, the data is available in a CSV file, named cars.csv. It is available in your current working directory, so the path to the file is simply 'cars.csv'.

Instructions
To import CSV files you still need the pandas package: import it as pd.
Use pd.read_csv() to import cars.csv data as a DataFrame. Store this dataframe as cars.
Print out cars. Does everything look OK?
"""
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv("cars.csv")

# Print out cars
print(cars)
""" sortie ipython
In [1]: import pandas as pd

In [2]: cars = pd.read_csv("cars.csv")

In [3]: print(cars)
  Unnamed: 0  cars_per_cap        country drives_right
0         US           809  United States         True
1        AUS           731      Australia        False
2        JAP           588          Japan        False
3         IN            18          India        False
4         RU           200         Russia         True
5        MOR            70        Morocco         True
6         EG            45          Egypt         True

<script.py> output:
      Unnamed: 0  cars_per_cap        country drives_right
    0         US           809  United States         True
    1        AUS           731      Australia        False
    2        JAP           588          Japan        False
    3         IN            18          India        False
    4         RU           200         Russia         True
    5        MOR            70        Morocco         True
    6         EG            45          Egypt         True
"""




"""
CSV to DataFrame (2)
100xp
Your read_csv() call to import the CSV data didn't generate an error, but the output is not entirely what we wanted. The row labels were imported as another column without a name.

Remember index_col, an argument of read_csv(), that you can use to specify which column in the CSV file should be used as a row label? Well, that's exactly what you need here!

Python code that solves the previous exercise is already included; can you make the appropriate changes to fix the data import?

Instructions
Run the code with Submit Answer and assert that the first column should actually be used as row labels.
Specify the index_col argument inside pd.read_csv(): set it to 0, so that the first column is used as row labels.
Has the printout of cars improved now?
"""
# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out cars
print(cars)
""" sortie ipython
<script.py> output:
         cars_per_cap        country drives_right
    US            809  United States         True
    AUS           731      Australia        False
    JAP           588          Japan        False
    IN             18          India        False
    RU            200         Russia         True
    MOR            70        Morocco         True
    EG             45          Egypt         True
"""




"""
Square Brackets (1)
100xp
In the video, you saw that you can index and select Pandas DataFrames in many different ways. The simplest, but not the most powerful way, is to use square brackets.

In the sample code on the right, the same cars data is imported from a CSV files as a Pandas DataFrame. To select only the cars_per_cap column from cars, you can use:

cars['cars_per_cap']
cars[['cars_per_cap']] 
The single bracket version gives a Pandas Series, the double bracket version gives a Pandas DataFrame.

Instructions
Use single square brackets to print out the country column of cars as a Pandas Series.
Use double square brackets to print out the country column of cars as a Pandas DataFrame.
Use double square brackets to print out a DataFrame with both the country and drives_right columns of cars, in this order.
"""
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country','drives_right']])
""" sortie ipython
In [1]: import pandas as pd
... cars = pd.read_csv('cars.csv', index_col = 0)

In [2]: print(cars['country'])
US     United States
AUS        Australia
JAP            Japan
IN             India
RU            Russia
MOR          Morocco
EG             Egypt
Name: country, dtype: object

In [3]: type(cars['country'])
Out[3]: pandas.core.series.Series

In [4]: print(cars[['country']])
           country
US   United States
AUS      Australia
JAP          Japan
IN           India
RU          Russia
MOR        Morocco
EG           Egypt

In [5]: type(cars[['country']])
Out[5]: pandas.core.frame.DataFrame

In [6]: print(cars[['country','drives_right']])
           country drives_right
US   United States         True
AUS      Australia        False
JAP          Japan        False
IN           India        False
RU          Russia         True
MOR        Morocco         True
EG           Egypt         True

<script.py> output:
    US     United States
    AUS        Australia
    JAP            Japan
    IN             India
    RU            Russia
    MOR          Morocco
    EG             Egypt
    Name: country, dtype: object
               country
    US   United States
    AUS      Australia
    JAP          Japan
    IN           India
    RU          Russia
    MOR        Morocco
    EG           Egypt
               country drives_right
    US   United States         True
    AUS      Australia        False
    JAP          Japan        False
    IN           India        False
    RU          Russia         True
    MOR        Morocco         True
    EG           Egypt         True
"""





"""
Square Brackets (2)
100xp
Square brackets can do more than just selecting columns. You can also use them to get rows, or observations, from a DataFrame. The following call selects the first five rows from the cars DataFrame:

cars[0:5]
The result is another DataFrame containing only the rows you specified.

Pay attention: You can only select rows using square brackets if you specify a slice, like 0:4. Also, you're using the integer indexes of the rows here, not the row labels!

Instructions
Select the first 3 observations from cars and print them out.
Select the fourth, fifth and sixth obseration, corresponding to row indexes 3, 4 and 5, and print them out.
"""
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])
""" sortie ipython
In [1]: import pandas as pd
... cars = pd.read_csv('cars.csv', index_col = 0)

In [2]: print(cars[1:4])
     cars_per_cap    country drives_right
AUS           731  Australia        False
JAP           588      Japan        False
IN             18      India        False

In [3]: print(cars[4:7])
     cars_per_cap  country drives_right
RU            200   Russia         True
MOR            70  Morocco         True
EG             45    Egypt         True

In [4]: print(cars)
     cars_per_cap        country drives_right
US            809  United States         True
AUS           731      Australia        False
JAP           588          Japan        False
IN             18          India        False
RU            200         Russia         True
MOR            70        Morocco         True
EG             45          Egypt         True

In [5]: print(cars[0:3])
     cars_per_cap        country drives_right
US            809  United States         True
AUS           731      Australia        False
JAP           588          Japan        False

In [6]: print(cars[3:6])
     cars_per_cap  country drives_right
IN             18    India        False
RU            200   Russia         True
MOR            70  Morocco         True

<script.py> output:
         cars_per_cap        country drives_right
    US            809  United States         True
    AUS           731      Australia        False
    JAP           588          Japan        False
         cars_per_cap  country drives_right
    IN             18    India        False
    RU            200   Russia         True
    MOR            70  Morocco         True
"""





"""
loc and iloc (1)
100xp
With loc and iloc you can do practically any data selection operation on DataFrames you can think of. loc is label-based, which means that you have to specify rows and columns based on their row and column labels. iloc is integer index based, so you have to specify rows and columns by their integer index like you did in the previous exercise.

Try out the following commands in the IPython Shell to experiment with loc and iloc to select observations. Each pair of commands here gives the same result.

cars.loc['RU']
cars.iloc[4]

cars.loc[['RU']]
cars.iloc[[4]]

cars.loc[['RU', 'AUS']]
cars.iloc[[4, 1]]
As before, code is included that imports the cars data as a Pandas DataFrame.

Instructions
Use loc or iloc to select the observation corresponding to Japan as a Series. The label of this row is JAP, the index is 2. Make sure to print the resulting Series.
Use loc or iloc to select the observations for Australia and Egypt as a DataFrame. You can find out about the labels/indexes of these rows by inspecting cars in the IPython Shell. Make sure to print the resulting DataFrame.
"""
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.iloc[[1, 6]])
""" sortie ipython
In [1]: import pandas as pd
... cars = pd.read_csv('cars.csv', index_col = 0)

In [2]: print(cars)
     cars_per_cap        country drives_right
US            809  United States         True
AUS           731      Australia        False
JAP           588          Japan        False
IN             18          India        False
RU            200         Russia         True
MOR            70        Morocco         True
EG             45          Egypt         True

In [3]: print(cars.iloc[2])
cars_per_cap      588
country         Japan
drives_right    False
Name: JAP, dtype: object

In [4]: print(cars.iloc[[1, 7]])

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(cars.iloc[[1, 7]])
  File "<stdin>", line 1311, in __getitem__
    return self._getitem_axis(key, axis=0)
  File "<stdin>", line 1614, in _getitem_axis
    self._is_valid_list_like(key, axis)
  File "<stdin>", line 1553, in _is_valid_list_like
    raise IndexError("positional indexers are out-of-bounds")
IndexError: positional indexers are out-of-bounds


In [5]: print(cars.iloc[[1, 7]])

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(cars.iloc[[1, 7]])
  File "<stdin>", line 1311, in __getitem__
    return self._getitem_axis(key, axis=0)
  File "<stdin>", line 1614, in _getitem_axis
    self._is_valid_list_like(key, axis)
  File "<stdin>", line 1553, in _is_valid_list_like
    raise IndexError("positional indexers are out-of-bounds")
IndexError: positional indexers are out-of-bounds


In [6]: print(cars.iloc[[1, 7]])

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(cars.iloc[[1, 7]])
  File "<stdin>", line 1311, in __getitem__
    return self._getitem_axis(key, axis=0)
  File "<stdin>", line 1614, in _getitem_axis
    self._is_valid_list_like(key, axis)
  File "<stdin>", line 1553, in _is_valid_list_like
    raise IndexError("positional indexers are out-of-bounds")
IndexError: positional indexers are out-of-bounds


In [7]: print(cars.iloc[[1, 6]])
     cars_per_cap    country drives_right
AUS           731  Australia        False
EG             45      Egypt         True

<script.py> output:
    cars_per_cap      588
    country         Japan
    drives_right    False
    Name: JAP, dtype: object
         cars_per_cap    country drives_right
    AUS           731  Australia        False
    EG             45      Egypt         True
"""





"""
loc and iloc (2)
100xp
loc and iloc also allow you to select both rows and columns from a DataFrame. To experiment, try out the following commands in the IPython Shell. Again, paired commands produce the same result.

cars.loc['IN', 'cars_per_cap']
cars.iloc[3, 0]

cars.loc[['IN', 'RU'], 'cars_per_cap']
cars.iloc[[3, 4], 0]

cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
cars.iloc[[3, 4], [0, 1]]
Instructions
Print out the drives_right value of the row corresponding to Morocco (its row label is MOR)
Print out a sub-DataFrame, containing the observations for Russia and Morocco and the columns country and drives_right.
"""
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR','drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU','MOR'],['country','drives_right']])
""" sortie ipython
In [1]: import pandas as pd
... cars = pd.read_csv('cars.csv', index_col = 0)

In [2]: print(cars)
     cars_per_cap        country drives_right
US            809  United States         True
AUS           731      Australia        False
JAP           588          Japan        False
IN             18          India        False
RU            200         Russia         True
MOR            70        Morocco         True
EG             45          Egypt         True

In [3]: print(cars.loc[['MOR','drives_right']])
              cars_per_cap  country drives_right
MOR                   70.0  Morocco         True
drives_right           NaN      NaN          NaN

In [4]: print(cars.loc['MOR','drives_right'])
True

In [5]: print(cars.loc[['RU','MOR'],['country','drives_right']])
     country drives_right
RU    Russia         True
MOR  Morocco         True

<script.py> output:
    True
         country drives_right
    RU    Russia         True
    MOR  Morocco         True
"""





"""
loc and iloc (3)
100xp
It's also possible to select only columns with loc and iloc. In both cases, you simply put a slice going from beginning to end in front of the comma:

cars.loc[:, 'country']
cars.iloc[:, 1]

cars.loc[:, ['country','drives_right']]
cars.iloc[:, [1, 2]]
Instructions
Print out the drives_right column as a Series using loc or iloc.
Print out the drives_right column as a DataFrame using loc or iloc.
Print out both the cars_per_cap and drives_right column as a DataFrame using loc or iloc.
"""
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:,['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['cars_per_cap','drives_right']])
""" sortie ipython
In [1]: import pandas as pd
... cars = pd.read_csv('cars.csv', index_col = 0)
... 

In [2]: print(cars.loc[:,'drives_right'])
US      True
AUS    False
JAP    False
IN     False
RU      True
MOR     True
EG      True
Name: drives_right, dtype: bool

In [3]: print(cars.loc[:,['drives_right']])
    drives_right
US          True
AUS        False
JAP        False
IN         False
RU          True
MOR         True
EG          True

In [4]: print(cars.loc[:,['cars_per_cap','drives_right']])
     cars_per_cap drives_right
US            809         True
AUS           731        False
JAP           588        False
IN             18        False
RU            200         True
MOR            70         True
EG             45         True

<script.py> output:
    US      True
    AUS    False
    JAP    False
    IN     False
    RU      True
    MOR     True
    EG      True
    Name: drives_right, dtype: bool
        drives_right
    US          True
    AUS        False
    JAP        False
    IN         False
    RU          True
    MOR         True
    EG          True
         cars_per_cap drives_right
    US            809         True
    AUS           731        False
    JAP           588        False
    IN             18        False
    RU            200         True
    MOR            70         True
    EG             45         True
"""
