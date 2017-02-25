"""
01/2017
Dataquest : Data Analyst Path
Step 2: Intermediate Python And Pandas
SubStep : Data Analysis With Pandas Intermediate : Computation with NumPy
"""



"""

"""



"""
1: The Dataset
In the previous mission, we worked with world_alcohol.csv, which records per capita alcohol consumption for each country. We'll use the same dataset in this mission, and eventually determine which country consumes the most alcohol per capita.

Here's what the first few rows look like:

Each row specifies how many liters of a type of alcohol the average citizen of a particular country drank in a given year. The first row, for example, shows how many liters of wine the typical Vietnamese citizen drank in 1986.

Here's a description of each column in the dataset:

Year -- The year the data in the row is for
WHO Region -- The region in which the country is located
Country -- The country of the data is for
Beverage Types -- The type of beverage
Display Value -- The average number of liters drunk per capita
"""


"""
2: Array Comparisons
One of the most powerful aspects of the NumPy module is the ability to make comparisons across an entire array. These comparisons result in Boolean values.

Here's an example of how we can do this with a vector:


vector = numpy.array([5, 10, 15, 20])
vector == 10
If you'll recall from an earlier mission, the double equals sign (==) compares two values. When used with NumPy, it will compare the second value to each element in the vector. If the value are equal, the Python interpreter returns True; otherwise, it returns False. It stores the Boolean results in a new vector.

For example, the code above will generate the vector [False, True, False, False], since only the second element in vector equals 10.

Here's an example with a matrix:


matrix = numpy.array([
                    [5, 10, 15],
                    [20, 25, 30],
                    [35, 40, 45]
                 ])
    matrix == 25
The final statement will compare 25 to every element in matrix. The result will be a matrix where elements are True or False:


[
    [False, False, False],
    [False, True,  False],
    [False, False, False]
]
In the result, True only appears in a single position - where the corresponding element in matrix is 25.

Now it's time to practice what we've learned!

Instructions
The variable world_alcohol already contains the data set we're working with.
Extract the third column in world_alcohol, and compare it to the string Canada. Assign the result to countries_canada.
Extract the first column in world_alcohol, and compare it to the string 1984. Assign the result to years_1984.
"""
countries_canada = world_alcohol[:,2] == "Canada"
years_1984 = world_alcohol[:,0] == "1984"
print(countries_canada)
print(years_1984)
""" Console output or Results
Output
[False False False ..., False False False]
[False False False ..., False False False]
"""




"""
3: Selecting Elements
We mentioned that comparisons are very powerful, but it may not have been obvious why on the last screen. Comparisons give us the power to select elements in arrays using Boolean vectors. This allows us to conditionally select certain elements in vectors, or certain rows in matrices.

Here's an example of how we would do this with a vector:


vector = numpy.array([5, 10, 15, 20])
equal_to_ten = (vector == 10)
​
print(vector[equal_to_ten])
The code above:

Creates vector.
Compares vector to the value 10, which generates a Boolean vector [False, True, False, False]. It assigns the result to equal_to_ten.
Uses equal_to_ten to only select elements in vector where equal_to_ten is True. This results in the vector [10].
We can use the same principle to select rows in matrices:


matrix = numpy.array([
                [5, 10, 15],
                [20, 25, 30],
                [35, 40, 45]
             ])
    second_column_25 = (matrix[:,1] == 25)
    print(matrix[second_column_25, :])
The code above:

Creates matrix.
Uses second_column_25 to select any rows in matrix where second_column_25 is True.
We end up with this matrix:


[
    [20, 25, 30]
]
We selected a single row from matrix, which was returned in a new matrix.

Instructions
Compare the third column of world_alcohol to the string Algeria.
Assign the result to country_is_algeria.
Select only the rows in world_alcohol where country_is_algeria is True.
Assign the result to country_algeria.
"""
country_is_algeria = world_alcohol[:,2] == "Algeria"
country_algeria = world_alcohol[country_is_algeria,:]
print(country_algeria)
""" Console output or Results
Output
[['1984' 'Africa' 'Algeria' 'Spirits' '0.01']
 ['1987' 'Africa' 'Algeria' 'Beer' '0.17']
 ['1987' 'Africa' 'Algeria' 'Spirits' '0.01']
 ['1986' 'Africa' 'Algeria' 'Wine' '0.1']
 ['1984' 'Africa' 'Algeria' 'Other' '0']
 ['1989' 'Africa' 'Algeria' 'Beer' '0.16']
 ['1989' 'Africa' 'Algeria' 'Spirits' '0.01']
 ['1989' 'Africa' 'Algeria' 'Wine' '0.23']
 ['1986' 'Africa' 'Algeria' 'Spirits' '0.01']
 ['1984' 'Africa' 'Algeria' 'Wine' '0.12']
 ['1985' 'Africa' 'Algeria' 'Beer' '0.19']
 ['1985' 'Africa' 'Algeria' 'Other' '0']
 ['1986' 'Africa' 'Algeria' 'Beer' '0.18']
 ['1985' 'Africa' 'Algeria' 'Wine' '0.11']
 ['1986' 'Africa' 'Algeria' 'Other' '0']
 ['1989' 'Africa' 'Algeria' 'Other' '0']
 ['1987' 'Africa' 'Algeria' 'Other' '0']
 ['1984' 'Africa' 'Algeria' 'Beer' '0.2']
 ['1985' 'Africa' 'Algeria' 'Spirits' '0.01']
 ['1987' 'Africa' 'Algeria' 'Wine' '0.1']]
"""





