""" 01/2017
Dataquest : Complete Data Analyst Path 
Step 1: Introduction To Python
SubStep : Python Programming: Beginner : Challenge: Files, Loops, and Conditional Logic
"""

"""
1: How Challenges Work
Our missions are structured around learning by doing, so you're ready to tackle problems in the real world. 
We've also designed challenges that will give you an opportunity to practice programming and data science by completing structured problems. 
Completing challenges will help you solidify concepts and apply what you've learned in the real world. 
Challenges will feel similar to missions, but with little instructional material and harder exercises. 
You can check your work as many times as you'd like, and we encourage you to experiment with your code. 
If you get stuck, write code to explore and review concepts you've learned, or refer back to the missions you've completed.

While you can reveal the solution code, we encourage you to think, make your own attempts, and experiment for a significant amount of time before doing so! 
If you have questions or run into issues, head over to the Dataquest forums or to our Slack community to get help.
"""


"""
2: Unisex Names
For this challenge, you'll be working with the data set behind this FiveThirtyEight article on common unisex (gender-neutral) names in the United States. You'll start by reading in the file and iteratively converting the data to more useful representations. At the end of this challenge, you'll filter the data so that it only includes the names that at least 1,000 people share.

The staff at FiveThirtyEight compiled this data set from information at the Social Security Adminstration's website. You'll work with a shortened version of the full data set to complete this challenge.

Here's a preview of the shortened data set, which is in a CSV file named dq_unisex_names.csv:


Casey,176544.328149
Riley,154860.66517300002
Jessie,136381.830656
Jackie,132928.78874000002
Avery,121797.41951600001
Jaime,109870.18729000002
Peyton,94896.39521599999
Each line contains two values separated by commas. The first value is the unisex name, and the second value is the estimated number of Americans with that name.
"""




"""
3: Read The File Into A String
To work with the data, you'll first need to read it into Python. This involves creating a File object, then using one of its methods to read the file into a string.

Instructions
Use the open() function with the following parameters to return a File object:
dq_unisex_names.csv for the file name
r for read mode
Then, use the read() method of the File object to read the file into a string.
Assign that string to a variable named names.

"""
names = open("dq_unisex_names.csv", "r").read()
""" result or Ipython output


"""




"""
4: Convert The String To A List
Now that you have a string representation of the file, convert it to a list of strings.

Instructions
Use the split() method that strings have to split on the new-line delimiter ("\n"), and assign the resulting list to names_list.
Select the first five elements in names_list, and assign them to first_five.
Display first_five using the print() function.

"""
f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split("\n")
first_five = names_list[0:5]
print(first_five)

""" result or Ipython output
Output
['Casey,176544.328149', 'Riley,154860.66517300002', 'Jessie,136381.830656', 'Jackie,132928.78874000002', 'Avery,121797.41951600001']

"""





"""
5: Convert The List Of Strings To A List Of Lists
When you displayed the first five elements, you may have noticed that they contained commas. Let's split each string element in names_list on the comma, and add the resulting lists to a new list named nested_list.

Instructions
Split each element in names_list on the comma delimiter (,) and append the resulting list to nested_list. To accomplish this:
Create an empty list and assign it to nested_list.
Write a for loop that iterates over names_list.
Within the loop body, run the split() method on each element to return a list (assign that list to comma_list).
Within the loop body, run the append() method to add each list (comma_list) to nested_list.
Use the print() function to display the first five elements in nested_list.

"""
f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list =[]
for row in names_list:
    comma_list =  row.split(",")
    nested_list.append(comma_list)
print(nested_list[0:5])

""" result or Ipython output
Output
[['Casey', '176544.328149'], ['Riley', '154860.66517300002'], ['Jessie', '136381.830656'], ['Jackie', '132928.78874000002'], 
['Avery', '121797.41951600001'], ['Jaime', '109870.18729000002'], ['Peyton', '94896.39521599999'], ['Kerry', '88963.92625'], 
['Jody', '80400.519199'], ['Kendall', '79210.873961'], ['Payton', '64151.630388'], ['Skyler', '53486.390419'], ['Frankie', '51288.068109'], 
['Pat', '44781.602373'], ['Quinn', '41920.940058'], ['Harley', '41237.565743'], ['Reese',  etc....

"""




"""
6: Convert Numerical Values
You now have a list of lists assigned to nested_list, where each inner list contains string elements. The second element (the estimated number of people with that name) in each list is a decimal value that you should convert to a float. By converting these values to floats, you'll be able to perform computations on them and analyze the data.

Instructions
Create a new list of lists called numerical_list where:
The element at index 0 for each list is the unisex name (as a string)
The element at index 1 for each list is the number of people who share that name (as a float)
To accomplish this:
Create an empty list and assign it to numerical_list.
Write a for loop that iterates over nested_list. In the loop body:
Retrieve the element at index 0 and assign it to a variable.
Retrieve the element at index 1, convert it to a float, and assign it to a variable.
Create a new list containing these two elements (in the same order).
Use the append() method to add this new list to numerical_list.
Finally, display the first five elements in numerical_list.


"""
print(nested_list[0:5])
numerical_list = []
for list in nested_list:
    index0 = list[0]
    index1 = float(list[1])
    new_list = [index0,index1]
    numerical_list.append(new_list)
print(numerical_list[0:5])
""" result or Ipython output
Output
[['Casey', '176544.328149'], ['Riley', '154860.66517300002'], ['Jessie', '136381.830656'], ['Jackie', '132928.78874000002'], ['Avery', '121797.41951600001']]
[['Casey', 176544.328149], ['Riley', 154860.66517300002], ['Jessie', 136381.830656], ['Jackie', 132928.78874000002], ['Avery', 121797.41951600001]]

"""



"""
7: Filter The List
The data set contains first names shared by at least 100 people. Let's limit it those shared by at least 1,000 people.

Instructions
Create a new list of strings called thousand_or_greater that only contains the names shared by 1,000 people or more.
To accomplish this:
Create an empty list and assign it to thousand_or_greater.
Write a for loop that iterates over numerical_list.
In the loop body, use an if statement to determine if the value at index 1 for that element (which is a list) is greater than or equal to 1000.
If the value is greater than or equal to 1000, use the append() method to add its name to thousand_or_greater.
Finally, display the first 10 elements in thousand_or_greater.

"""
# The last value is ~100 people
numerical_list[len(numerical_list)-1]
thousand_or_greater = []
for list in numerical_list:
    if list[1] >= 1000:
        thousand_or_greater.append(list[0])
print(thousand_or_greater[0:10])

""" result or Ipython output
Output
['Casey', 'Riley', 'Jessie', 'Jackie', 'Avery', 'Jaime', 'Peyton', 'Kerry', 'Jody', 'Kendall']

"""