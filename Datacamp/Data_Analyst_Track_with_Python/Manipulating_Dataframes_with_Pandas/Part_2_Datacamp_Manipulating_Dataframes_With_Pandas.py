"""
Datacamp - Manipulating DataFrames with pandas
https://www.datacamp.com/courses/manipulating-dataframes-with-pandas
Part 2 : Advanced indexing
Python 3.X
"""



"""
Having learned the fundamentals of working with DataFrames, you will now move on to more advanced indexing techniques.
You will learn about MultiIndexes, or hierarchical indexes, and learn how to interact with and extract data from them.
"""



""" question answer : 3
Index values and names
50xp
Which one of the following index operations does not raise an error?

The sales DataFrame which you have seen in the videos of the previous chapter has been pre-loaded for you and is available for exploration in the IPython Shell.

       eggs  salt  spam
month
Jan      47  12.0    17
Feb     110  50.0    31
Mar     221  89.0    72
Apr      77  87.0    20
May     132   NaN    52
Jun     205  60.0    55
Possible Answers
sales.index[0] = 'JAN' 1
sales.index[0] = sales.index[0].upper() 2
sales.index = range(len(sales)) 3
"""

""" results or consol output
In [1]: sales.index[0] = 'JAN'

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    sales.index[0] = 'JAN'
  File "<stdin>", line 1404, in __setitem__
    raise TypeError("Index does not support mutable operations")
TypeError: Index does not support mutable operations


In [2]: sales.index[0] = sales.index[0].upper()

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    sales.index[0] = sales.index[0].upper()
  File "<stdin>", line 1404, in __setitem__
    raise TypeError("Index does not support mutable operations")
TypeError: Index does not support mutable operations


In [3]: sales.index = range(len(sales))

In [4]:
"""



"""
Changing index of a DataFrame
100xp
As you saw in the previous exercise, indexes are immutable objects. This means that if you want to change or modify the index in a dataframe, then you need to change the whole index. You will do this now, using a list comprehension to create the new index.

A list comprehension is a succinct way to generate a list in one line. For example, the following list comprehension generates a list that contains the cubes of all numbers from 0 to 9: cubes = [i**3 for i in range(10)]. This is equivalent to the following code:

cubes = []
for i in range(10):
    cubes.append(i**3)
Before getting started, print the sales DataFrame in the IPython Shell and verify that the index is given by month abbreviations containing lowercase characters.

Instructions
Create a list new_idx with the same elements as in sales.index, but with all characters capitalized.
Assign new_idx to sales.index.
Print the sales dataframe. This has been done for you, so hit 'Submit Answer' and to see how the index changed.
"""
# Create the list of new indexes: new_idx
new_idx = [string.upper() for string in sales.index]

# Assign new_idx to sales.index
sales.index = new_idx

# Print the sales DataFrame
print(sales)
""" results or consol output
<script.py> output:
         eggs  salt  spam
    JAN    47  12.0    17
    FEB   110  50.0    31
    MAR   221  89.0    72
    APR    77  87.0    20
    MAY   132   NaN    52
    JUN   205  60.0    55
"""



"""
Changing index name labels
100xp
Notice that in the previous exercise, the index was not labeled with a name. In this exercise, you will set its name to 'MONTHS'.

Similarly, if all the columns are related in some way, you can provide a label for the set of columns.

To get started, print the sales DataFrame in the IPython Shell and verify that the index has no name, only its data (the month names).

Instructions
Assign the string 'MONTHS' to sales.index.name to create a name for the index.
Print the sales dataframe to see the index name you just created.
Now assign the string 'PRODUCTS' to sales.columns.name to give a name to the set of columns.
Print the sales dataframe again to see the columns name you just created.
"""
# Assign the string 'MONTHS' to sales.index.name
sales.index.name = 'MONTHS'

# Print the sales DataFrame
print(sales)

