"""
02/2017
Dataquest : Data Analyst Path
Step 1: Introduction To Python
SubStep : Python Programming Intermediate : List Comprehensions
"""


"""
1: The Data Set
In the previous mission, we worked with legislators.csv, which contains information on every person who has served in the U.S. Congress.
We cleaned up some missing data and added a column for birth year.

We'll continue to work with the same data set in this mission. Here's a preview of it in CSV format:


last_name,first_name,birthday,gender,type,state,party,birth_year
Bassett,Richard,1745-04-02,M,sen,DE,Anti-Administration,1745
Bland,Theodorick,1742-03-21,M,rep,VA,1742
Burke,Aedanus,1743-06-16,M,rep,SC,1743
Carroll,Daniel,1730-07-22,M,rep,MD,1730
The data set includes the following columns:

last_name -- The legislator's last name
first_name -- The legislator's first name
birthday -- the legislator's birthday
gender -- The legislator's gender
type -- The chamber in which the legislator served - either Senate (sen) or House of Representatives (rep)
state -- The state the legislator represents
party -- The legislator's party affiliation
birth_year -- integer values for the year the legislator was born
In this mission, we'll use the data to find the most common names among U.S. legislators of each gender.
Before diving into this, we'll explore some critical concepts, such as enumeration.
"""


"""
2: Enumerate
There are many situations where we'll need to iterate over multiple lists in tandem, such as this one:


animals = ["Dog", "Tiger", "SuperLion", "Cow", "Panda"]
viciousness = [1, 5, 10, 10, 1]
​
for animal in animals:
    print("Animal")
    print(animal)
    print("Viciousness")
In the example above, we have two lists. The second list describes the viciousness of the animals in the first list. A Dog has a viciousness level of 1, and a SuperLion has a viciousness level of 10. We want to retrieve the position of the item in animals the loop is currently on, so we can use it to look up the corresponding value in the viciousness list.

Unfortunately, we can't just loop through animals, and then tap into the second list.
Python has an enumerate() function that can help us with this, though. The enumerate() function allows us to have two variables in the body of a for loop -- an index, and the value.


for i, animal in enumerate(animals):
    print("Animal Index")  ## label
    print(i)
    print("Animal") ## label
    print(animal)
Here's a diagram of the Python logic that takes place when the code runs:

see img1.png

On every iteration of the loop, the value for i will become the value of the index in animals that corresponds to that iteration. animal will take on the value in animals that corresponds to the index i.

Here's another example of how we can use the enumerate() function to iterate over multiple lists in tandem:


animals = ["Dog", "Tiger", "SuperLion", "Cow", "Panda"]
viciousness = [1, 5, 10, 10, 1]
​
for i, animal in enumerate(animals):
    print("Animal")
    print(animal)
    print("Viciousness")
    print(viciousness[i])
In this example, we use the index variable i to index the viciousness list, and print the viciousness value that corresponds to the same index in animals.

Instructions
Enumerate the ships list using a for loop and the enumerate() function.
For each iteration of the loop:
Print the item from ships at the current index.
Print the item from cars at the current index.
"""
ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]
for i, list in enumerate(ships):
    print(list)
    print(cars[i])
    print("---------------")
""" Console Output or Results
Output
Andrea Doria
Ford Edsel
---------------
Titanic
Ford Pinto
---------------
Lusitania
Yugo
---------------
"""



"""
3: Adding Columns
We can even use the enumerate() function to add columns to lists of lists. For example, here's some starter code:


door_count = [4, 4]
cars = [
        ["black", "honda", "accord"],
        ["red", "toyota", "corolla"]
       ]
We can add a column to cars by appending a value to each inner list:


for i, car in enumerate(cars):
    car.append(door_count[i])
In the code above, we:

Use the enumerate() function to loop across each item in cars.
Find the corresponding value in door_count that has the index i (the same index as the current item in cars).
Add the value in door_count with index i to car.
After the code runs, each row in cars will have a door_count column.
Let's reinforce what we've learned by completing an exercise.

Instructions
Loop through each row in things using the enumerate() function.
Append the item in trees that has the same index (as the current thing) to the end of each row in things.
After the code runs, things should have an extra column.
"""
things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]
for i, row in enumerate(things):
    row.append(trees[i])
