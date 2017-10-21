# partie 3 : Python basics : Functions
# python 3.x



"""
Familiar functions
100xp

Out of the box, Python offers a bunch of built-in functions to make your life as a data scientist easier. You already know two such functions: print() and type(). You've also used the functions str(), int(), bool() and float() to switch between data type. These are built-in functions as well.

Calling a function is easy. To get the type of 3.0 and store the output as a new variable, result, you can use the following:

result = type(3.0)

The general recipe for calling functions is thus:

output = function_name(input)

Instructions

    Use print() in combination with type() to print out the type of var1.
    Use len() to get the length of the list var1. Wrap it in a print() call to directly print it out.
    Use int() to convert var2 to an integer. Store the output as out2.

"""

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))


# Convert var2 to an integer: out2
out2 = int(var2)

"""sortie Ipython
In [2]: print(type(var1))
<class 'list'>

In [3]: print(len(var1))
4

In [4]: out2 = int(var2)

In [5]: print(out2)
1

<script.py> output:
    <class 'list'>
    4
"""


""" réponse  3
Help!
50xp

Maybe you already know the name of a Python function, but you still have to figure out how to use it. Ironically, you have to ask for information about a function with another function: help(). In IPython specifically, you can also use ? before the function name.

To get help on the max() function, for example, you can use one of these calls:

help(max)
?max

Use the Shell on the right to open up the documentation on complex(). Which of the following statements is true?
Possible Answers

    complex() takes exactly two arguments: real and [, imag].
    complex() takes two arguments: real and imag. Both these arguments are required.
    complex() takes two arguments: real and imag. real is a required argument, imag is an optional argument.
    complex() takes two arguments: real and imag. If you don't specify imag, it is set to 1 by Python.
"""

In [1]: ?complex
Init signature: complex(self, /, *args, **kwargs)
Docstring:
complex(real[, imag]) -> complex number

Create a complex number from a real part and an optional imaginary part.
This is equivalent to (real + imag*1j) where imag defaults to 0.
Type:           type



"""
Multiple arguments
100xp

In the previous exercise, the square brackets around imag in the documentation showed us that the imag argument is optional. But Python also uses a different way to tell users about arguments being optional.

Have a look at the documentation of sorted() by typing help(sorted) in the IPython Shell.

You'll see that sorted() takes three arguments: iterable, key and reverse.

key=None means that if you don't specify the key argument, it will be None. reverse=False means that if you don't specify the reverse argument, it will be False.

In this exercise, you'll only have to specify iterable and reverse, not key. The first input you pass to sorted() will obviously be matched to the iterable argument, but what about the second input? To tell Python you want to specify reverse without changing anything about key, you can use =:

sorted(___, reverse = ___)

Two lists have been created for you on the right. Can you paste them together and sort them in descending order?
Instructions

    Use + to merge the contents of first and second into a new list: full.
    Call sorted() on full and specify the reverse argument to be True. Save the sorted list as full_sorted.
    Finish off by printing out full_sorted.

"""
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full,reverse = True)

# Print out full_sorted
print(full_sorted)

""" sortie Ipython
In [1]: ?sorted
Signature: sorted(iterable, key=None, reverse=False)
Docstring:
Return a new list containing all items from the iterable in ascending order.

A custom key function can be supplied to customise the sort order, and the
reverse flag can be set to request the result in descending order.
Type:      builtin_function_or_method

In [2]: first = [11.25, 18.0, 20.0]
... second = [10.75, 9.50]

In [3]: full = first + second

In [4]: full_sorted = sorted(full,reverse = True)

In [5]: print(full_sorted)
[20.0, 18.0, 11.25, 10.75, 9.5]

<script.py> output:
    [20.0, 18.0, 11.25, 10.75, 9.5]
"""




"""
String Methods
100xp

Strings come with a bunch of methods. Follow the instructions closely to discover some of them. If you want to discover them in more detail, you can always type help(str) in the IPython Shell.

A string room has already been created for you to experiment with.
Instructions

    Use the upper() method on room and store the result in room_up. Use the dot notation.
    Print out room and room_up. Did both change?
    Print out the number of o's on the variable room by calling count() on room and passing the letter "o" as an input to the method. We're talking about the variable room, not the word "room"!

"""
# string to experiment with: room
room = "poolhouse"

# Use upper() on room: room_up
room_up = room.upper()

# Print out room and room_up
print(room)
print(room_up)


# Print out the number of o's in room
print(room.count("o"))

"""sortie Ipython :
In [1]: room = "poolhouse"

In [2]: room_up = upper(room)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    room_up = upper(room)
NameError: name 'upper' is not defined


In [3]: room_up = room.upper()

In [4]: print(room_up)
POOLHOUSE

In [5]: print(room.count("o"))
3

<script.py> output:
    poolhouse
    POOLHOUSE
    3

"""



