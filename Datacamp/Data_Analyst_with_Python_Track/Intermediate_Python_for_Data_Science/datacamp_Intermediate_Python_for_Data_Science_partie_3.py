# Datacamp Intermediate Python for Data Science
# partie 3 : Logic, Control Flow and Filter

"""
Equality
100xp
To check if two Python values, or variables, are equal you can use ==. To check for inequality, you need !=. As a refresher, have a look at the following examples that all result in True. Feel free to try them out in the IPython Shell.

2 == (1 + 1)
"intermediate" != "python"
True != False
"Python" != "python"
When you write these comparisons in a script, you will need to wrap a print() function around them to see the output.

Instructions
In the editor on the right write code to see if True equals False.
Write Python code to check if -5 * 15 is not equal to 75.
Ask Python whether the strings "pyscript" and "PyScript" are equal.
What happens if you compare booleans and integers? Write code to see if True and 1 are equal.
"""
# Comparison of booleans
print(True == False)

# Comparison of integers
print(-5 * 15 != 75)

# Comparison of strings
print("pyscript" == "PyScript")

# Compare a boolean with an integer
print(True == 1)
""" sortie ipython
In [1]: True == False
Out[1]: False

In [2]: -5 * 15 == 75
Out[2]: False

In [3]: "pyscript" == "PyScript"
Out[3]: False

In [4]: True == 1
Out[4]: True

<script.py> output:
    False
    True
    False
    True
"""




"""
Greater and less than
100xp
In the video, Filip also talked about the less than and greater than signs, < and > in Python. You can combine them with an equals sign: <= and >=. Pay attention: <= is valid syntax, but =< is not.

All Python expressions in the following code chunk evaluate to True:

3 < 4
3 <= 4
"alpha" <= "beta"
Remember that for string comparison, Python determines the relationship based on alphabetical order.

Instructions
Write Python expressions, wrapped in a print() function, to check whether: - x is greater than or equal to -10. x has already been defined for you. - "test" is less than or equal to y. y has already been defined for you. - True is greater than False.
"""
# Comparison of integers
x = -3 * 6


# Comparison of strings
y = "test"


# Comparison of booleans
print(x >= -10)
print("test" <= y)
print(True > False)
""" sortie Ipython
In [1]: x = -3 * 6
... 

In [2]: y = "test"

In [3]: print(x >= -10)
False

<script.py> output:
    False

<script.py> output:
    False
    True
    True
"""


"""
Compare arrays
100xp
Out of the box, you can also use comparison operators with Numpy arrays.

Remember areas, the list of area measurements for different rooms in your house from the previous course? This time there's two Numpy arrays: my_house and your_house. They both contain the areas for the kitchen, living room, bedroom and bathroom in the same order, so you can compare them.

Instructions
Using comparison operators, generate boolean arrays that answer the following questions: - Which areas in my_house are greater than or equal to 18? - You can also compare two Numpy arrays element-wise. Which areas in my_house are smaller than the ones in your_house?

Make sure to wrap both commands in print() statement, so that you can inspect the output.
"""
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)
""" sortie Ipython
In [1]: import numpy as np
... my_house = np.array([18.0, 20.0, 10.75, 9.50])
... your_house = np.array([14.0, 24.0, 14.25, 9.0])
... 

In [2]: print(my_house >= 18)
... 
[ True  True False False]

In [3]: print(my_house < your_house)
[False  True  True False]

<script.py> output:
    [ True  True False False]
    [False  True  True False]
"""




"""
and, or, not (1)
100xp
A boolean is either 1 or 0, True or False. With boolean operators such as and, or and not, you can combine these booleans to perform more advanced queries on your data.

In the sample code on the right, two variables are defined: my_kitchen and your_kitchen, representing areas.

Instructions
Write Python expressions, wrapped in a print() function, to check whether: - my_kitchen is bigger than 10 and smaller than 18. - my_kitchen is smaller than 14 or bigger than 17. - double the area of my_kitchen is smaller than triple the area of your_kitchen.
"""
# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)

# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen * 2 < your_kitchen * 3)





""" réponse : 2 False  => False and True
and, or, not (2)
50xp
To see if you completely understood the boolean operators, have a look at the following piece of Python code:

x = 8
y = 9
not(not(x < 3) and not(y > 14 or y > 10))
What will the result be if you execute these three commands in the IPython Shell?

NB: Notice that not has a higher priority than and and or, it is executed first.

Possible Answers
True 1
False 2
Running these commands will result in an error.
"""

""" sortie Ipython
In [1]: x = 8
... y = 9

In [2]: not(not(x < 3) and not(y > 14 or y > 10))
Out[2]: False
"""







