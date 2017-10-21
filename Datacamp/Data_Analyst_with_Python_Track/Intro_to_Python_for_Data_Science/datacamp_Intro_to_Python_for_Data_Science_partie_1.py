# partie 1 : Python Basics
# python 3.x

"""
The Python Interface
100xp

In the Python script on the right, you can type Python code to solve the exercises. If you hit Submit Answer, your python script (script.py) is executed and the output is shown in the IPython Shell. DataCamp checks whether your submission is correct and gives you feedback.

You can hit Submit Answer as often as you want. If you're stuck, you can click Get Hint, and ultimately Get Solution.

You can also use the IPython Shell interactively by simply typing commands and hitting Enter. When you work in the shell directly, your code will not be checked for correctness so it is a great way to experiment.
Instructions

    Experiment in the IPython Shell; type 5 / 8, for example.
    Add another line of code to the Python script: print(7 + 10).
    Hit Submit Answer to execute the Python script and receive feedback.

"""

print(5 / 8)
print(7 + 10)


"""
Any comments?
100xp

Something that Filip didn't mention in his videos is that you can add comments to your Python scripts. Comments are important to make sure that you and others can understand what your code is about.

To add comments to your Python script, you can use the # tag. These comments are not run as Python code, so they will not influence your result. As an example, take the comment on the right, # Just testing division: it is completely ignored during execution.
Instructions

    Above the print(7 + 10), add the comment # Addition works too.

"""

# Just testing division
print(5 / 8)

# Addition works too
print(7 + 10)



"""
100 + 10% pendant 7 ans
Python as a calculator
100xp

Python is perfectly suited to do basic calculations. Apart from addition, subtraction, multiplication and division, there is also support for more advanced operations such as:

    Exponentiation: **. This operator raises the number to its left to the power of the number to its right: for example 4**2 will give 16.
    Modulo: %. It returns the remainder of the division of the number to the left by the number on its right, for example 18 % 7 equals 4.

The code in the script on the right gives some examples.
Instructions

Suppose you have $100, which you can invest with a 10% return each year. After one year, it's 100×1.1=110
dollars, and after two years it's 100×1.1×1.1=121. Add code on the right to calculate how much money you end up with after 7 years.
"""


# Addition and subtraction
print(5 + 5)
print(5 - 5)

# Multiplication and division
print(3 * 5)
print(10 / 2)

# Exponentiation
print(4 ** 2)

# Modulo
print(18 % 7)

# How much is your $100 worth after 7 years?
print((1.1 ** 7) * 100)


"""

Variable Assignment
100xp

In Python, a variable allows you to refer to a value with a name. To create a variable use =, like this example:

x = 5

You can now use the name of this variable, x, instead of the actual value, 5.
Instructions

    Create a variable savings with the value 100.
    Check out this variable by typing print(savings) in the script.

"""

# Create a variable savings
savings = 100

# Print out savings
print(savings)


"""
Calculations with variables
100xp

Remember how you calculated the money you ended up with after 7 years of investing $100? You did something like this:

100 * 1.10 ** 7

Instead of calculating with the actual values, you can use variables instead. The savings variable you've created in the previous exercise represents the $100 you started with. It's up to you to create a new variable to represent 1.10 and then redo the calculations!
Instructions

    Create a variable factor, equal to 1.10.
    Use savings and factor to calculate the amount of money you end up with after 7 years. Store the result in a new variable, result.
    Print out the value of result.

"""

# Create a variable savings
savings = 100

# Create a variable factor
factor = 1.10

# Calculate result
result = savings * (factor ** 7)

# Print out result
print(result)



"""
Other variable types
100xp

In the previous exercise, you worked with two Python data types:

    int, or integer: a number without a fractional part. savings, with the value 100, is an example of an integer.
    float, or floating point: a number that has both an integer and fractional part, separated by a point. factor, with the value 1.10, is an example of a float.

Next to numerical data types, there are two other very common data types:

    str, or string: a type to represent text. You can use single or double quotes to build a string.
    bool, or boolean: a type to represent logical values. Can only be True or False.

Instructions

    Create a new string, desc, with the value "compound interest".
    Create a new boolean, profitable, with the value True.
"""

# Create a variable desc
desc = "compound interest"

# Create a variable profitable
profitable = True


"""
Question => réponse 3
Guess the type
50xp

To find out the type of a value or a variable that refers to that value, you can use the type() function. Suppose you've defined a variable a, but you forgot the type of this variable. To determine the type of a, simply execute:

type(a)

We already went ahead and created three variables: a, b and c. You can use the IPython shell on the right to discover their type. Which of the following options is correct?
Possible Answers

    a is of type int, b is of type str, c is of type bool
    a is of type float, b is of type bool, c is of type str
    a is of type float, b is of type str, c is of type bool
    a is of type int, b is of type bool, c is of type str 
"""

""" sortie :
In [1]: type(a)
Out[1]: float

In [2]: type(b)
Out[2]: str

In [3]: type(c)
Out[3]: bool
"""



"""
Operations with other types
100xp

Filip mentioned that different types behave differently in Python.

When you sum two strings, for example, you'll get different behavior than when you sum two integers or two booleans.

In the script some variables with different types have already been created. It's up to you to use them.
Instructions

    Calculate the product of savings and factor. Store the result in year1.
    What do you think the resulting type will be? Find out by printing out the type of year1.
    Calculate the sum of desc and desc and store the result in a new variable doubledesc.
    Print out doubledesc. Did you expect this?
"""

# Several variables to experiment with
savings = 100
factor = 1.1
desc = "compound interest"

# Assign product of factor and savings to year1
year1 = savings * factor

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc

# Print out doubledesc
print(doubledesc)


"""
Type conversion
100xp

Using the + operator to paste together two strings can be very useful in building custom messages.

Suppose for example that you've calculated the return of your investment, and want to summarize the results in a string. Assuming the floats savings and result are defined, you can try something like this:

print("I started with $" + savings + " and now have $" + result + ". Awesome!")

This will not work, though, as you cannot simply sum strings and floats.

To fix the error, you'll need to explicitly convert the types of your variables. More specifically, you'll need str(), to convert a value into a string. str(savings), for example, will convert the float savings to a string.

Similar functions such as int(), float() and bool() will help you convert Python values into any type.
Instructions

    Hit Submit Answer to run the code on the right. Try to understand the error message.
    Fix the code on the right such that the printout runs without errors; use the function str() to convert the variables to strings.
    Convert the variable pi_string to a float and store this float as a new variable, pi_float.

"""

# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)




""" question numéro 3 a cocher?
Can Python handle everything?
50xp

Now that you know something more about combining different sources of information, have a look at the four Python expressions below. Which one of these will throw an error? You can always copy and paste this code in the IPython Shell to find out!
Possible Answers

    "I can add integers, like " + str(5) + " to strings."
    1
    "I said " + ("Hey " * 2) + "Hey!"
    2
    "The correct answer to this multiple choice exercise is answer number " + 2
    3
    True + False
    4
 """

 """ sortie :
 In [1]: "I can add integers, like " + str(5) + " to strings."
Out[1]: 'I can add integers, like 5 to strings.'

In [2]: "I said " + ("Hey " * 2) + "Hey!"
Out[2]: 'I said Hey Hey Hey!'

In [3]: "The correct answer to this multiple choice exercise is answer number " + 2

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    "The correct answer to this multiple choice exercise is answer number " + 2
TypeError: Can't convert 'int' object to str implicitly


In [4]: True + False
Out[4]: 1
"""