""" 01/2017
Dataquest : Complete Data Analyst Path 
Step 1: Introduction To Python
SubStep : Python Programming: Beginner : Booleans and If Statements
"""



"""
1: Booleans
In this mission, we'll learn how to express conditional logic. We can use conditional logic to add criteria to the code we write. Some examples of operations that use criteria include:

Finding all the integers in a list that are greater than 5.
Identifying which elements in a list are strings, and printing only those values.
We can break down both of these examples into logic we can code:

For each integer in a list, if the integer is greater than 5, add to the list greater_than_five.
For each element in a list, if the value has a string data type, use the print() function to display it; if it's not a string, ignore it.
Python has a class called Boolean that helps express conditional logic. There are only two Boolean values: True and False. Because they're words, Boolean values may look like strings, but they're an entirely separate class. For example, string operations like concatenation won't work with Booleans.

The following code example assigns True to t and False to f:


t = True
f = False
If we display the data type for either t or f, we'll see class 'bool', shorthand for Boolean.

Instructions
Assign the value True to the variable cat, and the value False to the variable dog.
Then, use the print() function and the type() function to display the type for cat.

"""
cat = True
dog = False
print(type(cat))
""" result or Ipython output

Output
<class 'bool'>

"""





"""
2: Boolean Operators
Python has comparison operators that allow us to compare variables:

== returns True if both variables are equivalent, and False if they're different
!= returns True if both variables are different, and False if they're equivalent
> returns True if the first variable is greater than the second variable, and False otherwise
< returns True if the first variable is less than the second variable, and False otherwise
>= returns True if the first variable is greater than or equal to the second variable, and False otherwise
<= returns True if the first variable is less than or equal to the second variable, and False otherwise
For now let's focus on the equality operators (== and !=). To compare two variables, place the operator between them. We recommend adding a space before and after the operator for better readability:


print(8 == 8) # True
print(8 != 8) # False
print(8 == 10) # False
print(8 != 10) # True
We can assign the result of a comparison to a Boolean variable:


# Use parentheses for cleaner code.
t = (8 == 8) # True
u = (8 != 8) # False
We can also compare strings, floats, Booleans, and even lists:


# All of these return True.
"8" == "8"
["January", "February"] == ["January", "February"]
5.0 == 5.0
The variable cities is a list of strings containing the city names from the crime rate dataset we used in the previous mission. We've created the list for you already.

Instructions
Use the Boolean operators to determine if the following pairs of values are equivalent:
The first element in cities and the string "Albuquerque". Assign the resulting Boolean value to first_alb.
The second element in cities and the string "Albuquerque". Assign the resulting Boolean value to second_alb.
The first element in cities and the last element in cities. Assign the resulting Boolean value to first_last.

"""
rint(cities)
first_alb = cities[0] == "Albuquerque"
second_alb = cities[1] == "Albuquerque"
first_last = cities[-1] == cities[0]
""" result or Ipython output
Output
['Albuquerque', 'Anaheim', 'Anchorage', 'Arlington', 'Atlanta', 'Aurora', 'Austin', 'Bakersfield', 'Baltimore', 'Boston', 'Buffalo', 'Charlotte-Mecklenburg', 'Cincinnati', 'Cleveland', 'Colorado Springs', 
'Corpus Christi', 'Dallas', 'Denver', 'Detroit', 'El Paso', 'Fort Wayne', 'Fort Worth', 'Fresno', 'Greensboro', 'Henderson', 'Houston', 'Indianapolis', 'Jacksonville', 'Jersey City', 'Kansas City', 'Las Vegas', 'Lexington', 'Lincoln', 'Long Beach', 
'Los Angeles', 'Louisville Metro', 'Memphis', 'Mesa', 'Miami', 'Milwaukee', 'Minneapolis', 'Mobile', 'Nashville', 'New Orleans', 'New York', 'Newark', 'Oakland', 'Oklahoma City', 'Omaha', 'Philadelphia', 
'Phoenix', 'Pittsburgh', 'Plano', 'Portland', 'Raleigh', 'Riverside', 'Sacramento', 'San Antonio', 'San Diego', 'San Francisco', 'San Jose', 'Santa Ana', 'Seattle', 'St. Louis', 'St. Paul', 'Stockton', 'Tampa', 'Toledo', 'Tucson', 'Tulsa', 'Virginia Beach', 'Washington', 'Wichita']

"""




