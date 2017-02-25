""" 01/2017
Dataquest : Data Analyst Path
Step 1: Introduction To Python
SubStep : Python Programming: Beginner : Customizing Functions and Debugging Errors
"""


"""
"""


"""
1: Overview
In this mission, we'll explore how to customize the functions we write, and apply what we've learned to improve our spell checker from the previous mission. For example, as code becomes increasingly modular (separated into functions), it can also become harder to debug. We'll delve into how to use the errors Python returns to debug our code.

Recall that our spell checker works by:

Reading in a file of correctly spelled words, tokenizing it into a list, and assigning it to the variable vocabulary
Reading in, cleaning, and tokenizing the text we want to spell check
Comparing each word (token) in the text with each word in vocabulary, and returning the ones it doesn't find
The file dictionary.txt contains a sequence of correctly spelled words, which we'll use to seed the vocabulary. The file story.txt contains a piece of text with some misspelled words. We added the current version of the spell checker as we wrote it in the previous mission to the following code cell.

Instructions
This step is a demo. Play around with code or advance to the next step.

"""
f = open("story.txt", 'r')
story_string = f.read()
vocabulary = open("dictionary.txt", "r").read()

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)

misspelled_words = []
clean_chars = [",", ".", "'", ";", "\n"]
tokenized_story = tokenize(story_string, clean_chars)
tokenized_vocabulary = tokenize(vocabulary, clean_chars)

for ts in tokenized_story:
    if ts not in tokenized_vocabulary:
        misspelled_words.append(ts)
print(misspelled_words)
""" Results or Console Output
Output
['frmer', '', 'prabably', '', 'decidid', 'grw', 'kniw', 'hd', 'goe', '', 'aroudn', '', 'almosty', 'perserved', '', 'stoped', '', 'crzy', '10', '', 'undetered', 'alternatng', '', 'mich', '']
"""





"""
2: Multiple Return Paths
So far we've explored with functions that have one return statement, and therefore one flow of execution. However, we've also learned how to use if statements to express conditional logic and create multiple return paths. Adding multiple ways to return a value can stop the flow of execution earlier and make our code run faster. Let's examine what this looks like.

The flip_coin() function below expects a float input value, and will either return "Heads" or "Tails", depending on the value we pass in:


def flip_coin(heads_probability):
    if heads_probability >= 0.5:
        return("Heads")
    else:
        return("Tails")
Multiple return paths make our functions more robust and more general by allowing us to write code that captures a wider range of outcomes. If each function could only contain one return path, then we'd have to write the following two functions to replicate the above behavior:


def is_heads(heads_probability):
    if heads_probability >= 0.5:
        return("Heads")
​
def is_tails(heads_probability):
    if heads_probability < 0.5:
        return("Tails")
In the next step, we'll learn how to combine multiple return paths with optional arguments to make the tokenize() function more flexible.



"""



