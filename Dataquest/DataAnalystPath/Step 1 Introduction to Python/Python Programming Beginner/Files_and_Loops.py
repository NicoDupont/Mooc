""" 01/2017
Dataquest : Complete Data Analyst Path 
Step 1: Introduction To Python
SubStep : Python Programming: Beginner : Files And Loops
"""

"""
1: Overview
In this mission, we'll learn how to work with files and use loops to iterate through lists. 
We'll be working with crime rate data for 73 cities in the United States. 
Datasets are often represented in files that you can download and manipulate. 
Before we get started, we'll first need to learn how to work with files in Python.
"""


"""
2: Opening Files
To open a file in Python, we use the open() function. This function accepts two different arguments (inputs) in the parentheses, always in the following order:

the name of the file (as a string)
the mode of working with the file (as a string)
We'll learn about the various modes in a later mission. For now, we'll just use "r", the mode for reading in files.

When entering multiple inputs, separate them with commas (,). For example, to open a file named story.txt in read mode, we write the following:


open("story.txt", "r")
The open() function returns a File object. This object stores the information we passed in, and allows us to call methods specific to the File class. We can assign the File object to a variable so we can refer to it later:


a = open("story.txt", "r")
Note that the File object, a, won't contain the actual contents of the file. It's instead an object that acts as an interface to the file and contains methods for reading in and modifying the file's contents (which we'll cover in the next screen).

Instructions
Use the open() function to create a File object.
The name of the file to open is "crime_rates.csv". Access the file in read mode ("r").
Assign this File object to the variable f.

"""
a = open("test.txt", "r")
print(a)
f = open("crime_rates.csv","r")
""" result or Ipython output
Output
<_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>

"""



"""
3: Reading In Files
File objects have a read() method that returns a string representation of the text in a file. Unlike the append() method from the previous mission, the read() method returns a value instead of modifying the object that calls the method. In the following code, we use the read() function to read the contents of "test.txt" into a File object, and assign that object to g:


f = open("test.txt", "r")
g = f.read()
Since g is a string, we can use the print() function to display the contents of the file:


f = open("test.txt", "r")
g = f.read()
print(g)

Instructions
Run the read() method on the File object f to return the string representation of crime_rates.csv.
Assign the resulting string to a new variable named data.

"""
f = open("crime_rates.csv", "r")
data = f.read()
""" result or Ipython output

"""




"""
4: Splitting
To make our string object data more useful, let's convert it into a list. Here's a preview of how the dataset looks:


Albuquerque,749\nAnaheim,371\nAnchorage,828\n
Each line is separated by the string \n, which is referred to as the new-line character. When we open a text file in a text editor, the editor will automatically split the text and create a new line wherever it sees the string \n:
In Python, we can use the split() method to turn a string object into a list of strings, like so:


["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
The split() method takes a string input corresponding to the delimiter, or separator. This delimiter determines how the string is split into elements in a list. For example, the delimiter for the crime rate data we just looked at is \n. Many other files use commas to separate elements:


sample = "john,plastic,joe"
split_list = sample.split(",")
# split_list is a list of _strings_: ["john", "plastic", "joe"]

Instructions
Split the string object data on the new-line character "\n", and store the result in a variable named rows. - Then, use the print() function to display the first five elements in rows.

"""
# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split("\n")
print(rows[5])
""" result or Ipython output
Output
['john', 'plastic', 'joe']
['How much wood', 'can a woodchuck chuck', 'if a woodchuck', 'could chuck wood?']
Aurora,425

"""