print(things)
""" Console Output or Results
Output
[['apple', 'monkey', 'cedar'],
['orange', 'dog', 'maple'],
['banana', 'cat', 'fig']]
"""



"""
4: List Comprehensions
We've written many short for loops to manipulate lists. Here's an example:


animals = ["Dog", "Tiger", "SuperLion", "Cow", "Panda"]
​
animal_lengths = []
for animal in animals:
    animal_lengths.append(len(animal))
It takes three lines to calculate the length of each string animals this way. However, we can condense this down to one line with a list comprehension:


animal_lengths = [len(animal) for animal in animals]
This comprehension consists of the list operation len(animal), the loop variable animal, and the list that we're iterating over, animals.

The diagram below visualizes how a list comprehension condenses a for loop:

see img2.png

Logically, the list comprehension:

Loops through each element in the animals list and assigns the current element to animal
Finds the length of each animal string
Generates a new list that contains all of the lengths as elements
Assigns the new list to animal_lengths
List comprehensions are much more compact notation, and can save space when you need to write multiple for loops.

Instructions
Use a list comprehension to create a new list called apple_prices_doubled, where you multiply each item in apple_prices by 2.
Use another list comprehension to create a new list called apple_prices_lowered, where you subtract 100 from each item in apple_prices.

"""
apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [ prices*2 for prices in apple_prices ]
apple_prices_lowered = [ prices-100 for prices in apple_prices ]
print(apple_prices)
print("-------------")
print(apple_prices_doubled)
print("-------------")
print(apple_prices_lowered)
""" Console Output or Results
Output
[100, 101, 102, 105]
-------------
[200, 202, 204, 210]
-------------
[0, 1, 2, 5]
"""



"""
5: Counting Female Names
Let's count how many times each female first name occurs in legislators. To limit our count to names from the modern era, we'll only look at those that appear after 1940. While names like Theodorick were common prior to 1940, they're rare today.

Here's a preview of what this dictionary will look like:


{
    'Nancy': 1,
    'Sandy': 1,
    'Carolyn': 1,
    'Melissa': 2,
    'Jo Ann': 2,
    ...
}
Now, let's work on creating it!

Instructions
Create an empty dictionary called name_counts.
Loop through each row in legislators.
If the gender column of the row equals F and the year column is greater than 1940:
Assign the first_name column of the row to the variable name.
If name is in name_counts:
Add 1 to the value associated with name in name_counts.
If name isn't in name_counts:
Set the value associated with name in name_counts to 1.
When the loop finishes, name_counts should contain each unique name in the first_name column of legislators as a key, and the corresponding number of times it appeared as the value.

"""
name_counts = {}
for row in legislators:
    if row[3] == "F" and row[7] > 1940:
        name = row[1]
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

print(name_counts)
""" Console Output or Results
utput
{'Marilyn': 1, 'Heather': 1, 'Barbara': 1, 'Karen': 2, 'Virginia': 1, 'Hilda': 1, 'Ann Marie': 1, 'Betty': 1, 'Sue': 1, 'Hillary': 1, 'Betsy': 1, 'Anne': 1, 'Nan': 1, 'Enid': 1, 'Carolyn': 1, 'Thelma': 1, 'Suzanne': 1, 'Cynthia': 1, 'Melissa': 2, 'Jean': 1, 'Jo Ann': 2, 'Katherine': 1, 'Lynn': 1, 'Deborah': 2, 'Gabrielle': 1, 'Mary': 2, 'Jane': 1, 'Sandy': 1, 'Kathleen': 2, 'Blanche': 1, 'Shelley': 2, 'Kay': 1, 'Denise': 1, 'Mary Jo': 1, 'Nancy': 1, 'Laura': 1, 'Ellen': 1, 'Olympia': 1, 'Jennifer': 1, 'Stephanie': 2}
"""



