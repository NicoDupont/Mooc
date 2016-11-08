# Datacamp - Python For Data Science Toolbox (Part 1)
# partie 2 : Scope and user-defined functions
# Python 3.X



"""   réponse : 4
Pop quiz on understanding scope
50xp

In this exercise, you will practice what you've learned about scope in functions. The variable num has been predefined as 5, alongside the following function definitions:

def func1():
    num = 3
    print(num)

def func2():
    global num
    double_num = num * 2
    num = 6
    print(double_num)

Try calling func1() and func2() in the shell, then answer the following questions:

    What are the values printed out when you call func1() and func2()?
    What is the value of num in the global scope after calling func1() and func2()?

Possible Answers

    func1() prints out 3, func2() prints out 6, and the value of num in the global scope is 3.
    1
    func1() prints out 3, func2() prints out 3, and the value of num in the global scope is 3.
    2
    func1() prints out 3, func2() prints out 10, and the value of num in the global scope is 10.
    3
    func1() prints out 3, func2() prints out 10, and the value of num in the global scope is 6.
    4
"""

""" sortie Ipython
In [1]: def func1():
...     num = 3
...     print(num)
... 
... def func2():
...     global num
...     double_num = num * 2
...     num = 6
...     print(double_num)

In [2]: func1()
3

In [3]: func2()
10

In [4]: num
Out[4]: 6
"""





"""  
The keyword global
100xp

Let's work more on your mastery of scope. In this exercise, you will use the keyword global within a function to alter the value of a variable defined in the global scope.
Instructions

    Use the keyword global to alter the object team in the global scope.
    Change the value of team in the global scope to the string "justice league". Assign the result to team.
    Hit the Submit button to see how executing your newly defined function change_team() changes the value of the name team!

"""
# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team

    # Change the value of team in global: team
    team = "justice league"
# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)
""" sortie Ipython
<script.py> output:
    teen titans
    justice league
"""





"""   quetion réponse : 3
Python's built-in scope
50xp

Here you're going to check out Python's built-in scope, which is really just a built-in module called builtins. However, to query builtins, you'll need to import builtins 'because the name builtins is not itself built in...No, I’m serious!' (Learning Python, 5th edition, Mark Lutz). After executing import builtins in the IPython Shell, execute dir(builtins) to print a list of all the names in the module builtins. Have a look and you'll see a bunch of names that you'll recognize! Which of the following names is NOT in the module builtins?
Possible Answers

    'sum'
    1
    'range'
    2
    'array'
    3
    'tuple'
    4
"""

""" sortie Ipython
In [1]: import builtins

In [2]: dir(builtins)
Out[2]: 
['ArithmeticError',
 'AssertionError',
 'AttributeError',
 'BaseException',
 'BlockingIOError',
 'BrokenPipeError',
 'BufferError',
 'BytesWarning',
 'ChildProcessError',
 'ConnectionAbortedError',
 'ConnectionError',
 'ConnectionRefusedError',
 'ConnectionResetError',
 'DeprecationWarning',
 'EOFError',
 'Ellipsis',
 'EnvironmentError',
 'Exception',
 'False',
 'FileExistsError',
 'FileNotFoundError',
 'FloatingPointError',
 'FutureWarning',
 'GeneratorExit',
 'IOError',
 'ImportError',
 'ImportWarning',
 'IndentationError',
 'IndexError',
 'InterruptedError',
 'IsADirectoryError',
 'KeyError',
 'KeyboardInterrupt',
 'LookupError',
 'MemoryError',
 'NameError',
 'None',
 'NotADirectoryError',
 'NotImplemented',
 'NotImplementedError',
 'OSError',
 'OverflowError',
 'PendingDeprecationWarning',
 'PermissionError',
 'ProcessLookupError',
 'RecursionError',
 'ReferenceError',
 'ResourceWarning',
 'RuntimeError',
 'RuntimeWarning',
 'StopAsyncIteration',
 'StopIteration',
 'SyntaxError',
 'SyntaxWarning',
 'SystemError',
 'SystemExit',
 'TabError',
 'TimeoutError',
 'True',
 'TypeError',
 'UnboundLocalError',
 'UnicodeDecodeError',
 'UnicodeEncodeError',
 'UnicodeError',
 'UnicodeTranslateError',
 'UnicodeWarning',
 'UserWarning',
 'ValueError',
 'Warning',
 'ZeroDivisionError',
 '__IPYTHON__',
 '__IPYTHON__active',
 '__build_class__',
 '__debug__',
 '__doc__',
 '__import__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'abs',
 'all',
 'any',
 'ascii',
 'bin',
 'bool',
 'bytearray',
 'bytes',
 'callable',
 'chr',
 'classmethod',
 'compile',
 'complex',
 'copyright',
 'credits',
 'delattr',
 'dict',
 'dir',
 'divmod',
 'dreload',
 'enumerate',
 'eval',
 'exec',
 'filter',
 'float',
 'format',
 'frozenset',
 'get_ipython',
 'getattr',
 'globals',
 'hasattr',
 'hash',
 'help',
 'hex',
 'id',
 'input',
 'int',
 'isinstance',
 'issubclass',
 'iter',
 'len',
 'license',
 'list',
 'locals',
 'map',
 'max',
 'memoryview',
 'min',
 'next',
 'object',
 'oct',
 'open',
 'ord',
 'pow',
 'print',
 'property',
 'range',
 'repr',
 'reversed',
 'round',
 'set',
 'setattr',
 'slice',
 'sorted',
 'staticmethod',
 'str',
 'sum',
 'super',
 'tuple',
 'type',
 'vars',
 'zip']
"""






