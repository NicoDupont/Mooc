# partie 3 : Python basics : Numpy
# python 3.x


"""
Your First Numpy Array
100xp

In this chapter, we're going to dive into the world of baseball. Along the way, you'll get comfortable with the basics of Numpy, a powerful package to do data science.

A list baseball has already been defined in the Python script, representing the height of some baseball players in centimeters. Can you add some code here and there to create a Numpy array from it?
Instructions

    Import the numpy package as np, so that you can refer to numpy with np.
    Use np.array() to create a Numpy array from baseball. Name this array np_baseball.
    Print out the type of np_baseball to check that you got it right.

"""
# Create list baseball 
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))
""" sortie Ipython
In [1]: baseball = [180, 215, 210, 210, 188, 176, 209, 200]

In [2]: import numpy as np

In [3]: np_baseball = np.array(baseball)

In [4]: print(type(np_baseball))
<class 'numpy.ndarray'>

<script.py> output:
    <class 'numpy.ndarray'>
"""




"""
Baseball players' height
100xp

You are a huge baseball fan. You decide to call the MLB (Major League Baseball) and ask around for some more statistics on the height of the main players. They pass along data on more than a thousand players, which is stored as a regular Python list: height. The height is expressed in inches. Can you make a Numpy array out of it and convert the units to centimeters?

height is already available and the numpy package is loaded, so you can start straight away (Source: stat.ucla.edu).
Instructions

    Create a Numpy array from height. Name this new array np_height.
    Print np_height.
    Multiply np_height with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array, np_height_m.
    Print out np_height_m and check if the output makes sense.

"""
# height is available as a regular list

# Import numpy
import numpy as np

# Create a Numpy array from height: np_height
np_height = np.array(height)

# Print out np_height
print(np_height)


# Convert np_height to m: np_height_m
np_height_m = np_height * 0.0254

# Print np_height_m
print(np_height_m)
""" sortie Ipython
In [1]: import numpy as np

In [2]: np_height = np.array(height)

In [3]: print(np_height)
[74 74 72 ..., 75 75 73]

In [4]: np_height_m = np_height * 0.0254

In [5]: print(np_height_m)
[ 1.8796  1.8796  1.8288 ...,  1.905   1.905   1.8542]

<script.py> output:
    [74 74 72 ..., 75 75 73]
    [ 1.8796  1.8796  1.8288 ...,  1.905   1.905   1.8542]
"""





"""
Baseball player's BMI
100xp

The MLB also offers to let you analyze their weight data. Again, both are available as regular Python lists: height and weight. height is in inches and weight is in pounds.

It's now possible to calculate the BMI of each baseball player. Python code to convert height to a Numpy array with the correct units is already available in the workspace. Follow the instructions step by step and finish the game!
Instructions

    Create a Numpy array from the weight list with the correct units. Multiply by 0.453592 to go from pounds to kilograms. Store the resulting Numpy array as np_weight_kg.
    Use np_height_m and np_weight_kg to calculate the BMI of each player. Use the following equation:
    BMI=weight(kg)height(m)2

Save the resulting numpy array as bmi.
Print out bmi.
"""
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Create array from height with correct units: np_height_m
np_height_m = np.array(height) * 0.0254

# Create array from weight with correct units: np_weight_kg 
np_weight_kg = np.array(weight) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / (np_height_m ** 2)

# Print out bmi
print(bmi)
""" sortie Ipython
In [1]: import numpy as np

In [2]: np_height_m = np.array(height) * 0.0254

In [3]: np_weight_kg = np.array(weight) * 0.453592

In [4]: bmi = np_weight_kg / (np_height_m ** 2)

In [5]: print(bmi)
[ 23.11037639  27.60406069  28.48080465 ...,  25.62295933  23.74810865
  25.72686361]

<script.py> output:
    [ 23.11037639  27.60406069  28.48080465 ...,  25.62295933  23.74810865
      25.72686361]
"""





