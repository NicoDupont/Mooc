# partie 5.2
# A Day at the Supermarket


"""
BeFOR We Begin
Before we begin our exercise, we should go over the Python for loop one more time. For now, we are only going to go over the for loop in terms of how it relates to lists and dictionaries. We'll explain more cool for loop uses in later courses.

for loops allow us to iterate through all of the elements in a list from the left-most (or zeroth element) to the right-most element. A sample loop would be structured as follows:

a = ["List of some sort”]
for x in a: 
    # Do something for every x
This loop will run all of the code in the indented block under the for x in a: statement. The item in the list that is currently being evaluated will be x. So running the following:

for item in [1, 3, 21]: 
    print item
would print 1, then 3, and then 21. The variable between for and in can be set to any variable name (currently item), but you should be careful to avoid using the word “list” as a variable, since that's a reserved word (that is, it means something special) in the Python language.

Instructions
Use a for loop to print out all of the elements in the list names.
"""

names = ["Adam","Alex","Mariah","Martine","Columbus"]
for names in names:
    print names
	
""" sortie :
Adam
Alex
Mariah
Martine
Columbus
"""

"""
This is KEY!
You can also use a for loop on a dictionary to loop through its keys with the following:

# A simple dictionary
d = {"foo" : "bar"}

for key in d: 
    print d[key]  # prints "bar" 
Note that dictionaries are unordered, meaning that any time you loop through a dictionary, you will go through every key, but you are not guaranteed to get them in any particular order.

Instructions
Use a for loop to go through the webster dictionary and print out all of the definitions.
"""

webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for xkey in webster:
    print webster[xkey]
	
	
""" sortie :
A star of a popular children's cartoon show.
Goes on the floor.
A small amount.
The sound a goat makes.
"""


"""
Control Flow and Looping
The blocks of code in a for loop can be as big or as small as they need to be.

While looping, you may want to perform different actions depending on the particular item in the list.

numbers = [1, 3, 4, 7]
for number in numbers: 
    if number > 6:
        print number
print "We printed 7."
In the above example, we create a list with 4 numbers in it.
Then we loop through the numbers list and store each item in the list in the variable number.
On each loop, if number is greater than 6, we print it out. So, we print 7.
Finally, we print out a sentence.
Make sure to keep track of your indentation or you may get confused!

Instructions
Like step 2 above, loop through each item in the list called a.
Like step 3 above, if the number is even, print it out. You can test if the item % 2 == 0 to help you out.
"""


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for x in a:
    if x % 2 == 0:
        print x


		
""" sortie :
0
2
4
6
8
10
12
"""


"""
Lists + Functions
Functions can also take lists as inputs and perform various operations on those lists.

def count_small(numbers):
    total = 0
    for n in numbers:
        if n < 10:
            total = total + 1
    return total

lost = [4, 8, 15, 16, 23, 42]
small = count_small(lost)
print small
In the above example, we define a function count_small that has one argument, numbers.
We initialize a variable total that we can use in the for loop.
For each item n in numbers, if n is less than 10, we increment total.
After the for loop, we return total.
After the function definition, we create an array of numbers called lost.
We call the count_small function, pass in lost, and store the returned result in small.
Finally, we print out the returned result, which is 2 since only 4 and 8 are less than 10.
Instructions
Write a function that counts how many times the string "fizz" appears in a list.

Write a function called fizz_count that takes a list x as input.
Create a variable count to hold the ongoing count. Initialize it to zero.
for each item in x:, if that item is equal to the string "fizz" then increment the count variable.
After the loop, please return the count variable.
For example, fizz_count(["fizz","cat","fizz"]) should return 2.
"""

# Write your function below!
def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count += 1
            
    return count

fizz_count(["fizz","cat","fizz"])



"""
String Looping
As we've mentioned, strings are like lists with characters as elements. You can loop through strings the same way you loop through lists! While we won't ask you to do that in this section, we've put an example in the editor of how looping through a string might work.

Instructions
Run the code to see string iteration in action!
"""

for letter in "Codecademy":
    print letter
    
# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter
		

""" sortie :
C
o
d
e
c
a
d
e
m
y


i
i
"""



"""
Your Own Store!
Okay—on to the core of our project.

Congratulations! You are now the proud owner of your very own Codecademy brand supermarket.

animal_counts = {
    "ant": 3,
    "bear": 6,
    "crow": 2
}
In the example above, we create a new dictionary called animal_counts with three entries. One of the entries has the key "ant" and the value 3.

Instructions
Create a new dictionary called prices using {} format like the example above.
Put these values in your prices dictionary, in between the {}:
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
Yeah, this place is really expensive. (Your supermarket subsidizes the zoo from the last course.)
"""

prices = {}
prices["banana"] = 4
prices["apple"] = 2
prices["orange"] = 1.5
prices["pear"] = 3



"""
Investing in Stock
Good work! As a store manager, you’re also in charge of keeping track of your stock/inventory.

Instructions
Create a stock dictionary with the values below.

"banana": 6
"apple": 0
"orange": 32
"pear": 15
"""