"""
6: None
Let's say we're trying to find the maximum value in a list. We might write some code that looks like this:


values = [50, 80, 100]
max_value = 0
for i in values:
    if i > max_value:
        max_value = i
We set max_value to a low value so that everything's greater than it. But what if we changed the values list slightly?


values = [-50, -80, -100]
max_value = 0
for i in values:
    if i > max_value:
        max_value = i
In the above scenario, max_value is 0 when the loop finishes. This is wrong, because 0 isn't in values; it's just a placeholder we used to initialize max_value.

We can resolve this kind of issue using the None object, which has a special data type called NoneType.

The None object indicates that the variable has no value. Rather than using the normal double equals sign (==) to check whether a value equals None, we use the variable is None syntax.

The is comparison operator checks for object equality. Using is instead of == prevents some custom classes from resolving to True when compared with None. We'll explore how to use operators with the None object in greater depth during a later mission. For now, let's see what the variable is None syntax looks like:


values = [-50, -80, -100]
max_value = None
for i in values:
    if max_value is None or i > max_value:
        max_value = i
In the example above, we:

Initialize max_value to None.
Loop through each item in values.
Check whether max_value equals None using the max_value is None syntax.
If max_value equals None, or if i > max_value, then we assign the value of i to max_value.
At the end of the loop, max_value will equal -50, which is the largest value in values.
"""




"""
7: Comparing With None
Comparing a value to None will usually generate an error.
This is actually helpful when we're writing code, because it prevents unexpected variables from being None.
For example, this code will cause an error:


a = None
a > 10
Therefore, when a value could potentially be None, and we want to compare it to another value, we should always include code that checks whether it actually is None first.

We can use two Boolean statements joined by or to do this. Here's an example:

max_value is None or i > max_value

The Python interpreter will evaluate the two statements in order.
If the first statement is True, it won't evaluate the second one.
This saves time, since when one statement is True, the whole or conditional is True.

The following code will assign True to b if a is None, or if a is greater than 10:


a = None
b = a is None or a > 10
The same logic applies to an and statement.
Because both conditions have to be True, if the first one is False, the Python interpreter won't evaluate the second one.
The example below shows how to write an and statement involving None that won't return an error.
It will assign True to b if a does not equal None and a is greater than 10:


a = None
b = a is not None and a > 10
Let's give this a try in our next exercise!

Instructions
Loop through each value in values.
Check whether the value is not None, and if it's greater than 30.
Append the result of the check to checks.
When finished, checks should be a list of Booleans indicating whether or not the corresponding items in values are not None and greater than 30.
"""
values = [None, 10, 20, 30, None, 50]
checks = []
for value in values:
    checks.append(value is not None and value > 30)

print(checks)
""" Console Output or Results
Output
[False, False, False, False, False, True]
"""



"""
8: Highest Female Name Count
name_counts is a dictionary where the keys are female first names from legislators, and the values are the number of times the names occured after 1940.

In order to extract the most common names from this dictionary, we need to determine the highest totals in name_counts. Once we know the totals, we can find the keys for them.

We can iterate through all of the keys in a dictionary like this:


fruits = {
        "apple": 2,
        "orange": 5,
        "melon": 10
    }
​
for fruit in fruits:
    rating = fruits[fruit]
In the loop above, we iterate through each key in fruits. We can access the corresponding value using fruits[fruit].

Let's identify the highest totals in the next exercise.

Instructions
Set max_value to None.
Loop through the keys in name_counts.
Assign the value associated with the key to count.
If max_value is None, or count is greater than max_value:
Assign count to max_value.
At the end of the loop, max_value will contain the largest value in name_counts.
"""
max_value = None
for keys, value in name_counts.items():
    count = value
    if max_value is None or count > max_value:
        max_value = count