"""
3: Booleans With "Greater Than"
We can use the greater than operator (>) to test whether one value is larger than another. Similarly, the greater than or equal to operator (>=) determines if one value is larger than or equal to a second value:


rates = [10, 15, 20]
​
rates[0] > rates[1] # False
rates[0] >= rates[0] # True

Instructions
The variable crime_rates is a list of integers containing the crime rates from the dataset. Perform the following comparisons:
Evaluate whether the first element in crime_rates is larger than the integer 500, and assign the Boolean result to first_500.
Evaluate whether the first element in crime_rates is larger than or equal to 749, and assign the Boolean result to first_749.
Evaluate whether the first element in crime_rates is greater than or equal to the last element in crime_rates, and assign the Boolean result to first_last.


"""
print(crime_rates)
first_500 = crime_rates[0] > 500
first_749 = crime_rates[0] >= 749
first_last= crime_rates[0] >= crime_rates[-1]
""" result or Ipython output
Output
[749, 371, 828, 503, 1379, 425, 408, 542, 1405, 835, 1288, 647, 974, 1383, 455, 658, 675, 615, 2122, 423, 362, 587, 543, 563, 168, 992, 1185,
 617, 734, 1263, 784, 352, 397, 575, 481, 598, 1750, 399, 1172, 1294, 992, 522, 1216, 815, 639, 1154, 1993, 919, 594, 1160, 636, 752, 130, 517,
  423, 443, 738, 503, 413, 704, 363, 401, 597, 1776, 722, 1548, 616, 1171, 724, 990, 169, 1177, 742]

"""




"""
4: Booleans With "Less Than"
We can use the less than operator (<) to test whether one value is smaller than another value. Similarly, the less than or equal to operator (<=) determines if one value is smaller than or equal to another value:


rates = [10, 15, 20]
​
rates[0] < rates[1] # True
rates[0] <= rates[0] # True

Instructions
The variable crime_rates is a list containing the crime rates from the dataset as integers. Perform the following comparisons:
Determine whether the second element in crime_rates is smaller than the integer 500, and assign the Boolean result to second_500.
Determine whether the second element in crime_rates is smaller than or equal to 371, and assign the Boolean result to second_371.
Determine whether the second element in crime_rates is smaller than or equal to the last element in crime_rates, and assign the Boolean result to second_last.

"""
print(crime_rates)
second_500 = crime_rates[1] < 500
second_371 = crime_rates[1] <= 371
second_last = crime_rates[1] <= crime_rates[-1]
""" result or Ipython output

Output
[749, 371, 828, 503, 1379, 425, 408, 542, 1405, 835, 1288, 647, 974, 1383, 455, 658, 675, 615, 2122, 423, 362, 587, 543, 563, 168, 992, 1185,
 617, 734, 1263, 784, 352, 397, 575, 481, 598, 1750, 399, 1172, 1294, 992, 522, 1216, 815, 639, 1154, 1993, 919, 594, 1160, 636, 752, 130, 517,
  423, 443, 738, 503, 413, 704, 363, 401, 597, 1776, 722, 1548, 616, 1171, 724, 990, 169, 1177, 742]

"""



"""
5: If Statements
Now that we know how to work with Boolean values, let's dive more into how we use Booleans to express conditional logic. To complement Booleans, Python contains the if operator. We can use this operator to write a statement that tests whether certain conditions exist. Our if statement will evaluate to either True or False, and only run the specified code when True.

For example, the following code checks whether the integer value assigned to sample_rate is larger than 5. This is referred to as a "conditional statement." It assigns the Boolean result to greater, and uses the print() function to display sample_rate if greater is True:


sample_rate = 749
greater = (sample_rate > 5)
if greater:                    #This is the conditional statement.
    print(sample_rate)
We can also specify the conditional statement inside the if statement:


if sample_rate > 5:            #This is the conditional statement.
    print(sample_rate)
The conditional statement after the if has to evaluate to either True or False.

Similar to for loops, we need to format if statements in the following way:

End the conditional statement with a colon (:)
Indent the code (that we want run when True) below the conditional statement
Also similar to for loops, if statements can contain multiple lines in the body, as long as their indentation aligns.


t = True
f = False
​
if t:
    print("Now you see me")
if f:
    print("Now you don't")
We'll end with a generalized representation of an if statement:

Instructions
Determine whether the third element in cities is equivalent to the string "Anchorage".
If it is, change the variable result to 1.

"""
result = 0
if cities[2] == "Anchorage":
    result = 1
