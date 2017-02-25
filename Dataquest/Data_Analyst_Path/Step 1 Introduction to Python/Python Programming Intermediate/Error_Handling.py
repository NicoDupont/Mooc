"""
02/2017
Dataquest : Data Analyst Path
Step 1: Introduction To Python
SubStep : Python Programming Intermediate : Error Handling
"""


"""
1: The Dataset
In this mission, we'll be working with legislators.csv, which records information on every historical member of the U.S. Congress.
Here's a preview of the dataset:

last_name,first_name,birthday,gender,type,state,party
Bassett,Richard,1745-04-02,M,sen,DE,Anti-Administration
Bland,Theodorick,1742-03-21,,rep,VA,
Burke,Aedanus,1743-06-16,,rep,SC,
Carroll,Daniel,1730-07-22,M,rep,MD,
The file includes these columns:

last_name -- the legislator's last name
first_name -- the legislator's first name
birthday -- the legislator's birthday
gender -- the legislator's gender
type -- the chamber in which the legislator served - either Senate (sen) or House of Representatives (rep)
state -- the state the legislator represents
party -- the legislator's party affiliation

As you can see from the data extract, some rows contain missing values for some columns.
For example, the gender and party columns are missing in the second row after the header row.
Missing data can cause errors, so it needs to be dealt with.
In this mission, we'll explore some of the errors that occur when we ignore missing values and how to handle them.

As we learn, we'll work on finding the most common names for U.S. legislators. We'll lay the groundwork in this mission, and bring it all together in the next one.
"""



"""
2: Sets
When exploring data, it's often useful to extract the unique elements in a list. For example, this list has duplicate values:


["Dog", "Cat", "Hippo", "Dog", "Cat", "Dog", "Dog", "Cat"]
Extracting the unique elements will give us:


["Dog", "Cat", "Hippo"]
Simplifying lists in this way can help you find unexpected values.

The result of this conversion is a set - a data type where each element is unique.
A set behaves very similarly to a list.
However, if you add an element to a set that it already contains, the set will ignore it. Also, the items in a set are unordered, while each item in a list has an index.

You can create a set with the set() function. Simply pass a list into the function, and the function will convert it:


unique_animals = set(["Dog", "Cat", "Hippo", "Dog", "Cat", "Dog", "Dog", "Cat"])
print(unique_animals)
We'll get {'Hippo', 'Cat', 'Dog'} as a result. Note that the interpreter encloses Sets in curly braces when it prints them.
Because Sets don't have indexes, the items in a set may display in a different order each time you print it.

You can add items to a set using the add() method:


unique_animals.add("Tiger")
Finally, you can remove items from a set with the remove() method:


unique_animals.remove("Dog")
If we want to convert a set to a list, we can use the list() method:


list(unique_animals)
Instructions
We've read legislators.csv into the variable legislators, which is a list of lists.
Extract the gender column from legislators and assign it to the variable gender.
Create an empty list named gender.
Loop over each item in legislators.
Append the fourth element in the item to gender.
Convert gender to a set.
Print out gender and see what the unique values are.
"""
gender = []
for list in legislators:
    gender.append(list[3])
gender = set(gender)
print(gender)
""" Console Outpur or Results
Output
{'', 'F', 'M'}
"""



"""
3: Exploring The Dataset
When you have a fresh dataset, it's always a good idea to look for any patterns, such as:

Missing data
Some files contain empty fields. Others may use a string like N/A to indicate missing values.
Values that don't make intuitive sense
A legislator with a birthday in 2050, for example, would indicate a problem with the data.
Recuring themes
One theme in this dataset is that the overwhelming majority of legislators are male.
Let's take a closer look at a few columns to see if we can identify any patterns.

Instructions
Extract the party column from legislators and convert it to a set. Assign the result to party.
Print out party and inspect the values.
Print out legislators and inspect the data.
"""
party = []
for list in legislators:
    party.append(list[6])