"""
Lightweight baseball players
100xp

To subset both regular Python lists and Numpy arrays, you can use square brackets:

x = [4 , 9 , 6, 3, 1]
x[1]
import numpy as np
y = np.array(x)
y[1]

For Numpy specifically, you can also use boolean Numpy arrays:

high = y > 5
y[high]

The code that calculates the BMI of all baseball players is already included. Follow the instructions and reveal interesting things from the data!
Instructions

    Create a boolean Numpy array: the element of the array should be True if the corresponding baseball player's BMI is below 21. You can use the < operator for this. Name the array light.
    Print the array light.
    Print out a Numpy array with the BMIs of all baseball players whose BMI is below 21. Use light inside square brackets to do a selection on the bmi array.

"""
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21 

# Print out light
print(light)


# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])
""" sortie Ipython
In [1]: import numpy as np

In [2]: np_height_m = np.array(height) * 0.0254
... np_weight_kg = np.array(weight) * 0.453592
... bmi = np_weight_kg / np_height_m ** 2

In [3]: light = bmi < 21 

In [4]: print(light)
[False False False ..., False False False]

In [5]: print(light[bmi<21])
[ True  True  True  True  True  True  True  True  True  True  True]

In [6]: print(bmi[light<21])
[ 23.11037639  27.60406069  28.48080465 ...,  25.62295933  23.74810865
  25.72686361]

In [7]: print(bmi[light])
[ 20.54255679  20.54255679  20.69282047  20.69282047  20.34343189
  20.34343189  20.69282047  20.15883472  19.4984471   20.69282047
  20.9205219 ]

<script.py> output:
    [False False False ..., False False False]
    [ 20.54255679  20.54255679  20.69282047  20.69282047  20.34343189
      20.34343189  20.69282047  20.15883472  19.4984471   20.69282047
      20.9205219 ]
"""





""" réponse : 2
Numpy Side Effects
50xp

As Filip explained before, Numpy is great to do vector arithmetic. If you compare its functionality with regular Python lists, however, some things have changed.

First of all, Numpy arrays cannot contain elements with different types. If you try to build such a list, some of the elments' types are changed to end up with a homogenous list. This is known as type coercion.

Second, the typical arithmetic operators, such as +, -, * and / have a different meaning for regular Python lists and Numpy arrays.

Have a look at this line of code:

np.array([True, 1, 2]) + np.array([3, 4, False])

Can you tell which code chunk builds the exact same Python object? The Numpy package is already imported as np, so you can start experimenting in the IPython Shell straight away!
Possible Answers

    np.array([True, 1, 2, 3, 4, False])
    1
    np.array([4, 3, 0]) + np.array([0, 2, 2])
    2
    np.array([1, 1, 2]) + np.array([3, 4, -1])
    3
    np.array([0, 1, 2, 3, 4, 5])
    4
"""

""" sortie Ipython
In [1]: import numpy as np

In [2]: test = np.array([True, 1, 2]) + np.array([3, 4, False])

In [3]: print(test)
[4 5 2]

In [4]: print(np.array([True, 1, 2, 3, 4, False]))
[1 1 2 3 4 0]

In [5]: print(np.array([4, 3, 0]) + np.array([0, 2, 2]))
[4 5 2]

In [6]: print(np.array([1, 1, 2]) + np.array([3, 4, -1]))
[4 5 1]

In [7]: print(np.array([0, 1, 2, 3, 4, 5]))
[0 1 2 3 4 5]
"""





"""
Subsetting Numpy Arrays
100xp

You've seen it with your own eyes: Python lists and Numpy arrays sometimes behave differently. Luckily, there are still certainties in this world. For example, subsetting (using the square bracket notation on lists or arrays) works exactly the same. To see this for yourself, try the following lines of code in the IPython Shell:

x = ["a", "b", "c"]
x[1]

np_x = np.array(x)
np_x[1]

The script on the right already contains code that imports numpy as np, and stores both the height and weight of the MLB players as Numpy arrays.
Instructions

    Subset np_weight: print out the element at index 50.
    Print out a sub-array of np_height: It contains the elements at index 100 up to and including index 110

"""
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight = np.array(weight)
np_height = np.array(height)

