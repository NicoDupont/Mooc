# Partie 2 :
#  Strings & Console Output


# Set the variable brian on line 3!
brian = "Hello life!"

# Assign your variables below, each on its own line!
caesar = "Graham"
praline = "John"
viking = "Teresa"
# Put your variables above this line
print caesar
print praline
print viking


# The string below is broken. Fix it using the escape backslash!

'This isn\'t flying, this is falling with style!'

"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "MONTY"[4]
print fifth_letter
c = "cats"[0]
n = "Ryan"[3]

parrot = "Norwegian Blue"
print len(parrot)

parrot = "Norwegian Blue"
print parrot.lower()

parrot = "norwegian blue"
print parrot.upper()

"""Declare and assign your variable on line 4,
then call your method on line 5!"""

pi = 3.14
print str(pi)



ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()


"""Tell Python to print "Monty Python"
to the console on line 4!"""
print "Monty Python"


# Printing Variables
"""Assign the string "Ping!" to
the variable the_machine_goes on
line 5, then print it out on line 6!"""

the_machine_goes = "Ping!"
print the_machine_goes

# concaténation de chaine
# Print the concatenation of "Spam and eggs" on line 3!
print "Spam " + "and " + "eggs"

# Turn 3.14 into a string on line 3!
print "The value of pi is around " + str(3.14)

# afficher des variables dans print
string_1 = "Camelot"
string_2 = "place"
print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)


name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")
print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

# Write your code below, starting on line 3!
my_string = "phrase"
print len(my_string)
print my_string.upper()


"""

str()

Now let's look at str(), which is a little less straightforward. The str() method turns non-strings into strings! For example:

str(2)

would turn 2 into "2".
Instructions

    Create a variable pi and set it to 3.14 on line 4.
    Call str(pi) on line 5, after print.
"""

"""Declare and assign your variable on line 4,
then call your method on line 5!"""

pi = 3.14
print str(pi)


"""
Dot Notation

Let's take a closer look at why you use len(string) and str(object), but dot notation (such as "String".upper()) for the rest.

lion = "roar"
len(lion)
lion.upper()

Methods that use dot notation only work with strings.

On the other hand, len() and str() can work on other data types.
Instructions

    On line 3, call the len() function with the argument ministry.
    On line 4, invoke the ministry's .upper() function.

"""

ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()


"""
Printing Strings

The area where we've been writing our code is called the editor.

The console (the window in the upper right) is where the results of your code is shown.

print simply displays your code in the console.
Instructions

Print "Monty Python" to the console.
"""

"""Tell Python to print "Monty Python"
to the console on line 4!"""

print "Monty Python"


"""
Printing Variables

Great! Now that we've printed strings, let's print variables
Instructions

    Declare a variable called the_machine_goes and assign it the string value "Ping!" on line 5.
    Go ahead and print the_machine_goes in line 6.

"""

"""Assign the string "Ping!" to
the variable the_machine_goes on
line 5, then print it out on line 6!"""

the_machine_goes = "Ping!"
print the_machine_goes

# sortie : Ping!


"""

String Concatenation

You know about strings, and you know about arithmetic operators. Now let's combine the two!

print "Life " + "of " + "Brian"

This will print out the phrase Life of Brian.

The + operator between strings will 'add' them together, one after the other. Notice that there are spaces inside the quotation marks after Life and of so that we can make the combined string look like 3 words.

Combining strings together like this is called concatenation. Let's try concatenating a few strings together now!
Instructions

Let's give it a try. Print the concatenated strings "Spam ", "and ", "eggs" on line 3, just like the example above.

Make sure you include the spaces after "Spam " and "and ".
"""

# Print the concatenation of "Spam and eggs" on line 3!
print "Spam " + "and " + "eggs"




"""
Explicit String Conversion

Sometimes you need to combine a string with something that isn't a string. In order to do that, you have to convert the non-string into a string.

print "I have " + str(2) + " coconuts!"

This will print I have 2 coconuts!.

The str() method converts non-strings into strings. In the above example, you convert the number 2 into a string and then you concatenate the strings together just like in the previous exercise.

Now try it yourself!
Instructions

    Run the code as-is. You get an error!
    Use str() to turn 3.14 into a string. Then run the code again.

"""


# Turn 3.14 into a string on line 3!

print "The value of pi is around " + str(3.14)



"""
String Formatting with %, Part 1

When you want to print a variable with a string, there is a better method than concatenating strings together.

name = "Mike"
print "Hello %s" % (name)

The % operator after a string is used to combine a string with variables. The % operator will replace a %s in the string with the string variable that comes after it.
Instructions

Take a look at the code in the editor. What do you think it'll do? Click Save & Submit when you think you know.
"""

string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)


# sortie : Let's not go to Camelot. 'Tis a silly place.





"""

String Formatting with %, Part 2

Remember, we used the % operator to replace the %s placeholders with the variables in parentheses.

name = "Mike"
print "Hello %s" % (name)

You need the same number of %s terms in a string as the number of variables in parentheses:

print "The %s who %s %s!" % ("Knights", "say", "Ni")
# This will print "The Knights who say Ni!"

Instructions

Now it's your turn! We have ___ in the code to show you what you need to change!

    Inside the string, replace the three ___ with %s.
    After the string but before the three variables, replace the final ___ with a %.
    Hit Save & Submit Code.
    Answer the questions in the console as they pop up! Type in your answer and hit Enter.

"""

name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

""" sortie :
What is your name? test
What is your quest? dfs
What is your favorite color? dsf
Ah, so your name is test, your quest is dfs, and your favorite color is dsf.
None
"""


"""

And Now, For Something Completely Familiar

Great job! You've learned a lot in this unit, including:

Three ways to create strings

'Alpha'
"Bravo"
str(3)

String methods

len("Charlie")
"Delta".upper()
"Echo".lower()

Printing a string

print "Foxtrot"

Advanced printing techniques

g = "Golf"
h = "Hotel"
print "%s, %s" % (g, h)

Instructions

Let's wrap it all up!

    On line 3, create the variable my_string and set it to any string you'd like.
    On line 4, print the length of my_string.
    On line 5, print the .upper() case version of my_string.
"""

# Write your code below, starting on line 3!

my_string = "phrase"
print len(my_string)
print my_string.upper()