party = set(party)
print(party)
print("------------------------")
print(legislators)
""" Console Outpur or Results
{'', 'Anti Jacksonian', 'Free Silver', 'Progressive', 'Democratic and Union Labor', 'Socialist', 'Ind. Republican-Democrat', 'Unionist', 'Constitutional Unionist', 'Democrat', 'Republican-Conservative', 'Jacksonian', 'Adams', 'Independent Democrat', 'Unknown', 'Law and Order', 'Pro-Administration', 'National Greenbacker', 'Farmer-Labor', 'Anti-Jacksonian', 'Whig', 'Conservative', 'Ind. Whig', 'Ind. Democrat', 'Anti-Administration', 'Unconditional Unionist', 'Jackson', 'American', 'Independent', 'Free Soil', 'Coalitionist', 'Liberal Republican', 'Union Labor', 'Prohibitionist', 'Jackson Republican', 'Union Democrat', 'States Rights', 'Silver Republican', 'Nonpartisan', 'Readjuster', 'Nullifier', 'Readjuster Democrat', 'Anti Masonic', 'Anti-Lecompton Democrat', 'Popular Democrat', 'Progressive Republican', 'Conservative Republican', 'New Progressive', 'Union', 'Adams Democrat', 'Populist', 'Democrat-Liberal', 'Anti Jackson', 'Crawford Republican', 'Liberty', 'Democratic Republican', 'Federalist', 'American Labor', 'Ind. Republican', 'Republican'}
------------------------
[['Bassett', 'Richard', '1745-04-02', 'M', 'sen', 'DE', 'Anti-Administration'], ['Bland', 'Theodorick', '1742-03-21', '', 'rep', 'VA', ''], ['Burke', 'Aedanus', '1743-06-16', '', 'rep', 'SC', ''], ['Carroll', 'Daniel', '1730-07-22', 'M', 'rep', 'MD', ''], ['Clymer', 'George', '1739-03-16', 'M', 'rep', 'PA', ''], ['Contee', 'Benjamin', '', 'M', 'rep', 'MD', ''],...
"""



"""
4: Missing Values
You may have noticed that the set representations of the gender and party columns on the previous two screens contained an empty string ('').
This indicates that one or more of the rows in the data have missing values in those columns.
Missing values are very common in real world data analysis, since the people compiling the datasets often don't have full information.

You can use one of the following strategies to address missing data:

Remove any rows that contain missing data.
Populate the empty fields with a specified value.
Populate the empty fields with a calculated value.
Use analysis techniques that work with missing data.
We'll work with missing data in more depth later on, but for now, we'll focus on populating empty fields with a specified value.

Here's how we could replace any missing values in the party column with the string No Party:


rows = [
    ["Bassett", "Richard", "1745-04-02", "M", "sen", "DE", "Anti-Administration"],
    ["Bland", "Theodorick", "1742-03-21", "", "rep", "VA", ""]
]
for row in rows:
    if row[6] == "":
        row[6] = "No Party"
Step by step, we:

Loop through each row in rows.
Check whether the party column (index 6) has a missing value.
If so, replace it with the string No Party.
Next, we'll populate the empty fields in the gender column.
Most U.S. legislators have historically been men (although this is changing), so we'll replace any missing values with the string M.

Instructions
Replace any missing values in the gender column of legislators with the string M.
When you're done, the gender column of legislators should only contain the values F and M.
"""
gender = []
for list in legislators:
    gender.append(list[3])

gender = set(gender)
print("--------------")
print(gender)

for list in legislators:
    if list[3] == "":
        list[3] = "M"

gender = []
for list in legislators:
    gender.append(list[3])

gender = set(gender)
print("--------------")
print(gender)
""" Console Outpur or Results
Output
--------------
{'', 'F', 'M'}
--------------
{'F', 'M'}
"""