"""
3: Optional Arguments
After we clean up the story text, we'll need to tokenize both it and the vocabulary. The process for both is actually the same (splitting on the whitespace character). To make our code more reusable, we can technically use the tokenize() function on both files. The vocabulary list doesn't need cleaning, however, so we need a way to specify when we want the input string to clean, and only run the cleaning logic in those cases.

We can accomplish this by modifying the tokenize() function in a few ways. First, we can wrap the code that cleans the input string in an if statement, so that it only runs if the Boolean value that's associated with an argument named clean evaluates to True. Then, we can add clean to the definition for the tokenize() function. This way, whenever we want to clean the input string, we just set clean to the Boolean value True. When we don't, we set clean to the Boolean value False.

One downside to adding more arguments is that anyone using our function would need to spend more time deciding on the values for them. In contrast, all of the arguments in the current version of the function are currently required - we have to pass in a value for each one to avoid returning an error. To add an optional argument and save time, we could specify a default value for it. When we call that function, we won't be required to pass in that parameter, and the Python interpreter will resort to the default value instead.

In the following code block, we modify the definition for the tokenize() function by adding a new parameter named clean, and specifying a default value for it:


def tokenize(text_string, special_characters, clean=False):
We don't need to pass in a third parameter; instead, Python will set clean to False by default. We can then use the same tokenize() function for both the vocabulary and the story text:


# We want story_string cleaned, so we set the third parameter to `True`.
tokenized_story = tokenize(story_string, clean_chars, True)
# Since we didn't pass in a value for the third parameter, `clean` will be set to `False` by default.
tokenized_vocabulary = tokenize(vocabulary, clean_chars)
We're still not done, though. Even though we made the clean parameter optional, we need to still update the code in the body of our function to incorporate the clean parameter. By default, we don't want to clean text_string. We therefore need to check whether clean is True, and only clean text_string if it is.

Instructions
Modify the tokenize() function:
Use an if statement to check whether clean is True. If so:
Clean text_string using clean_text, and assign the returned string to a variable.
Tokenize the new string variable using the split() method, and assign the returned list to another new variable.
Return this list.
Outside the if statement, write the code we want executed if clean is False:
Tokenize text_string using the split() method, and assign the returned list to a new variable.
Return this list.
Outside the tokenize() function:
Use the tokenize() function to clean and tokenize story_string, and assign the result to tokenized_story.
Use the tokenize() function to tokenize vocabulary, and assign the result to tokenized_vocabulary.
Finally, loop over each element in tokenized_story and check whether it exists in tokenized_vocabulary. If it doesn't, add it to misspelled_words.

"""
# Default code
def tokenize(text_string, special_characters, clean=False):
    if clean == True:
        cleaned = clean_text(text_string, special_characters)
        cleaned_tokenized = cleaned.split(" ")
        return cleaned_tokenized
    story_tokens = text_string.split(" ")
    return(story_tokens)

tokenized_story = []
tokenized_vocabulary = []
misspelled_words = []
tokenized_story = tokenize(story_string,clean_chars,True)
tokenized_vocabulary = tokenize(vocabulary,clean_chars)
for string in tokenized_story:
    if string not in tokenized_vocabulary:
        misspelled_words.append(string)
print(misspelled_words)
""" Results or Console Output
Output
['frmer', 'julius.', '', 'village,', 'prabably', 'world.', '', 'day,', 'decidid', 'grw', 'potatoes.\n\n', 'grow,', 'kniw', 'hd', 'goe',
'guidance.', '', 'aroudn', 'day.', '', 'almosty', 'immediately.\n\n', "shouldn't", 'on,', 'perserved.', '', 'soaked,', 'stoped', 'umbrella.',
'', 'storekeeper,', 'reggie,', 'journey.\n\n', 'crzy', 'farmer;', '10', 'back.', '', 'undetered', 'going.\n\n', 'alternatng', 'cold.', '', 'night,',
 'roadside.\n\n', 'mich', 'anguish,', 'farmer,', 'potatoes.\n\n', 'village,', 'seen.', '', 'months,', "julius's", 'praises.']
"""




"""
4: Named Arguments
So far, we've been passing in arguments to the functions we've written in the same order in which we originally specified them in the function definition. The Python interpreter uses the positions of the arguments passed in to assign each one to a specific variable inside the function. They're known as positional arguments for this reason. However, remembering the exact order of the arguments can become difficult as we increase the number of them a function can take. This is especially true with optional arguments.

To help alleviate this problem, the Python interpreter allows us to pass in named arguments in any order. This allows us to be more explicit in assigning values to the variables inside the function. When we call a function, we assign each value to the variable from the function definition.

Under the hood, Python uses a dictionary to map the argument names to the values we want when we call the function. Then, it uses that dictionary to make the values we passed in available within the function. Let's see what this looks like in code:


# All three of these statements assign the same values to the function arguments.
tokenized_story = tokenize(clean=False, text_string = story_string, special_characters = clean_chars)
tokenized_story = tokenize(text_string = story_string, clean=False, special_characters = clean_chars)
tokenized_story = tokenize(special_characters = clean_chars, text_string = story_string, clean=False)
Notice that the parentheses in the code above now include equals signs (=) that assign values to named arguments.

Because optional arguments have defaults, we can leave out the clean parameter altogether.


tokenized_story = tokenize(text_string=story_string, special_characters=clean_chars)
In later courses, we'll explore external libraries that have functions containing 10 or more optional arguments. The programmers who made them took advantage of named and optional arguments to create flexible functions that can work for many different use cases.

The one caveat is that we can't have named parameters before positional arguments. When calling functions, we should specify the positional arguments first, and then the named arguments.

Instructions
Explore named arguments by uncommenting the starter code and running the different function calls.
Use the print() function to verify the returned values are the same across the different function calls.
Click Next once you're done exploring.

"""
clean_chars = [",", ".", "'", ";", "\n"]