prices = {}
prices["banana"] = 4
prices["apple"] = 2
prices["orange"] = 1.5
prices["pear"] = 3

stock = {}
stock["banana"] = 6
stock["apple"] = 0
stock["orange"] = 32
stock["pear"] = 15



"""
Keeping Track of the Produce
Now that you have all of your product info, you should print out all of your inventory information.

once  = {'a': 1, 'b': 2}
twice = {'a': 2, 'b': 4}
for key in once:
    print "Once: %s" % once[key]
    print "Twice: %s" % twice[key]
In the above example, we create two dictionaries, once and twice, that have the same keys.
Because we know that they have the same keys, we can loop through one dictionary and print values from both once and twice.
Instructions
Loop through each key in prices.
Like the example above, for each key, print out the key along with its price and stock information. Print the answer in the following format:
apple
price: 2
stock: 0
Like the example above, because you know that the prices and stock dictionary have the same keys, you can access the stock dictionary while you are looping through prices.

When you're printing, you can use the syntax from the example above.
"""


prices = {}
prices["banana"] = 4
prices["apple"] = 2
prices["orange"] = 1.5
prices["pear"] = 3

stock = {}
stock["banana"] = 6
stock["apple"] = 0
stock["orange"] = 32
stock["pear"] = 15

for x in prices:
    print x
    print "price: %s" % prices[x] 
    print "stock: %s" % stock[x] 
	
	

""" sortie :
orange
price: 1.5
stock: 32
pear
price: 3
stock: 15
banana
price: 4
stock: 6
apple
price: 2
stock: 0
"""




"""
Something of Value
For paperwork and accounting purposes, let's record the total value of your inventory. It's nice to know what we're worth!

Instructions
Let's determine how much money you would make if you sold all of your food.

Create a variable called total and set it to zero.
Loop through the prices dictionaries.
For each key in prices, multiply the number in prices by the number in stock. Print that value into the console and then add it to total.
Finally, outside your loop, print total.
"""


prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]

total = 0
for x in prices:
    total += prices[x] * stock[x]
    print total

print total

""" sortie :
orange
price: 1.5
stock: 32
pear
price: 3
stock: 15
banana
price: 4
stock: 6
apple
price: 2
stock: 0
48.0
93.0
117.0
117.0
117.0
"""




"""
Shopping at the Market
Great work! Now we're going to take a step back from the management side and take a look through the eyes of the shopper.

In order for customers to order online, we are going to have to make a consumer interface. Don't worry: it's easier than it sounds!

Instructions
First, make a list called groceries with the values "banana","orange", and "apple".
"""
groceries = ["banana","orange","apple"]


"""
Making a Purchase
Good! Now you're going to need to know how much you’re paying for all of the items on your grocery list.

def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
n = [1, 2, 5, 10, 13]
print sum(n)
In the above example, we first define a function called sum with an argument numbers.
We initialize the variable total that we will use as our running sum.
For each number in the list, we add that number to the running sum total.
At the end of the function, we return the running sum.
After the function, we create, n, a list of numbers.
Finally, we call the sum(numbers) function with the variable n and print the result.
Instructions
Define a function compute_bill that takes one argument food as input.
In the function, create a variable total with an initial value of zero.
For each item in the food list, add the price of that item to total.
Finally, return the total.
Ignore whether or not the item you're billing for is in stock.

Note that your function should work for any food list.
"""


shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    prix = 0
    nb = 0
    for item in food:
        for price in prices:
            if item == price:
                prix = prices[price]
        for qt in stock:
            if item == qt:
                nb = stock[qt]
        #print nb
        #print prix
        #prix *= nb
        #print prix
        total += prix
        print total
    
    return total

compute_bill(["banana"])

# sortie : 4



"""
Stocking Out
Now you need your compute_bill function to take the stock/inventory of a particular item into account when computing the cost.

Ultimately, if an item isn't in stock, then it shouldn't be included in the total. You can't buy or sell what you don't have!

Instructions
Make the following changes to your compute_bill function:

While you loop through each item of food, only add the price of the item to total if the item's stock count is greater than zero.
If the item is in stock and after you add the price to the total, subtract one from the item's stock count.
"""

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    prix = 0
    nb = 0
    for item in food:
        for price in prices:
            if item == price:
                prix = prices[price]
        for qt in stock:
            if item == qt and stock[qt] > 0:
                total += prix
                stock[qt] -= 1

        print total
    
    return total
	

"""
Let's Check Out!
Perfect! You've done a great job with lists and dictionaries in this project. You've practiced:

Using for loops with lists and dictionaries
Writing functions with loops, lists, and dictionaries
Updating data in response to changes in the environment (for instance, decreasing the number of bananas in stock by 1 when you sell one).
Thanks for shopping at the Codecademy supermarket!

Instructions
Click Save & Submit Code to finish this course.
"""

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    prix = 0
    nb = 0
    for item in food:
        for price in prices:
            if item == price:
                prix = prices[price]
        for qt in stock:
            if item == qt and stock[qt] > 0:
                total += prix
                stock[qt] -= 1

        print total
    
    return total