"""
5: Loops
We now have a list representation of the dataset (rows). Each element in the dataset is a string containing a comma (,) that separates the city name from the crime rate. Because they're strings, we can use the split() method on each of them to separate those values. Accomplishing this based on what we know so far would be a cumbersome task. We would need to write 73 lines of code, one for each element in the list.

Ideally, we could specify the code we want to execute for each element in the list a single time. Python and most other programming languages allow you to do this with a loop. For example, here's a loop that prints each element in a list:


cities = ["Austin", "Dallas", "Houston"]
for city in cities:
    print(city)
Here are the steps Python takes when it runs this code:

Assigns the value at index 0 in the cities list ("Austin") to city.
Executes the indented code. Because the current value of city is "Austin", it runs print("Austin").
Assigns the value at index 1 in the cities list ("Dallas") to city.
Executes the indented code. Because the current value of city is "Dallas", it runs print("Dallas").
Assigns the value at index 2 from the cities list ("Houston") to city.
Executes the indented code. Because the current value of city is "Houston", it runs print("Houston").
Sees that there are no more elements in the list cities, and stops running.
This code uses a type of loop called a for loop. We can break the for loop down into two main components: the for loop itself, and the loop body that contains the code we want to run during each iteration.

Here are the things you need to include in each of these components:

for Loop

Syntax - the words for and in need to be included in the statement
Iterator variable - the variable name you decide to use to refer to each element in the list (city)
Sequence - the variable you want to iterate over (cities)
Colon - loop statements must end with a colon (:)
Loop Body

Indentation - every line of code within the loop should be indented four spaces
Logic - the actual code we want to execute for each element. In the above code block, for example, we update the iterator variable (city) in each iteration of the loop.
Here's a diagram displaying the values for city and the print() statement during each iteration of the loop:

The iterator variable, city, is a temporary variable that's only accessible within the for loop.

The very basic loop body we wrote above only contains one line of code. To write a loop body with multiple lines of code, we need to indent that code consistently (using four spaces). For example, the following code will run the print() statement three times for each element in cities:


for city in cities:
    print(city)
    print(city)
    print(city)
Here's an annotated diagram of the code:


As you become more familiar with loops, you'll learn how to express repetitive and complex logic efficiently.

"""





"""
6: Practice - Loops
Let's practice writing a for loop on a subset of the crime rate data.

Instructions
The variable ten_rows contains the first 10 elements in rows.
Write a for loop that:
iterates over each element in ten_rows
uses the print() function to display each element

"""
ten_rows = rows[0:10]
for rows in ten_rows:
    print(rows)
""" result or Ipython output
Output
Albuquerque,749
Anaheim,371
Anchorage,828
Arlington,503
Atlanta,1379
Aurora,425
Austin,408
Bakersfield,542
Baltimore,1405
Boston,835

"""



"""
7: List Of Lists
Now that we know how to execute code for each element in a list, we can use a loop to split those elements on a delimiter and append the results to a new list. So far, we've appended values like integers and strings, but we've never appended a list to a list. This is known as a list of lists, since each element is itself a list.

The following code:

splits each element in three_rows (which contains the first three elements from rows) on the comma delimiter (,)
appends the resulting list (split_list) to a new list we create (final_list)
displays the final list using the print() function

three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []
​
for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)

In the leftmost part of the diagram, you'll notice that the elements in three_rows are strings. In the right-most part of the diagram, you'll notice that the elements in final_list are lists.

Here's what the output looks like:

[['Albuquerque', '749'], ['Anaheim', '371'], ['Anchorage', '828']]

Recall that since only the indented code is executed as part of the loop, the unindented print() statement on the last line will execute only after the loop finishes. In the following code cell, we execute the code we visualized in the diagram, along with some additional print() statements. These print() statements retrieve individual elements from final_list. Note that they all display as list objects. You'll practice writing your own for loop in the next step. For now, explore and run the code we covered in this step in the code cell below.

Instructions
This step is a demo. Play around with code or advance to the next step.

"""
three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []
for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)
print(final_list[0])
print(final_list[1])
print(final_list[2])
""" result or Ipython output
Output
[['Albuquerque', '749'], ['Anaheim', '371'], ['Anchorage', '828']]
['Albuquerque', '749']
['Anaheim', '371']
['Anchorage', '828']


"""




"""
8: Practice - Splitting Elements In A List
Let's now convert the full dataset, rows, into a list of lists using the logic from the previous step.

Instructions
Write a for loop that splits each element in rows on the comma delimiter, and appends the resulting list to a new list named final_data.
Then, use the print() function and list slicing to display the first five elements in final_data.

"""
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
final_data = []
for row in rows:
    final_data.append(row.split(','))