"""
4: Comparisons With Multiple Conditions
On the last screen, we made comparisons based on a single condition. We can also perform comparisons with multiple conditions by specifying each one separately, then joining them with an ampersand (&). When constructing a comparison with multiple conditions, it's critical to put each one in parentheses.

Here's an example of how we would do this with a vector:


vector = numpy.array([5, 10, 15, 20])
equal_to_ten_and_five = (vector == 10) & (vector == 5)
In the above statement, we have two conditions, (vector == 10) and (vector == 5). We use the ampersand (&) to indicate that both conditions must be True for the final result to be True. The statement returns [False, False, False, False], because none of the elements can be 10 and 5 at the same time. Here's a diagram of the comparison logic:

We can also use the pipe symbol (|) to specify that either one condition or the other should be True:

vector = numpy.array([5, 10, 15, 20])
equal_to_ten_or_five = (vector == 10) | (vector == 5)
The code above will result in [True, True, False, False].

Instructions
Perform a comparison with multiple conditions, and join the conditions with &.
Compare the first column of world_alcohol to the string 1986.
Compare the third column of world_alcohol to the string Algeria.
Enclose each condition in parentheses, and join the conditions with &.
Assign the result to is_algeria_and_1986.
Use is_algeria_and_1986 to select rows from world_alcohol.
Assign the rows that is_algeria_and_1986 selects to rows_with_algeria_and_1986.
"""
is_algeria_and_1986 = (world_alcohol[:,0] == "1986") & (world_alcohol[:,2] == "Algeria")
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]
print(rows_with_algeria_and_1986)
""" Console output or Results
Output
[['1986' 'Africa' 'Algeria' 'Wine' '0.1']
 ['1986' 'Africa' 'Algeria' 'Spirits' '0.01']
 ['1986' 'Africa' 'Algeria' 'Beer' '0.18']
 ['1986' 'Africa' 'Algeria' 'Other' '0']]
"""






