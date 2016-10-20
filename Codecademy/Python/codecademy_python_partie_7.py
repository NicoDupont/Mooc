# Partie 7 :
# Lists and Functions


"""
List accessing
This exercise goes over just pulling information from a list, which we've covered in a previous section!

Instructions
Please add the code to print out the second element in the list.
"""

n = [1, 3, 5]

# Add your code below
print n[1]

# sortie : 3



"""
List element modification
You've already learned how to modify elements of a list in a previous section. This exercise is just a recap of that!

Instructions
On line 3, multiply the second element of the n list by 5
Overwrite the second element with that result.
Make sure to print the list when you are done!
"""

n = [1, 3, 5]
# Do your multiplication here
n[1] *= 5
print n
# sortie : [1, 15, 5]


"""
Appending to a list
Here, we'll quickly recap how to .append() elements to the end of a list.

Instructions
Append the number 4 to the end of the list n.
"""

n = [1, 3, 5]
# Append the number 4 here
n.append(4)
print n

# sortie : [1, 3, 5, 4]


"""
Removing elements from lists
This exercise will expand on ways to remove items from a list. You actually have a few options. For a list called n:

n.pop(index) will remove the item at index from the list and return it to you:
n = [1, 3, 5]
n.pop(1)
# Returns 3 (the item at index 1)
print n
# prints [1, 5]
n.remove(item) will remove the actual item if it finds it:
n.remove(1)
# Removes 1 from the list,
# NOT the item at index 1
print n
# prints [3, 5]
del(n[1]) is like .pop in that it will remove the item at the given index, but it won't return it:
del(n[1])
# Doesn't return anything
print n
# prints [1, 5]
Instructions
Remove the first item from the list n using either .pop(), .remove(), or del.
"""

n = [1, 3, 5]
# Remove the first item in the list here
del(n[0])
print n

# sortie : [3, 5]


"""
Changing the functionality of a function
In this exercise, you will just be making a minor change to a function to change what that function does.

Instructions
Change the function so the given argument is multiplied by 3 and returned.
"""

number = 5

def my_function(x):
    return x * 3

print my_function(number)


"""
More than one argument
This exercise is to recap how to use more than one argument in a function.

Instructions
Define a function called add_function that has 2 parameters x and y and adds them together.
"""

m = 5
n = 13
# Add add_function here!
def add_function(x,y):
    return x + y

print add_function(m, n)


"""
Strings in functions
This is a basic recap on using strings in functions.

Instructions
Write a function called string_function that takes in a string argument (s) and then returns that argument concatenated with the word 'world'. Don't add a space before world!
"""

n = "Hello"
# Your function here!
def string_function(s):
    return "%sworld" % s
    


print string_function(n)

"""
Passing a list to a function
You pass a list to a function the same way you pass any other argument to a function.

Instructions
Click Save & Submit Code to see that using a list as an argument in a function is essentially the same as using just a number or string!
"""

def list_function(x):
    return x
n = [3, 5, 7]
print list_function(n)

# [3, 5, 7]


"""
Using an element from a list in a function
Passing a list to a function will store it in the argument (just like with a string or a number!)

def first_item(items):
    print items[0]

numbers = [2, 7, 9]
first_item(numbers)
In the example above, we define a function called first_item. It has one argument called items.
Inside the function, we print out the item stored at index zero of items.
After the function, we create a new list called numbers.
Finally, we call the first_item function with numbers as its argument, which prints out 2.
Instructions
Change line 2 so that list_function returns only the item stored in index one of x, rather than the entire x list.
"""

def list_function(x):
    return x[1]

n = [3, 5, 7]
print list_function(n)

# sortie : 5


"""
Modifying an element of a list in a function
Modifying an element in a list in a function is the same as if you were just modifying an element of a list outside a function.

def double_first(n):
    n[0] = n[0] * 2

numbers = [1, 2, 3, 4]
double_first(numbers)
print numbers
We create a list called numbers.
We use the double_first function to modify that list.
Finally, we print out [2, 2, 3, 4]
When we pass a list to a function and modify that list, like in the double_first function above, we end up modifying the original list.

Instructions
Change list_function so that:

Add 3 to the item at index one of the list.
Store the result back into index one.
Return the list.
"""

def list_function(x):
    x[1] += 3
    return x
    

n = [3, 5, 7]
print list_function(n)

# sortie : [3, 8, 7]



"""
List manipulation in functions
You can also append or delete items of a list inside a function just as if you were manipulating the list outside a function.

my_list = [1, 2, 3]
my_list.append(4)
print my_list
# prints [1, 2, 3, 4]
The example above is just a reminder of how to append items to a list.

Instructions
Define a function called list_extender that has one parameter lst.
Inside the function, append the number 9 to lst.
Then return the modified list.
"""

n = [3, 5, 7]
# Add your function here
def list_extender(lst):
    lst.append(9)
    return lst
    
print list_extender(n)

# sortie : [3, 5, 7, 9]