# Print out the weight at index 50
print(np_weight[50])

# Print out sub-array of np_height: index 100 up to and including index 110
print(np_height[100:111])
""" sortie Ipython
In [1]: import numpy as np

In [2]: np_weight = np.array(weight)
... np_height = np.array(height)

In [3]: print(np_weight[50])
200

In [4]: print(np_weight[100:111])
[220 230 180 220 180 180 170 210 215 200 213]

<script.py> output:
    200
    [220 230 180 220 180 180 170 210 215 200 213]

<script.py> output:
    200
    [73 74 72 73 69 72 73 75 75 73 72]
"""




"""
Your First 2D Numpy Array
100xp

Before working on the actual MLB data, let's try to create a 2D Numpy array from a small list of lists.

In this exercise, baseball is a list of lists. The main list contains 4 elements. Each of these elements is a list containing the height and the weight of 4 baseball players, in this order. baseball is already coded for you in the script.
Instructions

    Use np.array() to create a 2D Numpy array from baseball. Name it np_baseball.
    Print out the type of np_baseball.
    Print out the shape attribute of np_baseball. Use np_baseball.shape.

"""
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
""" sortie Ipython
In [1]: baseball = [[180, 78.4],
...             [215, 102.7],
...             [210, 98.5],
...             [188, 75.2]]
... 

In [2]: import numpy as np

In [3]: np_baseball = np.array(baseball)

In [4]: print(type(np_baseball))
<class 'numpy.ndarray'>

In [5]: print(np_basebal.shape)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(np_basebal.shape)
NameError: name 'np_basebal' is not defined


In [6]: print(np_baseball.shape)
(4, 2)

<script.py> output:
    <class 'numpy.ndarray'>
    (4, 2)
"""




"""
Baseball data in 2D form
100xp

You have another look at the MLB data and realize that it makes more sense to restructure all this information in a 2D Numpy array. This array should have 1015 rows, corresponding to the 1015 baseball players you have information on, and 2 columns (for height and weight).

The MLB was, again, very helpful and passed you the data in a different structure, a Python list of lists. In this list of lists, each sublist represents the height and weight of a single baseball player. The name of this embedded list is baseball.

Can you store the data as a 2D array to unlock Numpy's extra functionality?
Instructions

    Use np.array() to create a 2D Numpy array from baseball. Name it np_baseball.
    Print out the shape attribute of np_baseball.

"""
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create a 2D Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)
""" sortie Ipython
In [1]: import numpy as np

In [2]: np_baseball = np.array(baseball)

In [3]: print(np_baseball.shape)
(1015, 2)

<script.py> output:
    (1015, 2)
"""







"""
Subsetting 2D Numpy Arrays
100xp

If your 2D Numpy array has a regular structure, i.e. each row and column has a fixed number of values, complicated ways of subsetting become very easy. Have a look at the code below where the elements "a" and "c" are extracted from a list of lists.

# regular list of lists
x = [["a", "b"], ["c", "d"]]
[x[0][0], x[1][0]]

# numpy
import numpy as np
np_x = np.array(x)
np_x[:,0]

For regular Python lists, this is a real pain. For 2D Numpy arrays, however, it's pretty intuitive! The indexes before the comma refer to the rows, while those after the comma refer to the columns. The : is for slicing; in this example, it tells Python to include all rows.

The code that converts the pre-loaded baseball list to a 2D Numpy array is already in the script. Add some lines to make the correct selections. Remember that in Python, the first element is at index 0!
Instructions

    Print out the 50th row of np_baseball.
    Make a new variable, np_weight, containing the entire second column of np_baseball.
    Select the height (first column) of the 124th baseball player in np_baseball and print it out.

"""
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight
np_weight = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123,0])
""" sortie Ipython

"""







