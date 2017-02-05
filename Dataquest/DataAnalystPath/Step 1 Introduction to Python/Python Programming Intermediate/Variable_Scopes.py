"""
02/2017
Dataquest : Data Analyst Path
Step 1: Introduction To Python
SubStep : Python Programming Intermediate : Variable Scopes
"""


"""
1: The Data Set
As we work through this mission, we'll be using a data set on student loan defaults in the United States.
It's very common for American students to borrow money to pay for college.
Because tuition costs are high, many students are unable to repay their loans.
When a student cannot pay off his or her loan, it goes into a status known as default.

Each row of our dataset represents a single university, and contains information about the number of its students who later defaulted on their loans.
While the data contains twelve columns, we'll be looking at a few in particular:

institution -- The name of the university
state -- The state in which the university is located
city -- The city in which the university is located
borrower_default_count_240 -- The total number of students who have defaulted on their loans
principal_outstanding_240 -- The total dollar amount of the loans in default
To make the data easier to work with, we've read each of these columns into its own list.
For example, you can access the entire city column by using the variable city.

Instructions
This step is a demo. Play around with code or advance to the next step.
"""
print(len(borrower_default_count_240))
print(borrower_default_count_240[0:10])
""" Console Output or Results
Output
1845
[1606, 1567, 269, 184, 93, 75, 52, 88, 12, 5]
"""



"""
2: Built-In Functions
Some Python functions are available by default, without having to import them. We call these built-in functions.
The sum() function, which works on lists, is one such built-in function.

Here are a few others:

len()
float()
min()
max()
Developers use these functions so often that it made sense to make them a part of the language itself.
You can find a full list of built-in Python functions here.

Instructions
Use the sum() function to add 6 and 11 and assign the result to total.
"""
total = sum([6,11])
""" Console Output or Results
Variables
 totalint (<class 'int'>)
17
"""



"""
3: Overwriting A Built-In Function
You're probably used to assigning values to variables, then accessing those values, like this:


b = 10
print(b)
The value 10 is assigned to variable b, which is why running the code displays 10.
Here's a slightly more complex example:


b = [1,2]
sum = sum(b)
sum(20)
This code will actually generate an error because sum no longer points to the built-in Python function but to the expression sum(b) instead.
Once we overwrite the sum variable with a value, we can't access the function anymore.
Calling sum(20) won't make any sense, because sum evalutes to a single integer value (the result of sum(b)).
If we called print(sum), it would print out the value 3.

On the next few screens, we'll delve into why this behavior occurs.

Instructions
Experiment with the code to see what happens before and after we overwrite the sum() function.
Click "Next Step" when you're done.
"""
sum = sum(borrower_default_count_240)

test = sum(principal_outstanding_240)
""" Console Output or Results

"""




"""
4: Scopes
When we write functions, we're writing reusable blocks of code. This means that no matter what's happening with the rest of the code we write, the function should operate in exactly the same way each time. This allows us to create programs that run in predictable ways. We wouldn't want a function to behave differently at random if we had a variable called total in our code. Let's say we wrote a function that adds two numbers:


def add(a,b):
    total = a + b
    return total
Inside the function, we're defining a variable named total. We could call the function like this:


total = 15
print(add(10, 20))
print(total)
Since functions are designed to be reusable, they have to be isolated from the rest of the program. Even though there's a variable called total inside the add function, that variable is not connected to the total variable in our script. For example, the script above would print out two different totals: first 30, then 15. That's because the variable total we defined in our script is in the global scope, whereas the total variable inside add is in a local scope.

Here's a diagram of how the variables look as the code runs:

see img4.png

The idea of variable scoping is extremely important in programming, and allows us to isolate what happens in functions from what happens in the rest of our program.

The global scope is whatever happens outside of a function. Anything that happens inside a function is in a local scope. There's only one global scope, but each function creates its own local scope.

Instructions
Use the find_average function to find the average of principal_outstanding_240, and assign the result to the variable average.
Afterwards, print the variable total to verify that it's unchanged in the global scope.
"""
def find_average(column):
    length = len(column)
    total = sum(column)
    return total / length

total = sum(borrower_default_count_240)
average =  find_average(principal_outstanding_240)
print(average)
print(total)
""" Console Output or Results
Output
563408.6590785908
499833
"""




