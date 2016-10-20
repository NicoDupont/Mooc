#PygLatin

"""
Break It Down

Now let's take what we've learned so far and write a Pig Latin translator.

Pig Latin is a language game, where you move the first letter of the word to the end and add "ay." So "Python" becomes "ythonpay." To write a Pig Latin translator in Python, here are the steps we'll need to take:

    Ask the user to input a word in English.
    Make sure the user entered a valid word.
    Convert the word from English to Pig Latin.
    Display the translation result.

Instructions

When you're ready to get coding, click Save and Submit. Since we took the time to write out the steps for our solution, you'll know what's coming next!
"""

"""

Ahoy! (or Should I Say Ahoyay!)

Let's warm up by printing a welcome message for our translator users.
Instructions

    Please print the phrase "Pig Latin".
"""

print "Pig Latin"


"""
Input!

Next, we need to ask the user for input.

name = raw_input("What's your name?")
print name

In the above example, raw_input() accepts a string, prints it, and then waits for the user to type something and press Enter (or Return).

In the interpreter, Python will ask:

What's your name? >

Once you type in your name and hit Enter, it will be stored in name.
Instructions

    On line 4, use raw_input("Enter a word:") to ask the user to enter a word. Save the results of raw_input() in a variable called original.
    Click Save & Submit Code
    Type a word in the console window and press Enter (or Return).
"""

print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word")


"""

Check Yourself!

Next we need to ensure that the user actually typed something.

empty_string = ""
if len(empty_string) > 0:
    # Run this block.
    # Maybe print something?
else:
    # That string must have been empty.

We can check that the user's string actually has characters!
Instructions

Write an if statement that verifies that the string has characters.

    Add an if statement that checks that len(original) is greater than zero. Don't forget the : at the end of the if statement!
    If the string actually has some characters in it, print the user's word.
    Otherwise (i.e. an else: statement), please print "empty".

You'll want to run your code multiple times, testing an empty string and a string with characters. When you're confident your code works, continue to the next exercise.
"""

print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word")
if len(original) > 0:
    print original
else:
    print "empty"
        

 # res :
 """
 Welcome to the Pig Latin Translator!
Enter a word test
test
"""


"""
Check Yourself... Some More

Now we know we have a non-empty string. Let's be even more thorough.

x = "J123"
x.isalpha()  # False

In the first line, we create a string with letters and numbers.

The second line then runs the function isalpha() which returns False since the string contains non-letter characters.

Let's make sure the word the user enters contains only alphabetical characters. You can use isalpha() to check this! For example:
Instructions

Use and to add a second condition to your if statement. In addition to your existing check that the string contains characters, you should also use .isalpha() to make sure that it only contains letters.

Don't forget to keep the colon at the end of the if statement!
"""

print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word")
if len(original) > 0 and original.isalpha():
    print original
else:
    print "empty"

"""

Pop Quiz!

When you finish one part of your program, it's important to test it multiple times, using a variety of inputs.
Instructions

Take some time to test your current code. Try some inputs that should pass and some that should fail. Enter some strings that contain non-alphabetical characters and an empty string.

When you're convinced your code is ready to go, click Save & Submit to move forward!
"""

print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word")
if len(original) > 0 and original.isalpha():
    print original
else:
    print "empty"


"""
Ay B C

Now we can get ready to start translating to Pig Latin! Let's review the rules for translation:

You move the first letter of the word to the end and then append the suffix 'ay'.
Example: python -> ythonpay

Let's create a variable to hold our translation suffix.
Instructions

Create a variable named pyg and set it equal to the suffix 'ay'.
"""

pyg = "ay"


"""

Word Up

Let's simplify things by making the letters in our word lowercase.

the_string = "Hello"
the_string = the_string.lower()

The .lower() function does not modify the string itself, it simply returns a lowercase-version. In the example above, we store the result back into the same variable.

We also need to grab the first letter of the word.

first_letter  = the_string[0]
second_letter = the_string[1]
third_letter  = the_string[2]

Remember that we start counting from zero, not one, so we access the first letter by asking for [0].
Instructions

Inside your if statement:

    Create a new variable called word that holds the .lower()-case conversion of original.
    Create a new variable called first that holds word[0], the first letter of word.

"""

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'

word = original.lower()
first = word[0]


"""

Move it on Back

Now that we have the first letter stored, we need to add both the letter and the string stored in pyg to the end of the original string.

Remember how to concatenate (i.e. add) strings together?

greeting = "Hello "
name = "D. Y."
welcome = greeting + name

Instructions

On a new line after where you created the first variable:

Create a new variable called new_word and set it equal to the concatenation of word, first, and pyg.
"""

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'

word = original.lower()
first = word[0]
new_word = word + first + pyg


"""
Ending Up

Well done! However, now we have the first letter showing up both at the beginning and near the end.

s = "Charlie"

print s[0]
# will print "C"

print s[1:4]
# will print "har"

    First we create a variable s and give it the string "Charlie"
    Next we access the first letter of "Charlie" using s[0]. Remember letter positions start at 0.
    Then we access a slice of "Charlie" using s[1:4]. This returns everything from the letter at position 1 up till position 4.

We are going to slice the string just like in the 3rd example above.
Instructions

Set new_word equal to the slice from the 1st index all the way to the end of new_word. Use [1:len(new_word)] to do this.
"""

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'

word = original.lower()
first = word[0]
new_word = word + first + pyg

s = "Charlie"
print s[0]
new_word = new_word[1:len(new_word)]

# sortie :
"""
Enter a word: test
test
C
"""

"""
Testing, Testing, is This Thing On?

Yay! You should have a fully functioning Pig Latin translator. Test your code thorougly to be sure everything is working smoothly.

You'll also want to take out any print statements you were using to help debug intermediate steps of your code. Now might be a good time to add some comments too! Making sure your code is clean, commented, and fully functional is just as important as writing it in the first place.
Instructions

When you're sure your translator is working just the way you want it, click Save & Submit Code to finish this project.
"""

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'

word = original.lower()
first = word[0]
new_word = word + first + pyg

s = "Charlie"
print s[0]
#récupérer 1 jusqu'a la fin
new_word = new_word[1:len(new_word)]
print new_word

"""
sortie :
Enter a word: test
test
C
esttay
"""