# These three lines represent different ways of expressing the same function call.
tokenized_story = tokenize(clean=False, text_string = story_string, special_characters = clean_chars)
tokenized_story = tokenize(text_string = story_string, clean=False, special_characters = clean_chars)
tokenized_story = tokenize(special_characters = clean_chars, text_string = story_string, clean=False)

# These two lines represent different ways of expressing the same function call.
tokenized_vocabulary = tokenize(text_string=vocabulary, special_characters=clean_chars)
tokenized_vocabulary = tokenize(special_characters=clean_chars, text_string=vocabulary)
""" Results or Console Output

"""




"""
5: Practice: Creating A More Compact Spell Checker
Let's practice what we've learned about functions so far by creating a function containing all the logic for our spell checker. We'll be able to use this function in other projects by simply remembering the arguments it takes, rather than the specific logic behind how it works. This is especially critical when we're working with many team members, and on a much larger code base that could contain thousands of functions.

Instructions
Create a function called spell_check():
Include the following arguments:
vocabulary_file - the location of the vocabulary text file
text_file - the location of the text we want to spell check
special_characters - with the default value of the list [",",".","'",";","\n"].
In the function body:
Create an empty list and assign it to misspelled_words.
Read both files into strings using the open() and read() functions: open(vocabulary_file).read()
Call the tokenize() function to tokenize the string containing the vocabulary. Assign the result to tokenized_vocabulary.
Call the tokenize() function to clean and tokenize the string containing the text we want to spell check. Assign the result to tokenized_text.
Write a for loop that iterates over tokenized_text. For each token in tokenized_text:
Write an if statement that checks whether the token isn't in tokenized_vocabulary, and if it's not equal to ''.
If it meets both criteria, append the token to misspelled_words.
Outside the for loop, return misspelled_words.
After we've written the function, call spell_check:
Pass in story.txt as the text_file parameter.
Pass in dictionary.txt as the vocabulary_file parameter.
Use the default value for special_characters.
Assign the result to final_misspelled_words.
Use the print() function to display final_misspelled_words.

"""
def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters, clean=False):
    cleaned_text = text_string
    if clean:
        cleaned_text = clean_text(text_string, special_characters)
    tokens = cleaned_text.split(" ")
    return(tokens)

final_misspelled_words = []

def spell_check(vocabulary_file,text_file,special_characters=[",",".","'",";","\n"]):
    misspelled_words = []
    f1 = open(vocabulary_file,"r").read()
    f2 = open(text_file,"r").read()
    tokenized_vocabulary = tokenize(f1,special_characters)
    print(tokenized_vocabulary)
    print("------------")
    tokenized_text = tokenize(f2,special_characters,True)
    print(tokenized_text)
    print("------------")
    for string in tokenized_text:
        if (string not in tokenized_vocabulary) and (string != ''):
            misspelled_words.append(string)
    return misspelled_words
final_misspelled_words = spell_check("dictionary.txt","story.txt")
print(final_misspelled_words)
""" Results or Console Output

"""


