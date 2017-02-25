"""
01/2017
Dataquest : Data Analyst Path
Step 2: Intermediate Python And Pandas
SubStep : Data Analysis With Pandas Intermediate : Getting Started With NumPy
"""



"""

"""



"""
1: The Dataset
In this mission, we'll be working with world_alcohol.csv, which contains data on how much alcohol is consumed per capita in each country.

Here are the first few rows of the data:
Each row specifies how many liters of a type of alcohol each citizen of a country drank in a given year. The first row shows how many liters of wine an average person in Vietnam drank in 1986.

Here's what each column represents:

Year -- the year the data in the row is for.
WHO Region -- the region in which the country is located.
Country -- the country the data is for.
Beverage Types -- the type of beverage the data is for.
Display Value -- the number of liters, on average, of the beverage type a citizen of the country drank in the given year.
"""

""" Console output or Results

"""




"""
2: Lists Of Lists
In previous missions, we worked with datasets like world_alcohol.csv by using lists of lists. This is a list that contains other lists inside. Here's how the first few rows of the data would look as a list of lists:


world_alcohol = [
                     [1986, "Western Pacific", "Viet Nam", "Wine", 0],
                     [1986, "Americas", "Uruguay", "Other", 0.5],
                     [1986, "Africa", "Cte d'Ivoire", "Wine", 1.62]
                    ]
We could retrieve the first row of the data and work with it as a list:


first_row = world_alcohol[0]
Here's what first_row would looks like, with the corresponding index above each item:

0	1	2	3	4
1986	"Western Pacific"	"Viet Nam"	"Wine"	0
first_row[0] would retrieve the value 1986, and first_row[3] would retrieve the value Wine.

To get a value from a list of lists, we first specify an index to retrieve the correct row, then an index to retrieve the correct item in that row. We could get the second item in the second row with world_alcohol[1][1].

While extracting single values and rows is easy with lists of lists, it's cumbersome to compute statistics and extract columns. If we wanted to compute the average of the Display Value column, here's what we'd have to do:


# Extract the values in the 5th column.
liters_drank = []
for row in world_alcohol:
    liters = row[4]
    liters_drank.append(liters)
liters_drank = liters_drank[1:len(liters_drank)]
​
# Calculate the average of the values in the 5th column.
total = 0
for item in liters_drank:
    total = total + float(item)
average = total / len(liters_drank)
print(average)
Step by step, we:

Use a for loop to iterate over world_alcohol. Within the for loop, we:
Extract each row's value for the fifth column and assign to liters.
We then append liters to liters_drank, which is a list that we use to store all of the values in the 5th column.
Outside the for loop, we remove the first item in liters_drank since it's just the column name (Display Value).
We then use a new for loop to iterate over liters_drank. Within the for loop, we:
Convert each value to a float and add it to the list total.
Outside the for loop, we calculate the average by dividing total by the number of elements in liters_drank.
Lastly, we print the average of liters_drank.
Instructions
Use the csv module to read world_alcohol.csv into the variable world_alcohol.
You can use the csv.reader function to accomplish this.
world_alcohol should be a list of lists.
Extract the first column of world_alcohol, and assign it to the variable years.
Use list slicing to remove the first item in years (this is a header).
Find the sum of all the items in years. Assign the result to total.
Remember to convert each item to a float before adding them together.
Divide total by the length of years to get the average. Assign the result to avg_year.
"""
import csv
csvfile = "world_alcohol.csv"
opencsvfile = open(csvfile)
readcsv_file = csv.reader(opencsvfile)
world_alcohol = list(readcsv_file)
print(world_alcohol[0:5])
years = []
for liste in world_alcohol:
    years.append(liste[0])
print(years[0:5])
nb_years = len(years)
years = years[1:nb_years]
print(years[0:5])
total = 0
for item in years:
    print(item[0])
    total = total + item[0]

print(total)
avg_year = total / nb_years
print(avg_year)
""" Console output or Results

"""




