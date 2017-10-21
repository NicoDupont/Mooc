# Datacamp Intermediate Python for Data Science
# partie 4 : Loop / Boucle




""" question réponse 3
while: warming up
50xp

The while loop is like a repeated if statement. The code is executed over and over again, as long as the condition is True. Have another look at its recipe.

while condition :
    expression

Can you tell how many printouts the following while loop will do?

x = 1
while x < 4 :
    print(x)
    x = x + 1

Possible Answers

    0
    1
    1
    2
    2
    3
    3
    4
    4
"""
""" sortie ipython
In [1]: x = 1
... while x < 4 :
...     print(x)
...     x = x + 1
1
2
3
"""





"""
Basic while loop
100xp

Below you can find the example from the video where the error variable, initially equal to 50.0, is divided by 4 and printed out on every run:

error = 50.0
while error > 1 :
    error = error / 4
    print(error)

This example will come in handy, because it's time to build a while loop yourself! We're going to code a while loop that implements a very basic control system for a reverted pendulum. If there's an offset from standing perfectly straight, the while loop will incrementally fix this offset.
Instructions

    Create the variable offset with an initial value of 8.
    Code a while loop that keeps running as long as offset is not equal to 0. Inside the while loop:
        Print out the sentence "correcting...".
        Next, decrease the value of offset by 1. You can do this with offset = offset - 1.
        Finally, print out offset so you can see how it changes.

"""
# Initialize offset
offset = 8

# Code the while loop
while offset != 0 :
    print("correcting...")
    offset -= 1
    print(offset)
""" sortie ipython
In [1]: offset = 8
... 

In [2]: while offset != 0 :
...     print("correcting...")
...     offset -= 1
...     print(offset)
correcting...
7
correcting...
6
correcting...
5
correcting...
4
correcting...
3
correcting...
2
correcting...
1
correcting...
0

<script.py> output:
    correcting...
    7
    correcting...
    6
    correcting...
    5
    correcting...
    4
    correcting...
    3
    correcting...
    2
    correcting...
    1
    correcting...
    0

In [3]: 
"""





"""
Add conditionals
100xp

The while loop that corrects the offset is a good start, but what if offset is negative? You can try to run the sample code on the right where offset is initialized to -6, but your sessions will be disconnected. The while loop will never stop running, because offset will be further decreased on every run. offset != 0 will never become False and the while loop continues forever.

Fix things by putting an if-else statement inside the while loop.
Instructions

    Inside the while loop, replace offset = offset - 1 by an if-else statement:
        If offset > 0, you should decrease offset by 1.
        Else, you should increase offset by 1.
    If you've coded things correctly, hitting Submit Answer should work this time.

"""
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
        offset = offset - 1
    else :
        offset = offset + 1
    print(offset)
""" sortie ipython
<script.py> output:
    correcting...
    -5
    correcting...
    -4
    correcting...
    -3
    correcting...
    -2
    correcting...
    -1
    correcting...
    0

"""





"""
Loop over a list
100xp

Have another look at the for loop that Filip showed in the video:

fam = [1.73, 1.68, 1.71, 1.89]
for height in fam : 
    print(height)

As usual, you simply have to indent the code with 4 spaces to tell Python which code should be executed in the for loop.

The areas variable, containing the area of different rooms in your house, is already defined.
Instructions

Write a for loop that iterates over all elements of the areas list and prints out every element separately.
"""
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for area in areas:
    print(area)
""" sortie ipython
<script.py> output:
    11.25
    18.0
    20.0
    10.75
    9.5
"""






"""
Indexes and values (1)
100xp

Using a for loop to iterate over a list only gives you access to every list element in each run, one after the other. If you also want to access the index information, so where the list element you're iterating over is located, you can use enumerate().

As an example, have a look at how the for loop from the video was converted:

fam = [1.73, 1.68, 1.71, 1.89]
for index, height in enumerate(fam) :
    print("index " + str(index) + ": " + str(height))

Instructions

Adapt the for loop in the sample code to use enumerate(). On each run, a line of the form "room x: y" should be printed, where x is the index of the list element and y is the actual list element, i.e. the area. Make sure to print out this exact string, with the correct spacing.
"""
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate()
for x ,a in enumerate(areas) :
    print("room " + str(x) + ": " + str(a))
""" sortie ipython
In [1]: areas = [11.25, 18.0, 20.0, 10.75, 9.50]

In [2]: for x ,a in enumerate(areas) :
...     print("room " + str(x) + ": " + str(a))
room 0: 11.25
room 1: 18.0
room 2: 20.0
room 3: 10.75
room 4: 9.5

<script.py> output:
    room 0: 11.25
    room 1: 18.0
    room 2: 20.0
    room 3: 10.75
    room 4: 9.5

"""