print(final_data[0:5])
""" result or Ipython output
Output
['Albuquerque,749', 'Anaheim,371', 'Anchorage,828', 'Arlington,503', 'Atlanta,1379']

[['Albuquerque', '749'], ['Anaheim', '371'], ['Anchorage', '828'], ['Arlington', '503'], ['Atlanta', '1379']]

"""




"""
9: Accessing Elements In A List Of Lists: The Manual Way
A list of lists has some unique interaction mechanisms. Using bracket notation to retrieve an element at a certain index returns a list object. However, using bracket notation on the resulting list will actually return a data point (such as a string or an integer).

In the following code, we retrieve the first list from final_data and assign it to first_list. We then retrieve the first element from first_list and assign it to first_list_first_value:


# Returns the first list: ['Albuquerque', '749'].
first_list = final_data[0]
​
# Returns the first list's first element: 'Albuquerque'.
first_list_first_value = first_list[0]
Since using bracket notation once returns a list, you can use bracket notation again on the resulting list without having to assign it to a variable first. Using double bracket notation is simpler. The following code uses double bracket notation to retrieve the value at index 0 for the first three elements in final_data:


# Returns the first list's first element, 'Albuquerque'.
first_list_first_value = final_data[0][0]
# Returns the second list's first element, 'Anaheim'.
second_list_first_value = final_data[1][0]
# Returns the third list's first element, 'Anchorage'.
third_list_first_value = final_data[2][0]

Instructions
five_elements contains the first five elements from final_data.
Create a list of strings named cities_list that contains the city names from each list in five_elements.


"""
print(five_elements)
cities_list = []
cities_list.append(five_elements[0][0])
cities_list.append(five_elements[1][0])
cities_list.append(five_elements[2][0])
cities_list.append(five_elements[3][0])
cities_list.append(five_elements[4][0])
""" result or Ipython output

Output
[['Albuquerque', '749'], ['Anaheim', '371'], ['Anchorage', '828'], ['Arlington', '503'], ['Atlanta', '1379']]
"""




"""
10: Looping Through A List Of Lists
Instead of appending each element from the nested list to a new list individually, we can use a for loop and specify the append logic within the loop body. Let's explore how we can replace the append() statements from the previous step with a for loop.

In the following code, we create a new list called crime_rates, and write a for loop that iterates through five_elements. In each iteration of the loop, we retrieve the string at index 1 from the current list (within five_elements), assign that string to the variable crime_rate, and use the append() method to add crime_rate to the list crime_rates.


crime_rates = []
​
for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]
​
    # crime_rate is a string, the crime rate of the city
    crime_rates.append(crime_rate)
Now it's your turn to apply what you've learned to the full dataset.

Instructions
Create a list of strings named cities_list that contains just the city names from final_data.
Recall that the city name is located at index 0 for each list in final_data.

"""
crime_rates = []

for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]
    # crime_rate is a string, the crime rate of the city.
    crime_rates.append(crime_rate)

cities_list = []
for row in final_data:
    final = row[0]
    cities_list.append(final)
""" result or Ipython output


"""



"""
11: Challenge
Let's practice synthesizing the concepts you've learned so far in this mission. Note that this exercise may be more challenging than the previous ones, and may take more time to complete.

Instructions
Create a list of integers named int_crime_rates that contains just the crime rates - as integers - from the list rows.
First create an empty list and assign it to a new variable int_crime_rates.
Then, write a for loop that iterates over rows and does the following:
uses the split() method to convert each string in rows into a list, based on the comma delimiter
converts the value at index 1 from that list to an integer using the int() function
uses the append() method to add each integer to int_crime_rates

"""
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
int_crime_rates = []
for row in rows:
    row_split = row.split(',')
    row_split[1] =  int(row_split[1])
    int_crime_rates.append(row_split[1])
""" result or Ipython output
Output
['Albuquerque,749', 'Anaheim,371', 'Anchorage,828', 'Arlington,503', 'Atlanta,1379']

"""