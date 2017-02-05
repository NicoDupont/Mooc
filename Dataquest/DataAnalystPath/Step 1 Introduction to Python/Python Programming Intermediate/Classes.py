"""
01/2017
Dataquest : Data Analyst Path
Step 1: Introduction To Python
SubStep : Python Programming Intermediate : Classes
"""


"""
1: NFL Data
For this mission, we'll be working with a data set containing the results of NFL games. The file includes every game from 2009-2013.

Each row in our data set represents a game. The first column is for the year it took place, and the second is for the week of the season (out of 17 total weeks). The third column records the winning team, and the fourth records the losing team.

To give you an idea of what the data set looks like, here are the first three rows:

Year  |  Week  |  Winner  |  Loser

The first row displays data on a game between the Steelers and the Titans. It took place during the first week of the 2009 season, and the Steelers won.
"""



"""
2: Introduction To Objects And Classes
In the last mission, we learned how modules help us write clean and concise code. Python also has a number of other features that can organize and structure code.

For example, it also supports objects. An object is a variable that has its own variables and behavior.
Let's imagine we're writing an application for choosing and customizing cars. We need to represent cars in our code, and allow people to modify and interact with them.
We could create a dictionary for each car, with keys like "color" and "model". However, this approach doesn't have any standardization regarding what information we should store about each car.
Some cars may have a "color" key, while others may not. We need a consistent way to represent and interact with cars in our code. Objects can help us do this.

Suppose we create an object called black_honda_accord.
This object has variables like color, make, and model that help represent the car's attributes.
We call these variables properties, and access them using dot notation.

print(black_honda_accord.color)
print(black_honda_accord.make)
print(black_honda_accord.model)

To create an object, we need some sort of template that tells us what properties the object should have.
For example, black_honda_accord has color, make and model properties.
If we want to create another car object that has this same behavior, we need a template.

This is where classes come into play.
A class is a template for new objects.
So, if we have a Car class with color, make, and model properties, we can create many different instances of the Car class, and they will all have their own values for those properties.
An instance is an object created from a template, or class. black_honda_accord is an instance of the Car class.
If we wanted to create a red_toyota_camry instance, we could do so, and it would have its own color, make, and model values.
"""




"""
3: Class Syntax
Before we begin working with classes, let's take a look at how we define them.
For a class called Car(), we'd use class Car(): to start a class definition.
Inside the class, we define a special function called __init__. This is where we define our properties.

The definition of our Car class looks like this:

class Car():
    def __init__(self):
        self.color = "black"
        self.make = "honda"
        self.model = "accord"

By assigning values to color, make, and model within __init__, we indicate that we want our Car instances to have color, make, and model properties with the default values we specified.
These values are appropriate for our black_honda_accord instance, but we'll have to customize them for our red_toyota_camry instance. We'll learn how to do that later in this mission.

Inside our class definition, we refer to properties using self.property_name.
For now, __init__ and self.property_name are just blocks of syntax you need to remember.
As you progress through the mission, though, you'll learn what this syntax means, and why it's important.

To create an instance of a class (in this case the Car class) we use black_honda_accord = Car().
To access the color of the instance black_honda_accord, we write black_honda_accord.color.
In the following exercise, you'll use this syntax to define a class that will represent NFL teams.
We'll interact with our NFL data set through this class for the duration of this mission.

Instructions
Create a class called Team.
Inside the class, create a name property. Assign the value "Tampa Bay Buccaneers" to this property.
Create an instance of the Team class, and assign it to the variable bucs.
Print the name property of the bucs instance.
"""
class Car():
    def __init__(self):
        self.color = "black"
        self.make = "honda"
        self.model = "accord"

black_honda_accord = Car()

print(black_honda_accord.color)

class Team():
    def __init__(self):
        self.name = "Tampa Bay Buccaneers"

bucs = Team()
print(bucs.name)
""" Console Outpur or Results
Output
black
Tampa Bay Buccaneers
"""



"""
4: Instance Methods And __init__
In addition to properties, instances can also have behavior.
We define this behavior using methods.
We actually just did this on the last screen. __init__ is a special method that the Python interpreter automatically calls whenever we create an instance of a class.

Recall that __init__ takes in a self parameter.
This parameter refers to the current instance, and allows us to access and add to its properties. self is passed in automatically when we call Team() (which calls __init__).

We can add more parameters to __init__, and pass them in explicitly when we call Team(). Suppose we want to add a name property to our Team class:


class Team():
    def __init__(self, name):
        self.name = name
We pass in the name parameter when we create an instance, and then that parameter becomes the team's name:


bucs = Team("Tampa Bay Buccaneers")
In the Team exercise from the previous screen, for example, we set the name property to "Tampa Bay Buccaneers" for all new instances we create with some_team = Team().

This time, let's add the name argument to our Team class's __init__ method in a way that allows us to create teams with any name.

Instructions
Add a name parameter to the __init__ method, and set the value of the self.name property to the name argument.
Make an instance of the class, passing in the value "New York Giants" to the __init__ function (when you write Team()).
Assign the result to the variable giants.
"""
class Team():
    def __init__(self, name):
        self.name = name

giants = Team("New York Giants")
""" Console Outpur or Results

"""



"""
5: The Self Keyword
Recall that we use the self keyword to add properties to a class. We just did this for our Team class on the previous screens.

Whenever we call a method on an instance of a class, self is the first argument to be passed in, though we never explicitly specify it in the method call.
Within method definitions, we can use self to access properties or methods on the current instance.

The code for our Team class looks a little like this:


class Team():
    def __init__(self, name):
        self.name = name
When we create an instance of the Team class, we write:


bucs = Team("Tampa Bay Buccaneers")
The Python interpreter automatically calls __init__, with self and "Tampa Bay Buccaneers" as its arguments. In this example, self is really just a reference to bucs, so when we set self.name inside the __init__ method, we are really setting bucs.name.
If we created a new team named my_team, we'd be setting my_team.name within the __init__ method.
However, we don't need to worry about the instance's name when we are defining a method, since we can always access it using self.
"""




