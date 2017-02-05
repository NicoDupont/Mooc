""" 01/2017
Dataquest : Complete Data Analyst Path
Step 1: Introduction To Python
SubStep : Python Programming: Beginner : Dictionaries
"""


"""
1: The Data Set
In this mission, we'll work with Los Angeles weather data from 2014. The dataset is a list of string elements that represent weather patterns:


["Sunny"
 "Sunny"
 "Sunny",
 ...,
 "Fog"]
The list contains 365 elements. The first element is for the type of weather that occurred on January 1st, and the last element represents the type of weather that occurred on December 31st.

We've loaded the list into the weather variable.


Instructions
Print the first element of weather.
Print the last element of weather.

"""
# Weather has been loaded in.
print(weather[0])
print(weather[-1])
""" result or Ipython output
Output
Sunny
Fog

"""



"""
2: Dictionaries
Let's say we have a set of students, along with their scores from a recent math test:


To store the students' names and their scores, we could use two lists:


students = ["Tom", "Jim", "Sue", "Ann"]
scores = [70, 80, 85, 75]
To figure out what score Sue got on the test, we'd first have to write a loop to find the index corresponding to the element Sue in the students list. We'd then have to find the value for that index in scores. Here's how we could do this:


indexes = [0,1,2,3]
name = "Sue"
score = 0
for i in indexes:
    if students[i] == name:
        score = scores[i]
print(score)
This is a complex piece of code for a simple task; we just want to find the value associated with a name.

To accomplish this in an easier way, we can use a dictionary. A dictionary is like a list in that it has indexes, but the indexes aren't necessarily sequential numbers. We can create our own indexes with values of any data type, including strings.

While we initiate a new list with square brackets ([), we create a new dictionary with curly braces ({). We can make an empty dictionary like this:


scores = {}
To add values to an existing dictionary, we specify the index to the left of the equals sign, and the value it should have on the right side. We use square brackets ([) to specify the index.


scores["Tom"] = 70
Taken together, we call the index and value key/value pairs. In this mission, however, we'll refer to the dictionary values on the right side of the equals sign as elements, just like the elements in a list.

The code above will create the index Tom in the scores dictionary, and associate the element 70 with it. To look up the test score for Tom, we would simply write:


scores["Tom"]
This would return the element 70 because we associated it with the index Tom in the dictionary scores. We use square brackets ([) to add values to dictionaries or look up values.

We can add the rest of the students' scores in the same way:


scores["Jim"] = 80
scores["Sue"] = 85
scores["Ann"] = 75

"""






"""
3: Practice Populating A Dictionary
Recall that to create a dictionary, we first define it with curly braces ({), then add values for specific indexes. We call the values elements, and refer to the indexes as dictionary keys:


students = {}
students["Jerry"] = 60
In the example above, we create an empty dictionary called students, then specify that the dictionary key Jerry should have the value 60. To find the value (that's now an element) associated with the dictionary key Jerry, we'd look up Jerry in the dictionary students:


print(students["Jerry"])
The code above would display 60.

A dictionary key can be a string, integer, or float:


students[10] = 100


Instructions
Assign the value 1 to the key Aquaman in a new dictionary named superhero_ranks.
Assign the value 2 to the key Superman in superhero_ranks.

"""
superhero_ranks = {}
superhero_ranks["Aquaman"] = 1
superhero_ranks["Superman"] = 2
print(superhero_ranks)
""" result or Ipython output
Output
{'Aquaman': 1, 'Superman': 2}

"""





"""
4: Practice Indexing A Dictionary
We can look up values in dictionaries by using square brackets. When we pass in a dictionary key, we retrieve the value associated with that key:


students["Tom"]

Instructions
Look up FDR in president_ranks and assign the result to a new variable fdr_rank.
Look up Lincoln in president_ranks and assign the result to a new variable lincoln_rank.
Look up Aquaman in president_ranks and assign the result to a new variable aquaman_rank.

"""
president_ranks = {}
president_ranks["FDR"] = 1
president_ranks["Lincoln"] = 2
president_ranks["Aquaman"] = 3
fdr_rank = president_ranks["FDR"]
lincoln_rank = president_ranks["Lincoln"]
aquaman_rank = president_ranks["Aquaman"]
print(fdr_rank,lincoln_rank,aquaman_rank)
""" result or Ipython output
Output
1 2 3

"""





"""
5: Defining A Dictionary With Values
So far, we've created a dictionary and added elements to it in multiple steps:


students = {}
students["Tom"] = 60
students["Jim"] = 70
This approach is cumbersome when we want to add multiple dictionary keys. Fortunately, we can create a dictionary and add elements to it in a single step:


students = {
    "Tom": 60,
    "Jim": 70
}
In the example above, we create a dictionary, then specify that the key Tom should have the value 60, and the key Jim should have the value 70.

We do this by entering the dictionary key, then a colon (:), then the value. We separate each key/value pair with a comma. If we wanted to, we could add more students like this:


students = {
    "Tom": 60,
    "Jim": 70,
    "Sue": 85,
    "Ann": 80
}
We can use this technique to specify as many key/value pairs as we'd like.


Instructions
Create a dictionary named animals with the following keys and values:
The key 7 corresponding to the value raven.
The key 8 corresponding to the value goose.
The key 9 corresponding to the value duck.
Create a dictionary named times with the following keys and values:
The key morning corresponding to the value 9.
The key afternoon corresponding to the value 14.
The key evening corresponding to the value 19.
The key night corresponding to the value 23.

"""
random_values = {"key1": 10, "key2": "indubitably", "key3": "dataquest", 3: 5.6}
print(random_values)
animals = {7:"raven",8:"goose",9:"duck"}
times = {"morning":9,"afternoon":14,"evening":19,"night":23}
""" result or Ipython output
Output
{'key2': 'indubitably', 3: 5.6, 'key1': 10, 'key3': 'dataquest'}

"""





