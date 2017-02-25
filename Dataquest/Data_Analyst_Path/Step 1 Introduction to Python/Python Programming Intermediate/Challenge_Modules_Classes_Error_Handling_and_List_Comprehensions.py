"""
02/2017
Dataquest : Data Analyst Path
Step 1: Introduction To Python
SubStep : Python Programming Intermediate : Challenge: Modules, Classes, Error Handling, and List Comprehensions
"""


"""
1: How Challenges Work
At Dataquest, we're huge believers in learning through doing, and we hope this shows in your learning experiences.
While missions focus on introducing concepts, challenges give you the opportunity to engage in deliberate practice by completing structured problems.
You can read more about deliberate practice on Wikipedia and on Nautilus.

If you have questions or run into issues, head over to the Dataquest forums or our Slack community.
"""



"""
2: Introduction To The Data
In this challenge, you'll practice using modules, classes, and list comprehensions to process and represent a data set in Python. You'll be working with data on NFL player suspensions. The FiveThirtyEight team compiled the data set for a piece on domestic violence. You can download it here. The data set contains all domestic violence-related suspensions issued before 2014.

Here's a preview of what the file, nfl_suspensions_data.csv, looks like:

see img3.png

name	team	games	category	desc.	year	source
F. Davis	WAS	Indef.	Substance abuse, repeated offense	Marijuana-related	2014	http://www.cbssports.com/nfl/eye-on-football/24448694/redskins-te-fred-davis-suspended-Indefiniteinitely-by-nfl
J. Blackmon	JAX	Indef.	Substance abuse, repeated offense		2014	http://espn.go.com/nfl/story/_/id/11257934/justin-blackmon-jacksonville-jaguars-arrested-marijuana-possession
L. Brazill	IND	Indef.	Substance abuse, repeated offense		2014	http://www.nfl.com/news/story/0ap2000000364622/article/lavon-brazill-released-by-colts-in-wake-of-suspension
Let's read the file into Python and explore the data to become more familiar with it.

Instructions
Read the dataset into a list of lists.
Import the csv module.
Create a File handler for nfl_suspensions_data.csv.
Use the csv.reader() and list() methods to read the file into a list named nfl_suspensions.
Remove the first list in nfl_suspensions, which contains the header row of the CSV file.
Select all lists in nfl_suspensions, except the for the one at index 0.
Assign the resulting list of lists back to the variable nfl_suspensions.
Count the number of times each value in the year column occurs.
Create an empty dictionary called years.
Use a for loop to iterate over the list in nfl_suspensions representing the year column:
Extract that row's value for the year column and assign it to row_year.
If row_year is already a key in years, add 1 to the value for that key.
If row_year isn't already a key in years, set the value for the key to 1.
Use the print() function to display the dictionary years.
"""
import csv

f = open("nfl_suspensions_data.csv", 'r')
nfl_suspensions = list(csv.reader(f))

header = nfl_suspensions[0]
nfl_suspensions = nfl_suspensions[1:len(nfl_suspensions)]

years = {}
for row in nfl_suspensions:
    if row[5] in years:
        years[row[5]] += 1
    else:
        years[row[5]] = 1

print(years)
""" Console Output or Results
Output
{'1997': 3, '2007': 17, '1947': 1, '1989': 17, '2014': 29, '2005': 8, '2003': 9, '2013': 40, '   ': 1, '1946': 1, '1986': 1, '2004': 6, '2008': 10, '1983': 1, '1998': 2, '2002': 7, '2012': 45, '2010': 21, '2011': 13, '2000': 1, '1993': 1, '1963': 1, '2006': 11, '2001': 3, '1995': 1, '1990': 3, '1999': 5, '1994': 1, '2009': 10}
"""



"""
3: Unique Values
Let's explore the values in these columns by using sets and list comprehensions.

Instructions
Retrieve the unique values in the team column and assign the list to unique_teams.
Use a list comprehension to create a new list containined just the values in the team column.
Use the set() function to return a list containing only the unique values and assign to unique_teams.
Retrieve the unique values in the games column and assign the list to unique_games.
Use a list comprehension to create a new list containined just the values in the games column.
Use the set() function to return a list containing only the unique values and assign to unique_games.
Display unique_teams and unique_games.
"""
unique_teams = []
values = [ row[1] for row in nfl_suspensions ]
unique_teams = set(values)

unique_games = []
values = [ row[2] for row in nfl_suspensions ]
unique_games = set(values)
        
print(unique_teams)
print("--------------------")
print(unique_games)
""" Console Output or Results
Output
{'FREE', 'PIT', 'MIA', 'NO', 'BUF', 'TB', 'CLE', 'PHI', 'DET', 'STL', 'ARI', 'IND', 'DEN', 'SD', 'KC', 'GB', 'CAR', 'NYJ', 'NYG', 'BAL', 'DAL', 'TEN', 'JAX', 'HOU', 'SEA', 'LA', 'CHI', 'SF', 'WAS', 'MIN', 'NE', 'ATL', 'OAK', 'CIN'}
--------------------
{'2', '10', '36', '16', '5', '4', '3', '1', 'Indef.', '6', '14', '20', '8', '32'}
"""





"""
4: Suspension Class
Next, let's create a Suspension class that we can use to represent each NFL suspension in the data set.

Instructions
Create the Suspension class.
Define the __init__() method with the following criteria:
The sole required parameter is a list representing a row from the dataset.
To create a Suspension instance, we want to be able to pass in a list from nfl_suspensions.
Currently, we're only interested in storing the name, team, games and year columns. Upon instantiation:
Set the name value for that row to the name property.
Set the team value for that row to the team property.
Set the games value for that row to the games property.
Set the year value for that row to the year property.
Create a Suspension instance using the third row in nfl_suspensions, and assign it to the variable third_suspension.
"""
class Suspension():
    def __init__(self,list_values):
        self.name = list_values[0]
        self.team = list_values[1]
        self.games = list_values[2]
        self.year = list_values[5]
        

third_suspension = Suspension(nfl_suspensions[2])
print(third_suspension.name)
print(third_suspension.team)
print(third_suspension.games)
print(third_suspension.year)
""" Console Output or Results
Output
L. Brazill
IND
Indef.
2014
"""




"""
5: Tweaking The Suspension Class
Let's tweak the Suspension class a bit to extend its functionality. Right now, the value for year is a string, rather than an integer. Let's modify the Suspension class so that it stores the values as integers.

Instructions
Instead of assigning the value at index 5 to the year property directly, use a try except block that:
Tries to cast the value at index 5 to an integer
If an exception is thrown, assign the value 0 to the year property instead
Create a method called get_year() that returns the year value for that Suspension instance.
Create a Suspension instance using the 23rd row, and assign it to missing_year.
Use the get_year() method to assign the year of the missing_year suspension instance to twenty_third_year.
"""
class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0
    
    def get_year(self):
        return self.year
        
missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()

print(missing_year.name)
print(missing_year.team)
print(missing_year.games)
print(twenty_third_year)
""" Console Output or Results
Output
P. Hornung
GB
14
0
"""




"""
6: Next Steps
In this challenge, you honed your knowledge of list comprehensions and class creation. 
You also practiced using the csv module, as well as handling exceptions with a try catch block. 
Next, you'll learn about variable scopes.
"""