"""
5: Parsing Birth Years
While we're looking for the most common names of U.S. legislators, the year of birth could also be of interest.
For example, we could use that field to identify historical naming trends, and explore how popular names have changed from 1820 to today.

As you may have noticed, the birthday column has the format 1820-01-02, which is hard to work with.
However, it's common to reformat values to simplify them. In this case, we can split the date into its component parts:


date = "1820-01-02"
parts = date.split("-")
print(parts)
This will create a list ["1820", "01", "02"].
The first item in the list is the year the legislator was born, the second is the month, and the last is the day.

Instructions
Create an empty list named birth_years.
Loop through each item in legislators.
Split the value in the birthday column on the - character.
Assign the result to parts.
Extract the first item in parts and append it to birth_years.
At the end, birth_years will be a list containing the birth years of all the legislators in legislators.
"""
birth_years = []
for list in legislators:
    parts = list[2].split("-")
    birth_years.append(parts[0])

print(birth_years)
""" Console Output or Results
Output
['1745', '1742', '1743', '1730', '1739', '', '1738', '1745', '1748', '1734', '1756', '', '1737', '1754', '1736', '', '1727', '1733', '1732', '1737', '1739', '1734', '1740', '1745', '1728', '', '1738', '1737', '1739', '1744', '', '1761', '1756', '1752', '1737', '1745', '1744', '1742', '1726', '', '1733', '1741', '', '1756', '', '1721', '', '1764', '', '1740', '1745', '1745', '', '1735', '1745', '', '1753', '1748', '1749', '1740', '1746', '1729', '', '', '1726', '1748', '1756', '', '1753', '', '', '1753', '', '1739', '', '1738', '1741', '1750', '1761', '', '1758', '1744', '1759', '1743', '1736', '', '1741', '1739', '', '1745', '1751', '1743', '1754', '1758', '1743', '1764', '1727', '1749', '1751', '1739', '1753', '', '1758', '1752', '', '1755', '1753', '1747', '', '1751', '1752', '1760', '1756', '', '1753', '1754', '1749', '1758', '1743', '',
"""


"""
6: Try/Except Blocks
Converting a column to a different data type is a common operation in data analysis.
For example, we just extracted the year on the previous screen, but it's in string form.
To find the average year in which legislators were born, we'll need to convert the data to integers first.
We can perform this conversion with the int() function.
The only challenge is that the year column has missing values.
If we try to convert a missing value, we'll get an error:


int('')
The code above will cause a ValueError, because an empty string can't be converted to an integer.

Not all errors should halt execution, though. Sometimes we expect a certain type of error, and want to handle it in a specific way that allows the code to complete. We can manage errors with something known as a try/except block. If you surround the code that causes an error with a try/except block, the error will be handled, and the code will continue to run:


try:
    int('')
except Exception:
    print("There was an error")
In the example above, the Python interpreter will try to run int(''), and generate a ValueError.
Instead of stopping the code from executing, it will be handled by the except statement, which will print the message There was an error.
The Python interpreter will continue to run any lines of code that come after the except statement.

Instructions
Convert the string hello to a float with the float() function.
Wrap the code that does the conversion in a try/except block.
In the except statement, print out Error converting to float..
"""
try:
    float("hello")
except Exception:
    print("Error converting to float..")
""" Console Output or Results
Output
Error converting to float..
"""



"""
7: Exception Instances
When the Python interpreter generates an exception, it actually creates an instance of the Exception class. This class has certain properties that help us debug the error. We can access the instance of the Exception class in the except statement body:


try:
    int('')
except Exception as exc:
    print(type(exc))
In the example above, we use the as statement to assign the instance of the Exception class to the variable exc. We can then access the variable in the except statement body. Printing type(exc) will display the type of Exception that occured in the try statement body.

We can also convert the Exception class to a string and print out the error message:


try:
    int('')
except Exception as exc:
    print(str(exc))
This will print a message that will help us debug the error.

Instructions
Write a statement that attempts to convert an empty string to an integer, and wrap it in a try/except block.
Capture the Exception instance.
Print the type of the Exception instance.
Convert the Exception instance to a string and print it out.
"""
try:
    int('')
except Exception as exc:
    print(type(exc))
""" Console Outpur or Results
Output
<class 'ValueError'>
"""



