""" 
01/2017
Dataquest : Data Analyst Path 
Step 1: Introduction To Python
SubStep : Python Programming Intermediate : Modules
"""



"""
1: Introduction To The NFL Data Set
For this mission, we'll be working with a data set that contains the results of National Football League (NFL) games. It includes every game of every season from 2009-2013.

Each row in our data set represents a game. The first column is for the year it took place, and the second is for the week of the season (out of 17 total weeks). The third column records the winning team, and the fourth records the losing team.

Here's a preview of the data:

The first row is for a game between the Steelers and the Titans. It took place during the first week of the 2009 season, and the Steelers won.
"""



"""
2: Introduction To Modules
A module is a collection of functions and variables that have been bundled together in one file. Modules serve three primary purposes:

Using small modules can help organize larger applications.
Bundling useful logic into modules helps programmers share code with one another more easily.
Using someone else's pre-written code can save you the trouble of having to write tedious code yourself.
Python comes with countless modules that programmers can use. To access a module, we import it using Python's import statement.


import my_module
By importing my_module, we're indicating that we want to use some of the functions or variables from a pre-existing file called my_module.py. (The Python interpreter already knows where to look for module files on your machine.) Note that the name of the module is the same as the name of the Python file, but without the extension. Once we import a module, we can access its functions and variables using dot notation (a period).


my_module.some_function()
In the code above, we call some_function(), which we know exists within my_module. Behind the scenes, my_module is stored as a module object, with methods and properties attached to it. For now, all you need to know is that we can access functions within a module using a period.

In this mission, we'll be using some of the modules from the Python Standard Library.

The Standard Library is a vast collection of useful tools that comes with the Python language. It contains a number of modules that you can easily import into your code.
"""



"""
3: The Math Module
Modules are usually organized around a theme. In later missions, for example, we'll use modules organized around themes like statistical analysis or data visualization. On this screen, we'll be working with modules that specialize in mathematical operations and manipulating CSV files.

The math module has utility functions for performing certain mathematical operations. You can read the documentation for the math module if you'd like.

The sqrt() function inside the module takes a number as an argument, and returns the square root of that number. math.sqrt(4.0) would evaluate to 2.0, for example. The ceil() function returns the smallest integer that's greater than or equal to the input. In other words, it rounds the input up. The floor() function returns the largest integer that's less than or equal to the input. In other words, it rounds down.

Instructions
Use the sqrt() function within the math module to assign the square root of 16.0 to a.
Use the ceil() function within the math module to assign the ceiling of 111.3 to b.
Use the floor() function within the math module to assign the floor of 89.9 to c.
"""
import math
a = math.sqrt(16)
b = math.ceil(111.3)
c = math.floor(89.9)
print(a)
print(b)
print(c)
""" Console output or Results
Output
4.0
112
89
"""




"""
4: Variables Within Modules
So far, we've only worked with the functions defined within modules. Now, let's explore how to use the variables defined within modules. We access a module's variables with dot notation, just like we do with functions.


import my_module
print(my_module.some_value)
The code above prints some_value, which is a variable defined in my_module.

The math module defines mathematical constants such as pi. This makes it easier to perform computations. Since these are variables within math, we can access them with dot notation.

Instructions
Assign the square root of pi to a.
Assign the ceiling of pi to b.
Assign the floor of pi to c.
"""
import math

print(math.pi)
a = math.sqrt(math.pi)
b = math.ceil(math.pi)
c = math.floor(math.pi)
print(a)
print(b)
print(c)
""" Console output or Results
Output
3.141592653589793
1.7724538509055159
4
3
"""



"""
5: The CSV Module
In previous missions, we learned how to work with CSV files by:

Opening a file
Reading the contents of that file into a string
Splitting the string on the newline character
Splitting each line on the comma character
We can work with CSV files more easily through the csv module. This module has a reader() function that takes a file object as its argument, and returns an object that represents our data. We'll cover objects in more depth in the next mission, but for now, we'll simply convert this object to a list and use that result.

To read data from a file called "my_data.csv", we first import the csv module:


import csv
Next, we open the file:


f = open("my_data.csv")
Then, we call the module's reader() function:


csvreader = csv.reader(f)
Finally, we convert the result to a list:


my_data = list(csvreader)
Instructions
Read all of the data from "nfl.csv" into a list variable named nfl using the csv module.
"""
import csv
nfl = list(csv.reader(open("nfl.csv")))
print(nfl[:5])
""" Console output or Results
Output
[['2009', '1', 'Pittsburgh Steelers', 'Tennessee Titans'], 
['2009', '1', 'Minnesota Vikings', 'Cleveland Browns'], 
['2009', '1', 'New York Giants', 'Washington Redskins'], 
['2009', '1', 'San Francisco 49ers', 'Arizona Cardinals'],
['2009', '1', 'Seattle Seahawks', 'St. Louis Rams']]
"""



"""
6: Counting How Many Times A Team Won
Now that we have a list representation of the file's contents, we can start analyzing the data. We'll begin by counting up the wins for a particular team.

Instructions
In the following cell, add code that:
Imports and uses the csv module to load data from our "nfl.csv" file
Counts how many games the "New England Patriots" won from 2009-2013
To do this, set a counter to 0 and increment by 1 for each row that has "New England Patriots" in the winner column
Assigns the count to patriots_wins
"""
import csv
nfl = list(csv.reader(open("nfl.csv")))
cpt = 0
for row in nfl:
    if row[2] == "New England Patriots":
        cpt+=1