"""
List Methods
100xp

Strings are not the only Python types that have methods associated with them. Lists, floats, integers and booleans are also types that come packaged with a bunch of useful methods. In this exercise, you'll be experimenting with:

    index(), to get the index of the first element of a list that matches its input and
    count(), to get the number of times an element appears in a list.

You'll be working on the list with the area of different parts of a house: areas.
Instructions

    Use the index() method to get the index of the element in areas that is equal to 20.0. Print out this index.
    Call count() on areas to find out how many times 14.5 appears in the list. Again, simply print out this number.

"""

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 14.5 appears in areas
print(areas.count(14.5))

""" sortie Ipython :
In [1]: areas = [11.25, 18.0, 20.0, 10.75, 9.50]

In [2]: print(areas.index(20.0))
2

In [3]: print(areas.count(14.5))
0

<script.py> output:
    2
    0
 """



 """
List Methods (2)
100xp

Most list methods will change the list they're called on. Examples are:

    append(), that adds an element to the list it is called on,
    remove(), that removes the first element of a list that matches the input, and
    reverse(), that reverses the order of the elements in the list it is called on.

You'll be working on the list with the area of different parts of the house: areas.
Instructions

    Use append() twice to add the size of the poolhouse and the garage again: 24.5 and 15.45, respectively. Make sure to add them in this order.
    Print out areas
    Use the reverse() method to reverse the order of the elements in areas.
    Print out areas once more.

 """
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)


# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

 """ sortie Ipython :
In [1]: areas = [11.25, 18.0, 20.0, 10.75, 9.50]

In [2]: areas.append(24.5)
... areas.append(15.45)

In [3]: print(areas)
[11.25, 18.0, 20.0, 10.75, 9.5, 24.5, 15.45]

In [4]: areas.reverse()

In [5]: print(areas)
[15.45, 24.5, 9.5, 10.75, 20.0, 18.0, 11.25]

<script.py> output:
    [11.25, 18.0, 20.0, 10.75, 9.5, 24.5, 15.45]
    [15.45, 24.5, 9.5, 10.75, 20.0, 18.0, 11.25]
 """




  """
Import package
100xp

As a data scientist, some notions of geometry never hurt. Let's refresh some of the basics.

For a fancy clustering algorithm, you want to find the circumference C
and area A of a circle. When the radius of the circle is r, you can calculate C and A

as:

C=2πr
A=πr2

To use the constant pi, you'll need the math package. A variable r is already coded in the script. Fill in the code to calculate C and A and see how the print() functions create some nice printouts.
Instructions

    Import the math package. Now you can access the constant pi with math.pi.
    Calculate the circumference of the circle and store it in C.
    Calculate the area of the circle and store it in A.

 """
# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2 * math.pi * r

# Calculate A
A = math.pi * r ** 2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))
 """ sortie Ipython :
In [2]: import math

In [3]: C = 2 * math.pi * r

In [4]: A = math.pi * r ** 2

In [5]: print("Circumference: " + str(C))
... print("Area: " + str(A))
Circumference: 2.701769682087222
Area: 0.5808804816487527

<script.py> output:
    Circumference: 2.701769682087222
    Area: 0.5808804816487527
 """




  """
Selective import
100xp

General imports, like import math, make all functionality from the math package available to you. However, if you decide to only use a specific part of a package, you can always make your import more selective:

from math import pi

Let's say the Moon's orbit around planet Earth is a perfect circle, with a radius r (in km) that is defined in the script.
Instructions

    Perform a selective import from the math package where you only import the radians function.
    Calculate the distance travelled by the Moon over 12 degrees of its orbit. Assign the result to dist. You can calculate this as r∗ϕ

, where r is the radius and ϕ
is the angle in radians. To convert an angle in degrees to an angle in radians, use the radians() function, which you just imported.
Print out dist.
 """
# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon if 12 degrees. Store in dist.
dist = r  * radians(12)

# Print out dist
print(dist)
 """ sortie Ipython :
In [1]: r = 192500

In [2]: from math import radians

In [3]: dist = r  * radians(12)

In [4]: print(dist)
40317.10572106901

<script.py> output:
    40317.10572106901
 """



  """  => réponse 4
There are several ways to import packages and modules into Python. Depending on the import call, you'll have to use different Python code.

Suppose you want to use the function inv(), which is in the linalg subpackage of the scipy package. You want to be able to use this function as follows:

my_inv([[1,2], [3,4]])

Which import statement will you need in order to run the above code without an error?
Possible Answers

    import scipy
    1
    import scipy.linalg
    2
    from scipy.linalg import my_inv
    3
    from scipy.linalg import inv as my_inv
    4
 """

 """ sortie Ipython :
In [1]: import scipy

In [2]: my_inv([[1,2], [3,4]])

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    my_inv([[1,2], [3,4]])
NameError: name 'my_inv' is not defined


In [3]: import scipy.linalg

In [4]: my_inv([[1,2], [3,4]])

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    my_inv([[1,2], [3,4]])
NameError: name 'my_inv' is not defined


In [5]: from scipy.linalg import my_inv

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    from scipy.linalg import my_inv
ImportError: cannot import name 'my_inv'


In [6]: from scipy.linalg import inv as my_inv

In [7]: my_inv([[1,2], [3,4]])
Out[7]: 
array([[-2. ,  1. ],
       [ 1.5, -0.5]])
 """