"""
2D Arithmetic
100xp

Remember how you calculated the Body Mass Index for all baseball players? Numpy was able to perform all calculations element-wise. For 2D Numpy arrays this isn't any different! You can combine matrices with single numbers, with vectors, and with other matrices.

Execute the code below in the IPython shell and see if you understand:

import numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
np_mat * 2
np_mat + np.array([10, 10])
np_mat + np_mat

np_baseball is coded for you; it's again a 2D Numpy array with 3 columns representing height, weight and age.
Instructions

    You managed to get hold on the changes in weight, height and age of all baseball players. It is available as a 2D Numpy array, update. Add np_baseball and update and print out the result.
    You want to convert the units of height and weight. As a first step, create a Numpy array with three values: 0.0254, 0.453592 and 1. Name this array conversion.
    Multiply np_baseball with conversion and print out the result.

"""
# baseball is available as a regular list of lists
# update is available as 2D Numpy array

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and update
print(np_baseball + update)

# Create Numpy array: conversion
conversion = np.array([0.0254,0.453592,1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)
""" sortie Ipython
In [1]: import numpy as np

In [2]: np_mat = np.array([[1, 2],
...                    [3, 4],
...                    [5, 6]])

In [3]: np_mat * 2
Out[3]: 
array([[ 2,  4],
       [ 6,  8],
       [10, 12]])

In [4]: np_mat + np.array([10, 10])
Out[4]: 
array([[11, 12],
       [13, 14],
       [15, 16]])

In [5]: np_mat + np_mat
Out[5]: 
array([[ 2,  4],
       [ 6,  8],
       [10, 12]])

In [6]: import numpy as np

In [7]: 

In [7]: np_baseball = np.array(baseball)

In [8]: print(np_baseball + update)
[[  75.2303559   168.83775102   23.99      ]
 [  75.02614252  231.09732309   35.69      ]
 [  73.1544228   215.08167641   31.78      ]
 ..., 
 [  76.09349925  209.23890778   26.19      ]
 [  75.82285669  172.21799965   32.01      ]
 [  73.99484223  203.14402711   28.92      ]]

In [9]: conversion = np.array([0.0254,0.453592,1])

In [10]: print(np_baseball * conversion)
[[  1.8796   81.64656  22.99   ]
 [  1.8796   97.52228  34.69   ]
 [  1.8288   95.25432  30.78   ]
 ..., 
 [  1.905    92.98636  25.19   ]
 [  1.905    86.18248  31.01   ]
 [  1.8542   88.45044  27.92   ]]

In [11]: print(np_baseball)
[[  74.    180.     22.99]
 [  74.    215.     34.69]
 [  72.    210.     30.78]
 ..., 
 [  75.    205.     25.19]
 [  75.    190.     31.01]
 [  73.    195.     27.92]]

<script.py> output:
    [[  75.2303559   168.83775102   23.99      ]
     [  75.02614252  231.09732309   35.69      ]
     [  73.1544228   215.08167641   31.78      ]
     ..., 
     [  76.09349925  209.23890778   26.19      ]
     [  75.82285669  172.21799965   32.01      ]
     [  73.99484223  203.14402711   28.92      ]]
    [[  1.8796   81.64656  22.99   ]
     [  1.8796   97.52228  34.69   ]
     [  1.8288   95.25432  30.78   ]
     ..., 
     [  1.905    92.98636  25.19   ]
     [  1.905    86.18248  31.01   ]
     [  1.8542   88.45044  27.92   ]]
"""








"""
Average versus median
100xp

You now know how to use Numpy functions to a get a better feeling for your data. It basically comes down to importing Numpy and then calling several simple functions on the Numpy arrays:

import numpy as np
x = [1, 4, 8, 10, 12]
np.mean(x)
np.median(x)

The baseball data is available as a 2D Numpy array with 3 columns (height, weight, age) and 1015 rows. The name of this Numpy array is np_baseball. After restructuring the data, however, you notice that some height values are abnormally high. Follow the instructions and discover which summary statistic is best suited if you're dealing with so-called outliers.
Instructions

    Create Numpy array np_height, that is equal to first column of np_baseball.
    Print out the mean of np_height.
    Print out the median of np_height.

"""
# np_baseball is available

# Import numpy
import numpy as np

# Create np_height from np_baseball
np_height = np_baseball[:,0]

# Print out the mean of np_height
print(np.mean(np_height))


# Print out the median of np_height
print(np.median(np_height))
""" sortie Ipython
In [1]: import numpy as np

In [2]: np_height = np_baseball[:,0]

In [3]: print(np.mean(np_height))
1586.46108374

In [4]: # Print out the median of np_height
... print(np.median(np_height))
74.0

<script.py> output:
    1586.46108374
    74.0
"""







"""
Explore the baseball data
100xp

Because the mean and median are so far apart, you decide to complain to the MLB. They find the error and send the corrected data over to you. It's again available as a 2D Numpy array np_baseball, with three columns.

The Python script on the right already includes code to print out informative messages with the different summary statistics. Can you finish the job?
Instructions

    The code to print out the mean height is already included. Complete the code for the median height. Replace None with the correct code.
    Use np.std() on the first column of np_baseball to calculate stddev. Replace None with the correct code.
    Do big players tend to be heavier? Use np.corrcoef() to store the correlation between the first and second column of np_baseball in corr. Replace None with the correct code.

"""
# np_baseball is available

# Import numpy
import numpy as np

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
print("Correlation: " + str(corr))
""" sortie Ipython
In [1]: import numpy as np

In [2]: avg = np.mean(np_baseball[:,0])
... print("Average: " + str(avg))
Average: 73.6896551724

In [3]: med = np.median(np_baseball[:,0])
... print("Median: " + str(med))
Median: 74.0

In [4]: stddev = np.std(np_baseball[:,0])
... print("Standard Deviation: " + str(stddev))
Standard Deviation: 2.31279188105

In [5]: corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
... print("Correlation: " + str(corr))
Correlation: [[ 1.          0.53153932]
 [ 0.53153932  1.        ]]

<script.py> output:
    Average: 73.6896551724
    Median: 74.0
    Standard Deviation: 2.31279188105
    Correlation: [[ 1.          0.53153932]
     [ 0.53153932  1.        ]]
"""







"""
Blend it all together
100xp

In the last few exercises you've learned everything there is to know about heights and weights of baseball players. Now it's time to dive into another sport: soccer.

You've contacted the FIFA for some data and they handed you two lists. The lists are the following: positions = ['GK', 'M', 'A', 'D', ...] heights = [191, 184, 185, 180, ...] Each element in the lists corresponds to a player. The first list, positions, contains strings representing each player's position. The possible positions are: 'GK' (goalkeeper), 'M' (midfield), 'A' (attack) and 'D' (defense). The second list, heights, contains integers representing the height of the player in cm. The first player in the lists is a goalkeeper and is pretty tall (191 cm).

You're fairly confident that the median height of goalkeepers is higher than that of other players on the soccer field. Some of your friends don't believe you, so you are determined to show them using the data you received from FIFA and your newly acquired Python skills.
Instructions

    Convert heights and positions, which are regular lists, to numpy arrays. Call them np_heights and np_positions.
    Extract all the heights of the goalkeepers. You can use a little trick here: use np_positions == 'GK' as an index for np_heights. Assign the result to gk_heights.
    Extract all the heights of the all the other players. This time use np_positions != 'GK' as an index for np_heights. Assign the result to other_heights.
    Print out the median height of the goalkeepers using np.median(). Replace None with the correct code.
    Do the same for the other players. Print out their median height. Replace None with the correct code.

"""
# heights and positions are available as lists

# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np.where(np_positions == 'GK')]

# Heights of the other players: other_heights
other_heights = np_heights[np.where(np_positions != 'GK')]

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))
""" sortie Ipython
In [24]: print("Median height of goalkeepers: " + str(np.median(gk_heights)))
Median height of goalkeepers: 188.0

In [25]: print("Median height of other players: " + str(np.median(other_heights)))
Median height of other players: 181.0

<script.py> output:
    Median height of goalkeepers: 188.0
    Median height of other players: 181.0
"""






"""

"""

""" sortie Ipython

"""