""" 01/2017
Dataquest : Complete Data Analyst Path 
Step 1: Introduction To Python
SubStep : Python Programming: Beginner : Python Basics
"""

"""
2: Display Values Using The Print Function
In the last step, we assigned values to variables but didn't see any sort of visual confirmation. After we assign a value to a variable, we can confirm using the print() function. A function is a segment of reusable code that accepts an input value and produces an output value of some kind. While some functions modify the values associated with variables, the print() function only displays them. We'll learn more about functions later in this course.

To use the print() function, you pass in a value into the parentheses:


print(365)
If you pass in a variable name instead of a value, the print() function will look up the associated value and display it. The following code assigns the value 365 to the variable num_days and then displays 365:


num_days = 365
print(num_days)

Anything you display using the print() function will appear in the output box below the code editor:

Instructions
Add a line of code that uses the print() function to display the value associated with china.
Add a line of code that uses the print() function to display the value associated with india.
Add a line of code that uses the print() function to display the value associated with united_states
"""
china = 123
india = 124
united_states = 134
print(china)
print(india)
print(united_states)
""" result or Ipython output
Output
123
124
134
"""




"""
3: Data Types
While programming languages come in many different flavors, the most common one is object-oriented programming, or OOP for short. An object is a value or variable that belongs to a specific class. A class contains a shared blueprint for all objects that are instances of that class. For now, you can think of objects as being variables and classes as being types. In later missions, we'll learn how to create our own classes and dive more into how to organize our code well using object-oriented programming.

We've been working with whole numbers like 123 and 134, which are known as integers. When we assign a value an integer value to a variable, we say that the variable is an instance of the integer class. The two most common numerical types in Python are integer and float, which is used to represent fractional values. 3.5 and 4.1111 are both examples of float values.

The most common non-numerical type is a string, which is used to represent text. To represent a piece of text as a string value, surround the text with either single quotes (') or double quotes ("). 'Hello' and "Hello World!" are both examples of string values. Unlike variable names, strings can contain special characters and spaces.

You can assign a string to a variable in the same way you'd assign it a numeric value:


hello = 'Hello'
hello_world = "Hello World!"
When you use the print() function to display a string value (or a variable associated with a string value), the quotation marks won't be displayed.

You may have noticed a pattern here. Numerical values like integers and floats don't require quotation marks, but strings do. The way in which you enter a value tells Python what data type it is. Python will use the data type to determine how the value should be handled. For example, Python allows integer variables to be divided, but not string variables. We'll learn more about that soon, but first let's practice some of the concepts you've learned so far.

Instructions
Assign the string value "China" to china_name.
Assign the integer value 123 to china_rounded. This is the rounded value for the hottest temperature) ever recorded in China.
Assign the float value 122.5 to china_exact. This is the exact value for the hottest temperature ever recorded in China.
Use the print() function to display china_name, china_rounded, and china_exact.
Note that we're really asking you to display the values associated with these variables but we'll stick to ths shorter wording from now on.
"""
china_name = "China"
china_rounded = 123
china_exact = 122.5
print(china_name,china_rounded,china_exact)
""" result or Ipython output
Output
China 123 122.5
"""




"""
4: The Type Function
We can look up the data type of a variable's value using the type() function. Similar to the print() function, you pass a value (or variable) into the parantheses. Unlike the print() function, however, the type() function won't display anything. Instead, it will return the data type as a value, which can be assigned to another variable or displayed using the print() function:


hello = 'Hello'
hello_type = type(hello)
print(hello_type)
This will return the string class 'str', which means that the value associated with hello is a string (str is short for string). To avoid having to create a variable each time, you can chain the print() and type() functions:


hello = 'Hello'
print(type(hello))


Instructions
Display the type for the value associated with china_exact.

"""
china_name = "China"
china_exact = 122.5
print(type(china_exact))
""" result or Ipython output
Output
<class 'float'>
"""