"""  
Nested Functions I
100xp

You've learned in the last video about nesting functions within functions. One reason why you'd like to do this is to avoid writing out the same computations within functions repeatedly. There's nothing new about defining nested functions: you simply define it as you would a regular function with def and embed it inside another function!

In this exercise, inside a function three_shouts(), you will define a nested function inner() that concatenates a string object with !!!. three_shouts() then returns a tuple of three elements, each a string concatenated with !!! using inner(). Go for it!
Instructions

    Complete the function header of the nested function with the fuction name inner() and a single parameter word.
    Complete the return value: each element of the tuple should be a call to inner(), passing in the parameters from three_shouts() as arguments to each call.

"""
# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))
""" sortie Ipython
<script.py> output:
    ('a!!!', 'b!!!', 'c!!!')
"""





"""  
Nested Functions II
100xp
Great job, you've just nested a function within another function. One other pretty cool reason for nesting functions is the idea of a closure. This means that the nested or inner function remembers the state of its enclosing scope when called. Thus, anything defined locally in the enclosing scope is available to the inner function even when the outer function has finished execution.

Let's move forward then! In this exercise, you will complete the definition of the inner function inner_echo() and then call echo() a couple of times, each with a different argument. Complete the exercise and see what the output will be!

Instructions
Complete the function header of the inner function with the function name inner_echo() and a single parameter word1.
Complete the function echo() so that it returns inner_echo.
We have called echo(), passing 2 as an argument, and assigned the resulting function to twice. Your job is to call echo(), passing 3 as an argument. Assign the resulting function to thrice.
Hit Submit to call twice() and thrice() and print the results.
"""
# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))
""" sortie Ipython
<script.py> output:
    hellohello hellohellohello
"""





"""  
The keyword nonlocal and nested functions
100xp
Let's once again work further on your mastery of scope! In this exercise, you will use the keyword nonlocal within a nested function to alter the value of a variable defined in the enclosing scope.

Instructions
Assign to echo_word the string word, concatenated with itself.
Use the keyword nonlocal to alter the value of echo_word in the enclosing scope.
Alter echo_word to echo_word concatenated with '!!!'.
Call the function echo_shout(), passing it a single argument 'hello'.
"""
# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""
    
    # Concatenate word with itself: echo_word
    echo_word = word * 2
    
    #Print echo_word
    print(echo_word)
    
    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""    
        #Use echo_word in nonlocal scope
        nonlocal echo_word
        
        #Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'
    
    # Call function shout()
    shout()
    
    #Print echo_word
    print(echo_word)

#Call function echo_shout() with argument 'hello'    
echo_shout('hello' )
""" sortie Ipython
<script.py> output:
    hellohello
    hellohello!!!
"""





"""  
Functions with one default argument
100xp
In the previous chapter, you've learned to define functions with more than one parameter and then calling those functions by passing the required number of arguments. In the last video, Hugo built on this idea by showing you how to define functions with default arguments. You will practice that skill in this exercise by writing a function that uses a default argument and then calling the function a couple of times.

Instructions
Complete the function header with the function name shout_echo. It accepts an argument word1 and a default argument echo with default value 1, in that order.
Use the * operator to concatenate echo copies of word1. Assign the result to echo_word.
Call shout_echo() with just the string, "Hey". Assign the result to no_echo.
Call shout_echo() with the string "Hey" and the value 5 for the default argument, echo. Assign the result to with_echo.
"""
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo("Hey")

# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo("Hey",5)

# Print no_echo and with_echo
print(no_echo)
print(with_echo)
""" sortie Ipython
<script.py> output:
    Hey!!!
    HeyHeyHeyHeyHey!!!
"""





"""  
Functions with multiple default arguments
100xp
You've now defined a function that uses a default argument - don't stop there just yet! You will now try your hand at defining a function with more than one default argument and then calling this function in various ways.

After defining the function, you will call it by supplying values to all the default arguments of the function. Additionally, you will call the function by not passing a value to one of the default arguments - see how that changes the output of your function!

Instructions
Complete the function header with the function name shout_echo. It accepts an argument word1, a default argument echo with default value 1 and a default argument intense with default value False, in that order.
In the body of the if statement, capitalize the string object echo_word by applying the method upper() on it.
Call shout_echo() with the string, "Hey", the value 5 for echo and the value True for intense. Assign the result to with_big_echo.
Call shout_echo() with the string "Hey" and the value True for intense. Assign the result to big_no_echo.
 Take Hint (-30xp)
"""
# Define shout_echo
def shout_echo(word1, echo=1, intense=False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Capitalize echo_word if intense is True
    if intense is True:
        # Capitalize and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'

    # Return echo_word
    return echo_word_new

# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo("Hey",5,True)

# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo("Hey",intense=True)

# Print values
print(with_big_echo)
print(big_no_echo)
""" sortie Ipython
<script.py> output:
    HEYHEYHEYHEYHEY!!!
    HEY!!!
"""





"""  
Function with variable-length arguments (*args)
100xp
Flexible arguments enable you to pass a variable number of arguments to a function. In this exercise, you will practice defining a function that accepts a variable number of string arguments.

The function you will define is gibberish() which can accept a variable number of string values. Its return value is a single string composed of all the string arguments concatenated together in the order they were passed to the function call. You will call the function with a single string argument and see how the output changes with another call using more than one string argument. Recall from the previous video that, within the function definition, args is a tuple.

Instructions
Complete the function header with the function name gibberish. It accepts a single flexible argument *args.
Initialize a variable hodgepodge to an empty string.
Return the variable hodgepodge at the end of the function body.
Call gibberish() with the single string, "luke". Assign the result to one_word.
Hit the Submit button to call gibberish() with multiple arguments and to print the value to the Shell.
"""
# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""

    # Initialize an empty string: hodgepodge
    hodgepodge=""

    # Concatenate the strings in args
    for word in args:
        hodgepodge += word

    # Return hodgepodge
    return hodgepodge

# Call gibberish() with one string: one_word
one_word = gibberish("luke")

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word)
print(many_words)
""" sortie Ipython
<script.py> output:
    luke
    lukeleiahanobidarth
"""




"""  
Function with variable-length keyword arguments (**kwargs)
100xp
Let's push further on what you've learned about flexible arguments - you've used *args, you're now going to use **kwargs! What makes **kwargs different is that it allows you to pass a variable number of keyword arguments to functions. Recall from the previous video that, within the function definition, kwargs is a dictionary.

To understand this idea better, you're going to use **kwargs in this exercise to define a function that accepts a variable number of keyword arguments. The function simulates a simple status report system that prints out the status of a character in a movie.

Instructions
Complete the function header with the function name report_status. It accepts a single flexible argument **kwargs.
Iterate over the key-value pairs of kwargs to print out the keys and values, separated by a colon ':'.
In the first call to report_status(), pass the following keyword-value pairs: name="luke", affiliation="jedi" and status="missing'.
In the second call to report_status(), pass the following keyword-value pairs: name="anakin", affiliation="sith lord" and status="deceased'.
"""
# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for keys, values in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(keys + ": " + values)

    print("\nEND REPORT")

# First call to report_status()
report_status(name="luke",affiliation="jedi",status="missing")

# Second call to report_status()
report_status(name="anakin", affiliation="sith lord", status="deceased")
""" sortie Ipython
<script.py> output:
    
    BEGIN: REPORT
    
    name: luke
    status: missing
    affiliation: jedi
    
    END REPORT
    
    BEGIN: REPORT
    
    name: anakin
    status: deceased
    affiliation: sith lord
    
    END REPORT
"""