""" result or Ipython output


"""





"""
6: Nesting If Statements
We can nest if statements to specify multiple criteria. In the following code example, we first test whether an integer is greater than 500, and then check whether it's greater than 1000. Python only evaluates the inner if statement if the outer if statement evaluates to True.


value = 1500
​
if value > 500:
    if value > 1000:
        print("This number is HUGE!")

Instructions
Write a piece of code that nests the following concepts in the order in which they appear:
An if statement that tests whether the first element in crime_rates is larger than 500
A second if statement that tests whether the second element in crime_rates is larger than 300
If both statements evaluate to True, assign the value True to the variable both_conditions

"""
both_conditions = False
if crime_rates[0] > 500:
    if crime_rates[1] > 300:
        both_conditions = True
""" result or Ipython output


"""




"""
7: If Statements And For Loops
We can also nest if statements within for loops, and vice versa. For example, we can search a list for the existence of a specific value by combining a for loop with an if statement. The if statement determines whether the current element is equivalent to the value we're interested in:


found = False
for city in cities:
    if city == 'Washington':
        found = True
We've set the value found set to False by default. If one of the elements in cities is equivalent to the string "Washington", then Python assigns the Boolean value True to found.

We can also use a for loop and an if statement to determine the index for a specific value in a list. To accomplish this, we can create an integer variable named counter outside the for loop and increment it by 1 with each iteration. If the value at the current iteration of the loop matches our desired value, we can set another integer variable, index, to the current value of counter:


counter = 0
index = 0
​
for city in cities:
    if city == "Washington":
        index = counter
    counter += 1
Keep in mind that in the above implementation, if there are multiple instances of the desired value ("Washington") in the list, the variable index will update each time. This means that once the for loop finishes, index will contain the last index location the loop finds (not the first one).

Instructions
Create a new list, five_hundred_list, that contains only the elements from crime_rates that are greater than 500. To accomplish this, you'll need a for loop and an if statement:
The for loop specifies which list we want to iterate over and the name of the iterator variable (we use cr in our answer).
The if statement determines whether the current element (cr) is larger than 500.
If the current element (cr) is larger than 500, use the append() method to add it to five_hundred_list.

"""
five_hundred_list = []
for cr in crime_rates:
    if cr > 500:
        five_hundred_list.append(cr)
""" result or Ipython output


"""




"""
8: Find The Highest Crime Rate
Now that we know how to combine if statements and for loops, we can find the highest crime rate in the crime_rates list.

Here's one way we can approach this task:

Assign the value at index 0 in crime_rates to a new integer variable called highest
Use a for loop that compares each value in crime_rates to highest, and assigns that value to highest if it's larger
If the first value (at index 0) is the largest value in the list, then the value assigned to highest will never change. Otherwise, each time the loop finds a value that's larger than highest, it will assign that value to highest. The value assigned to highest only changes when a new value in the list is larger than it. When the loop completes, we're guaranteed to have the largest value.

Instructions
Find the largest integer in crime_rates using the strategy we just outlined, and assign that value to the variable highest.

"""
print(crime_rates)
highest = 0
for cr in crime_rates:
    if cr > highest:
        highest = cr
print(highest)
""" result or Ipython output
[749, 371, 828, 503, 1379, 425, 408, 542, 1405, 835, 1288, 647, 974, 1383, 455, 658, 675, 615, 2122, 423, 362, 587, 543, 563, 168, 992, 1185,
 617, 734, 1263, 784, 352, 397, 575, 481, 598, 1750, 399, 1172, 1294, 992, 522, 1216, 815, 639, 1154, 1993, 919, 594, 1160, 636, 752, 130, 517,
  423, 443, 738, 503, 413, 704, 363, 401, 597, 1776, 722, 1548, 616, 1171, 724, 990, 169, 1177, 742]

>>> 2122

"""