"""
Boolean operators with Numpy
100xp
Before, the operational operators like < and >= worked with Numpy arrays out of the box. Unfortunately, this is not true for the boolean operators and, or, and not.

To use these operators with Numpy, you will need np.logical_and(), np.logical_or() and np.logical_not(). Here's an example on the my_house and your_house arrays from before to give you an idea:

logical_and(your_house > 13, 
            your_house < 15)
Instructions
Generate boolean arrays that answer the following questions: - Which areas in my_house are greater than 18.5 or smaller than 10? - Which areas are smaller than 11 in both my_house and your_house? Make sure to wrap both commands in print() statement, so that you can inspect the output.
"""
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5,my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11,your_house < 11))
""" sortie Ipython
In [1]: import numpy as np
... my_house = np.array([18.0, 20.0, 10.75, 9.50])
... your_house = np.array([14.0, 24.0, 14.25, 9.0])

In [2]: print(np.logical_or(my_house > 18.5,my_house < 10))
... 
[False  True False  True]

In [3]: print(np.logical_or(my_house < 11,your_house < 11))
[False False  True  True]

<script.py> output:
    [False  True False  True]
    [False False  True  True]

In [4]: print(np.logical_and(my_house < 11,your_house < 11))
[False False False  True]

<script.py> output:
    [False  True False  True]
    [False False False  True]
"""





""" question réponse : 2
Warmup
50xp

To experiment with if and else a bit, have a look at this code sample:

area = 10.0
if(area < 9) :
    print("small")
elif(area < 12) :
    print("medium")
else :
    print("large")

What will the output be if you run this piece of code in the IPython Shell?
Possible Answers

    small
    1
    medium
    2
    large
    3
    The syntax is incorrect; this code will produce an error.
"""

""" sortie Ipython
In [1]: area = 10.0
... if(area < 9) :
...     print("small")
... elif(area < 12) :
...     print("medium")
... else :
...     print("large")
medium
"""






"""
if
100xp

It's time to take a closer look around in your house.

Two variables are defined in the sample code: room, a string that tells you which room of the house we're looking at, and area, the area of that room.
Instructions

    Examine the if statement that prints out "Looking around in the kitchen." if room equals "kit".
    Write another if statement that prints out "big place!" if area is greater than 15.

"""
# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area > 15:
    print("big place!")
""" sortie Ipython

<script.py> output:
    looking around in the kitchen.
"""








"""
Add else
100xp

On the right, the if construct for room has been extended with an else statement so that "looking around elsewhere." is printed if the condition room = "kit" evaluates to False.

Can you do a similar thing to add more functionality to the if construct for area?
Instructions

Add an else statement to the second control structure so that "pretty small." is printed out if area > 15 evaluates to False.
"""
# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

# if-else construct for area
if area > 15 :
    print("big place!")
else :
    print("pretty small.")
""" sortie Ipython

<script.py> output:
    looking around in the kitchen.
    pretty small.
"""






"""
Customize further: elif
100xp

It's also possible to have a look around in the bedroom. The sample code contains an elif part that checks if room equals "bed". In that case, "looking around in the bedroom." is printed out.

It's up to you now! Make a similar addition to the second control structure to further customize the messages for different values of area.
Instructions

Add an elif to the second control structure such that "medium size, nice!" is printed out if area is greater than 10.
"""
# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10:
    print("medium size, nice!")
else :
    print("pretty small.")
""" sortie Ipython

<script.py> output:
    looking around in the bedroom.
    medium size, nice!
"""







"""
Driving right (1)
100xp

Remember that cars dataset, containing the cars per 1000 people (cars_per_cap) and whether people drive right (drives_right) for different countries (country)? The code that imports this data in CSV format into Python as a DataFrame is available on the right.

In the video, you saw a step-by-step approach to filter observations from a DataFrame based on boolean arrays. Let's start simple and try to find all observations in cars where drives_right is True.

drives_right is a boolean column, so you'll have to extract it as a Series and then use this boolean Series to select observations from cars.
Instructions

    Extract the drives_right column as a Pandas Series and store it as dr.
    Use dr, a boolean Series, to subset the cars DataFrame. Store the resulting selection in sel.
    Print sel, and assert that drives_right is True for all observations.

"""
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars["drives_right"]

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)
""" sortie Ipython
In [1]: import pandas as pd
... cars = pd.read_csv('cars.csv', index_col = 0)

In [2]: dr = cars[:,"drives_right"] > 0

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    dr = cars[:,"drives_right"] > 0
  File "<stdin>", line 2057, in __getitem__
    return self._getitem_column(key)
  File "<stdin>", line 2064, in _getitem_column
    return self._get_item_cache(key)
  File "<stdin>", line 1384, in _get_item_cache
    res = cache.get(item)
TypeError: unhashable type: 'slice'


In [3]: dr = cars["drives_right"] > 0

In [4]: dr
Out[4]: 
US      True
AUS    False
JAP    False
IN     False
RU      True
MOR     True
EG      True
Name: drives_right, dtype: bool

In [5]: dr = cars["drives_right"]

In [6]: sel = cars[dr]

In [7]: print(sel)
     cars_per_cap        country drives_right
US            809  United States         True
RU            200         Russia         True
MOR            70        Morocco         True
EG             45          Egypt         True

<script.py> output:
         cars_per_cap        country drives_right
    US            809  United States         True
    RU            200         Russia         True
    MOR            70        Morocco         True
    EG             45          Egypt         True

"""