# Assign the string 'PRODUCTS' to sales.columns.name
sales.columns.name = 'PRODUCTS'

# Print the sales dataframe again
print('---------------')
print(sales)

""" results or consol output
<script.py> output:
            eggs  salt  spam
    MONTHS
    JAN       47  12.0    17
    FEB      110  50.0    31
    MAR      221  89.0    72
    APR       77  87.0    20
    MAY      132   NaN    52
    JUN      205  60.0    55
    ---------------
    PRODUCTS  eggs  salt  spam
    MONTHS
    JAN         47  12.0    17
    FEB        110  50.0    31
    MAR        221  89.0    72
    APR         77  87.0    20
    MAY        132   NaN    52
    JUN        205  60.0    55
"""



"""
Building an index, then a DataFrame
100xp
You can also build the DataFrame and index independently, and then put them together. If you take this route, be careful, as any mistakes in generating the DataFrame or the index can cause the data and the index to be aligned incorrectly.

In this exercise, the sales DataFrame has been provided for you without the month index. Your job is to build this index separately and then assign it to the sales DataFrame. Before getting started, print the sales DataFrame in the IPython Shell and note that it's missing the month information.

Instructions
Generate a list months with the data ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']. This has been done for you.
Assign months to sales.index.
Print the modified sales dataframe and verify that you now have month information in the index.
"""
# Generate the list of months: months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Assign months to sales.index
sales.index = months

# Print the modified sales DataFrame
print(sales)
""" results or consol output
<script.py> output:
         eggs  salt  spam
    Jan    47  12.0    17
    Feb   110  50.0    31
    Mar   221  89.0    72
    Apr    77  87.0    20
    May   132   NaN    52
    Jun   205  60.0    55
"""




"""
Extracting data with a MultiIndex
100xp

In the video, Dhavide explained the concept of a hierarchical index, or a MultiIndex. You will now practice working with these types of indexes.

The sales DataFrame you have been working with has been extended to now include State information as well. In the IPython Shell, print the new sales DataFrame to inspect the data. Take note of the MultiIndex!

Extracting elements from the outermost level of a MultiIndex is just like in the case of a single-level Index. You can use the .loc[] accessor as Dhavide demonstrated in the video.
Instructions

    Print sales.loc[['CA', 'TX']]. Note how New York is excluded.
    Print sales['CA':'TX']. Note how New York is included.

"""
# Print sales.loc[['CA', 'TX']]
print(sales.loc[['CA', 'TX']])
print('------------------------')
# Print sales['CA':'TX']
print(sales['CA':'TX'])
""" results or consol output
<script.py> output:
                 eggs  salt  spam
    state month
    CA    1        47  12.0    17
          2       110  50.0    31
    TX    1       132   NaN    52
          2       205  60.0    55
    ------------------------
                 eggs  salt  spam
    state month
    CA    1        47  12.0    17
          2       110  50.0    31
    NY    1       221  89.0    72
          2        77  87.0    20
    TX    1       132   NaN    52
          2       205  60.0    55
"""



"""
Setting & sorting a MultiIndex
100xp

In the previous exercise, the MultiIndex was created and sorted for you. Now, you're going to do this yourself! With a MultiIndex, you should always ensure the index is sorted. You can skip this only if you know the data is already sorted on the index fields.

To get started, print the pre-loaded sales DataFrame in the IPython Shell to verify that there is no MultiIndex.
Instructions

    Create a MultiIndex by setting the index to be the columns ['state', 'month'].
    Sort the MultiIndex using the .sort_index() method.
    Print the sales DataFrame. This has been done for you, so hit 'Submit Answer' to verify that indeed you have an index with the fields state and month!

"""
# Set the index to be the columns ['state', 'month']: sales
sales = sales.set_index(['state', 'month'])
print(sales)
print('-------------------')

# Sort the MultiIndex: sales
sales = sales.sort_index()