"""
5: Converting Types
So far, we've represented numeric values with the integer and float data types. You can also represent them as strings, which will allow you to take advantage of the features unique to that data type. Python contains functions that will convert a value to a different data type.

The str() function converts numeric variables and values into strings. Specifically, it returns a string representation of the value that's passed in:


str_eight = str(8)
eight = 8
str_eight_two = str(eight)
The int() function does the reverse; it will attempt to convert a string into an integer, but will result in an error if the string isn't actually an integer (e.g., "January").


str_eight = "8"
int_eight = int(str_eight)
You'll learn more about errors in a later mission, but the key idea is that an error stops your code from completing all the way through and displays a message describing the mistake you made.

Instructions
Convert china_rounded to a string and assign to int_to_str.
Then, convert int_to_str to an integer and assign the result to str_to_int.

"""
china_rounded = 123
int_to_str = str(china_rounded)
str_to_int = int(int_to_str)
""" result or Ipython output

"""





"""
6: Comments
You can organize your code by inserting comments. Comments are notes that help people - including yourself - understand the code. The Python interpreter recognizes comments and treats them as plain text and won't attempt to execute them along with the rest of the code. These are the two main types of comments you can add to your code:

inline comment
single-line comment
An inline comment is useful whenever you want to annotate, or add more detail to, a specific statement. To add an inline comment at the end of a statement, start with the hash character (#) and then add your comment:


china = 123 # Number one in population.
india = 124 # Number two in population.
united_states = 134 # Number three in population.
While you don't need to add a space after the hash character (#), this is considered good style and makes your comments cleaner and easier to read.

A single-line comment spans the full line and is useful when you want to separate your code into sections. To specify that you want a line of text to be treated as a comment, start the line with the hash character (#):


# Assigning values to variables.
china = 123
india = 124
united_states = 134
​
# Displaying values associated with variables.
print(china)
print(india)
print(united_states)

Instructions
Before each assignment statement, add a single-line comment of your choosing.

"""
# comment 1
china = 123
# comment 2
india = 124
# comment 3
united_states = 134
""" result or Ipython output

"""




"""
7: Arithmetic Operators
A key part of data science is performing calculations using numerical values. Python has multiple arithmetic operators that allow you to express calculations between values. Here are the main arithmetic operators:

Addition: +.
Subtraction: -.
Multiplication: *.
Division: /.
Exponent: **.
The operator goes between the values that need to be in the calculation. For example, the following code adds 123 and 124 using the addition operator:


123 + 124
Unfortunately, just performing a calculation like this isn't useful. This is because after the Python interpreter carries out the calculation, the resulting value disappears because it wasn't assigned to any variable. In the following code, we assign the result of the sum to a variable instead:


sum_top_two = 123 + 124
You can also perform calculations using variables. Before carrying out the calculation, Python will look up the associated values:


china = 123
india = 124
sum_top_two = china + india
Lastly, you can use arithmetic operators to perform calculations that involve both variables and values:


india_squared = india ** 2
double_china = china * 2


Instructions
Add the integer value 10 to china and assign the resulting value to the new variable china_plus_10.
Multiply united_states by 100 and assign the resulting value to the new variable us_times_100.
Display the variables china_plus_10 and us_times_100 using the print() function.

"""
china_plus_10 = china + 10
us_times_100 = united_states * 100
print(china_plus_10,us_times_100)
""" result or Ipython output
Output
133 13400
"""




"""
8: Order Of Operations
In the last step, we used a single operator to combine two values (e.g. 123 + 124). When using multiple operators (e.g. 3 + 5 * 2), we need rules that determine which order the calculations will be performed in. Take a look at the following example:


result = 5 + 5 + 5 / 10
If we add the three 5's first, we'll get a different answer than if we divided 5 by 10 first then performed the addition:

Differences in OOO

Python, and many programming languages, use the order of operations rules from mathematics to determine the specific priority that calculations have. An easy way to remember the order of operations is PEMDAS. Here's a breakdown of what each letter means, along with the relevant Python operators:

Parentheses: ( and ).
Exponents: **.
Multiplication: *.
Division: /.
Addition: +.
Subtraction: -.
The Python interpreter processes calculations in the following order:

Calculations in parentheses.
Calculations using exponents.
Division or multiplication (these rank equally and are processed left to right in the order they appear).
Addition or subtraction (these also rank equally and are processed left to right in the order they appear).
Here's a diagram that walks through each step of applying the order of operations:

OOO Without Parentheses

Because the interpreter didn't find any parentheses or exponents, it looked for any multiple or division calculations. When it found 5 / 10, it performed that calculation first. Finally, it looked for any addition or subtraction calculations and performed the summation of the three values. If we instead use parentheses to group the summation first, that calculation is performed first:

OOO With Parentheses

Let's use what we've learned to convert the three Fahrenheit values we've been working with to Celsius.

Instructions
Subtract 32 from china, multiply the result by the float 0.56, and assign the final result to china_celsius
Subtract 32 from india, multiply the result by the float 0.56, and assign the final result to india_celsius.
Subtract 32 from united_states, multiply the result by the float 0.56, and assign the final result to us_celsius.

"""
china = 123
india = 124
united_states = 134
china_celsius = (china - 32) * 0.56
india_celsius = (india - 32) * 0.56
us_celsius = (united_states - 32) * 0.56
""" result or Ipython output

"""