"""
Indexes and values (2)
100xp

For non-programmer folks, room 0: 11.25 is strange. Wouldn't it be better if the count started at 1?
Instructions

Adapt the print() function in the for loop on the right so that the first printout becomes "room 1: 11.25", the second one "room 2: 18.0" and so on.
"""
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(area))
""" sortie ipython
In [1]: areas = [11.25, 18.0, 20.0, 10.75, 9.50]

In [2]: for index, area in enumerate(areas) :
...     print("room " + str(index+1) + ": " + str(area))
room 1: 11.25
room 2: 18.0
room 3: 20.0
room 4: 10.75
room 5: 9.5

<script.py> output:
    room 1: 11.25
    room 2: 18.0
    room 3: 20.0
    room 4: 10.75
    room 5: 9.5
"""






"""
Loop over list of lists
100xp

Remember the house variable from the Intro to Python course? Have a look at its definition on the right. It's basically a list of lists, where each sublist contains the name and area of a room in your house.

It's up to you to build a for loop from scratch this time!
Instructions

Write a for loop that goes through each sublist of houses and prints out the x is y sqm, where x is the name of the room and y is the area of the room.
"""
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for x in house:
    print("the " + str(x[0]) + " is " + str(x[1]) + " sqm")
""" sortie ipython
In [1]: house = [["hallway", 11.25], 
...          ["kitchen", 18.0], 
...          ["living room", 20.0], 
...          ["bedroom", 10.75], 
...          ["bathroom", 9.50]]

In [2]: for x in house:
...     print(x)
['hallway', 11.25]
['kitchen', 18.0]
['living room', 20.0]
['bedroom', 10.75]
['bathroom', 9.5]

In [3]: print(x[0])
bathroom

In [4]: for x in house:
...     print("the" + str(x[0]) + " is " +str(x[1]))
thehallway is 11.25
thekitchen is 18.0
theliving room is 20.0
thebedroom is 10.75
thebathroom is 9.5

In [5]: for x in house:
...     print("the " + str(x[0]) + " is " + str(x[1]) + " sqm")
the hallway is 11.25 sqm
the kitchen is 18.0 sqm
the living room is 20.0 sqm
the bedroom is 10.75 sqm
the bathroom is 9.5 sqm

<script.py> output:
    the hallway is 11.25 sqm
    the kitchen is 18.0 sqm
    the living room is 20.0 sqm
    the bedroom is 10.75 sqm
    the bathroom is 9.5 sqm

"""





"""
Loop over dictionary
100xp

In Python 3, you need the items() method to loop over a dictionary:

world = { "afghanistan":30.55, 
          "albania":2.77,
          "algeria":39.21 }

for key, value in world.items() :
    print(key + " -- " + str(value))

Remember the europe dictionary that contained the names of some European countries as key and their capitals as corresponding value? Go ahead and write a loop to iterate over it!
Instructions

Write a for loop that goes through each key:value pair of europe. On each iteration, "the capital of x is y" should be printed out, where x is the key and y is the value of the pair.
"""
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn', 
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'australia':'vienna' }
          
# Iterate over europe
for key, value in europe.items():
    print("the capital of " + str(key) + " is " + str(value))
    #ou 
for eur in europe:
    print("the capital of " + str(eur) + " is " + str(europe[eur]))

""" sortie ipython
script.py> output:
    the capital of italy is rome
    the capital of poland is warsaw
    the capital of germany is bonn
    the capital of spain is madrid
    the capital of france is paris
    the capital of australia is vienna
    the capital of norway is oslo
"""





"""
Loop over Numpy array
100xp

If you're dealing with a 1D Numpy array, looping over all elements can be as simple as:

for x in my_array :
    ...

If you're dealing with a 2D Numpy array, it's more complicated. A 2D array is built up of multiple 1D arrays. To explicitly iterate over all separate elements of a multi-dimensional array, you'll need this syntax:

for x in np.nditer(my_array) :
    ...

Two Numpy arrays that you might recognize from the intro course are available in your Python session: np_height, a Numpy array containing the heights of Major League Baseball players, and np_baseball, a 2D Numpy array that contains both the heights (first column) and weights (second column) of those players.
Instructions

    Import the numpy package under the local alias np.
    Write a for loop that iterates over all elements in np_height and prints out "x inches" for each element, where x is the value in the array.
    Write a for loop that visits every element of the np_baseball array and prints it out.

"""
# Import numpy as np
import numpy as np

# For loop over np_height
for height in np_height:
    print(str(height) + " inches")

# For loop over np_baseball
for baseball in np.nditer(np_baseball):
    print(baseball)
""" sortie ipython

"""






"""
Loop over DataFrame (1)
100xp

Iterating over a Pandas DataFrame is typically done with the iterrows() method. Used in a for loop, every observation is iterated over and on every iteration the row label and actual row contents are available:

for lab, row in brics.iterrows() :
    ...

In this and the following exercises you will be working on the cars DataFrame. It contains information on the cars per capita and whether people drive right or left for seven countries in the world.
Instructions

Write a for loop that iterates over the rows of cars and on each iteration perform two print() calls: one to print out the row label and one to print out all of the rows contents.

"""
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for car, row in cars.iterrows():
    print(car)
    print(row)