# Print the sales DataFrame
print(sales)
""" results or consol output
<script.py> output:
                 eggs  salt  spam
    state month
    CA    1        47  12.0    17
          2       110  50.0    31
    NY    1       221  89.0    72
          2        77  87.0    20
    TX    1       132   NaN    52
          2       205  60.0    55
    -------------------
                 eggs  salt  spam
    state month
    CA    1        47  12.0    17
          2       110  50.0    31
    NY    1       221  89.0    72
          2        77  87.0    20
    TX    1       132   NaN    52
          2       205  60.0    55
"""



"""
Using .loc[] with nonunique indexes
100xp

As Dhavide mentioned in the video, it is always preferable to have a meaningful index that uniquely identifies each row. Even though pandas does not require unique index values in DataFrames, it works better if the index values are indeed unique. To see an example of this, you will index your sales data by 'state' in this exercise.

As always, begin by printing the sales DataFrame in the IPython Shell and inspecting it.
Instructions

    Set the index of sales to be the column 'state'.
    Print the sales DataFrame to verify that indeed you have an index with state values.
    Access the data from 'NY' and print it to verify that you obtain two rows.

"""
# Set the index to the column 'state': sales
sales = sales.set_index(['state'])

# Print the sales DataFrame
print(sales)
print('--------------')
# Access the data from 'NY'
print(sales.loc['NY'])
""" results or consol output
<script.py> output:
           month  eggs  salt  spam
    state
    CA         1    47  12.0    17
    CA         2   110  50.0    31
    NY         1   221  89.0    72
    NY         2    77  87.0    20
    TX         1   132   NaN    52
    TX         2   205  60.0    55
    --------------
           month  eggs  salt  spam
    state
    NY         1   221  89.0    72
    NY         2    77  87.0    20
"""



"""
Indexing multiple levels of a MultiIndex
100xp

Looking up indexed data is fast and efficient. And you have already seen that lookups based on the outermost level of a MultiIndex work just like lookups on DataFrames that have a single-level Index.

Looking up data based on inner levels of a MultiIndex can be a bit trickier. In this exercise, you will use your sales DataFrame to do some increasingly complex lookups.

The trickiest of all these lookups are when you want to access some inner levels of the index. In this case, you need to use slice(None) in the slicing parameter for the outermost dimension(s) instead of the usual :, or use pd.IndexSlice. You can refer to the pandas documentation for more details. For example, in the video, Dhavide used the following code to extract rows from all Symbols for the dates Oct. 3rd through 4th inclusive:

stocks.loc[(slice(None), slice('2016-10-03', '2016-10-04')), :]

Pay particular attention to the tuple (slice(None), slice('2016-10-03', '2016-10-04')).
Instructions

    Look up data for the New York column ('NY') in month 1.
    Look up data for the California and Texas columns ('CA', 'TX') in month 2.
    Look up data for all states in month 2. Use (slice(None), 2) to extract all rows in month 2.

"""
# Look up data for NY in month 1: NY_month1
NY_month1 = sales.loc[('NY',1)]

# Look up data for CA and TX in month 2: CA_TX_month2
CA_TX_month2 = sales.loc[(['CA','TX'],2),:]

# Look up data for all states in month 2: all_month2
all_month2 = sales.loc[(slice(None), 2),:]
print('-------------------')
print(NY_month1)
print('-------------------')
print(CA_TX_month2)
print('-------------------')
print(all_month2)
print('-------------------')
""" results or consol output
<script.py> output:
    -------------------
    eggs    221.0
    salt     89.0
    spam     72.0
    Name: (NY, 1), dtype: float64
    -------------------
                 eggs  salt  spam
    state month
    CA    2       110  50.0    31
    TX    2       205  60.0    55
    -------------------
                 eggs  salt  spam
    state month
    CA    2       110  50.0    31
    NY    2        77  87.0    20
    TX    2       205  60.0    55
    -------------------
"""