"""
Printing out a list item by item in a function
This exercise is to go over how to utilize every element in a list in a function. You can use the existing code to complete the exercise and see how running this operation inside a function isn't much different from running this operation outside a function.

Don't worry about the range function quite yet—we'll explain it later in this section.

Instructions
Define a function called print_list that has one argument called x.
Inside that function, print out each element one by one. Use the existing code as a scaffold.
Then call your function with the argument n.
"""

n = [3, 5, 7]
    
def print_list(x):
    for i in range(0, len(x)):
        print x[i]
    
print_list(n)

# sortie :
"""
3
5
7
"""




"""
Modifying each element in a list in a function
This exercise shows how to modify each element in a list. It is useful to do so in a function as you can easily put in a list of any length and get the same functionality. As you can see, len(n) is the length of the list.

Instructions
Create a function called double_list that takes a single argument x (which will be a list) and multiplies each element by 2 and returns that list. Use the existing code as a scaffold.
"""
n = [3, 5, 7]

# Don't forget to return your new list!

def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    
    return x
    
print double_list(n)

# sortie : [6, 10, 14]




"""
Passing a range into a function
Okay! Range time. The Python range() function is just a shortcut for generating a list, so you can use ranges in all the same places you can use lists.

range(6) # => [0,1,2,3,4,5]
range(1,6) # => [1,2,3,4,5]
range(1,6,3) # => [1,4]
The range function has three different versions:

range(stop)
range(start, stop)
range(start, stop, step)
In all cases, the range() function returns a list of numbers from start up to (but not including) stop. Each item increases by step.

If omitted, start defaults to zero and step defaults to one.

Instructions
On line 6, replace the ____ with a range() that returns a list containing [0, 1, 2].
"""

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(0,3,1)) # Add your range between the parentheses!

# sortie : [0, 2, 4]




"""
Iterating over a list in a function
Now that we've learned about range, we have two ways of iterating through a list.

Method 1 - for item in list:

for item in list:
    print item
Method 2 - iterate through indexes:

for i in range(len(list)):
    print list[i]
Method 1 is useful to loop through the list, but it's not possible to modify the list this way. Method 2 uses indexes to loop through the list, making it possible to also modify the list if needed. Since we aren't modifying the list, feel free to use either one on this lesson!

Instructions
Create a function that returns the sum of a list of numbers.

On line 3, define a function called total that accepts one argument called numbers. It will be a list.
Inside the function, create a variable called result and set it to zero.
Using one of the two methods above, iterate through the numbers list.
For each number, add it to result.
Finally, return result.
Create a function called total that adds up all the elements of an arbitrary list and returns that count, using the existing code as a hint. Use a for loop so it can be used for any size list.
"""

n = [3, 5, 7]

def total(numbers):
    result = 0
    for x in numbers:
        result += x
    
    return result




"""
Using strings in lists in functions
Now let's try working with strings!

for item in list:
    print item

for i in range(len(list)):
    print list[i]
The example above is just a reminder of the two methods for iterating over a list.

Instructions
Create a function that concatenates strings.

Define a function called join_strings accepts an argument called words. It will be a list.
Inside the function, create a variable called result and set it to "", an empty string.
Iterate through the words list and append each word to result.
Finally, return the result.
Don't add spaces between the joined strings!
"""

n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for carac in words:
        result += carac
    return result

print join_strings(n)

#sortie : MichaelLieberman



"""
Using two lists as two arguments in a function
Using multiple lists in a function is no different from just using multiple arguments in a function!

a = [1, 2, 3]
b = [4, 5, 6]
print a + b
# prints [1, 2, 3, 4, 5, 6]
The example above is just a reminder of how to concatenate two lists.

Instructions
Create a function that joins two lists together.

On line 4, define a function called join_lists that has two arguments, x and y. They will both be lists.
Inside that function, return the result of concatenating x and y together.
"""

m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x,y):
    concat = x+ y
    return concat

print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]

# sortie : [1, 2, 3, 4, 5, 6]


"""
Using a list of lists in a function
Finally, this exercise shows how to make use of a single list that contains multiple lists and how to use them in a function.

list_of_lists = [[1,2,3], [4,5,6]]

for lst in list_of_lists:
    for item in lst:
        print item
In the example above, we first create a list containing two items, each of which is a list of numbers.
Then, we iterate through our outer list.
For each of the two inner lists (as lst), we iterate through the numbers (as item) and print them out.
We end up printing out:

1
2
3
4
5
6
Instructions
Create a function called flatten that takes a single list and concatenates all the sublists that are part of it into a single list.

On line 3, define a function called flatten with one argument called lists.
Make a new, empty list called results.
Iterate through lists. Call the looping variable numbers.
Iterate through numbers.
For each number, .append() it to results.
Finally, return results from your function.
"""

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results = []
    for numbers in lists:
        for nb in numbers:
            results.append(nb)
    return results

print flatten(n)


# sortie : [1, 2, 3, 4, 5, 6, 7, 8, 9]