"""
8: The Pass Keyword
On the previous screen, we printed a message each time an error occurred:


try:
    int('')
except Exception:
    print("There was an error")
However, there are times when we don't want to do anything specific to handle errors; we just want the code to keep running. This is common when looping over a long list, and performing the same operation multiple times. In cases like this, printing lots of errors messages would be fairly annoying. For example, running the following code results in many errors:


numbers = [1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    try:
        int('')
    except Exception:
        print("There was an error")
Unfortunately, we can't just leave out the print statement to avoid this, since that would cause an error:


numbers = [1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    try:
        int('')
    except Exception:
That's because any Python statement that ends in a colon (:) needs to have an indented body below it. Instead, we can use the pass keyword to avoid generating an error:


try:
    int('')
except Exception:
    pass
While the pass keyword doesn't actually do anything, it's a valid statement body. It offers a solution when we don't want an error to stop code execution, but also don't want to do anything in the except statement body.

Instructions
Loop through each element in birth_years.
Assign the element to year.
Try to convert year to an integer using the int() function.
Wrap the conversion in a try/except block.
Use the pass keyword in the except statement body.
Append year to converted_years.
"""
converted_years = []

for list in birth_years:
    year = list
    print(year)
    try:
        year = int(year)
    except Exception:
        pass
    converted_years.append(year)
""" Console Output or Results

"""



"""
9: Convert Birth Years To Integers
Let's convert all of the birth years in legislators to integers.
To change the items in a list of lists, we need to loop over the top-level list (items):


items = [
    [1, "1", 2],
    [2, "", 3],
    [5, "5", 3]
]
​
for item in items:
    item[1] = int(item[1])

The above code will modify the second element in each item (embedded list).
In other words, it will convert all of the values in the second column of items to integers.

Instructions
Loop through each row in legislators.
Parse the birth year from the birthday column.
Convert the birth year to an integer, and assign it to birth_year.
Wrap this code in a try/except block.
If there's an exception, assign 0 to birth_year.
Append birth_year to the row with the append() method.
When finished, legislators should have an extra column for birth year.
"""
for row in legislators:
    try:
        birth_year =  int(row[2].split("-")[0])
    except Exception:
        birth_year = 0
    row.append(birth_year)

print(legislators[0:5])
""" Console Outpur or Results
Output
[['Bassett', 'Richard', '1745-04-02', 'M', 'sen', 'DE', 'Anti-Administration', 1745],
['Bland', 'Theodorick', '1742-03-21', 'M', 'rep', 'VA', '', 1742],
['Burke', 'Aedanus', '1743-06-16', 'M', 'rep', 'SC', '', 1743],
['Carroll', 'Daniel', '1730-07-22', 'M', 'rep', 'MD', '', 1730],
['Clymer', 'George', '1739-03-16', 'M', 'rep', 'PA', '', 1739]]
"""



"""
10: Fill In Years Without A Value
We finished parsing the birth years to integers, but now we have several birth years with the value 0. Here are the first few items in the birth_year column of legislators:


[1745,
 1742,
 1743,
 1730,
 1739,
 0,
 1738,
 1745,
 1748,
 ...
]
While exploring the dataset, you may have noticed that the legislators appear in roughly chronological order.
We can use this knowledge to populate the missing values intelligently.

Earlier, we replaced missing values with a fixed value M. This time, because the values generally appear in chronological order, we can loop through each year and replace any 0 values with the values from the previous rows.

By doing this, we'll make sure each legislator without a birth year is assigned one that's relatively close to the actual date.

Instructions
Create a variable called last_value, and set it to 1.
Loop through each row in legislators.
If the year column (index 7) equals 0, replace it with last_value.
Assign the value of the year column (index 7) to last_value.
After the code runs, each row previously containing 0 for birth_year column will now instead have the previous row's value for the same column.
"""
last_value = 1
for row in legislators:
    if row[7] == 0:
        row[7] = last_value
    last_value = row[7]
""" Console Outpur or Results

"""



"""
11: Next Steps
In this mission, we did some basic exploration and manipulation with legislators.csv, and laid the groundwork for our names project.
In the next mission, we'll learn some advanced list concepts, then find the most common names for U.S. legislators who served after 1940.
"""