"""  
Bringing it all together (1)
100xp
Recall the Bringing it all together exercise in the previous chapter where you did a simple Twitter analysis by developing a function that counts how many tweets are in certain languages. The output of your function was a dictionary that had the language as the keys and the counts of tweets in that language as the value.

In this exercise, we will generalize the Twitter language analysis that you did in the previous chapter. You will do that by including a default argument that takes a column name.

For your convenience, pandas has been imported as pd and the 'tweets.csv' file has been imported into the dataframe tweets_df. Parts of the code from your previous work are also provided.

Instructions
Complete the function header by supplying the parameter for the dataframe df and the parameter col_name with a default value of 'lang' for the dataframe column name.
Call count_entries() by passing the tweets_df dataframe and the column name 'lang'. Assign the result to result1.
Call count_entries() by passing the tweets_df dataframe and the column name 'source'. Assign the result to result2.
"""
# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in dataframe
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1

        # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df,'lang')

# Call count_entries(): result2
result2 = count_entries(tweets_df,'source')

# Print result1 and result2
print(result1)
print(result2)
""" sortie Ipython
<script.py> output:
    {'et': 1, 'und': 2, 'en': 97}
    {'<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>': 33, '<a href="http://www.twitter.com" rel="nofollow">Twitter for BlackBerry</a>': 2, '<a href="http://ifttt.com" rel="nofollow">IFTTT</a>': 1, '<a href="http://www.myplume.com/" rel="nofollow">Plume\xa0for\xa0Android</a>': 1, '<a href="http://www.facebook.com/twitter" rel="nofollow">Facebook</a>': 1, '<a href="http://www.google.com/" rel="nofollow">Google</a>': 2, '<a href="http://twitter.com/#!/download/ipad" rel="nofollow">Twitter for iPad</a>': 6, '<a href="http://rutracker.org/forum/viewforum.php?f=93" rel="nofollow">newzlasz</a>': 2, '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>': 26, '<a href="http://linkis.com" rel="nofollow">Linkis.com</a>': 2, '<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>': 24}
"""





"""  
Bringing it all together (2)
100xp
Wow, you've just generalized your Twitter language analysis that you did in the previous chapter to include a default argument for the column name. You're now going to generalize this function one step further by allowing the user to pass it a flexible argument, that is, in this case, as many column names as the user would like!

Once again, for your convenience, pandas has been imported as pd and the 'tweets.csv' file has been imported into the dataframe tweets_df. Parts of the code from your previous work are also provided.

Instructions
Complete the function header by supplying the parameter for the dataframe df and the flexible argument *args.
Complete the for loop within the function definition so that the loop occurs of the tuple args.
Call count_entries() by passing the tweets_df dataframe and the column name 'lang'. Assign the result to result1.
Call count_entries() by passing the tweets_df dataframe and the column names 'lang' and 'source'. Assign the result to result2.
"""
# Define count_entries()
def count_entries(df, *args):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    #Initialize an empty dictionary: cols_count
    cols_count = {}
    
    # Iterate over column names in args
    for col_name in args:
    
        # Extract column from DataFrame: col
        col = df[col_name]
    
        # Iterate over the column in dataframe
        for entry in col:
    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
    
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'lang', 'source')

# Print result1 and result2
print(result1)
print(result2)
""" sortie Ipython
<script.py> output:
    {'et': 1, 'und': 2, 'en': 97}
    {'<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>': 33, 'und': 2, 'en': 97, '<a href="http://www.myplume.com/" rel="nofollow">Plume\xa0for\xa0Android</a>': 1, '<a href="http://www.facebook.com/twitter" rel="nofollow">Facebook</a>': 1, '<a href="http://rutracker.org/forum/viewforum.php?f=93" rel="nofollow">newzlasz</a>': 2, '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>': 26, '<a href="http://linkis.com" rel="nofollow">Linkis.com</a>': 2, '<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>': 24, 'et': 1, '<a href="http://www.twitter.com" rel="nofollow">Twitter for BlackBerry</a>': 2, '<a href="http://ifttt.com" rel="nofollow">IFTTT</a>': 1, '<a href="http://www.google.com/" rel="nofollow">Google</a>': 2, '<a href="http://twitter.com/#!/download/ipad" rel="nofollow">Twitter for iPad</a>': 6}
"""