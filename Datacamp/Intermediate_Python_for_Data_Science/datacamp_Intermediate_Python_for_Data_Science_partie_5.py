# Datacamp Intermediate Python for Data Science
# partie 5 : Case Study: Hacker Statistics




""" 
Random float
100xp

Randomness has many uses in science, art, statistics, cryptography, gaming, gambling, and other fields. You're going to use randomness to simulate a game.

All the functionality you need is contained in the random package, a sub-package of numpy. In this exercise, you'll be using two functions from this package: - seed(): sets the random seed, so that your results are the reproducible between simulations. As an argument, it takes an integer of your choosing. If you call the function, no output will be generated. - rand(): if you don't specify any arguments, it generates a random float between zero and one.
Instructions

    Import numpy as np.
    Use seed() to set the seed; as an argument, pass 123.
    Generate your first random float with rand() and print it out.

"""
# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())
""" sortie ipython
In [1]: import numpy as np
... 

In [2]: np.random.seed(123)

In [3]: print(np.random.rand())
0.6964691855978616

<script.py> output:
    0.6964691855978616
"""



""" 
Roll the dice
100xp

In the previous exercise, you used rand(), that generates a random float between 0 and 1.

As Filip explained in the video you can just as well use randint(), also a function of the random package, to generate integers randomly. The following call generates the integer 4, 5, 6 or 7 randomly. 8 is not included.

import numpy as np
np.random.randint(4, 8)

Numpy has already been imported as np and a seed has been set. Can you roll some dice?
Instructions

    Use randint() with the appropriate arguments to randomly generate the integer 1, 2, 3, 4, 5 or 6. This simulates a dice. Print it out.
    Repeat the outcome to see if the second throw is different. Again, print out the result.

"""
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))
""" sortie ipython
<script.py> output:
    3
    5

<script.py> output:
    6
    3
"""





""" 
Determine your next move
100xp

In the Empire State Building bet, your next move depends on the number of eyes you throw with the dice. We can perfectly code this with an if-elif-else construct!

The sample code assumes that you're currently at step 50. Can you fill in the missing pieces to finish the script?
Instructions

    Roll the dice. Use randint() to create the variable dice.
    Finish the if-elif-else construct by replacing ___:
        If dice is 1 or 2, you go one step down.
        if dice is 3, 4 or 5, you go one step up.
        Else, you throw the dice again. The number of eyes is the number of steps you go up.
    Print out dice and step. Given the value of dice, was step updated correctly?

"""
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 :
    step = step +1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)
""" sortie ipython
<script.py> output:
    6
    53
"""




""" 
The next step
100xp

Before, you have already wrote Python code that determines the next step based on the previous step. Now it's time to put this code inside a for loop so that we can simulate a random walk.
Instructions

    Make a list random_walk that contains the first step, which is the integer 0.
    Finish the for loop:
        The loop should run 100 times.
        On each iteration, set step equal to the last element in the random_walk list. You can use the index -1 for this.
        Next, let the if-elif-else construct update step for you.
        The code that appends step to random_walk is already coded.
    Print out random_walk.

"""
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)
""" sortie ipython
<script.py> output:
    [0, 3, 4, 5, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0, -1, 0, 5, 4, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 7, 8, 9, 10, 11, 10, 14, 15, 14, 15, 14, 15, 16, 17, 18, 19, 20, 21, 24, 25, 26, 27, 32, 33, 37, 38, 37, 38, 39, 38, 39, 40, 42, 43, 44, 43, 42, 43, 44, 43, 42, 43, 44, 46, 45, 44, 45, 44, 45, 46, 47, 49, 48, 49, 50, 51, 52, 53, 52, 51, 52, 51, 52, 53, 52, 55, 56, 57, 58, 57, 58, 59]
"""