print(max_value)
print(name_counts)
""" Console Output or Results
Output
2
------------
{'Marilyn': 1, 'Heather': 1, 'Barbara': 1, 'Karen': 2, 'Thelma': 1, 'Virginia': 1, 'Hilda': 1, 'Jean': 1, 'Sue': 1, 'Betty': 1, 'Stephanie': 2, 'Anne': 1, 'Nan': 1, 'Enid': 1, 'Carolyn': 1, 'Mary': 2, 'Suzanne': 1, 'Laura': 1, 'Cynthia': 1, 'Melissa': 2, 'Blanche': 1, 'Jo Ann': 2, 'Kay': 1, 'Lynn': 1, 'Deborah': 2, 'Gabrielle': 1, 'Jane': 1, 'Sandy': 1, 'Kathleen': 2, 'Hillary': 1, 'Shelley': 2, 'Katherine': 1, 'Denise': 1, 'Betsy': 1, 'Nancy': 1, 'Ann Marie': 1, 'Ellen': 1, 'Olympia': 1, 'Jennifer': 1, 'Mary Jo': 1}
"""



"""
9: The Items Method
The code we used on the previous screen to access the keys and values in a dictionary was slightly awkward. We can simplify this process with the items() method, which allows us to iterate through keys and values at the same time.


fruits = {
    "apple": 2,
    "orange": 5,
    "melon": 10
}
​
for fruit, rating in fruits.items():
    print(rating)
The items() method makes our code clearer and more compact.

Instructions
Use the items() method to iterate through the keys and values in plant_types.
Print each key in plant_types.
Print each value in plant_types.
"""
plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for keys, value in plant_types.items():
    print("%keys)
    print(value)
""" Console Output or Results
Output
maple
tree
orchid
flower
cedar
tree
"""



"""
10: Finding The Most Common Female Names
As we learned on a previous screen, the most common female names occur two times in name_counts.
Therefore, we want to extract any keys in name_counts that have the value 2.

Instructions
Loop through the keys in name_counts.
If any value in name_counts equals 2, append its key to top_female_names.
When you're finished, top_female_names will be a list of the most common names of female legislators.
"""
top_female_names = []
for keys,value in name_counts.items():
    if value == 2:
        top_female_names.append(keys)
print(top_female_names)
""" Console Output or Results
Output
['Karen', 'Stephanie', 'Mary', 'Melissa', 'Jo Ann', 'Deborah', 'Kathleen', 'Shelley']
"""



"""
11: Finding The Most Common Male Names
Now that we know how to find the most common female names, we can repeat the same process for male names.

Instructions
Create a dictionary called male_name_counts.
Loop through legislators.
Count how many times each name with "M" in the gender column and a birth year after 1940 occurs.
Store the results in male_name_counts.
Find the highest value in male_name_counts and assign it to highest_male_count.
Append any keys from male_name_counts with a value equal to highest_male_count to top_male_names.
"""
male_name_counts = {}
for row in legislators:
    if row[3] == "M" and row[7] > 1940:
        name = row[1]
        if name in male_name_counts:
            male_name_counts[name] += 1
        else:
            male_name_counts[name] = 1

print(male_name_counts)
print("--------------------")

highest_male_count =  None
for keys, value in male_name_counts.items():
    count = value
    if highest_male_count is None or count > highest_male_count:
        highest_male_count = count

print(highest_male_count)
print("--------------------")

top_male_names = []
for keys,value in male_name_counts.items():
    if value == highest_male_count:
        top_male_names.append(keys)
print(top_male_names)
""" Console Output or Results
Output
{'Larry': 5, 'Eric': 3, 'George': 6, 'Francisco': 1, 'Lincoln': 3, 'Kendrick': 1, 'Kent': 2, 'Barack': 1, 'Gregory': 1, 'Michael': 20, 'Adam': 1, 'Jon': 6, 'Walter': 3, 'Larkin': 1, 'Charles': 17, 'Gary': 3, 'Rahm': 1, 'C.L.': 1, 'Elizabeth': 1, 'Clifford': 1, 'Zach': 1, 'Gerald': 3, 'Trey': 1, 'Brad': 2, 'Carl': 1, 'Huey': 1, 'Ronald': 2, 'Philip': 2, 'Steven': 5, 'Ron': 3, 'David': 24, 'Calvin': 1, 'Byron': 1, 'Virgil': 1, 'Joseph': 5, 'Lewis': 1, 'Jo': 1, 'Paul': 6, 'Glenn': 2, 'Howard': 1, 'Aníbal': 1, 'James': 31, 'L.': 1, 'Henry': 2, 'Bob': 10, 'Merrill': 1, 'Earl': 3, 'Tommy': 1, 'Tony': 1, 'Thaddeus': 1, 'H.': 2, 'Bruce': 2, 'Andrea': 1, 'Artur': 1, 'Harry': 2, 'Russ': 1, 'Dirk': 1, 'W.': 2, 'Mike': 2, 'William': 21, 'Asa': 1, 'Connie': 1, 'Lawrence': 1, 'Newton': 1, 'Martin': 3, 'Judd': 1, 'Mark': 9, 'Anthony': 3, 'Travis': 1, 'Tim': 3, 'Harley': 1, 'Phil': 2, 'Jonas': 1, 'Myron': 1, 'J.': 3, 'Jesse': 1, 'Samuel': 2, 'Max': 3, 'Preston': 1, 'Jerry': 1, 'Todd': 2, 'Robert': 24, 'Richard': 9, 'Linda': 1, 'R.': 1, 'Les': 1, 'Douglas': 1, 'Greg': 1, 'Kenny': 1, 'Harold': 3, 'Duncan': 1, 'Christopher': 6, 'Vito': 1, 'Daniel': 4, 'Dennis': 6, 'Ted': 1, 'Kenneth': 1, 'Luis': 1, 'Brian': 4, 'Heath': 1, 'Scott': 4, 'Elton': 1, 'Clete': 1, 'Russell': 1, 'Ben': 4, 'Eldon': 1, 'Rod': 2, 'Ciro': 1, 'Norm': 1, 'Geoff': 1, 'Edward': 3, 'Gene': 1, 'J.C.': 1, 'Alan': 3, 'Frederick': 2, 'Melvin': 1, 'Nathan': 1, 'Gilbert': 1, 'Jeffrey': 1, 'Ken': 2, 'Jay': 2, 'Rick': 4, 'Cleo': 1, 'Donald': 4, 'Mendel': 1, 'Carte': 1, 'Ray': 1, 'Chester': 1, 'Joe': 4, 'Doug': 1, 'Allen': 2, 'Jill': 1, 'Karan': 1, 'Ric': 1, 'Felix': 1, 'Rodney': 2, 'Baron': 1, 'Sam': 1, 'Parker': 1, 'Lyle': 1, 'Fred': 2, 'Zachary': 1, 'Clyde': 1, 'Trent': 1, 'Bobby': 2, 'Barton': 1, 'Nicholas': 1, 'John': 35, 'Jim': 6, 'Craig': 2, 'Victor': 3, 'Floyd': 1, 'Robin': 1, 'Jeff': 2, 'Jaime': 1, 'Wayne': 2, 'Royden': 1, 'Peter': 9, 'Anh': 1, 'Tillie': 1, 'Patrick': 3, 'Evan': 1, 'Stephen': 1, 'Dick': 1, 'Thomas': 18, 'Jeb': 1, 'Randall': 1, 'Van': 1, 'Chip': 1, 'Leslie': 1, 'Steve': 4, 'Gordon': 1, 'Kweisi': 1, 'Tom': 2, 'Hansen': 1, 'Frank': 6, 'Billy': 1, 'Sheila': 1, 'Don': 1, 'Carol': 1, 'Spencer': 1, 'Susan': 1, 'Mel': 2, 'Timothy': 3, 'Bill': 3, 'Meldon': 1, 'Terry': 1, 'Raymond': 2, 'Chris': 2, 'Ronnie': 1, 'Lane': 1, 'Ed': 2, 'Jack': 2, 'Marjorie': 1, 'Lynn': 1, 'Dan': 3, 'Claudine': 1, 'Albert': 3, 'Jason': 1, 'Silvestre': 1, 'Milton': 1, 'C.': 1, 'Dean': 1, 'Bart': 1, 'Vincent': 1, 'Ernest': 2, 'Randy': 1}
--------------------
35
--------------------
['John']
"""
