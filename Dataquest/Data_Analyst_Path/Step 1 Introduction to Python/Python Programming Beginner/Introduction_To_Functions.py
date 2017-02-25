""" 01/2017
Dataquest : Data Analyst Path
Step 1: Introduction To Python
SubStep : Python Programming: Beginner : Introduction to Functions
"""


"""
"""


"""
1: Overview
In this mission, we'll explore how to build a basic spell checker. Spell checkers work by comparing each word in a passage of text with a set of correctly spelled words. In this mission, we'll learn how to:

Read in a vocabulary of correctly spelled words from a text file
Use more string methods to process text data
Create functions that allow us to more easily reuse our spell checker's components
The file dictionary.txt is a plain text file containing a sequence of correctly spelled words.
Plain text files don't have to adhere to the CSV standard.
This means that we'll need to explore the file to understand how to parse it. dictionary.txt consists of 1 line of text that separates each word with a single whitespace (" "). Here's a preview:

Because the file consists of a single line, the preview above truncates most of the text. Reading a plain text file into a string is similar to reading a CSV file into a string. The main difference is how we split the file. Each line (representing a row) in a CSV file is separated by the newline character (\n), and each value in a line is separated by the comma delimiter (,). To refresh your memory, here's what a CSV file looks like:

Instructions
Read the file dictionary.txt into a string variable named vocabulary.
Then, display vocabulary using the print() function.


"""
vocabulary = open("dictionary.txt","r").read()
print(vocabulary)
""" Results or Consol Output
Output
a about after almost along alternating an and anguish around at back ball became best but buy came cold come crop crazy curled day days
decided decided eat even ever everyone farmer farmer find finest for found freezing farmer gave go going great grow growing guidance had
hard he heat him his if immediately in into it journey julius juliuss keep knew last long magic managed many much months named never night
noble noon of on once one out people persevered potatoes probably praises raining reggie roadside sang searing secret seek seen set shouldnt
sign sky sleep so soaked started stopped store storekeeper that the there this to told travelled trees tried try umbrella underneath undeterred
village was were who whole wondered world

"""



"""
2: Tokenizing The Vocabulary
Before we can compare each word in a piece of text against each word in our vocabulary, we need to convert the vocabulary to a list. We call the process of converting text into a set of individual components tokenization. This is an important step when working with any text data. The goal of tokenization is to convert a large body of text into smaller tokens, or components, that we can work with. In this case, each token is a word in the vocabulary.

When we displayed the string vocabulary using the print() function, you may have noticed that the output was displayed on a single line. While CSV files have a widely accepted standard, plain text files don't. This means that when we're trying to read in a plain text file, we need to explore the file and understand its structure first. Rather than a table with many rows and columns, the string vocabulary resembles a single row of words, each separated by the whitespace character (" "). We need to split vocabulary on the whitespace character to convert our vocabulary of correctly spelled words to a list.

Instructions
Use the string method split() to split vocabulary on the whitespace character (' ').
Assign the resulting list to tokenized_vocabulary.
Display the first five elements in tokenized_vocabulary.

"""
vocabulary = open("dictionary.txt", "r").read()
tokenized_vocabulary = vocabulary.split(' ')
print(tokenized_vocabulary[0:5])
""" Results or Consol Output
Output
['a', 'about', 'after', 'almost', 'along']

"""





"""
3: Replacing Special Characters
The file story.txt contains a few paragraphs of text that we'll spell check.
Each paragraph consists of one or more sentences on a single line; in other words, the paragraphs end with the newline character.
An empty line separates each paragraph. Here's a preview of the file:

You may have noticed that some of the words in the story are connected to punctuation marks, or special characters (such as , and ;). Before we can tokenize the story, we need to remove the special characters, which aren't actually part of the words.

We'll also need to remove the newline characters so we can split the lines on the whitespace delimiter. We can accomplish this by using the string method replace() to replace all instances of a character with another one. This method takes two arguments:

The string we want to remove
The string that should take its place
The replace() method returns a new copy of the string with the substitutions we specify. The following example replaces all commas (,) with whitespace characters (""):


text = "Howdy,my,name"
text = text.replace(",", "")
The string text no longer contains commas, and is now "Howdymyname".

Instructions
We've read story.txt into the string story_string, and used the replace() method to remove all periods (.) and commas (,). Next, add code that removes single quotes ('), semi-colons (;), and newline characters ("\n").

"""
f = open("story.txt", 'r')
story_string = f.read()