""" sortie ipython
<script.py> output:
    US
    cars_per_cap              809
    country         United States
    drives_right             True
    Name: US, dtype: object
    AUS
    cars_per_cap          731
    country         Australia
    drives_right        False
    Name: AUS, dtype: object
    JAP
    cars_per_cap      588
    country         Japan
    drives_right    False
    Name: JAP, dtype: object
    IN
    cars_per_cap       18
    country         India
    drives_right    False
    Name: IN, dtype: object
    RU
    cars_per_cap       200
    country         Russia
    drives_right      True
    Name: RU, dtype: object
    MOR
    cars_per_cap         70
    country         Morocco
    drives_right       True
    Name: MOR, dtype: object
    EG
    cars_per_cap       45
    country         Egypt
    drives_right     True
    Name: EG, dtype: object
"""




"""
Loop over DataFrame (2)
100xp

The row data that's generated by iterrows() on every run is a Pandas Series. This format is not very convenient to print out. Luckily, you can easily select variables from the Pandas Series using square brackets:

for lab, row in brics.iterrows() :
    print(row['country'])

Instructions

Adapt the code in the for loop such that the first iteration prints out "US: 809", the second iteration "AUS: 731", and so on. Make sure to print out this exact string, with the correct spacing.
"""
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(str(lab) +": "+str(row["cars_per_cap"]))
""" sortie Ipython
In [1]: import pandas as pd
... cars = pd.read_csv('cars.csv', index_col = 0)

In [2]: cars
Out[2]: 
     cars_per_cap        country drives_right
US            809  United States         True
AUS           731      Australia        False
JAP           588          Japan        False
IN             18          India        False
RU            200         Russia         True
MOR            70        Morocco         True
EG             45          Egypt         True

In [3]: for lab, row in cars.iterrows() :
...     print(str(lab) +": "+str(row["cars_per_cap"]))
US: 809
AUS: 731
JAP: 588
IN: 18
RU: 200
MOR: 70
EG: 45

<script.py> output:
    US: 809
    AUS: 731
    JAP: 588
    IN: 18
    RU: 200
    MOR: 70
    EG: 45
"""


"""
Add column (1)
100xp

In the video, Filip showed you how to add the length of the country names of the brics DataFrame in a new column:

for lab, row in brics.iterrows() :
    brics.loc[lab, "name_length"] = len(row["country"])

You can do similar things on the cars DataFrame.
Instructions

    Use a for loop to add a new column, named COUNTRY, that contains a uppercase version of the country names in the "country" column. You can use the string method upper() for this.
    To see if your code worked, print out cars. Don't indent this code, so that it's not part of the for loop.

"""
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for car, row in cars.iterrows() :
    cars.loc[car, "COUNTRY"] = row["country"].upper()


# Print cars
print(cars)
""" sortie Ipython
In [1]: import pandas as pd
... cars = pd.read_csv('cars.csv', index_col = 0)

In [2]: # Code for loop that adds COUNTRY column
... for car, row in cars.iterrows() :
...     car.loc[car, "COUNTRY"] = row["country"].upper()

Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
    car.loc[car, "COUNTRY"] = row["country"].upper()
AttributeError: 'str' object has no attribute 'loc'


In [3]: for car, row in cars.iterrows() :
...     cars.loc[car, "COUNTRY"] = row["country"].upper()

In [4]: cars
Out[4]: 
     cars_per_cap        country drives_right        COUNTRY
US            809  United States         True  UNITED STATES
AUS           731      Australia        False      AUSTRALIA
JAP           588          Japan        False          JAPAN
IN             18          India        False          INDIA
RU            200         Russia         True         RUSSIA
MOR            70        Morocco         True        MOROCCO
EG             45          Egypt         True          EGYPT

<script.py> output:
         cars_per_cap        country drives_right        COUNTRY
    US            809  United States         True  UNITED STATES
    AUS           731      Australia        False      AUSTRALIA
    JAP           588          Japan        False          JAPAN
    IN             18          India        False          INDIA
    RU            200         Russia         True         RUSSIA
    MOR            70        Morocco         True        MOROCCO
    EG             45          Egypt         True          EGYPT

"""




"""
Add column (2)
100xp

Using iterrows() to iterate over every observation of a Pandas DataFrame is easy to understand, but not very efficient. On every iteration, you're creating a new Pandas Series.

If you want to add a column to a DataFrame by calling a function on another column, the iterrows() method in combination with a for loop is not the preferred way to go. Instead, you'll want to use apply().

Compare the iterrows() version with the apply() version to get the same result in the brics DataFrame:

for lab, row in brics.iterrows() :
    brics.loc[lab, "name_length"] = len(row["country"])

brics["name_length"] = presidents["country"].apply(len)

We can do a similar thing to call the upper() method on every name in the country column. However, upper() is a method, so we'll need a slightly different approach:
Instructions

    Replace the for loop with a one-liner that uses .apply(str.upper). The call should give the same result: a column COUNTRY should be added to cars, containing an uppercase version of the country names.
    As usual, print out cars to see the fruits of your hard labor

"""
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)
""" sortie Ipython
In [1]: import pandas as pd
... cars = pd.read_csv('cars.csv', index_col = 0)

In [2]: cars["COUNTRY"] = cars["country"].apply(upper)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    cars["COUNTRY"] = cars["country"].apply(upper)
NameError: name 'upper' is not defined
"""