"""
5: Replacing Values
We can also use comparisons to replace values in an array, based on certain conditions. Here's an example of how we would do this for a vector:


vector = numpy.array([5, 10, 15, 20])
equal_to_ten_or_five = (vector == 10) | (vector == 5)
vector[equal_to_ten_or_five] = 50
print(vector)
This code will complete the following steps:

Create an array vector.
Compare vector to 10 and 5, and generate a vector that's True where vector is equal to either value.
Select only the elements in vector where equal_to_ten_or_five is True.
Replace the selected values with the value 50.
The result will be [50, 50, 15, 20].

Here's a diagram showing what takes place at each step in the process:

We can perform the same replacement on a matrix. To do this, we'll need to use indexing to select a column or row first:


matrix = numpy.array([
            [5, 10, 15],
            [20, 25, 30],
            [35, 40, 45]
         ])
    second_column_25 = matrix[:,1] == 25
    matrix[second_column_25, 1] = 10
The code above will result in:


[
    [5, 10, 15],
    [20, 10, 30],
    [35, 40, 45]
 ]
Instructions
Replace all instances of the string 1986 in the first column of world_alcohol with the string 2014.
Replace all instances of the string Wine in the fourth column of world_alcohol with the string Grog.
"""
print(world_alcohol[0:5])
print("----------------")
world_alcohol[world_alcohol[:,0] == "1986",0] = "2014"
print(world_alcohol[0:5])
print("----------------")
world_alcohol[world_alcohol[:,3] == "Wine",3] = "Grog"
print(world_alcohol[0:5])
print("----------------")
""" Console output or Results
Output
[['1986' 'Western Pacific' 'Viet Nam' 'Wine' '0']
 ['1986' 'Americas' 'Uruguay' 'Other' '0.5']
 ['1985' 'Africa' "Cte d'Ivoire" 'Wine' '1.62']
 ['1986' 'Americas' 'Colombia' 'Beer' '4.27']
 ['1987' 'Americas' 'Saint Kitts and Nevis' 'Beer' '1.98']]
----------------
[['2014' 'Western Pacific' 'Viet Nam' 'Wine' '0']
 ['2014' 'Americas' 'Uruguay' 'Other' '0.5']
 ['1985' 'Africa' "Cte d'Ivoire" 'Wine' '1.62']
 ['2014' 'Americas' 'Colombia' 'Beer' '4.27']
 ['1987' 'Americas' 'Saint Kitts and Nevis' 'Beer' '1.98']]
----------------
[['2014' 'Western Pacific' 'Viet Nam' 'Grog' '0']
 ['2014' 'Americas' 'Uruguay' 'Other' '0.5']
 ['1985' 'Africa' "Cte d'Ivoire" 'Grog' '1.62']
 ['2014' 'Americas' 'Colombia' 'Beer' '4.27']
 ['1987' 'Americas' 'Saint Kitts and Nevis' 'Beer' '1.98']]
----------------
"""





"""
6: Replacing Empty Strings
We'll soon be working with the Display Value column, which shows how much alcohol the average citizen of a country drinks. However, because world_alcohol currently has a unicode datatype, all of the values in the column are strings. To add these values together or perform any other mathematical operations on them, we'll have to convert the data in the column to floats.

Before we can do this, we need to address the empty string values ('') that appear where there was no original data for the given country and year. If we try to convert the data in the column to floats without removing these values first, we'll get a ValueError. Thankfully, we can remove these items using the replacement technique we learned on the last screen.

Instructions
Compare all the items in the fifth column of world_alcohol with an empty string ''. Assign the result to is_value_empty.
Select all the values in the fifth column of world_alcohol where is_value_empty is True, and replace them with the string 0.
"""
is_value_empty = world_alcohol[:,4] == ''
world_alcohol[is_value_empty,4] = "0"
""" Console output or Results
Output
[['1986' 'Western Pacific' 'Viet Nam' 'Wine' '0']
 ['1986' 'Americas' 'Uruguay' 'Other' '0.5']
 ['1985' 'Africa' "Cte d'Ivoire" 'Wine' '1.62']
 ...,
 ['1986' 'Europe' 'Switzerland' 'Spirits' '2.54']
 ['1987' 'Western Pacific' 'Papua New Guinea' 'Other' '0']
 ['1986' 'Africa' 'Swaziland' 'Other' '5.15']]
"""




"""
7: Converting Data Types
We can convert the data type of an array with the astype() method. Here's an example of how this works:


vector = numpy.array(["1", "2", "3"])
vector = vector.astype(float)
The code above will convert all of the values in vector to floats: [1.0, 2.0, 3.0].

We'll do something similar with the fifth column of world_alcohol, which contains information on how much alcohol the average citizen of a country drank in a given year. To determine which country drinks the most, we'll have to convert the values in this column to float values. That's because we can't add or perform calculations on these values while they're strings.

Instructions
Extract the fifth column from world_alcohol, and assign it to the variable alcohol_consumption.
Use the astype() method to convert alcohol_consumption to the float data type.
"""
alcohol_consumption = world_alcohol[:,4]
print(alcohol_consumption)
print("------------------")
alcohol_consumption = alcohol_consumption.astype(float)
print(alcohol_consumption)
""" Console output or Results
Output
['0' '0.5' '1.62' ..., '2.54' '0' '5.15']
------------------
[ 0.    0.5   1.62 ...,  2.54  0.    5.15]
"""