""" 
How low can you go?
100xp

Things are shaping up nicely! You already have code that calculates your location in the Empire State Building after 100 dice throws. However, there's something we haven't thought about - you can't go below 0!

A typical way to solve problems like this is by using max(). If you pass max() two arguments, the biggest one gets returned. For example, to make sure that a variable x never goes below 10 when you decrease it, you can use:

x = max(10, x - 1)

Instructions

    Use max() in a similar way to make sure that step doesn't go below zero if dice <= 2.
    Hit Submit Answer and check the contents of random_walk.

"""
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)
""" sortie ipython
<script.py> output:
    [0, 3, 4, 5, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 6, 5, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 8, 9, 10, 11, 12, 11, 15, 16, 15, 16, 15, 16, 17, 18, 19, 20, 21, 22, 25, 26, 27, 28, 33, 34, 38, 39, 38, 39, 40, 39, 40, 41, 43, 44, 45, 44, 43, 44, 45, 44, 43, 44, 45, 47, 46, 45, 46, 45, 46, 47, 48, 50, 49, 50, 51, 52, 53, 54, 53, 52, 53, 52, 53, 54, 53, 56, 57, 58, 59, 58, 59, 60]
"""





""" 
Visualize the walk
100xp

Let's visualize this random walk! Remember how you could use matplotlib to build a line plot?

import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()

The first list you pass is mapped onto the x axis and the second list is mapped onto the y axis.

If you pass only one argument, Python will know what to do and will use the index of the list to map onto the x axis, and the values in the list onto the y axis.
Instructions

Add some lines of code after the for loop:

    Import matplotlib.pyplot as plt.
    Use plt.plot() to plot random_walk.
    Finish off with plt.show() to actually display the plot.

"""
# Initialization
import numpy as np
np.random.seed(123)
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)
#random_walk en ordonné et compteur longueur de la liste en x

# Show the plot
plt.show()
""" sortie ipython

"""





""" 
Simulate multiple walks
100xp

A single random walk is one thing, but that doesn't tell you if you have a good chance at winning the bet.

To get an idea about how big your chances are of reaching 60 steps, you can repeatedly simulate the random walk and collect the results. That's exactly what you'll do in this exercise.

The sample code already puts you in the right direction. Another for loop is wrapped around the code you already wrote. It's up to you to add some bits and pieces to make sure all results are recorded correctly.
Instructions

    Initialize all_walks to an empty list.
    Fill in the specification of the for loop so that the random walk is simulated 10 times.
    At the end of the top-level for loop, append random_walk to the all_walks list.
    Finally, after the top-level for loop, print out all_walks.

"""
# Initialization
import numpy as np
np.random.seed(123)

# Initialize all_walks
all_walks = []

# Simulate random walk 10 times
for i in range(10) :
    
    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)
""" sortie ipython
Visualize all walks
100xp

all_walks is a list of lists: every sub-list represents a single random walk. If you convert this list of lists to a Numpy array, you can start making interesting plots! matplotlib.pyplot is already imported as plt.

The nested for loop is already coded for you - don't worry about it. For now, focus on the code that comes after this for loop.
Instructions

    Use np.array() to convert all_walks to a Numpy array, np_aw.
    Try to use plt.plot() on np_aw. Also include plt.show(). Does it work out of the box?
    Transpose np_aw by calling np.transpose() on np_aw. Call the result np_aw_t. Now every row in np_all_walks represents the position after 1 throw for the 10 random walks.
    Use plt.plot() to plot np_aw_t; also include a plt.show(). Does it look better this time?

"""





""" 
Visualize all walks
100xp

all_walks is a list of lists: every sub-list represents a single random walk. If you convert this list of lists to a Numpy array, you can start making interesting plots! matplotlib.pyplot is already imported as plt.

The nested for loop is already coded for you - don't worry about it. For now, focus on the code that comes after this for loop.
Instructions

    Use np.array() to convert all_walks to a Numpy array, np_aw.
    Try to use plt.plot() on np_aw. Also include plt.show(). Does it work out of the box?
    Transpose np_aw by calling np.transpose() on np_aw. Call the result np_aw_t. Now every row in np_all_walks represents the position after 1 throw for the 10 random walks.
    Use plt.plot() to plot np_aw_t; also include a plt.show(). Does it look better this time?

"""
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123)
all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()
""" sortie ipython

"""