print(story_string)
story_string = story_string.replace(".","")
story_string = story_string.replace(",","")
story_string = story_string.replace("'","")
story_string = story_string.replace(";","")
story_string = story_string.replace("\n","")
""" Results or Consol Output


"""








"""
4: Functions
We'd like to be able to use our spell checker on any text file - not just story.txt. Because we'll always need to remove the punctuation from the file we want to spell check, we can bundle the code we wrote to do that as a function, then run the function each time we need it. A function works by taking an input value, running a specific block of code, and returning another value. For example, we've used the type() function, which:

Accepts an input value
Looks up the input value's class
Returns that class
Instead of figuring out how to look up an object's type and writing the code from scratch, we can simply use Python's type() function. This saves us a significant amount of time, because we can take advantage of functions others have written and perfected, without having to implement the solution ourselves.

We can also write and reuse our own functions. For example, we could write a function that:

Accepts an input value (a string)
Strips the punctuation from the input string
Returns the new, cleaned string
Functions play a few key roles when writing code:

They allow us to use other people's code without a deep understanding of how it was written (e.g., we used the type() function without reading the code inside it). We call this information hiding.
They break down complex logic into smaller components or modules. We refer to this as modularity, which is especially important when working on teams. Modularity makes it easier for someone else to read, understand, use, and build upon our code.
They streamline our code and make it easier to maintain. Programmers reuse the same functions in multiple situations across a project. That means they generalize the function as much as possible to maximize its usefulness. we call this process abstraction, which is an important part of reducing our code's complexity, especially for larger projects.
Now that we've laid out some of the benefits of functions, lets dive into the syntax!



"""








"""
5: Practice: Creating A Function That Cleans Text
A function includes the following five parts:

the def keyword - Defines the function
Function name - The name of the function
Arguments - The optional input values
Function body - The code within the function
Return value - The optional value that's returned
Let's look at a simple function named clean_text() that replaces all commas (,) with blank spaces (""), and then returns the resulting string. Note that a blank space ("") is different from a single whitespace character (" "):


def clean_text(string_value):
    cleaned_value = string_value.replace(",", "")
    return(cleaned_value)
sentence = "Howdy,james,bond!"
sentence = clean_text(sentence)
Let's walk through the code. The function above:

Takes in a single input value named string_value
Replaces all commas in string_value with blank spaces
Assigns the new string to cleaned_value
Returns cleaned_value to the code that called the function
The syntax for creating a function is similar to that used in a for loop. Both of these:

Require us to indent each level of code by four spaces
Allow us to use a temporary variable in the definition syntax, which we can then refer to in the body
Unlike a for loop, a function can return a value to the code that called it. For example, we passed cleaned_value in to the return() statement, which is assigned to the variable sentence. return() will return the value associated with cleaned_value, overwriting sentence.

Note that any code in the function after the return statement doesn't execute:


def clean_text(string_value):
    cleaned_value = string_value.replace(",", "")
    return(cleaned_value)
    # This doesn't get executed!
    cleaned_value = cleaned_value.replace(":", "")
​
sentence = "Howdy,james,bond!"
sentence = clean_text(sentence)
To practice what we've learned so far, complete the logic for the clean_text() function.

Instructions
Finish the clean_text() function by adding in code that:
Replaces all periods (.) in cleaned_string with blank spaces, and assigns the resulting string object to cleaned_string.
Replaces all commas (,) in cleaned_string with blank spaces, and assigns the resulting string object to cleaned_string
Replaces all single quotes (') in cleaned_string with blank spaces, and assigns the resulting string object to cleaned_string
Replaces all semi-colons (;) in cleaned_string with blank spaces, and assigns the resulting string object to cleaned_string
Replaces all newline characters ("\n") in cleaned_string with blank spaces, and assigns the resulting string object to cleaned_string
Returns cleaned_string
Once you've completed the clean_text() function:
Call the clean_text() function.
Pass in story_string.
Assign the result to cleaned_story.

"""
f = open("story.txt", 'r')
story_string = f.read()