"""
8: Computing With NumPy
Now that alcohol_consumption consists of numeric values, we can perform computations on it. NumPy has a few built-in methods that operate on arrays. You can view all of them in the documentation. For now, here are a few important ones:

sum() -- Computes the sum of all the elements in a vector, or the sum along a dimension in a matrix
mean() -- Computes the average of all the elements in a vector, or the average along a dimension in a matrix
max() -- Identifies the maximum value among all the elements in a vector, or the maximum along a dimension in a matrix
Here's an example of how we'd use one of these methods on a vector:


vector = numpy.array([5, 10, 15, 20])
vector.sum()
This would add together all of the elements in vector, and result in 50.

With a matrix, we have to specify an additional keyword argument, axis. The axis dictates which dimension we perform the operation on. 1 means that we want to perform the operation on each row, and 0 means on each column. The example below performs an operation across each row:


matrix = numpy.array([
                [5, 10, 15],
                [20, 25, 30],
                [35, 40, 45]
             ])
    matrix.sum(axis=1)
This would compute the sum for each row, resulting in [30, 75, 120].

Instructions
Use the sum() method to calculate the sum of the values in alcohol_consumption. Assign the result to total_alcohol.
Use the mean() method to calculate the average of the values in alcohol_consumption. Assign the result to average_alcohol.
"""
total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()
""" Console output or Results
Variables
 average_alcoholfloat64 (<class 'numpy.float64'>)
1.2001719373656738
 total_alcoholfloat64 (<class 'numpy.float64'>)
3908.96
 alcohol_consumptionndarray (<class 'numpy.ndarray'>)
array([ 0.  ,  0.5 ,  1.62, ...,  2.54,  0.  ,  5.15])
"""






"""
9: Total Annual Alcohol Consumption
Each country is associated with several rows for different types of beverages:


[['1986', 'Americas', 'Canada', 'Other', ''],
   ['1986', 'Americas', 'Canada', 'Spirits', '3.11'],
   ['1986', 'Americas', 'Canada', 'Beer', '4.87'],
   ['1986', 'Americas', 'Canada', 'Wine', '1.33']]
To find the total amount the average person in Canada drank in 1986, for example, we'd have to add up all 4 of the rows shown above, then repeat this process for each country.

Instructions
Create a matrix called canada_1986 that only contains the rows in world_alcohol where the first column is the string 1986 and the third column is the string Canada.
Extract the fifth column of canada_1986, replace any empty strings ('') with the string 0, and convert the column to the float data type. Assign the result to canada_alcohol.
Compute the sum of canada_alcohol. Assign the result to total_canadian_drinking.
"""
is_canada_and_1986 = (world_alcohol[:,0] == "1986") & (world_alcohol[:,2] == "Canada")
canada_1986 = world_alcohol[is_canada_and_1986,:]
is_value_empty = world_alcohol[:,4] == ''
canada_1986[is_value_empty,4] = "0"
canada_alcohol = canada_1986[:,4].astype(float)
total_canadian_drinking = canada_alcohol.sum()
""" Console output or Results
Variables
 total_canadian_drinkingfloat64 (<class 'numpy.float64'>)
9.3100000000000005
 canada_alcoholndarray (<class 'numpy.ndarray'>)
array([ 0.  ,  3.11,  4.87,  1.33])
 world_alcohol
 is_canada_and_1986
 is_value_empty
 canada_1986ndarray (<class 'numpy.ndarray'>)
array([['1986', 'Americas', 'Canada', 'Other', '0'],
       ['1986', 'Americas', 'Canada', 'Spirits', '3.11'],
       ['1986', 'Americas', 'Canada', 'Beer', '4.87'],
       ['1986', 'Americas', 'Canada', 'Wine', '1.33']],
      dtype='<U75')
 floattype (<class 'type'>)
float
"""





"""
10: Calculating Consumption For Each Country
Now that we know how to calculate the average consumption of all types of alcohol for a single country and year, we can scale up the process and make the same calculation for all countries in a given year. Here's a rough process:

Create an empty dictionary called totals.
Select only the rows in world_alcohol that match a given year. Assign the result to year.
Loop through a list of countries. For each country:
Select only the rows from year that match the given country.
Assign the result to country_consumption.
Extract the fifth column from country_consumption.
Replace any empty string values in the column with the string 0.
Convert the column to the float data type.
Find the sum of the column.
Add the sum to the totals dictionary, with the country name as the key.
After the code executes, you'll have a dictionary containing all of the country names as keys, with the associated alcohol consumption totals as the values.
Instructions
We've assigned the list of all countries to the variable countries.
Find the total consumption for each country in countries for the year 1989.
Refer to the steps outlined above for help.
When you're finished, totals should contain all of the country names as keys, with the corresponding alcohol consumption totals for 1989 as values.
"""
totals = {}