""" 
Implement clumsiness
100xp

With this neatly written code of yours, changing the number of times the random walk should be simulated is super-easy. You simply update the range() function in the top-level for loop.

There's still something we forgot! You're a bit clumsy and you have a 0.1% chance of falling down. That calls for another random number generation. Basically, you can generate a random float between 0 and 1. If this value is less than or equal to 0.001, you should reset step to 0.
Instructions

    Change the range() function so that the simulation is performed 250 times.
    Finish the if condition so that step is set to 0 if a random float is less or equal to 0.001. Use np.random.rand().

"""
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123)
all_walks = []

# Simulate random walk 250 times
for i in range(250) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.001 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()
""" sortie ipython

"""





""" 
Plot the distribution
100xp

All these fancy visualizations has put us on a sidetrack. We still have to solve the million-dollar problem: What are the odds that you'll reach 60 steps high on the Empire State Building?

Basically, you want to know about the end points of all the random walks you've simulated. These end points have a certain distribution that you can visualize with a histogram.
Instructions

    To make sure we've got enough simulations, go crazy. Simulate the random walk 1000 times.
    From np_aw_t, select the last row. This contains the endpoint of all 1000 random walks you've simulated. Store this Numpy array as ends.
    Use plt.hist() to build a histogram of ends. Don't forget plt.show() to display the plot.

"""
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123)
all_walks = []

# Simulate random walk 1000 times
for i in range(1000) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()
""" sortie ipython

"""




"""  question : réponse => 3  (>=60%)
Calculate the odds / Calculer les chances 
50xp

The histogram of the previous exercise was created from a Numpy array ends, that contains 1,000 integers. Each integer represents the end point of a random walk. To calculate the chance that this end point is greater than or equal to 60, you can count the number of integers in ends that are greater than or equal to 60 and divide that number by 1000, the total number of simulations.

Well then, what's the estimated chance that you'll reach 60 steps high if you play this Empire State Building game? The ends array is everything you need; it's available in your Python session so you can make calculations in the IPython Shell.
Possible Answers

    48.8%
    76.90%
    78.80%
    95.86%
"""

""" sortie ipython
In [1]: import matplotlib.pyplot as plt
... import numpy as np
... np.random.seed(123)
... all_walks = []
... 
... # Simulate random walk 1000 times
... for i in range(1000) :
...     random_walk = [0]
...     for x in range(100) :
...         step = random_walk[-1]
...         dice = np.random.randint(1,7)
...         if dice <= 2:
...             step = max(0, step - 1)
...         elif dice <= 5:
...             step = step + 1
...         else:
...             step = step + np.random.randint(1,7)
...         if np.random.rand() <= 0.001 :
...             step = 0
...         random_walk.append(step)
...     all_walks.append(random_walk)
... 
... # Create and plot np_aw_t
... np_aw_t = np.transpose(np.array(all_walks))
... 
... # Select last row from np_aw_t: ends
... ends = np_aw_t[-1,:]
... 
... # Plot histogram of ends, display plot
... plt.hist(ends)
... plt.show()

In [2]: ends.shape
Out[2]: (1000,)

In [3]: ends[5,:]

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    ends[5,:]
IndexError: too many indices for array


In [4]: ends[5]
Out[4]: 49

In [5]: ends[0]
Out[5]: 70

In [6]: ends[0:10]
Out[6]: array([ 70,  94,  82,  66, 107,  49,  72, 116,  65,  78])

In [7]: test = ends > 60

In [8]: test[0:10]
Out[8]: array([ True,  True,  True,  True,  True, False,  True,  True,  True,  True], dtype=bool)

In [9]: test2 = ends[test]

In [10]: test3=len(test2)

In [11]: test3
Out[11]: 769

In [12]: 769/1000
Out[12]: 0.769

In [13]: odds >= 0.769

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    odds >= 0.769
NameError: name 'odds' is not defined


In [14]: odds = 0.769

In [15]: test = ends >= 60

In [16]: test2 = ends[test]

In [17]: test3=len(test2)

In [18]: test3
Out[18]: 788
"""