"""
3: Introducing NumPy
Using NumPy, we can much more efficiently analyze data than we can using lists. NumPy is a Python module that is used to create and manipulate multidimensional arrays.

An array is a collection of values. Arrays have one or more dimensions. An array dimension is the number of indices it takes to extract a value. In a list, we specify a single index, so it is one-dimensional:


first_row =  [1986, "Western Pacific", "Viet Nam", "Wine", 0]
print(first_row[0])
The code above will print out 1986. A list is similar to a NumPy one-dimensional array, or vector, because we only need a single index to get a value.

world_alcohol.csv, on the other hand, looks like this:

To extract a single value, we need to specify a row index then a column index. 1, 2 results in Uruguay. 2, 3 results in Wine.

This is a two-dimensional array, also known as a matrix. Data sets are usually distributed in the form of matrices, and NumPy makes it extremely easy to read in and work with matrices.
"""





"""
4: Using NumPy
To get started with NumPy, we first need to import it using import numpy. We can then read in datasets using the numpy.genfromtxt() function.

Since world_alcohol.csv is a csv file, rows are separated by line breaks, and columns are separated by commas, like this:


Year,WHO region,Country,Beverage Types,Display Value
1986,Western Pacific,Viet Nam,Wine,0
1986,Americas,Uruguay,Other,0.5
1985,Africa,Cte d'Ivoire,Wine,1.62
In files like this, the comma is called the delimiter, because it indicates where each field ends and a new one begins. Other delimiters, such as tabs, are occasionally used, but commas are the most common.

To use , we need to pass a keyword argument called delimiter that indicates what character is the delimiter:


import numpy
nfl = numpy.genfromtxt("nfl.csv", delimiter=",")
The above code would read in the nfl.csv file into a NumPy array. NumPy arrays are represented using the numpy.ndarray class. We'll refer to ndarray objects as NumPy arrays in our material.

Instructions
Import NumPy.
Use the genfromtxt() function to read world_alcohol.csv into the world_alcohol variable.
Use the type() and print() functions to display the type for world_alcohol.
"""
import numpy
world_alcohol = numpy.genfromtxt("world_alcohol.csv",delimiter=",")
print(type(world_alcohol))
""" Console output or Results
Output
<class 'numpy.ndarray'>
"""




"""
5: Creating Arrays
We can directly construct arrays from lists using the numpy.array() function.

The numpy.array() function can take a list or list of lists as input. When we input a list, we get a one-dimensional array as a result:


vector = numpy.array([5, 10, 15, 20])
When we input a list of lists, we get a matrix as a result:


matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
Instructions
Create a vector from the list [10, 20, 30].
Assign the result to the variable vector.
Create a matrix from the list of lists [[5, 10, 15], [20, 25, 30], [35, 40, 45]].
Assign the result to the variable matrix.
"""
vector = numpy.array([10, 20, 30])
matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(vector)
print(matrix)
""" Console output or Results
Output
[10 20 30]
[[ 5 10 15]
 [20 25 30]
 [35 40 45]]
"""





"""
6: Array Shape
Vectors have a certain number of elements. The vector below has 5 elements:
Matrices have a certain number of rows, and a certain number of columns. The matrix below has 5 columns and 3 rows:It's often useful to know how many elements an array contains. We can use the ndarray.shape property to figure out how many elements are in the array.

For vectors, the shape property contains a tuple with 1 element. A tuple is a kind of list where the elements can't be changed.


vector = numpy.array([1, 2, 3, 4])
print(vector.shape)
The code above would result in the tuple (4,). This tuple indicates that the array vector has one dimension, with length 4, which matches our intuition that vector has 4 elements.

For matrices, the shape property contains a tuple with 2 elements.


matrix = numpy.array([[5, 10, 15], [20, 25, 30]])
print(matrix.shape)
The above code will result in the tuple (2,3) indicating that matrix has 2 rows and 3 columns.

Instructions
Assign the shape of vector to vector_shape.
Assign the shape of matrix to matrix_shape.
"""
vector = numpy.array([10, 20, 30])
matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
vector_shape = vector.shape
matrix_shape = matrix.shape
print(vector_shape)
print(matrix_shape)
""" Console output or Results
Output
(3,)
(3, 3)
"""