def clean_text(text_string):
    cleaned_string = text_string.replace(".","")
    cleaned_string = cleaned_string.replace(",","")
    cleaned_string = cleaned_string.replace("'","")
    cleaned_string = cleaned_string.replace(";","")
    cleaned_string = cleaned_string.replace("\n","")
    return cleaned_string

cleaned_story = clean_text(story_string)
""" Results or Consol Output

"""




"""
6: Changing Word Case
Some of the words in our story text contain uppercase letters (e.g. J in the word Julius), while our vocabulary (stored in tokenized_vocabulary) is in all lowercase. To compare the two, we'll need to change the uppercase letters in the story to lowercase.

We can use the string method lower() to convert all of the characters in a string to lowercase. In the following code block, we use the string method lower() to change all of the letters in words to lowercase, and assign the returned string to lower_words.


words = "Michael JACKSON Thriller"
lower_words = words.lower()
lower_words now contains the string "michael jackson thriller". You'll notice that all uppercase characters were converted to lowercase, while the existing lowercase characters were untouched.

Instructions
Modify the clean_text() function so that it converts cleaned_string to lowercase before returning it.

"""
def clean_text(text_string):
    cleaned_string = text_string.replace(",","")
    cleaned_string = cleaned_string.replace(".","")
    cleaned_string = cleaned_string.replace("'", "")
    cleaned_string = cleaned_string.replace(";", "")
    cleaned_string = cleaned_string.replace("\n", "")
    return(cleaned_string.lower())
cleaned_story = clean_text(story_string)
""" Results or Consol Output


"""





"""
7: Multiple Arguments
While the clean_text() function we have right now is useful for story.txt, we didn't set it up to handle other files. To clean multiple stories with different sets of special characters, we'd have to modify the function each time, which can be very cumbersome. This means that our clean_text() function isn't reusable enough.

To improve it, we can set it up so that we can pass in the special characters we want to remove as additional arguments. Instead of specifying a single argument (text_string), we can enter multiple arguments and separate them with commas. Using multiple arguments (instead of manually assigning variables within the functions themselves) allows us to write more general functions that work for a wider range of use cases.

Before we modify our clean_text() function, let's look at some examples of using multiple arguments. In the following code, we define a function strip_text() that removes all instances of a specific string that we specify using the strip_string argument:


def strip_text(text_string, strip_string):
    replacement_string = ""
    cleaned_string = text_string.replace(strip_string, replacement_string)
​
    return(cleaned_string)
​
howdy_1 = strip_text("Howdy!", "!")
howdy_2 = strip_text("Howdy...", ".")
The code above assigns the same string "Howdy" to both howdy_1 and howdy_2. We hard coded the value for replacement_string ("") - the new string that should replace all instances of the strip_string - within the function. However, we can specify that we want to pass in replacement_string as an argument instead:


def strip_text(text_string, strip_string, replacement_string):
    cleaned_string = text_string.replace(strip_string, replacement_string)
    return(cleaned_string)
howdy_1 = strip_text("Howdy!", "!", "")
howdy_2 = strip_text("Howdy...", ".", "")
While this version of the code gives the same results, our function is more general, and we can use it across a wider range of situations. Let's modify our clean_text() function in a similar way. Change the code so that the function takes an additional argument - a list of strings corresponding to the special characters we want to remove.

Instructions
Modify the clean_text() function below in the following ways:
Add another argument called special_characters.
Modify the function body so that it loops over all special_characters that are punctuation marks, and removes each one:
Assign the input variable text_string to cleaned_string.
Write a for loop that:
Iterates over the input variable special_characters.
Uses replace() to remove all of the instances of the current special character in cleaned_string.
Outside the loop, use lower() to make all the text in cleaned_string lowercase, and then return it.
Once you've written the function, run clean_text():
Pass in story_string as the first argument.
Pass in clean_chars as the second argument.
Assign the result to cleaned_story.
Print cleaned_story.


"""
f = open("story.txt", 'r')
story_string = f.read()
clean_chars = [",", ".", "'", ";", "\n"]

# Previous code for clean_text().
def clean_text(text_string,special_characters):
    cleaned_string = text_string
    for sc in special_characters:
        cleaned_string = cleaned_string.replace(sc,"")
    return(cleaned_string.lower())