"""
5: Scope Isolation
Local scopes aren't just isolated from the global scope - they're also isolated from every other local scope. Our code creates a local scope when it calls a function, and destroys it when the function finishes running. Calling the same function twice will create two separate local scopes. This ensures that any variables our code creates inside the function disappear when the function finishes running, and don't affect the rest of the program.

Here's an example:


def add(a,b):
    total = a + b
    return total
​
def subtract(a,b):
    total = a - b
    return total
​
print(add(1,5))
print(subtract(1,5))
Even though both of the functions in the code above define a variable called total within them, each one has its own local scope. After each function is called, the values for both total variables disappear, because all the variables defined inside the local scope are removed. The code snippet above doesn't define any variables in the global scope.

Here's how the variables look when the code is run:

see img5.png

Instructions
Calculate the average of principal_outstanding_240 with the find_average() function, and assign the result to the variable average.
Calculate the length of principal_outstanding_240 with the find_length() function, and assign the result to the variable principal_length.
Afterwards, verify that the variable length is unchanged in the global scope.
Also verify that changing the order in which you call find_average and find_length doesn't alter the results.
"""
def find_average(column):
    length = len(column)
    total = sum(column)
    return total / length

def find_length(column):
    length = len(column)
    return length

length = len(borrower_default_count_240)
average = find_average(principal_outstanding_240)
principal_length = find_length(principal_outstanding_240)
print(length)
print("--------------")
print(average)
print("--------------")
print(principal_length)
print("--------------")
""" Console Output or Results
Output
1845
--------------
563408.6590785908
--------------
1845
--------------
"""




"""
6: Scope Inheritance
When our code uses a variable name in a local scope that it hasn't defined there yet, the Python interpreter will check whether the variable exists in the global scope.

Here's an example:


total = 50
def find_average(column):
    length = len(column)
    return total / length
In the code above, we use the total variable inside find_average() without having first defined it. In this case, the Python interpreter will check whether total exists in the global scope. Because it does, the Python interpreter will return 50 / length from the find_average() function.

Here's a diagram:

see img6.png

Instructions
Find the average of principal_outstanding_240 with the find_average() function, and assign the result to the variable average.
Verify that the find_average() function used the value length from the global scope.
"""
def find_average(column):
    total = sum(column)
    # In this function, we are going to pretend that we forgot to calculate the length
    return total / length

length = 10
average= find_average(principal_outstanding_240)
print(length)
""" Console Output or Results
Output
10
"""




"""
7: Inheritance Limits
There are limits to how much we can work with global scope variables inside a local scope. These limits allow functions to be reusable, and prevent them from changing how your script behaves.

Here's an example of what won't work:

a = 2
def alter_a():
    a = a * 2
    return a

The function above will cause an error. That's because while we can access the value of a global scope variable inside a local scope, we can't change the value of that variable.

Instructions
Experiment with the code to see what happens before and after we call the find_total() function. Click "Next Step" when you're done.
"""




"""
8: Built-In Inheritance
As we recently learned, if we use a variable in a local scope that isn't defined there, the Python interpreter will look for it in the global scope. If it doesn't find the variable there, it will check whether the variable is a built-in function name.

Here's an example of the type of code that would generate this behavior:


def total(a):
    return sum(a)
We use the sum variable in the total() function, but don't define in the local scope or the global scope. This variable is actually a built-in function called sum(). So the Python interpreter calls the function, and uses it to add the values in the list a.

If other code in the global scope overwrites the built-in function, then the interpreter uses the value in the global scope:


sum = 10
​
def total(a):
    return sum(a)
​
print(total([1,2]))
The code above will cause an error, because the interpreter will use the global scope value for sum in the total() function. That's because the global scope value for sum is an integer, and won't work as a function.
"""





"""
9: Global Variables
Global variables are variables that are available across all scopes. We can access and change the value of a global variable inside any global scope or local scope.

While Global variables can sometimes be handy, the developer community generally doesn't recommend using them. That's because they make functions dependent on the value of variables in the global scope, and prevent them from being reusable in any situation.

Still, let's take a look at how we would use them. We define global variables with the global keyword.


global total
total = 10
​
def add_to_total(a):
    total = total + a
​
add_to_total(20)
print(total)
The code above will add 20 to total, then print out 30.

When we create a global variable, we can't create it and assign a value to it on the same line. We first define the variable as global using the global keyword, then assign a value to it on a separate line.

We can also define global variables inside local scopes:


def test_function():
    global a
    a = 10
​
test_function()
print(a)
Because we defined a with the global keyword, this code will print out 10.

Instructions
Create a new function:
Make a global variable b inside the function.
Assign the value 20 to b inside the function.
Call the function.
Print out b.
"""
def new_function():
    global b
    b = 20

new_function()
print(b)
""" Console Output or Results
Output
20
"""




"""
10: Inheritance Rules
When we use a variable anywhere in a Python script, the Python interpreter will look for its value according to some simple rules. It will:

Start with the local scope, if any. If the variable is defined here, it will use that value.
Look at any enclosing scopes, starting with the innermost. These are "outside" local scopes. If the variable is defined in any of them, it will use the value.
Look in the global scope. If the variable is there, it uses the value.
Look in the built-in functions.
Throw an error if it doesn't find the variable.
A simple way to remember this is LEGBE, which stands for "Local, Enclosing, Global, Built-ins, Error".
"""