"""
7: Data Types
Each value in a NumPy array has to have the same data type. NumPy data types are similar to Python data types, but have slight differences. You can find a full list of NumPy data types here, but here are some of the common ones:

bool -- Boolean. Can be True or False.
int -- Integer values. An example is 10. Can be int16, int32, or int64. The suffix 16, 32, or 64 indicates how long the number can be, in bytes (we'll dive more into bytes later on). The larger the suffix, the larger the integers can be.
float -- Floating point values. An example is 10.6. Can be float16, float32, or float64. The suffix 16, 32, or 64 indicates how many numbers after the decimal point the number can have. The larger the suffix, the more precise the float can be.
string -- String values. Can be string or unicode. We'll get more into what unicode is later on, but the difference between string and unicode is how the characters are stored by the computer.
NumPy will automatically figure out an appropriate data type when reading in data or converting lists to arrays. You can check the data type of a NumPy array using the dtype property.


numbers = numpy.array([1, 2, 3, 4])
numbers.dtype
Because numbers only contains integers, its data type is int64.

Instructions
Assign the data type of world_alcohol to the variable world_alcohol_dtype.
"""
world_alcohol_dtype = world_alcohol.dtype
print(world_alcohol_dtype)
""" Console output or Results
Output
float64
"""





"""
8: Inspecting The Data
Here's how the first few rows of world_alcohol look:


array([[             nan,              nan,              nan,              nan,              nan],
       [  1.98600000e+03,              nan,              nan,              nan,   0.00000000e+00],
       [  1.98600000e+03,              nan,              nan,              nan,   5.00000000e-01]])
There are a few concepts we haven't been introduced to yet that we'll get into one by one:

Many items in world_alcohol are nan.
The entire first row is nan.
Some of the numbers are written like 1.98600000e+03.
The data type of world_alcohol is float. Because all of the values in a NumPy array have to have the same data type, NumPy attempted to convert all of the columns to floats when they were read in. The numpy.genfromtxt() function will attempt to guess the correct data type of the array it creates.

In this case, the WHO Region, Country, and Beverage Types columns are actually strings, and couldn't be converted to floats. When NumPy can't convert a value to a numeric data type like float or integer, it uses a special nan value that stands for Not a Number. NumPy assigns an na value, which stands for Not Available, when the value doesn't exist. nan and na values are types of missing data. We'll dive more into how to deal with missing data in later missions.

The whole first row of world_alcohol.csv is a header row that contains the names of each column. This is not actually part of the data, and consists entirely of strings. Since the strings couldn't be converted to floats properly, NumPy uses nan values to represent them.

If you haven't seen scientific notation before, you might not recognize numbers like 1.98600000e+03. Scientific notation is a way to condense how very large or very precise numbers are displayed. We can represent 100 in scientific notation as 1e+02. The e+02 indicates that we should multiply what comes before it by 10 ^ 2(10 to the power 2, or 10 squared). This results in 1 * 100, or 100. Thus, 1.98600000e+03 is actually 1.986 * 10 ^ 3, or 1986. 1000000000000000 can be written as 1e+15.

In this case, 1.98600000e+03 is actually longer than 1986, but NumPy displays numeric values in scientific notation by default to account for larger or more precise numbers.
"""








"""
9: Reading In The Data Properly
Our data wasn't read in properly, which resulted in NumPy trying to convert strings to floats, and nan values. We can fix this by specifying in the numpy.genfromtxt() function that we want to read in all the data as strings. While we're at it, we can also specify that we want to skip the header row of world_alcohol.csv.

We can do this by:

Specifying the keyword argument dtype when reading in world_alcohol.csv, and setting it to "U75". This specifies that we want to read in each value as a 75 byte unicode data type. We'll dive more into unicode and bytes later on, but for now, it's enough to know that this will read in our data properly.
Specifying the keyword argument skip_header, and setting it to 1. This will skip the first row of world_alcohol.csv when reading in the data.
Instructions
Use the numpy.genfromtxt() function to read in world_alcohol.csv:
Set the dtype parameter to "U75".
Set the skip_header parameter to 1.
Set the delimiter parameter to ,.
Assign the result to world_alcohol.
Use the print() function to display world_alcohol.
"""
world_alcohol = numpy.genfromtxt("world_alcohol.csv",delimiter=",",skip_header=1,dtype="U75")
print(world_alcohol)
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
10: Indexing Arrays
We can index NumPy arrays very similarly to how we index regular Python lists. Here's how we would index a NumPy vector:


vector = numpy.array([5, 10, 15, 20])
print(vector[0])
The above code would print the first element of vector, or 5.

Indexing matrices is similar to indexing lists of lists. Here's a refresher on indexing lists of lists:


list_of_lists = [
        [5, 10, 15],
        [20, 25, 30]
       ]
The first item in list_of_lists is [5, 10, 15]. If we wanted to access the element 15, we could do this:


first_item = list_of_lists[0]
first_item[2]
We could also condense the notation like this:


list_of_lists[0][2]
We can index matrices in a similar way, but we place both indices inside square brackets. The first index specifies which row the data comes from, and the second index specifies which column the data comes from:


matrix = numpy.array([
                        [5, 10, 15],
                        [20, 25, 30]
                     ])
print(matrix[1,2])
In the above code, we pass two indices into the square brackets when we index matrix. This will result in the value in the second row and the third column, or 30.

Instructions
Assign the amount of alcohol Uruguayans drank in other beverages per capita in 1986 to uruguay_other_1986. This is the second row and fifth column.
Assign the country in the third row to third_country. Country is the third column.
"""
uruguay_other_1986 = world_alcohol[1][4]
third_country = world_alcohol[2][2]
print(uruguay_other_1986)
print(third_country)
""" Console output or Results
Output
0.5
Cte d'Ivoire
"""





"""
11: Slicing Arrays
We can slice vectors very similarly to how we slice lists:


vector = numpy.array([5, 10, 15, 20])
print(vector[0:3])
The above code will print out 5, 10, 15. Like lists, vector slicing is from the first index up to but not including the second index.

Matrix slicing is a bit more complex, and has four forms:

When we want to select one entire dimension, and a single element from the other.
When we want to select one entire dimension, and a slice of the other.
When you want to select a slice of one dimension, and a single element from the other.
When we want to slice both dimensions.
We'll dive into the first form in this screen. When we want to select one whole dimension, and an element from the other, we can do this:


matrix = numpy.array([
                    [5, 10, 15],
                    [20, 25, 30],
                    [35, 40, 45]
                 ])
print(matrix[:,1])
This will select all of the rows, but only the column with index 1. So we'll end up with 10, 25, 40, which is the whole second column.

The colon by itself : specifies that the entirety of a single dimension should be selected. Think of the colon as selecting from the first element in a dimension up to and including the last element.

Instructions
Assign the whole third column from world_alcohol to the variable countries.
Assign the whole fifth column from world_alcohol to the variable alcohol_consumption.
"""
countries = world_alcohol[:,2]
alcohol_consumption =  world_alcohol[:,4]
""" Console output or Results
Variables
 countriesndarray (<class 'numpy.ndarray'>)
array(['Viet Nam', 'Uruguay', "Cte d'Ivoire", ..., 'Switzerland',
       'Papua New Guinea', 'Swaziland'],
      dtype='<U75')
 alcohol_consumptionndarray (<class 'numpy.ndarray'>)
array(['0', '0.5', '1.62', ..., '2.54', '0', '5.15'],
      dtype='<U75')
 world_alcoholndarray (<class 'numpy.ndarray'>)
array([['1986', 'Western Pacific', 'Viet Nam', 'Wine', '0'],
       ['1986', 'Americas', 'Uruguay', 'Other', '0.5'],
       ['1985', 'Africa', "Cte d'Ivoire", 'Wine', '1.62'],
       ...,
       ['1986', 'Europe', 'Switzerland', 'Spirits', '2.54'],
       ['1987', 'Western Pacific', 'Papua New Guinea', 'Other', '0'],
       ['1986', 'Africa', 'Swaziland', 'Other', '5.15']],
      dtype='<U75')
"""





"""
12: Slicing One Dimension
When we want to select one whole dimension, and a slice of the other, we can do this:


matrix = numpy.array([
                    [5, 10, 15],
                    [20, 25, 30],
                    [35, 40, 45]
                 ])
print(matrix[:,0:2])
This will select all the rows, and columns with index 0, and index 1. We'll end up with:


[
    [5, 10],
    [20, 25],
    [35, 40]
]
We can select rows by specifying a colon in the columns area:


print(matrix[1:3,:])
The code above will select rows 1 and 2, and all of the columns. We'll end up with this:


[
    [20, 25, 30],
    [35, 40, 45]
]
We can also select a single value alongside an entire dimension:


print(matrix[1:3,1])
The code above will print rows 1 and 2 and column 1:


[
     [25, 40]
]
Instructions
Assign all the rows and the first 2 columns of world_alcohol to first_two_columns.
Assign the first 10 rows and the first column of world_alcohol to first_ten_years.
Assign the first 10 rows and all of the columns of world_alcohol to first_ten_rows.
"""
first_two_columns = world_alcohol[:,0:2]
first_ten_years = world_alcohol[0:10,0]
first_ten_rows = world_alcohol[0:10,]
print(first_two_columns)
print(first_ten_years)
print(first_ten_rows)
""" Console output or Results
Output
[['1986' 'Western Pacific']
 ['1986' 'Americas']
 ['1985' 'Africa']
 ...,
 ['1986' 'Europe']
 ['1987' 'Western Pacific']
 ['1986' 'Africa']]
['1986' '1986' '1985' '1986' '1987' '1987' '1987' '1985' '1986' '1984']
[['1986' 'Western Pacific' 'Viet Nam' 'Wine' '0']
 ['1986' 'Americas' 'Uruguay' 'Other' '0.5']
 ['1985' 'Africa' "Cte d'Ivoire" 'Wine' '1.62']
 ['1986' 'Americas' 'Colombia' 'Beer' '4.27']
 ['1987' 'Americas' 'Saint Kitts and Nevis' 'Beer' '1.98']
 ['1987' 'Americas' 'Guatemala' 'Other' '0']
 ['1987' 'Africa' 'Mauritius' 'Wine' '0.13']
 ['1985' 'Africa' 'Angola' 'Spirits' '0.39']
 ['1986' 'Americas' 'Antigua and Barbuda' 'Spirits' '1.55']
 ['1984' 'Africa' 'Nigeria' 'Other' '6.1']]
"""





"""
13: Slicing Arrays
When we want to slice both dimensions, we can do this:


matrix = numpy.array([
                    [5, 10, 15],
                    [20, 25, 30],
                    [35, 40, 45]
                 ])
print(matrix[1:3,0:2])
This will select rows with index 1 and 2, and columns with index 0 and 1:


[
    [20, 25],
    [35, 40]
]
Instructions
Assign the first 20 rows of the columns at index 1 and 2 of world_alcohol to first_twenty_regions.
"""
first_twenty_regions = world_alcohol[0:20,1:3]
print(first_twenty_regions)
""" Console output or Results
Output
[['Western Pacific' 'Viet Nam']
 ['Americas' 'Uruguay']
 ['Africa' "Cte d'Ivoire"]
 ['Americas' 'Colombia']
 ['Americas' 'Saint Kitts and Nevis']
 ['Americas' 'Guatemala']
 ['Africa' 'Mauritius']
 ['Africa' 'Angola']
 ['Americas' 'Antigua and Barbuda']
 ['Africa' 'Nigeria']
 ['Africa' 'Botswana']
 ['Americas' 'Guatemala']
 ['Western Pacific' "Lao People's Democratic Republic"]
 ['Eastern Mediterranean' 'Afghanistan']
 ['Western Pacific' 'Viet Nam']
 ['Africa' 'Guinea-Bissau']
 ['Americas' 'Costa Rica']
 ['Africa' 'Seychelles']
 ['Europe' 'Norway']
 ['Africa' 'Kenya']]
"""





"""
14: Next Steps
We've learned some of the basics of the NumPy library and how to work with NumPy arrays. In the next mission, we'll build on this foundation to determine which country consumes the most alcohol.
"""