"""
6: Modifying Dictionary Values
We can modify the elements in a dictionary, just like we can with a list:


students = {
    "Tom": 60,
    "Jim": 70
}
For example, we can replace the element we've associated with a key:


students["Tom"] = 65
The code above would change the element for the key Tom to 65.

We can also modify an existing element:


students["Tom"] = students["Tom"] + 5
The code above would add 5 to the value for the key Tom.

Instructions
Add the key Ann and value 85 to the dictionary students.
Replace the value for the key Tom with 80.
Add 5 to the value for the key Jim.


"""
students = {
    "Tom": 60,
    "Jim": 70
}
students["Ann"] = 85
students["Tom"] = 80
students["Jim"] = students["Jim"] + 5
""" result or Ipython output


"""





"""
7: The In Statement And Dictionaries
In the last mission, we used the in statement to check whether an element occurred in a list:


animals = ["Cat", "Dog"]
found = "Cat" in animals
We can also use the in statement to check whether a key occurs in a dictionary:


students = {
    "Tom": 60,
    "Jim": 70
}
"Tom" in students would return True, and "Sue" in students would return in False.

Instructions
Check whether jupiter is a key in planet_numbers, and assign the resulting Boolean value to jupiter_found.
Check whether earth is a key in planet_numbers, and assign the resulting Boolean value to earth_found.


"""
planet_numbers = {"mercury": 1, "venus": 2, "earth": 3, "mars": 4}
jupiter_found = "jupiter" in planet_numbers
earth_found = "earth" in planet_numbers
print(jupiter_found,earth_found)
""" result or Ipython output

Output
False True

"""



"""
8: The Else Statement
We learned about the if statement in a previous mission. The if statement runs a segment of code if a condition is True:


if temperature > 50:
    print("It's hot!")
In the code above, the if statement checks whether the variable temperature is greater than 50, and prints out It's hot! if it is.

We can also print a different message if the temperature is less than or equal to 50:


if temperature > 50:
    print("It's hot!")
if temperature <= 50:
    print("It's cold!")
If temperature is greater than 50, we'll see It's hot!, and if it's less than or equal to 50, we'll see It's cold!. In other words, we print one statement when temperature > 50 equals True, and another statement when temperature > 50 equals False.

Performing different actions depending on whether a condition is true or false is a common scenario in programming. The else statement offers a simpler way to do this:


if temperature > 50:
    print("It's hot!")
else:
    print("It's cold!")
The code above is much simpler than the previous example, but results in the same outcome. If temperature > 50 is True, then it executes the code in the if statement block. If temperature > 50 is False, then it executes the code in the else statement block.

When using if/else statements, only one of the blocks will execute. That means the code above will only print It's hot! or It's cold! - never both.

"""






"""
9: Practicing With The Else Statement
Else statements allow us to simplify our code. Here's an example:


scores = [80, 100, 60, 30]
high_scores = []
low_scores = []
for score in scores:
    if score > 70:
        high_scores.append(score)
    else:
        low_scores.append(score)
The code above will add a score to high_scores if score is greater than 70, and to low_scores otherwise.

Instructions
Append any names in planet_names that are longer than 5 characters to long_names. Otherwise, append the names to short_names. To accomplish this:
Loop through each item in planet_names.
Use the len() function to find the length of the item.
If the length is greater than 5, append the item to long_names.
Otherwise, append it to short_names.
When complete, short_names should contain any planet names less than 6 characters long, and long_names should contain any planet names 6 characters or longer.


"""
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]
short_names = []
long_names = []
for planet in planet_names:
    if len(planet) < 6:
        short_names.append(planet)
    else:
        long_names.append(planet)
print(short_names)
print(long_names)
""" result or Ipython output
Output
['Venus', 'Earth', 'Mars']
['Mercury', 'Jupiter', 'Saturn', 'Neptune', 'Uranus']

"""





"""
10: Counting With Dictionaries
We now have all the pieces we need to count how many times each element occurs in a dictionary. Let's practice our skills in the following exercise.


Instructions
Count the number of times that each element occurs in the list named pantry that appears in the code block below. You'll need to:
Create an empty dictionary named pantry_counts.
Loop through each item in pantry.
If the item appears in pantry_counts, add 1 to the value in pantry_counts for the item's key.
Otherwise, add the item to pantry_counts as a key, with the value 1.
When finished, each item in pantry will have its own key in pantry_counts, and its value will be the number of times the item appears in pantry.

"""
pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]
pantry_counts = {}
for pan in pantry:
    if pan in pantry_counts:
        pantry_counts[pan] = pantry_counts[pan] + 1
    else:
        pantry_counts[pan] = 1
print(pantry_counts)

""" result or Ipython output
Output
{'grape': 2, 'orange': 2, 'potato': 1, 'apple': 3, 'tomato': 1}

"""





"""
11: Counting The Weather
Now that we have some practice counting with dictionaries, it's time to count how often each type of weather occurs in the weather list.

Instructions
Count how many times each type of weather occurs in the weather list, and store the results in a new dictionary called weather_counts.
When finished, weather_counts should contain a key for each different type of weather in the weather list, along with its associated frequency.
Here's a preview of how the result should format the weather_counts dictionary (note that you'll be using real values, rather than the dummy ones below):


"""
weather_counts = {}
for wea in weather:
    if wea in weather_counts:
        weather_counts[wea] = weather_counts[wea] + 1
    else:
        weather_counts[wea] = 1
print(weather_counts)
""" result or Ipython output
Output
{'Fog-Rain': 4, 'Rain': 25, 'Thunderstorm': 1, 'Fog': 125, 'Sunny': 210}

"""