"""
Driving right (2)
100xp

The code in the previous example worked fine, but you actually unnecessarily created a new variable dr. You can achieve the same result without this intermediate variable. Put the code that computes dr straight into the square brackets that select observations from cars.
Instructions

Convert the code on the right to a one-liner that calculates the variable sel as before.
"""
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)
""" sortie Ipython
script.py> output:
         cars_per_cap        country drives_right
    US            809  United States         True
    RU            200         Russia         True
    MOR            70        Morocco         True
    EG             45          Egypt         True
"""






"""
Cars per capita (1)
100xp

Let's stick to the cars data some more. This time you want to find out which countries have a high cars per capita figure. In other words, in which countries do many people have a car, or maybe multiple cars.

Similar to the previous example, you'll want to build up a boolean Series, that you can then use to subset the cars DataFrame to select certain observations. If you want to do this in a one-liner, that's perfectly fine!
Instructions

    Select the cars_per_cap column from cars as a Pandas Series and store it as cpc.
    Use cpc in combination with a comparison operator and 500. You want to end up with a boolean Series that's True if the corresponding country has a cars_per_cap of more than 500 and False otherwise. Store this boolean Series as many_cars.
    Use many_cars to subset cars, similar to what you did before. Store the result as car_maniac.
    Print out car_maniac to see if you got it right.

"""
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars["cars_per_cap"] 
many_cars = cpc > 500
car_maniac = cars[many_cars]


# Print car_maniac
print(car_maniac)
""" sortie Ipython
In [1]: import pandas as pd
... cars = pd.read_csv('cars.csv', index_col = 0)

In [2]: cpc = cars["cars_per_cap"]

In [3]: cpc
Out[3]: 
US     809
AUS    731
JAP    588
IN      18
RU     200
MOR     70
EG      45
Name: cars_per_cap, dtype: int64

In [4]: many_cars = cars[cpc] > 500

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    many_cars = cars[cpc] > 500
  File "<stdin>", line 2051, in __getitem__
    return self._getitem_array(key)
  File "<stdin>", line 2096, in _getitem_array
    return self.take(indexer, axis=1, convert=True)
  File "<stdin>", line 1669, in take
    convert=True, verify=True)
  File "<stdin>", line 3932, in take
    indexer = maybe_convert_indices(indexer, n)
  File "<stdin>", line 1872, in maybe_convert_indices
    raise IndexError("indices are out-of-bounds")
IndexError: indices are out-of-bounds


In [5]: many_cars = cpc > 500

In [6]: many_cars
Out[6]: 
US      True
AUS     True
JAP     True
IN     False
RU     False
MOR    False
EG     False
Name: cars_per_cap, dtype: bool

In [7]: car_maniac = cars[many_cars]

In [8]: print(car_maniac)
     cars_per_cap        country drives_right
US            809  United States         True
AUS           731      Australia        False
JAP           588          Japan        False

<script.py> output:
         cars_per_cap        country drives_right
    US            809  United States         True
    AUS           731      Australia        False
    JAP           588          Japan        False

In [9]: 

"""






"""
Cars per capita (2)
100xp

Remember about np.logical_and(), np.logical_or() and np.logical_not(), the Numpy variants of the and, or and not operators? You can also use them on Pandas Series to do more advanced filtering operations.

Take this example that selects the observations that have a cars_per_cap between 10 and 80. Try out these lines of code step by step to see what's happening.

cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 10, cpc < 80)
medium = cars[between]

Instructions

    Use the code sample above to create a DataFrame medium, that includes all the observations of cars that have a cars_per_cap between 100 and 500.
    Print out medium.

"""
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]



# Print medium
print(medium)
""" sortie Ipython
<script.py> output:
        cars_per_cap country drives_right
    RU           200  Russia         True
"""
