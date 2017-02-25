""" 01/2017
Dataquest : Complete Data Analyst Path 
Step 1: Introduction To Python
SubStep : Python Programming: Beginner : List Operations
"""

"""
1: Introduction To The Data Set
In this mission, we'll look at daily weather data for Los Angeles (L.A.) during 2014. Here's a look at the beginning of la_weather.csv, the data set we'll be working:


Day,Type of Weather
1,Sunny
2,Sunny
3,Sunny
4,Sunny
5,Sunny
6,Rain
7,Sunny
8,Sunny
9,Fog
10,Rain
In an earlier mission, we split a CSV file into rows. We'll be doing the same thing here, so it's useful to think of each line in the data file as a separate row. Each row contains multiple values separated by a comma (,).

The first row in our data is the header row, which contains labels for the values beneath them. As the header row indicates, each row has two values:

Day - A number from 1 to 365 indicating the day of the year. January 1st is 1, and December 31st is 365.
Type of Weather - The type of weather experienced on that day. The values that may appear here include Rain, Sunny, Fog, Fog-Rain, or Thunderstorm.
Our ultimate goal is to count how many times each type of weather occurred over the course of the year. During this mission, we'll learn how to manipulate the data with lists, and make good progress towards that goal. In the next mission, we'll fit all the pieces together and tally up the data.
"""


"""
2: Parsing The File
Because our data is in a CSV file, we'll need to read the file in before we can work with it. In an earlier mission, we read a CSV file into a list, and we'll do the same here.

To read the file in, we'll need to:

Open it with the open() function. This will return a File object.
Read the open file into a variable using the read() method. This will return in a string.
Split the data into rows on the newline character (\n). This will result in a list.
Loop through each row, and split each row into a list on the comma character (,). This will result in a list of lists.
Here's the code we used to parse the crime_rates.csv file in an earlier mission:


f = open("crime_rates.csv", 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

Instructions
Open and read in la_weather.csv.
Split the data on the newline character to convert it to a list of rows.
Split each row on the comma and append each list to weather_data.

"""
weather_data = []
rows = open("la_weather.csv", 'r').read().split('\n')
for row in rows:
    weather_data.append(row.split(","))
""" result or Ipython output


"""






"""
3: Getting A Single Column From The Data
We've been thinking of our data in terms of rows, where rows are horizontal, from left to right:

The diagram above shows the first four rows in the data, along with their corresponding row numbers. Each item in a row records different information, but refers to the same day.

Another way to think of the data is in terms of values that are alike, or columns. Columns are vertical, from top to bottom:

In the above diagram, we grouped the data by column. Each value in a column records similar information. Column 1 shows the Day of the year, and column 2 shows the Type of Weather that occurred on that day.

The first value in each column is from the header row; it labels the data that appears in the column. While not all data sets include headers, they're helpful to have.

Since we'll be counting the total number of times each type of weather occurred during the year, we don't need the Day column.

You may recall that in a previous mission, we did the following to extract a column:

Looped over each row.
Retrieved the second element of the row.
Appended the second element to a list of items.
Here's an example of what this process looks like:


numbers = [[1,2],[3,4],[5,6],[7,8]]
second_column = []
for item in numbers:
    value = item[1]
    second_column.append(value)

Instructions
Loop over each row in weather_data.
Append the second item in each row to the weather list.
When complete, weather should contain each value from the Type of Weather column.

"""
# weather_data has already been read in automatically to make things easier.
weather = []
for row in weather_data:
    weather.append(row[1])
print(weather[0:5])
""" result or Ipython output
Output
['Type of Weather', 'Sunny', 'Sunny', 'Sunny', 'Sunny']

"""






"""
4: Counting The Items In A List
To verify that we selected the Type of Weather column properly, let's tally the number of items in weather.

Instructions
Count the number of items in weather. You can accomplish this by:
Looping over each element in weather.
Adding 1 to count for each element.
When finished, count should equal the number of items in weather.


"""
count = 0
for item in weather:
    count += 1
print(count)
""" result or Ipython output
Output
366

"""







"""
5: Removing The Header
When we created the weather list, we included the header. The first few items in weather look like this:

We want to tally how many times each type of weather occurred in L.A. To do this, we'll need to remove the string Type of Weather from the beginning of our list. If we don't do this, our count will include the header, which isn't part of the data set. The header is just a string that tells us what kind of values are in a column.

To remove the header we can use a list slicing. weather contains 366 elements, and the last list index value is 365. We'll want to create a slice that goes from the second element (index 1) to the end of the list.

Instructions
Slice the weather list to remove the header.
The slice should only remove the first element in the list.
Assign the slice to new_weather.

"""
new_weather = weather[1:len(weather)]
print(weather[0:5])
print(new_weather[0:5])
""" result or Ipython output
Output
['Type of Weather', 'Sunny', 'Sunny', 'Sunny', 'Sunny']
['Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny']

"""






"""
6: The In Statement
In Python, it's often very useful to check whether a certain element is present in a list. One way to perform this check is to use a for loop:


animals = ["cat", "dog", "rabbit"]
for animal in animals:
    if animal == "cat":
        print("Cat found")
This is a lot of code for a common operation, though. Luckily, Python has the in statement, which allows us to check whether a list contains a specific element much more quickly:


animals = ["cat", "dog", "rabbit"]
if "cat" in animals:
    print("Cat found")
The in statement checks whether certain value occurs within a list, and returns True if it does. If not, the statement returns False.

We can directly assign the result to a variable as well:


animals = ["cat", "dog", "rabbit"]
cat_found = "cat" in animals


Instructions
Use the in statement to check whether the value cat is in the list animals, and assign the result to cat_found.
Use the in statement to check whether the value space_monster is in the list animals, and assign the result to space_monster_found.

"""
animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = "cat" in animals
space_monster_found = "space_monster" in animals
print(cat_found,space_monster_found)
""" result or Ipython output
Output
True False

"""






"""
7: Weather Types
We can use the in statement to discover which types of weather the new_weather list contains. At the start of this mission, we specified that the data set includes Rain, Sunny, Fog, Fog-Rain, and Thunderstorm. Let's verify that each of these types occurs in new_weather, and that we properly removed the header in a previous step.

Instructions
Loop through each item in the weather_types list.
Check whether the item occurs in the new_weather list.
Append the result of the check to weather_type_found.
At the end, weather_type_found should be a list of Boolean values.

"""
weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []
for type in weather_types:
    print(type) #just check row iteration
    if type in new_weather:
        weather_type_found.append(True)
    else:
        weather_type_found.append(False)
print(weather_type_found)
""" result or Ipython output
Output
Rain
Sunny
Fog
Fog-Rain
Thunderstorm
Type of Weather
[True, True, True, True, True, False]

"""






"""
8: Counting The Weather
In this mission, we covered list slicing, columns, and the in statement. We also formatted the weather data correctly so it will be ready for further analysis. 
In the next mission, we'll count up how many times each type of weather occurred in our data.

"""