cleaned_story = clean_text(story_string,clean_chars)
print(cleaned_story)
""" Results or Consol Output
Output
there was once a great and noble frmer named julius  he was the best farmer in his village and prabably even the whole world
one day he decidid to grw potatoes julius knew that potatoes were hard to grow so he kniw he hd to goe to the magic farmer
in the sky to seek his guidance  julius set out on his journey aroudn noon one day  it started raining almosty immediately julius
wondered if this was a sign that he shouldnt go on but he perserved  he became soaked and stoped in the store to buy an umbrella
he told the storekeeper reggie about his journey reggie told him that he was crzy to seek out the magic farmer the last 10 people
to try to find him had never come back  julius was undetered and decided to keep going he travelled many long days in alternatng
searing heat and freezing cold  at night he curled into a ball and tried to sleep underneath trees along the roadside after mich anguish
julius found the magic farmer who gave him the secret of growing potatoes julius came back to the village and managed to grow the finest
crop the village had ever seen  everyone had potatoes to eat for months and sang juliuss praises

"""




"""
8: Tokenizing The Story
Now that we have a function that cleans up the story, let's tokenize it from a string into a list. A whitespace character (\" \") separates each word in cleaned_story. We can use the string method split() to split cleaned_story on a single whitespace character and return a list of tokens.

In the spirit of making our code more reusable, let's create a new function called tokenize() that both cleans and tokenizes the story text. Python allows us to call a function from within another function, which means we can call the clean_text() function from within the tokenize() function. This allows us to separate the concerns of each of these functions:

The tokenize() function focuses on converting a string to a list of tokens.
The clean_text() function focuses on cleaning a string.
Using functions to separate tasks spares us from having to write the same code in multiple places. It also makes it easier for others to understand our code. Doing this will become more important as our projects increase in complexity.

Instructions
Create a new function called tokenize():
Include the following arguments:
text_string - First argument, for the string we want to clean and tokenize
special_characters - Second argument, for the list of strings representing the special characters we want to replace
In the function body:
Clean text_string by calling the clean_text() function, and assign the result to cleaned_story.
Tokenize cleaned_story by splitting on a single whitespace character (" "), and assign the resulting list to story_tokens.
Return story_tokens.
After you've created the tokenize() function:
Call the tokenize() function. Pass in story_string as the first argument and clean_chars as the second argument.
Assign the result to tokenized_story.
Finally, print the first 10 values in tokenized_story.


"""
def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

clean_chars = [",", ".", "'", ";", "\n"]
cleaned_story = clean_text(story_string, clean_chars)
def tokenize(text_string,special_characters):
    cleaned_story = clean_text(story_string, clean_chars)
    story_tokens = cleaned_story.split(" ")
    return story_tokens
tokenized_story = tokenize(story_string, clean_chars)
print(tokenized_story[0:10])
""" Results or Consol Output
Output
['there', 'was', 'once', 'a', 'great', 'and', 'noble', 'frmer', 'named', 'julius']

"""







"""
9: Finding Misspelled Words
Now that we have tokenized versions of both the story and the vocabulary, we can run our spell checker. Recall that we want to compare each word in the tokenized story with each word in the tokenized vocabulary, and return all tokens not found in the vocabulary.

Instructions
Create an empty list named misspelled_words.
Write a for loop that:
Iterates over tokenized_story.
Uses an if statement that evaluates whether the current token is in tokenized_vocabulary and if it isn't, appends the current token to misspelled_words.
Print misspelled_words.


"""
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

misspelled_words = []
for token in tokenized_story:
    if token not in tokenized_vocabulary:
        misspelled_words.append(token)
print(misspelled_words)
""" Results or Consol Output
Output
['frmer', '', 'prabably', '', 'decidid', 'grw', 'kniw', 'hd', 'goe', '', 'aroudn', '', 'almosty', 'perserved', '', 'stoped', '', 'crzy', '10', '', 'undetered', 'alternatng', '', 'mich', '']

"""



"""
10: Next Steps
You'll notice that many of the elements in misspelled_words were empty whitespace characters (""), rather than true misspellings. We'll devise a way to handle this issue in the next mission. We'll also explore other ways to customize function behavior, and learn to use error messages to debug our code.
"""