is_1989 = world_alcohol[:,0] == "1989"
world_alcohol_1989 = world_alcohol[is_1989,:]

for countrie in countries:
    #print(countrie)
    is_countrie = world_alcohol_1989[:,2] == countrie
    world_alcohol_1989_countrie = world_alcohol_1989[is_countrie,:]
    is_value_empty = world_alcohol_1989_countrie[:,4] == ''
    world_alcohol_1989_countrie[is_value_empty,4] = "0"
    consumption = world_alcohol_1989_countrie[:,4].astype(float)
    totals[countrie] = consumption.sum()

print(totals)
""" Console output or Results
{'Portugal': 15.350000000000001, 'South Africa': 9.2100000000000009, 'Belarus': 7.9799999999999995, 'Saint Lucia': 11.619999999999999, 'Morocco': 0.69999999999999996, 'Austria': 13.9, 'Yemen': 0.20000000000000001, 'Chile': 8.6499999999999986, 'Zambia': 3.3700000000000001, 'Greece': 10.15, 'Canada': 9.0, "Democratic People's Republic of Korea": 3.6799999999999997, 'Congo': 3.1500000000000004, 'Lesotho': 2.02, 'Mauritania': 0.02, 'Nicaragua': 2.5, 'Liberia': 5.6100000000000003, 'Togo': 2.2199999999999998, 'Democratic Republic of the Congo': 1.9199999999999999, 'Papua New Guinea': 1.1099999999999999, 'Guatemala': 2.4700000000000002, 'Malta': 7.1299999999999999, 'Switzerland': 13.849999999999998, 'Spain': 13.280000000000001, 'Eritrea': 0.28999999999999998, 'Guinea': 0.20999999999999999, "Lao People's Democratic Republic": 5.9500000000000002, 'Argentina': 10.82, 'Zimbabwe': 4.9199999999999999, 'Sweden': 7.4699999999999998, 'Latvia': 7.0399999999999991, 'Mauritius': 3.54, 'Chad': 0.30000000000000004, 'Malaysia': 0.68000000000000005, 'Djibouti': 0.87, 'France': 16.050000000000001, 'Cabo Verde':
"""




"""
11: Finding The Country That Drinks The Most
Now that we've computed total alcohol consumption for each country in 1989, we can loop through the totals dictionary to find the country with the highest value.

The process we've outlined below will help you find the key with the highest value in a dictionary:

Create a variable called highest_value that will keep track of the highest value. Set its value to 0.
Create a variable called highest_key that will keep track of the key associated with the highest value. Set its value to None.
Loop through each key in the dictionary.
If the value associated with the key is greater than highest_value, assign the value to highest_value, and assign the key to highest_key.
After the code runs, highest_key will be the key associated with the highest value in the dictionary.
Instructions
Find the country with the highest total alcohol consumption.
To do this, you'll need to find the key associated with the highest value in the totals dictionary.
Follow the process outlined above to find the highest value in totals.
When you're finished, highest_value will contain the highest average alcohol consumption, and highest_key will contain the country that had the highest per capital alcohol consumption in 1989.
"""
highest_value = 0
highest_key = None
for item, value  in totals.items():
    if value > highest_value:
        highest_value = value
        highest_key = item
print(highest_value)
print(highest_key)
""" Console output or Results
Output
16.29
Hungary
"""





"""
12: NumPy Strengths And Weaknesses
You should now have a good foundation in NumPy, and in handling issues with your data. NumPy is much easier to work with than lists of lists, because:

It's easy to perform computations on data.
Data indexing and slicing is faster and easier.
We can convert data types quickly.
Overall, NumPy makes working with data in Python much more efficient. It's widely used for this reason, especially for machine learning.

You may have noticed some limitations with NumPy as you worked through the past two missions, though. For example:

All of the items in an array must have the same data type. For many datasets, this can make arrays cumbersome to work with.
Columns and rows must be referred to by number, which gets confusing when you go back and forth from column name to column number.
In the next few missions, we'll learn about the Pandas library, one of the most popular data analysis libraries. Pandas builds on NumPy, but does a better job addressing the limitations of NumPy.
"""