"""
9: Console
So far, we've been working in the code editor interface by writing multiple lines of code in a text file and running the code in the text file all at once. The console is a programming environment that's helpful whenever we want to rapidly prototype and iterate on our code. In the console, every line of code we write is run using the Python read-eval-print loop, or REPL for short.

Every line of code is read by the Python interpreter, evaluated, then any output is printed out below our code. Here's a preview of the console in action:

DQ Console

As you can tell from the screenshot, we don't need to explicitly use a print() statement to display the result of a calculation. We can even display the value associated with a variable by typing the variable name:

DQ Console Variable

To switch to the console interface, click on the Console button:

DQ Switch To Console

After you type a line of code, press the Enter key to have the interpreter evaluate your code. In this step, we don't perform any answer checking on your code and encourage you to experiment working in the console.

Instructions
Get familiar with the console by:
Dividing 5 by 10.
Assigning the value 103 to the variable indonesia then displaying indonesia.

"""

""" result or Ipython output

>>> 5 / 10
0.5

>>> indonesia = 103

>>> indonesia
103
"""





"""
10: Using A List To Store Multiple Values
So far, we've been storing individual values in variables. Often in data science, we're working with thousands of data points that are grouped together in a certain way and have an order to them. We need a container that can hold multiple values that we can use to perform operations on.

We can use a list, which is an object that represents a sequence of values. For example, the months in a year can be represented as a list as a sequence of strings ("January", "February", and so on). The most basic way to make a list is to create an empty one first, and then adding values to it. To create an empty list, assign a pair of empty brackets [] to a variable:


# months is an empty list (contains no values).
months = []
To add values to a list object, use the list.append() method. This method accepts a value and adds it to a list object. Unlike functions, methods are called using dot notation (.) on a specific object. months is a list object and the Python interpreter knows that list.append() can be used. You can see the methods available to list objects here.

In the following code snippet, we use the list.append() method to add the string "January" then the string "February" to the list months. The list.append() method is called on an instance of the list class (months) and modifies that specific object:


months = []
months.append("January")
months.append("February")
Lastly, list objects can store values of multiple types:


months = []
months.append(1)
months.append("January")
months.append(2)
months.append("February")

Instructions
Create two empty lists, countries and temperatures.
Add the following strings to the list countries, in the following order:
"China".
"India".
"United States".
Add the following float values to the list temperatures, in the following order:
122.5.
124.0.
134.1.
Use the variables display or the print() function to display the lists.

"""
countries = []
temperatures = []
countries.append("China")
countries.append("India")
countries.append("United States")
temperatures.append(122.5)
temperatures.append(124.0)
temperatures.append(134.1)
print(countries,temperatures)
""" result or Ipython output
Output
['China', 'India', 'United States'] [122.5, 124.0, 134.1]
"""



"""
11: Creating Lists With Values
In the last step, we learned how to populate lists by:

creating an empty list: months = [].
then adding values to the list using the list.append() method: months.append(1).
This can become tedious when working with multiple lists, because you have to write many lines of code (one for each value in the list). You can instead create a list and populate a values all in one line using the following syntax:


months = [1, "January", 2, "February"]
You may be wondering why we would ever want to create an empty list and add values manually. That technique is useful when you only want to add values that meet specific criteria. In that case, you need an empty placeholder list that you can append items to individually. As you work with lists, you'll start to learn the best technique for a given situation.

Instructions
Create and populate the list temps with the following values in a single line of code, in the following order:
"China".
122.5.
"India".
124.0.
"United States".
134.1.

"""
temps = ["China",122.5,"India",124.0,"United States",134.1]
""" results or Ipython console

"""