"""
6: Types Of Errors
As we begin to take greater advantage of functions to organize our code, it can become more complex. We need to better understand the kinds of mistakes we can make when writing it. We've talked briefly about errors, or mistakes that prevent our code from working as we expect, in previous missions. Now it's time to learn more about them.

The two main types of errors are:

Syntax errors
Runtime errors
Before code can be run, it must be parsed by the Python interpreter and organized into a data structure that represents the flow and complexity of the code we wrote. If the interpreter encounters any code that doesn't adhere to Python's language rules, it halts the parsing and returns an error. Rich coding environments like Atom and IPython Notebook help us prevent these types of errors through syntax highlighting - a feature that displays different parts of our code (such as brackets) in different colors. Syntax highlighting makes it easier to read our code and spot errors. Some examples of syntax errors include:

Missing ending quotes or starting quotes
Using improper indentation
Using improper keywords
Runtime errors only occur when the code is actually running, which makes them harder to catch and prevent beforehand. Some examples of runtime errors include:

Calling a function before it's defined
Calling a method or attribute that the object doesn't contain
Attempting to convert a value to an incompatible data type
Let's explore some more specific examples of these types of errors.



"""




"""
7: Syntax Errors
Here's a simple example of a syntax error:


# Missing ending quotes.
the_answer = "42
When we run the above line of code, we'll get back an error message describing the mistake we made, as well as the Python interpreter's best guess as to where it occurred:

Imgur

Python uses the SyntaxError class to represent syntax errors, and displays the error message after the colon. The interpreter may sometimes struggle to pinpoint the problematic code that caused the error. In the following code block, for example, we attempt to define the find() function, but misspell the def keyword as de:


# `def` keyword misspelled as `de`.
de find():
    print("42")
The error message suggests that the mistake was in the function name, rather than the def keyword:

Imgur

Sometimes the Python interpreter will return an IndentationError instead of a SyntaxError. This object represents a more specific syntax error that makes it easier to debug our code. We'll see an IndentationError when the indentation in our code is inconsistent. Here's an example:


def find():
    print("42")
     print("what, really?")
Notice that the second print statement is indented differently than the first one (with one extra space). It also doesn't follow the indentation rules for code blocks such as if statements and for loops. It will return the following error:

Imgur

Let's practice debugging and fixing syntax errors in the spell checker code from the previous step.

Instructions
The starter code contains multiple syntax errors. Scan and edit the code to resolve these errors.
When you're ready, click Check to see if any errors are returned.

"""
def spell_check(vocabulary_file, text_file, special_characters=[",",".","'",";","\n"):
    misspelled_words = []
    vocabulary = open(vocabulary_file).read()
    text = open(text_file.read()

     tokenized_vocabulary = tokenize(vocabulary, special_characters)
    tokenized_text = tokenize(text, special_characters, True)

    for ts in tokenized_text:
        if ts not in tokenized_vocabulary and ts != '':
            misspelled_words.append(ts)
    return(misspelled_words)

final_misspelled_words = spell_check(vocabulary_file="dictionary.txt", text_file="story.txt")
print(final_misspelled_words)

"""
Become =>>>
"""

def spell_check(vocabulary_file, text_file, special_characters=[",",".","'",";","\n"]):
    misspelled_words = []
    vocabulary = open(vocabulary_file).read()
    text = open(text_file).read()

    tokenized_vocabulary = tokenize(vocabulary, special_characters)
    tokenized_text = tokenize(text, special_characters, True)

    for ts in tokenized_text:
        if ts not in tokenized_vocabulary and ts != '':
            misspelled_words.append(ts)
    return(misspelled_words)

final_misspelled_words = spell_check(vocabulary_file="dictionary.txt", text_file="story.txt")
print(final_misspelled_words)

""" Results or Console Output
Output
  File "<ipython-input-1-1e31be076bc7>", line 2
    def spell_check(vocabulary_file, text_file, special_characters=[",",".","'",";","\n"):
                                                                                        ^
SyntaxError: invalid syntax

=>>

Output
['frmer', 'prabably', 'decidid', 'grw', 'kniw', 'hd', 'goe', 'aroudn', 'almosty', 'perserved', 'stoped', 'crzy', '10', 'undetered', 'alternatng', 'mich']

"""




"""
8: Runtime Errors
Runtime errors are very common. While code often works in predictable situations, runtime errors occur when it fails at handling a case the programmer didn't account for.

Because runtime errors occur when our code is running and can't be detected during parsing, they're more difficult to prevent than syntax errors. As you become more proficient in programming, however, you'll learn to identify potential runtime errors beforehand and prevent them from occurring. Python and most other programming languages include tools like error handling and automated tests that help you manage and reduce runtime errors. As your code becomes more complex, you'll learn how to incorporate errors into the functions you write to so that they fail gracefully, and prevent certain negative behavior from occuring.

The documentation for Python 3.5 includes a full list of possible errors. If you glance at the hierarchy of errors here, the SyntaxError class is a small fraction of the entire tree of possibilities; the rest are runtime errors. Let's look at some examples of runtime errors.

"""





"""
9: TypeError And ValueError
In the following code, we try to concatenate a string and an integer. This returns a TypeError because the Python interpreter expects values being added to be the same type.


forty_two = 42
forty_two + "42"
Specifically, it returns the following error:

Imgur

You may have noticed that runtime errors look a little different. For example, the error appears twice (TypeError is in the top left and bottom left corners). In addition, the text Traceback (most recent call last) appears at the top right corner. The traceback displays all the code that was executed, ending with the most recent call that actually caused the error. While the code in this example is very simple, we'll explore some errors where the traceback is more useful later in this mission.

Another common runtime error is the ValueError, which is generated when the type is correct but the value is still improper. A ValueError is returned when we try to convert a string representing a non-numeric value into a numeric type, such as a float. Recall that we use the float() function to cast, or convert, a value to a float:


float("guardians")
The example above will return this error:

Imgur

While trying to cast a string to a float isn't automatically an issue (which is why there was no TypeError), the specific value that we tried to cast was problematic. The float() function didn't know how to cast "guardians" into a float, and returned an instance of ValueError instead.

Instructions
The code cell contains the sample code from this step. Experiment with it to explore other runtime errors.
You could try:
Concatenating an integer to a string, instead of the other way around
Casting "guardians" into an integer instead using the int() function
When you're done exploring, click Next to move onto the next step.

"""
forty_two = 42
forty_two + "42"

float("guardians")

"""
Become =>>>
"""


""" Results or Console Output
TypeErrorTraceback (most recent call last)
<ipython-input-1-bfa12cc5c32c> in <module>()
      1 import numpy;import pandas;import random;import io;random.seed(1);numpy.random.seed(1);import matplotlib.pyplot as plt
      2 forty_two = 42
----> 3 forty_two + "42"
      4
      5 float("guardians")

TypeError: unsupported operand type(s) for +: 'int' and 'str'

=>>>



"""





"""
10: IndexError And AttributeError
The IndexError is a common error that's returned when we try to access an element that's not in a list's index. Trying to access the fifth element in a list containing only two elements would return this error, for example. Here's what this looks like:


lives = [1,2,3]
lives[4]
The example above will return the following error:

Imgur

Since there's no value at index four, an IndexError is returned, along with an arrow pointing to the problematic line of code. If we're working with a list and don't know its length, use the len() function to look up the number of elements before attempting to access them.

The final runtime error we'll explore is the AttributeError. This occurs when we try to call a method or attribute on an object that doesn't contain it. In the following code, we try to call the split() method on the File handler instance, instead of using the read() method to read it into a string first:


f = open("story.txt")
f.split(" ")
Here's the error that's returned:

Imgur

TextIOWrapper is a built-in Python object that represents the File handler. It does not contain the split() method. Since the Python interpreter couldn't find the split() method within the TextIOWrapper class, it returned an instance of AttributeError.



"""




"""
11: Traceback
When calling a function that uses other functions, our function calls become nested. This can make it harder to debug, since the code that triggered the error is usually inside the function, and different than the code we called. In the following example, we try to pass an integer in to the special_characters parameter. This is problematic because the code in the spell_check() body was written under the assumption that special_characters would always be a list of strings:

Imgur

The traceback shows the series of function calls that occurred. The topmost function call is the highest level of code we wrote, and oftentimes the section we need to fix. The last function call is where the error actually occurred.

Instructions
Edit the default code and remove the error.
Don't set a value for the special_characters argument. Instead, let the spell_check() function use the default value for it.

"""
def spell_check(vocabulary_file, text_file, special_characters=[",",".","'",";","\n"]):
    misspelled_words = []
    vocabulary = open(vocabulary_file).read()
    # Add ending parentheses.
    text = open(text_file).read()

    # Fix indentation.
    tokenized_vocabulary = tokenize(vocabulary, special_characters)
    tokenized_text = tokenize(text, special_characters, True)

    for ts in tokenized_text:
        if ts not in tokenized_vocabulary and ts != '':
            misspelled_words.append(ts)
    return(misspelled_words)

final_misspelled_words = spell_check(vocabulary_file="dictionary.txt", text_file="story.txt", special_characters=1)
print(final_misspelled_words)

"""
become =>>>
"""

def spell_check(vocabulary_file, text_file, special_characters=[",",".","'",";","\n"]):
    misspelled_words = []
    vocabulary = open(vocabulary_file).read()
    # Add ending parentheses.
    text = open(text_file).read()

    # Fix indentation.
    tokenized_vocabulary = tokenize(vocabulary, special_characters)
    tokenized_text = tokenize(text, special_characters, True)

    for ts in tokenized_text:
        if ts not in tokenized_vocabulary and ts != '':
            misspelled_words.append(ts)
    return(misspelled_words)

final_misspelled_words = spell_check(vocabulary_file="dictionary.txt", text_file="story.txt")
print(final_misspelled_words)

""" Results or Console Output
Output

TypeErrorTraceback (most recent call last)
<ipython-input-1-132549c00ff8> in <module>()
     15     return(misspelled_words)
     16
---> 17 final_misspelled_words = spell_check(vocabulary_file="dictionary.txt", text_file="story.txt", special_characters=1)
     18 print(final_misspelled_words)

<ipython-input-1-132549c00ff8> in spell_check(vocabulary_file, text_file, special_characters)
      8     # Fix indentation.
      9     tokenized_vocabulary = tokenize(vocabulary, special_characters)
---> 10     tokenized_text = tokenize(text, special_characters, True)
     11
     12     for ts in tokenized_text:

<ipython-input-1-411653249ddf> in tokenize(text_string, special_characters, clean)
     10     cleaned_text = text_string
     11     if clean:
---> 12         cleaned_text = clean_text(text_string, special_characters)
     13     tokens = cleaned_text.split(" ")
     14     return(tokens)

<ipython-input-1-411653249ddf> in clean_text(text_string, special_characters)
      2 def clean_text(text_string, special_characters):
      3     cleaned_string = text_string
----> 4     for string in special_characters:
      5         cleaned_string = cleaned_string.replace(string, "")
      6     cleaned_string = cleaned_string.lower()

TypeError: 'int' object is not iterable

=>>>

Output
['frmer', 'prabably', 'decidid', 'grw', 'kniw', 'hd', 'goe', 'aroudn', 'almosty', 'perserved', 'stoped', 'crzy', '10', 'undetered', 'alternatng', 'mich']

"""




"""
12: Next Steps
In this mission, we customized functions in new ways, practiced using these techniques to create a compact spell checker function, and learned how to identify and debug common errors.
These strategies will help you account for potential errors and write code that's easier to maintain.
Next in this course is your first guided project, where we'll explore how to use the Jupyter notebook environment for writing code, exploring data, and more.
"""
