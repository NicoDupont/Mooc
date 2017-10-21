# Datacamp - Python For Data Science Toolbox (Part 1)
# partie 1 : Writing your own functions 
# Python 3.X


"""  réponse : 3
Strings in Python
50xp

In the video, you learned of another standard Python datatype, strings. Recall that these represent textual data. To assign the string 'DataCamp' to a variable company, you execute:

company = 'DataCamp'

You've also learned to use the operations + and * with strings. Unlike with numeric types such as ints and floats, the + operator concatenates strings together, while the * concatenates multiple copies of a string together. In this exercise, you will use the + and * operations on strings to answer the question below. Execute the following code in the shell:

object1 = "data" + "analysis" + "visualization"
object2 = 1 * 3
object3 = "1" * 3

What are the values in object1, object2, and object3, respectively?
Possible Answers

    object1 contains "data + analysis + visualization", object2 contains "1*3", object3 contains 13.
    1
    object1 contains "data+analysis+visualization", object2 contains 3, object3 contains "13".
    2
    object1 contains "dataanalysisvisualization", object2 contains 3, object3 contains "111".
    3
"""

""" sortie Ipython
In [1]: object1 = "data" + "analysis" + "visualization"

In [2]: object2 = 1 * 3
... object3 = "1" * 3

In [3]: object1
Out[3]: 'dataanalysisvisualization'

In [4]: object2
Out[4]: 3

In [5]: object3
Out[5]: '111'
"""





"""  question réponse : 
Recapping built-in functions
50xp

In the video, Hugo briefly examined the return behavior of the built-in functions print() and str(). Here, you will use both functions and examine their return values. A variable x has been preloaded for this exercise. Run the code below in the console. Pay close attention to the results to answer the question that follows.

    Assign str(x) to a variable y1: y1 = str(x)
    Assign print(x) to a variable y2: y2 = print(x)
    Check the types of the variables x, y1, and y2.

What are the types of x, y1, and y2?
Possible Answers

    They are all str types.
    1
    x is a float, y1 is an float, and y2 is a str.
    2
    x is a float, y1 is a str, and y2 is a NoneType.
    3
    They are all NoneType types.
    4
"""

""" sortie Ipython
In [1]: y1 = str(x)

In [2]: type(y1)
Out[2]: str

In [3]: y2 = print(x)
4.89

In [4]: type(y2)
Out[4]: NoneType

In [5]: type(x)
Out[5]: float
"""






""" 
Write a simple function
100xp

In the last video, Hugo described the basics of how to define a function. You will now write your own function!

Define a function, shout(), which simply prints out a string with three exclamation marks '!!!' at the end. The code for the square() function that we wrote earlier is found below. You can use it as a pattern to define shout().

def square():
    new_value = 4 ** 2
    return new_value

Note that the function body is indented 4 spaces already for you. Function bodies need to be indented by a consistent number of spaces and the choice of 4 is common.
Instructions

    Complete the function header by adding the appropriate function name, shout.
    In the function body, concatenate the string, 'congratulations' with another string, '!!!'. Assign the result to shout_word.
    Print the value of shout_word.
    Call the shout function.

"""
# Define the function shout
def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = 'congratulations'+'!!!'
    
    # Print shout_word
    print(shout_word)

# Call shout
shout()
""" sortie Ipython

"""







""" 
Single-parameter functions
100xp

Congratulations! You have successfully defined and called your own function! That's pretty cool.

In the previous exercise, you defined and called the function shout(), which printed out a string concatenated with '!!!'. You will now update shout() by adding a parameter so that it can accept and process any string argument passed to it. Also note that shout(word), the part of the header that specifies the function name and parameter(s), is known as the signature of the function. You may encounter this term in the wild!
Instructions

    Complete the function header by adding the parameter name, word.
    Assign the result of concatenating word with '!!!' to shout_word.
    Print the value of shout_word.
    Call the shout() function, passing to it the string, 'congratulations'.

"""
# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout with the string 'congratulations'
shout('congratulations')
""" sortie Ipython
<script.py> output:
    congratulations!!!
"""