print(cpt)
patriots_wins = cpt
""" Console output or Results
Output
61
"""




"""
7: Making A Function That Counts Wins
Let's write a function that counts the wins for any NFL team. Recall that we define a function in the following format:


def my_func(input):
    ...
    return output
The def keyword signals that we're defining a function named my_func, which takes input as a parameter. The function performs a computation, probably using input somewhere along the way, to generate output. Finally, it returns output to the code that called the function.

Instructions
Write a function called nfl_wins that takes a team name as input.
The function should return the number of games the team won in the period covered by the data set.
Use the function to assign the number of "Dallas Cowboys" wins to cowboys_wins.
Use the function to assign the number of "Atlanta Falcons" wins to falcons_wins.
 Need a hint?
"""
import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here.
def nfl_wins(team):
    cpt = 0
    for row in nfl:
        if row[2] == team:
            cpt+=1
    patriots_wins = cpt
    return patriots_wins

cowboys_wins = nfl_wins("Dallas Cowboys")
falcons_wins = nfl_wins("Atlanta Falcons")
print(cowboys_wins)
print(falcons_wins)
""" Console output or Results
Output
41
49
"""




"""
8: A Brief Note About Booleans
You may remember from previous missions that a Boolean expression evaluates to either True or False. If we have the following variables:


a = 5
b = 10
then a == 5 would be True, and b == 5 would be False. So far, we've only used comparison operators (such as == and >) to produce Boolean values, but we can also use Boolean operators.

A good example of a Boolean operator is the and operator, which tests whether all conditions are True. a == 5 and b == 10 would be True, since both of the statements joined by the and operator are True. a == 5 and b == 5 would be False, since b == 5 is False. The and operator will only evaluate to True when all of the conditions we specify are True.

The following truth table describes all possible values for two hypothetical Boolean variables, A and B, as well as the corresponding value of the Boolean expression A and B.

A		B		A and B
False  False   False
False  True    False
True   False   False
True   True    True

"""





"""
9: The Or Keyword
The or operator tests whether any of the given statements are true. So, a == 10 or b == 10 would be True, since at least one of those statements is True. a == 10 or b == 5 is False, since neither of the statements are True.

The following truth table describes all possible values for two Boolean variables, A and B, as well as the corresponding value of the expression A or B.

A		B		A or B
False  False   False
False  True    True
True   False   True
True   True    True

"""





"""
10: Working With Boolean Operators
Now that we have a handle on Boolean operators, let's practice working with them.

Instructions
There are several Boolean expressions and comments in the following code cell. Enter True or False below each one to indicate what the expression will evaluate as.
For instance, if you think the first expression is True, assign True to result1.
"""
a = 5
b = 10
# a == 5
result1 = True

# a < 5 or b > a
result2 = True

# a < 5 and b > a
result3 = False

# a == 5 or b == 5
result4 = True

# a > b or a == 10
result5 = False






"""
11: Counting Wins In A Given Year
Let's make a function that counts the number of victories a given team won during a particular year. To do this, we'll loop through our data and check for rows that meet both of our "win" criteria: (1) the win must be for the given team, and (2) it must have occurred during the year we specify. We can use Boolean operators to accomplish this.

Instructions
Modify the nfl_wins function so that it takes two string inputs: (1) a team name, and (2) a year.
Name this new function nfl_wins_in_a_year.
Your function should output the number of victories the team won in the given year (as an integer).
Use the and operator to combine Booleans. For each row in the data set, check whether the desired team won, and whether the game took place during the correct year.
Use your function to assign the number of games the "Cleveland Browns" won in "2010" to browns_2010_wins.
Use your function to assign the number of games the "Philadelphia Eagles" won in "2011" to eagles_2011_wins.
"""
import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

def nfl_wins_in_a_year(team,year):
    count = 0
    for row in nfl:
        if row[2] == team and row[0] == year :
            count = count + 1
    return count

browns_2010_wins = nfl_wins_in_a_year("Cleveland Browns","2010")
eagles_2011_wins = nfl_wins_in_a_year("Philadelphia Eagles","2011")
print(browns_2010_wins)
print(eagles_2011_wins)
""" Console output or Results
Output
5
8
"""




"""
12: Sharing Modules
The Standard Library doesn't contain all Python modules. Python users create many of them independently, and then make them available online so other developers can benefit from them. If you want to use these modules, you'll need to download them from the Web before importing them into your code. Tools like Anaconda come with install utilities that make it easy to download popular online modules.

To use a module you wrote yourself, you'll need to save it to your machine in the location designated for Python module files. Suppose you write a module containing functions that perform some simple data analysis. You may find that it's quite useful, and decide to publish it so others can download and use it.

Developers publish and download modules all the time. This spirit of sharing is core to programming, and helps foster a community of individuals and corporations that work toward the common goal of advancing technology.

Modules are one of several tools designed to organize code and make common tasks easier. In the next mission, we'll learn about classes, another language construct that can streamline and organize our code.
"""