"""
6: More Instance Methods
So far, we've learned to customize how an instance is created using the special __init__ method.
But that's just the beginning. We can define any method we'd like for a particular class to customize how instances of that class behave.

Methods are very similar to functions, and we define them with the same syntax. The only difference is that methods are "attached" to instances, while functions aren't.
We can use methods to run custom code that interacts with those instances.

To use a method:

Define it in the code for the class.
Call it on an instance of that class.
Let's return to our Team class to see what this looks like. Suppose we want to print the team's name. The revisions to our class might look like this:


## original code
class Team():
    def __init__(self, name):
        self.name = name
​
## new method
    def print_name(self):
        print(self.name)
Since the new print method acts on individual instances of the Team class, we call it an instance method.
The interpreter doesn't call it automatically like the __init__ method. Instead, we would call it explicitly in our code. We call instance methods using dot notation:


bucs = Team("Tampa Bay Buccaneers") ## From previous screen. Creates an instance of the Team class and auto-calls `__init__`, based on the class definition.
...
bucs.print_name() ## Calls the method on the instance.
By defining instance methods that we call explicitly, we are customizing our instances' behavior. Let's practice what we've learned, and write a method that performs some analysis on our NFL data set.

We've already loaded the data set into the nfl variable for you.

Instructions
Add an instance method called count_total_wins to the definition for the Team class.
The method should take no arguments (except self), and should return the number of games the team won during the period this data set describes.
Use the instance method to assign the number of wins by the "Denver Broncos" to broncos_wins.
Use the instance method to assign the number of wins by the "Kansas City Chiefs" to chiefs_wins.
"""
import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# The NFL data is loaded into the nfl variable.
class Team():
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

    # Your method goes here
    def count_total_wins(self):
        count = 0
        for row in nfl:
            if row[2] == self.name:
                count = count + 1
        return count



bucs = Team("Tampa Bay Buccaneers")
bucs.print_name()

broncos_wins = Team("Denver Broncos").count_total_wins()
chiefs_wins = Team("Kansas City Chiefs").count_total_wins()
print(broncos_wins)
print("------------------")
print(chiefs_wins)
""" Console Outpur or Results
Output
Tampa Bay Buccaneers
46
------------------
34
"""



"""
7: Adding To The Init Function
On the previous screen, we loaded the nfl variable for you outside of the Team class. However, this approach isn't ideal. The purpose of classes is to organize our code, and a big part of organizing code is abstraction. We don't want to have to worry about loading the data set into an nfl variable before using our class, and if we share our code with someone else, they shouldn't have to worry about it either.

Instead of loading the file outside of our class, we should automatically load it whenever we create a new instance of our class, and store it as an instance property. We can do this by adding code to the class definition.

Recall that we can use the csv module to read a data set from a csv file:

f = open("somefile.csv", 'r')
csvreader = csv.reader(f)
dataset = list(csvreader)

Instructions
Add code that reads the data from nfl.csv and stores it in the new property self.nfl property within the __init__ method.
Alter the code in the count_total_wins method so that it uses the self.nfl property instead of the nfl variable (which no longer exists).
Use this instance method to assign the number of wins by the "Jacksonville Jaguars" to jaguars_wins.
"""
import csv
class Team():
    def __init__(self, name):
        self.name = name
        f = open("nfl.csv", 'r')
        csvreader = csv.reader(f)
        dataset = list(csvreader)
        self.nfl = dataset

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count

jaguars_wins = Team("Jacksonville Jaguars").count_total_wins()
print(jaguars_wins)
""" Console Outpur or Results
Output
26
"""



"""
8: Wins In A Year
Let's add a count_wins_in_year method to the definition for our class. When you call this method on a Team instance, it should count and return the number of victories the team won during the year we passed in.

We'll need to check for games that the given team won, and that took place during the given year. Recall that we can use the and keyword to test whether multiple conditions are true.

Instructions
Add a method to the Team class that computes how many victories a team won in a given year.
The count_wins_in_year method should take a year string as an argument (e.g. "2011"), and return the number of wins the team had in that year.
Use the instance method to assign the number of games the "San Francisco 49ers" won in "2013" to niners_wins_2013.
"""
import csv
class Team():
    def __init__(self, name):
        self.name = name
        f = open("nfl.csv", 'r')
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count

    def count_wins_in_year(self,year):
        count = 0
        for row in self.nfl:
            if row[2] == self.name and row[0] == year:
                count = count + 1
        return count

niners_wins_2013 = Team("San Francisco 49ers").count_wins_in_year("2013")
print(niners_wins_2013)
""" Console Outpur or Results
Output
12
"""



"""
9: Conclusion
If we wanted to count an NFL team's wins without using objects, we could write a count_total_wins function.
But if we later decided to count wins for a particular year, we'd have to write an entirely new function, and pass the team's name for every function call.
We'd also need to load in our nfl variable somewhere in the code. While all of this is possible, the code would lack structure and organization.

With classes, we bundle all of that data and behavior together in one location.
An instance of the Team class is all we need to count how many wins a team had in a given time period. Once we add behavior to a class, every instance of the class will be able to perform that behavior.
As we develop our application, we can add more properties to classes to extend their functionality.
Using classes and instances helps organize our code, and allows us to represent real-world concepts in well-defined code constructs.
"""