"""
12: Accessing Elements In A List
Now that we know how to create a list and add values to it, let's learn how to access and work with the values in a list we've created. Each value in the list has an index, or position, associated with it. A list starts at index 0 and goes all the way to one less than the total number of values, or elements, in the list. If you have a list with 5 values, for example, the indexes will range from 0 to 4.

The main quirk of list indexes is that to access the first element in a list, we actually use the index value 0 - not 1. The second element is accessed with index value 1, the third element with index value 2, and so on. This is known as zero indexing. While many programming languages use zero indexing, some, like MATLAB, do not.

To return the value that has a given index, pass the integer for the index into bracket notation. In the following code, we create a list named years with five elements, and access the first, second, and fifth elements in the list. We assign each of the accessed values to new variables:


years = [2010, 2011, 2012, 2013, 2014]
first_value = years[0] # 2010
second_value = years[1] # 2011
fifth_value = years[4] # 2014
The Python interpreter expects that the bracketed integer value will be within the list's range of indexes. Passing in a non-integer value or an integer value outside of the range of indexes (e.g. index 7 for a list only containing 5 elements) will result in an error.

Instructions
Select the first element from the list countries and assign to the new variable china.
Select the first element from the list temperatures and assign to the new variable china_temperature.

"""
countries = []
temperatures = []

countries.append("China")
countries.append("India")
countries.append("United States")

temperatures.append(122.5)
temperatures.append(124.0)
temperatures.append(134.1)

# Add your code here.
china = countries[0]
china_temperature = temperatures[0]
""" results or Ipython console

"""




"""
13: Retrieving The Length Of A List
We mentioned earlier that trying to lookup a value at an index that's not in the list will return an error and cause your code to halt. You may be wondering how we avoid accidentally looking up a value that's outside the index of a list. Python's len() function returns the length of a list, or the number of elements in that list. The function returns this value as an integer:


int_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
twelve = len(int_months) # Contains the integer value 12.
If we're ever unsure about the number of elements in a list, we can pass the list into the len() function. Because the len() function returns an integer, we can subtract 1 from this number to retrieve the index of the last element.


int_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
eleven = len(int_months) - 1
last_value = int_months[eleven] # Contains the value at index 11.

Instructions
Add the lengths of the countries and temperatures list objects and assign the sum to two_sum.

"""
countries = ["China", "India", "United States", "Indonesia", "Brazil", "Pakistan"]
temperatures = [122.5, 124.0, 134.1, 103.1, 112.5, 128.3]
two_sum = len(countries) + len(temperatures)
""" results or Ipython console

"""





"""
14: Slicing Lists
If we have a list containing thousands of values and want to retrieve the ones between index 10 and 500, this would be a lot of work with what we know so far. Fortunately, lists have a feature called slicing that allows you to return all of the values between a starting index and an ending index. When you slice a list, you return a new list containing just the values you're interested in. The value at the starting index and all of the values in between will be returned. The value at the ending index will not.

To slice a list, pass the starting and ending index positions into the brackets as integer values, separated by a colon :. In the following code, we use the slice 2:4 to return a new list containing the values at indices 2 and 3:


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
# Values at index 2, 3, but not 4.
two_four = months[2:4]
Here's a diagram of the same slice:

In the following code, we use the len() function to retrieve the total number of elements in the list months, and use it as the ending index:


# Values at index 3, 4, 5 and 6.
ending_index = len(months)
three_six = months[3:ending_index]
We also returned a list three_six that contains the last four elements in the list months by specifying a slice from the starting index (3) to the ending index (len(months)).

Instructions
Select the second, third, and fourth elements from countries and assign the resulting list to countries_slice.
Select the last three elements in temperatures and assign to temperatures_slice.

"""
countries = ["China", "India", "United States", "Indonesia", "Brazil", "Pakistan"]
temperatures = [122.5, 124.0, 134.1, 103.1, 112.5, 128.3]
countries_slice = countries[1:4]
temperatures_slice = temperatures[-3:len(temperatures)]
""" results or Ipython console

"""