""" 
Functions that return single values
100xp

You're getting very good at this! Try your hand at another modification to the shout() function so that it now returns a single value instead of printing within the function. Recall that the return keyword lets you return values from functions. Parts of the function shout(), which you wrote earlier, are shown. Returning values is generally more desirable than printing them out because, as you saw eariler, a print() call assigned to a variable has type NoneType.
Instructions

    In the function body, concatenate the string in word with '!!!' and assign to shout_word.
    Replace the print() statement with the appropriate return statement.
    Call the shout() function, passing to it the string, 'congratulations', and assigning the call to the variable, yell.
    To check if yell contains the value returned by shout(), print the value of yell.

"""
# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Replace print with return
    return(shout_word)

# Pass 'congratulations' to shout: yell
yell = shout('congratulations')

# Print yell
print(yell)
""" sortie Ipython
<script.py> output:
    congratulations!!!
"""






""" 
Functions with multiple parameters
100xp

Hugo discussed the use of multiple parameters in defining functions in the last lecture. You are now going to use what you've learned to modify the shout() function further. Here, you will modify shout() to accept two arguments. Parts of the function shout(), which you wrote earlier, are shown.
Instructions

    Modify the function header such that it accepts two parameters, word1 and word2, in that order.
    Concatenate each of word1 and word2 with '!!!' and assign to shout1 and shout2, respectively.
    Concatenate shout1 and shout2 together, in that order, and assign to new_shout.
    Pass the strings 'congratulations' and 'you', in that order, to a call to shout(). Assign the return value to yell.

"""
# Define shout with parameters word1 and word2
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 +'!!!'
    
    # Concatenate shout1 with shout2: new_shout
    new_shout = shout1 + shout2 

    # Return new_shout
    return new_shout

# Pass 'congratulations' and 'you' to shout(): yell
yell = shout('congratulations', 'you')

# Print yell
print(yell)
""" sortie Ipython
<script.py> output:
    congratulations!!!you!!!
"""







""" 
A brief introduction to tuples
100xp

Alongside learning about functions, you've also learned about tuples! Here, you will practice what you've learned about tuples: how to construct, unpack, and access tuple elements.

A three-element tuple named nums has been preloaded for this exercise. Before completing the script, perform the following:

    Print out the value of nums in the IPython shell. Note the elements in the tuple.
    In the IPython shell, try to change the first element of nums to the value 2 by doing an assignment: nums[0] = 2. What happens?

Instructions

    Unpack nums to the variables num1, num2, and num3.
    Construct a new tuple, even_nums composed of the same elements in nums, but with the 1st element replaced with the value, 2.

"""
# Unpack nums into num1, num2, and num3
num1, num2, num3 = nums

# Construct even_nums
even_nums = (2, num2, num3)
""" sortie Ipython
In [1]: nums
Out[1]: (3, 4, 6)

In [2]: num1, num2, num3 = nums
... 
... # Construct even_nums
... even_nums = nums
... even_nums[0] = 2

Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
    even_nums[0] = 2
TypeError: 'tuple' object does not support item assignment


In [3]: nums[0] = 2

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    nums[0] = 2
TypeError: 'tuple' object does not support item assignment


In [4]: even_nums = (2, num2, num3)
"""






""" 
Function that return multiple values
100xp

In the previous exercise, you constructed tuples, assigned tuples to variables, and unpacked tuples. Here you will return mutiple values from a function using tuples. Let's now update our shout() function to return multiple values. Instead of returning just one string, we will return two strings with the string !!! concatenated to each.

Note that the return statement return x, y has the same result as return (x, y): the former actually packs x and y into a tuple under the hood!
Instructions

    Modify the function header such that the function name is now shout_all, and it accepts two parameters, word1 and word2, in that order.
    Concatenate the string '!!!' to each of word1 and word2 and assign to shout1 and shout2, respectively.
    Construct a tuple shout_words, composed of shout1 and shout2.
    Call shout_all() with the strings 'congratulations' and 'you' and assign the result to yell1 and yell2 (remember, shout_all returns 2 variables!).

"""
# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)

    # Return shout_words
    return shout_words

# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations','you')

# Print yell1 and yell2
print(yell1)
print(yell2)
""" sortie Ipython
<script.py> output:
    congratulations!!!
    you!!!

"""





""" 
Bringing it all together (1)
100xp

You've got your first taste of writing your own functions in the previous exercises. You've learned how to add parameters to your own function definitions, return a value or multiple values with tuples, and how to call the functions you've defined.

In this and the following exercise, you will bring together all these concepts and apply them to a simple data science problem. You will load a dataset and develop functionalities to extract simple insights from the data.

For this exercise, your goal is to recall how to load a dataset into a dataframe. The dataset contains Twitter data and you will iterate over entries in a column to build a dictionary with keys the names of languages and values the number of tweets in the given language. The file tweets.csv is available in your current directory.
Instructions

    Import the pandas package with the alias pd.
    Import the file 'tweets.csv' using the pandas function read_csv(). Assign the resulting dataframe to df.
    Complete the for loop by iterating over col, the 'lang' column in the dataframe df.
    Complete the bodies of the if-else statements in the for loop: if the key is in the dictionary langs_count, add 1 to its current value, else add the key to langs_count and set its value to 1. Use the loop variable entry in your code.

"""
# Import pandas
import pandas as pd

# Import Twitter data as dataframe: df
df = pd.read_csv('tweets.csv')

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in df
for entry in col:

    # If the language is in langs_count, add 1
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)
""" sortie Ipython
In [1]: import pandas as pd
... 
... # Import Twitter data as dataframe: df
... df = pd.read_csv('tweets.csv')

In [2]: df.head()
Out[2]: 
   contributors  coordinates                      created_at  \
0           NaN          NaN  Tue Mar 29 23:40:17 +0000 2016   
1           NaN          NaN  Tue Mar 29 23:40:17 +0000 2016   
2           NaN          NaN  Tue Mar 29 23:40:17 +0000 2016   
3           NaN          NaN  Tue Mar 29 23:40:17 +0000 2016   
4           NaN          NaN  Tue Mar 29 23:40:17 +0000 2016   

                                            entities  \
0  {'hashtags': [], 'user_mentions': [{'screen_na...   
1  {'hashtags': [{'text': 'cruzsexscandal', 'indi...   
2  {'hashtags': [], 'user_mentions': [], 'symbols...   
3  {'hashtags': [], 'user_mentions': [], 'symbols...   
4  {'hashtags': [], 'user_mentions': [{'screen_na...   

                                   extended_entities  favorite_count  \
0  {'media': [{'sizes': {'large': {'w': 1024, 'h'...               0   
1  {'media': [{'sizes': {'large': {'w': 500, 'h':...               0   
2                                                NaN               0   
3                                                NaN               0   
4                                                NaN               0   

  favorited filter_level  geo                  id  \
0     False          low  NaN  714960401759387648   
1     False          low  NaN  714960401977319424   
2     False          low  NaN  714960402426236928   
3     False          low  NaN  714960402367561730   
4     False          low  NaN  714960402149416960   

                         ...                          quoted_status_id  \
0                        ...                                       NaN   
1                        ...                                       NaN   
2                        ...                                       NaN   
3                        ...                              7.149239e+17   
4                        ...                                       NaN   

  quoted_status_id_str  retweet_count  retweeted  \
0                  NaN              0      False   
1                  NaN              0      False   
2                  NaN              0      False   
3         7.149239e+17              0      False   
4                  NaN              0      False   

                                    retweeted_status  \
0  {'retweeted': False, 'text': ".@krollbondratin...   
1  {'retweeted': False, 'text': '@dmartosko Cruz ...   
2                                                NaN   
3                                                NaN   
4  {'retweeted': False, 'text': 'The anti-America...   

                                              source  \
0  <a href="http://twitter.com" rel="nofollow">Tw...   
1  <a href="http://twitter.com" rel="nofollow">Tw...   
2  <a href="http://www.facebook.com/twitter" rel=...   
3  <a href="http://twitter.com/download/android" ...   
4  <a href="http://twitter.com/download/iphone" r...   

                                                text   timestamp_ms truncated  \
0  RT @bpolitics: .@krollbondrating's Christopher...  1459294817758     False   
1  RT @HeidiAlpine: @dmartosko Cruz video found.....  1459294817810     False   
2  Njihuni me Zonjën Trump !!! | Ekskluzive https...  1459294817917     False   
3  Your an idiot she shouldn't have tried to grab...  1459294817903     False   
4  RT @AlanLohner: The anti-American D.C. elites ...  1459294817851     False   

                                                user  
0  {'utc_offset': 3600, 'profile_image_url_https'...  
1  {'utc_offset': None, 'profile_image_url_https'...  
2  {'utc_offset': 7200, 'profile_image_url_https'...  
3  {'utc_offset': None, 'profile_image_url_https'...  
4  {'utc_offset': -18000, 'profile_image_url_http...  

[5 rows x 31 columns]

In [3]: langs_count = {}

In [4]: col = df['lang']

In [5]: col
Out[5]: 
0      en
1      en
2      et
3      en
4      en
5      en
6      en
7      en
8      en
9      en
10     en
11     en
12     en
13     en
14     en
15     en
16     en
17     en
18     en
19     en
20    und
21     en
22     en
23     en
24     en
25     en
26     en
27     en
28     en
29    und
     ... 
70     en
71     en
72     en
73     en
74     en
75     en
76     en
77     en
78     en
79     en
80     en
81     en
82     en
83     en
84     en
85     en
86     en
87     en
88     en
89     en
90     en
91     en
92     en
93     en
94     en
95     en
96     en
97     en
98     en
99     en
Name: lang, dtype: object

Traceback (most recent call last):
  File "script.py", line 17, in <module>
    if entry in langs_count.keys():
AttributeError: 'int' object has no attribute 'keys'


In [6]: langs_count.keys()
Out[6]: dict_keys([])

Traceback (most recent call last):
  File "script.py", line 21, in <module>
    langs_count += entry
TypeError: unsupported operand type(s) for +=: 'dict' and 'str'


<script.py> output:
    {'und': 2, 'et': 1, 'en': 97}
"""







""" 
Bringing it all together (2)
100xp

Great job! You've now defined the functionality for iterating over entries in a column and building a dictionary with keys the names of languages and values the number of tweets in the given language.

In this exercise, you will define a function with the functionality you developed in the previous exercise, return the resulting dictionary from within the function, and call the function with the appropriate arguments.

For your convenience, the pandas package has been imported as pd and the 'tweets.csv' file has been imported into the tweets_df variable.
Instructions

    Define the function count_entries(), which has two parameters. The first parameter is df for the dataframe and the second is col_name for the column name.
    Complete the bodies of the if-else statements in the for loop: if the key is in the dictionary langs_count, add 1 to its current value, else add the key to langs_count and set its value to 1. Use the loop variable entry in your code.
    Return the langs_count dictionary from inside the count_entries() function.
    Call the count_entries() function by passing to it tweets_df and the name of the column, 'lang'. Assign the result of the call to the variable result.

"""
# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over lang column in dataframe
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return langs_count

# Call count_entries(): result
result = count_entries(tweets_df,'lang')

# Print the result
print(result)
""" sortie Ipython
<script.py> output:
    {'und': 2, 'et': 1, 'en': 97}
"""
