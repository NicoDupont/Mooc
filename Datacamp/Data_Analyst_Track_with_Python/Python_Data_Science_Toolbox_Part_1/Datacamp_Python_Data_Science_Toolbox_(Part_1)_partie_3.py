# Datacamp - Python For Data Science Toolbox (Part 1)
# partie 3 : Lambda functions and error-handling
# Python 3.X



"""   question réponse : 2
Pop quiz on lambda functions
50xp
In this exercise, you will practice writing a simple lambda function and calling this function. Recall what you know about lambda functions and answer the following questions:

How would you write a lambda function add_bangs that adds three exclamation points '!!!' to the end of a string a?
How would you call add_bangs with the argument 'hello'?
You may use the IPython shell to test your code.

Possible Answers
The lambda function definition is: add_bangs = (a + '!!!'), and the function call is: add_bangs('hello'). 1
The lambda function definition is: add_bangs = (lambda a: a + '!!!'), and the function call is: add_bangs('hello'). 2
The lambda function definition is: (lambda a: a + '!!!') = add_bangs, and the function call is: add_bangs('hello').
"""

""" sortie Ipython

"""





"""   
Writing a lambda function you already know
100xp
Some function definitions are simple enough that they can be converted to a lambda function. By doing this, you write less lines of code, which is pretty awesome and will come in handy, especially when you're writing and maintaining big programs. In this exercise, you will use what you know about lambda functions to convert a function that does a simple task into a lambda function. Take a look at this function definition:

def echo_word(word1, echo):
    """Concatenate echo copies of word1."""
    words = word1 * echo
    return words
The function echo_word takes 2 parameters: a string value, word1 and an integer value, echo. It returns a string that is a concatenation of echo copies of word1. Your task is to convert this simple function into a lambda function.

Instructions
Define the lambda function echo_word using the variables word1 and echo. Replicate what the original function definition for echo_word() does above.
Call echo_word() with the string argument 'hey' and the value 5, in that order. Assign the call to result.
"""
# Define echo_word as a lambda function: echo_word
echo_word = (lambda word1, echo: word1 * echo)

# Call echo_word: result
result = echo_word('hey',5)

# Print result
print(result)
""" sortie Ipython
<script.py> output:
    heyheyheyheyhey
"""






"""   
Map() and lambda functions
100xp
So far, you've used lamdba functions to write short, simple functions as well as to redefine functions with simple functionality. The best use case for lambda functions, however, are for when you want these simple functionalities to be anonymously embedded within larger expressions. What that means is that the functionality is not stored in the environment, unlike a function defined with def. To understand this idea better, you will use a lambda function in the context of the map() function.

Recall from the video that map() applies a function over an object, such as a list. Here, you can use lambda functions to define the function that map() will use to process the object. For example:

nums = [2, 4, 6, 8, 10]

result = map(lambda a: a ** 2, nums)
You can see here that a lambda function, which raises a value a to the power of 2, is passed to map() alongside a list of numbers, nums. The map object that results from the call to map() is stored in result. You will now practice the use of lambda functions with map(). For this exercise, you will map the functionality of the add_bangs() function you defined in previous exercises over a list of strings.

Instructions
In the map() call, pass a lambda function that concatenates the string '!!!' to a string item; also pass the list of strings, spells. Assign the resulting map object to shout_spells.
Convert shout_spells to a list and print out the list.
"""
# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item + '!!!', spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)

# Convert shout_spells into a list and print it
print(shout_spells_list)
""" sortie Ipython
<script.py> output:
    ['protego!!!', 'accio!!!', 'expecto patronum!!!', 'legilimens!!!']
"""




"""   
Filter() and lambda functions
100xp
In the previous exercise, you used lambda functions to anonymously embed an operation within map(). You will practice this again in this exercise by using a lambda function with filter(), which may be new to you! The function filter() offers a way to filter out elements from a list that doesn't satisfy certain criteria.

Your goal in this exercise it to use filter() to create, from an input list of strings, a new list that contains only strings that have more than 6 characters.

Instructions
In the filter() call, pass a lambda function and the list of strings, fellowship. The lambda function should check if the number of characters in a string member is greater than 6; use the len() function to do this. Assign the resulting filter object to result.
Convert result to a list and print out the list.
"""
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda item: len(item) > 6, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Convert result into a list and print it
print(result_list)
""" sortie Ipython
<script.py> output:
    ['samwise', 'aragorn', 'legolas', 'boromir']
"""



"""   
Reduce() and lambda functions
100xp
You're getting very good at using lambda functions! Here's one more function to add to your repertoire of skills. The reduce() function is useful for performing some computation on a list and, unlike map() and filter(), returns a single value as a result. To use reduce(), you must import it from the functools module.

Remember gibberish() from a few exercises back?

# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""
    hodgepodge = ''
    for word in args:
        hodgepodge += word
    return hodgepodge
gibberish() simply takes a list of strings as an argument and returns, as a single-value result, the concatenation of all of these strings. In this exercise, you will replicate this functionality by using reduce() and a lambda function that concatenates strings together.

Instructions
Import the reduce function from the functools module.
In the reduce() call, pass a lambda function that takes two string arguments item1 and item2 and concatenates them; also pass the list of strings, stark. Assign the result to result. The first argument to reduce() should be the lambda function and the second argument is the list stark.
"""
# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'eddard', 'jon']

# Use result() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1 + item2 , stark)

# Print the result
print(result)
""" sortie Ipython
<script.py> output:
    robbsansaaryaeddardjon
"""





"""   question réponse : 3
Pop quiz about errors
50xp
In the video, Hugo talked about how errors happen when functions are supplied arguments that they are unable to work with. In this exercise, you will identify which function call raises an error and what type of error is raised.

Take a look at the following function calls to len():

len('There is a beast in every man and it stirs when you put a sword in his hand.')

len(['robb', 'sansa', 'arya', 'eddard', 'jon'])

len(525600)

len(('jaime', 'cersei', 'tywin', 'tyrion', 'joffrey'))
Which of the function calls raises an error and what type of error is raised?

Possible Answers
The call len('There is a beast in every man and it stirs when you put a sword in his hand.') raises a TypeError. 1
The call len(['robb', 'sansa', 'arya', 'eddard', 'jon']) raises an IndexError. 2
The call len(525600) raises a TypeError. 3
The call len(('jaime', 'cersei', 'tywin', 'tyrion', 'joffrey')) raises a NameError. 4
"""

""" sortie Ipython
In [1]: len('There is a beast in every man and it stirs when you put a sword in his hand.')
Out[1]: 76

In [2]: len(['robb', 'sansa', 'arya', 'eddard', 'jon'])
Out[2]: 5

In [3]: len(525600)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    len(525600)
TypeError: object of type 'int' has no len()


In [4]: len(('jaime', 'cersei', 'tywin', 'tyrion', 'joffrey'))
Out[4]: 5
"""






"""   
Error handling with try-except
100xp
A good practice in writing your own functions is also anticipating the ways in which other people (or yourself, if you accidentally misuse your own function) might use the function you defined.

As in the previous exercise, you saw that the len() function is able to handle input arguments such as strings, lists, and tuples, but not int type ones and raises an appropriate error and error message when it encounters invalid input arguments. One way of doing this is through exception handling with the try-except block.

In this exercise, you will define a function as well as use a try-except block for handling cases when incorrect input arguments are passed to the function.

Recall the shout_echo() function you defined in previous exercises; parts of the function definition are provided in the sample code. Your goal is to complete the exception handling code in the function definition and provide an appropriate error message when raising an error.

Instructions
Initialize the variables echo_word and shout_words to empty strings.
Add the keywords try and except in the appropriate locations for the exception handling block.
Use the * operator to concatenate echo copies of word1. Assign the result to echo_word.
Concatenate the string '!!!' to echo_word. Assign the result to shout_words.
"""
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Initialize empty strings: echo_word, shout_words
    echo_word = ""
    shout_words = ""
    

    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo

        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + '!!!'
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")

    # Return shout_words
    return shout_words

# Call shout_echo
shout_echo("particle", echo="accelerator")
""" sortie Ipython
<script.py> output:
    word1 must be a string and echo must be an integer.
"""




"""   
Another way to raise an error is by using raise. In this exercise, you will add a raise statement to the shout_echo() function you defined before to raise an error message when the value supplied to by the user to the echo argument is less than 0.

The call to shout_echo() uses valid argument values. To test and see how the raise statement works, simply change the value for the echo argument to a negative value. Don't forget to change it back to valid values to move on to the next exercise!

Instructions
Complete the if statement by checking if the value of echo is less than 0.
In the body of the if statement, add a raise statement that raises the error message 'echo must be greater than 0' when the value supplied by the user to echo is less than 0.
"""
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo<0:
        raise ValueError('echo must be greater than 0')

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo
shout_echo("particle", echo=5)
""" sortie Ipython

"""





"""   
Bringing it all together (1)
100xp
This is awesome! You have now learned how to write anonymous functions using lambda, how to pass lambda functions as arguments to other functions such as map(), filter(), and reduce(), as well as how to write errors and output custom error messages within your functions. You will now put together these learnings to good use by working with a Twitter dataset. Before practicing your new error handling skills,in this exercise, you will write a lambda function and use filter() to select retweets, that is, tweets that begin with the string 'RT'.

To help you accomplish this, the Twitter data has been imported into the dataframe, tweets_df. Go for it!

Instructions
In the filter() call, pass a lambda function and the sequence of tweets as strings, tweets_df['text']. The lambda function should check if the first 2 characters in a tweet x are 'RT'. Assign the resulting filter object to result. To get the first 2 characters in a tweet x, use x[0:2]. To check equality, use a Boolean filter with ==.
Convert result to a list and print out the list.
"""
# Select retweets from the Twitter dataframe: result
result = filter(lambda item: item[0:2].upper() == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)
""" sortie Ipython
<script.py> output:
    RT @bpolitics: .@krollbondrating's Christopher Whalen says Clinton is the weakest Dem candidate in 50 years https://t.co/pLk7rvoRSn https:/…
    RT @HeidiAlpine: @dmartosko Cruz video found.....racing from the scene.... #cruzsexscandal https://t.co/zuAPZfQDk3
    RT @AlanLohner: The anti-American D.C. elites despise Trump for his America-first foreign policy. Trump threatens their gravy train. https:…
    RT @BIackPplTweets: Young Donald trump meets his neighbor  https://t.co/RFlu17Z1eE
    RT @trumpresearch: @WaitingInBagdad @thehill Trump supporters have selective amnisia.
    RT @HouseCracka: 29,000+ PEOPLE WATCHING TRUMP LIVE ON ONE STREAM!!!
    
    https://t.co/7QCFz9ehNe
    RT @urfavandtrump: RT for Brendon Urie
    Fav for Donald Trump https://t.co/PZ5vS94lOg
    RT @trapgrampa: This is how I see #Trump every time he speaks. https://t.co/fYSiHNS0nT
    RT @trumpresearch: @WaitingInBagdad @thehill Trump supporters have selective amnisia.
    RT @Pjw20161951: NO KIDDING: #SleazyDonald just attacked Scott Walker for NOT RAISING TAXES in WI! #LyinTrump
    #NeverTrump  #CruzCrew  https…
    RT @urfavandtrump: RT for Brendon Urie
    Fav for Donald Trump https://t.co/PZ5vS94lOg
    RT @ggreenwald: The media spent all day claiming @SusanSarandon said she might vote for Trump. A total fabrication, but whatever... https:/…
    RT @Pjw20161951: NO KIDDING: #SleazyDonald just attacked Scott Walker for NOT RAISING TAXES in WI! #LyinTrump
    #NeverTrump  #CruzCrew  https…
    RT @trapgrampa: This is how I see #Trump every time he speaks. https://t.co/fYSiHNS0nT
    RT @mitchellvii: So let me get this straight.  Any reporter can assault Mr Trump at any time and Corey can do nothing?  Michelle is clearly…
    RT @paulbenedict7: How #Trump Sacks RINO Strongholds by Hitting Positions Held by Dems and GOP https://t.co/D7ulnAJhis   #tcot #PJNET https…
    RT @DRUDGE_REPORT: VIDEO:  Trump emotional moment with Former Miss Wisconsin who has terminal illness... https://t.co/qt06aG9inT
    RT @ggreenwald: The media spent all day claiming @SusanSarandon said she might vote for Trump. A total fabrication, but whatever... https:/…
    RT @DennisApgar: Thank God I seen Trump at first stop in Wisconsin media doesn't know how great he is, advice watch live streaming https://…
    RT @paulbenedict7: How #Trump Sacks RINO Strongholds by Hitting Positions Held by Dems and GOP https://t.co/D7ulnAJhis   #tcot #PJNET https…
    RT @DRUDGE_REPORT: VIDEO:  Trump emotional moment with Former Miss Wisconsin who has terminal illness... https://t.co/qt06aG9inT
    RT @DennisApgar: Thank God I seen Trump at first stop in Wisconsin media doesn't know how great he is, advice watch live streaming https://…
    RT @mitchellvii: So let me get this straight.  Any reporter can assault Mr Trump at any time and Corey can do nothing?  Michelle is clearly…
    RT @sciam: Trump's idiosyncratic patterns of speech are why people tend either to love or hate him https://t.co/QXwquVgs3c https://t.co/P9N…
    RT @Norsu2: Nightmare WI poll for Ted Cruz has Kasich surging: Trump 29, Kasich 27, Cruz 25. https://t.co/lJsgbLYY1P #NeverTrump
    RT @thehill: WATCH: Protester pepper-sprayed point blank at Trump rally https://t.co/B5f65Al9ld https://t.co/skAfByXuQc
    RT @sciam: Trump's idiosyncratic patterns of speech are why people tend either to love or hate him https://t.co/QXwquVgs3c https://t.co/P9N…
    RT @ggreenwald: The media spent all day claiming @SusanSarandon said she might vote for Trump. A total fabrication, but whatever... https:/…
    RT @DebbieStout5: Wow! Last I checked it was just 12 points &amp; that wasn't more than a day ago. Oh boy Trump ppl might want to rethink🤔 http…
    RT @tyleroakley: i'm a messy bitch, but at least i'm not voting for trump
    RT @vandives: Trump supporters r tired of justice NOT being served. There's no justice anymore. Hardworking Americans get screwed. That's n…
    RT @AP: BREAKING: Trump vows to stand by campaign manager charged with battery, says he does not discard people.
    RT @AP: BREAKING: Trump vows to stand by campaign manager charged with battery, says he does not discard people.
    RT @urfavandtrump: RT for Jerrie (Little Mix)
    Fav for Donald Trump https://t.co/nEVxElW6iG
    RT @urfavandtrump: RT for Jerrie (Little Mix)
    Fav for Donald Trump https://t.co/nEVxElW6iG
    RT @NoahCRothman: When Walker was fighting for reforms, Trump was defending unions and collective bargaining privileges https://t.co/e1UWNN…
    RT @RedheadAndRight: Report: Secret Service Says Michelle Fields Touched Trump https://t.co/c5c2sD8VO2
    
    This is the only article you will n…
    RT @AIIAmericanGirI: VIDEO=&gt; Anti-Trump Protester SLUGS Elderly Trump Supporter in the Face
    https://t.co/GeEryMDuDY
    RT @NoahCRothman: When Walker was fighting for reforms, Trump was defending unions and collective bargaining privileges https://t.co/e1UWNN…
    RT @JusticeRanger1: @realDonaldTrump @Pudingtane @DanScavino @GOP @infowars @EricTrump 
    URGENT PUBLIC TRUMP ALERT:
    COVERT KILL MEANS https:…
    RT @AIIAmericanGirI: VIDEO=&gt; Anti-Trump Protester SLUGS Elderly Trump Supporter in the Face
    https://t.co/GeEryMDuDY
    RT @RedheadAndRight: Report: Secret Service Says Michelle Fields Touched Trump https://t.co/c5c2sD8VO2
    
    This is the only article you will n…
    RT @JusticeRanger1: @realDonaldTrump @Pudingtane @DanScavino @GOP @infowars @EricTrump 
    URGENT PUBLIC TRUMP ALERT:
    COVERT KILL MEANS https:…
    RT @Schneider_CM: Trump says nobody had ever heard of executive orders before Obama started signing them. Never heard of the Emancipation P…
    RT @RonBasler1: @DavidWhitDennis @realDonaldTrump @tedcruz 
    
    CRUZ SCREWS HOOKERS
    
    CRUZ / CLINTON
    RT @DonaldsAngel: Former Ms. WI just said that she is terminally ill but because of Trump pageant, her 7 yr. old son has his college educat…
    RT @Schneider_CM: Trump says nobody had ever heard of executive orders before Obama started signing them. Never heard of the Emancipation P…
    RT @DonaldsAngel: Former Ms. WI just said that she is terminally ill but because of Trump pageant, her 7 yr. old son has his college educat…
    RT @Dodarey: @DR8801 @SykesCharlie Charlie, let's see you get a straight "yes" or "no" answer from Cruz a/b being unfaithful to his wife @T…
    RT @RonBasler1: @DavidWhitDennis @realDonaldTrump @tedcruz 
    
    CRUZ SCREWS HOOKERS
    
    CRUZ / CLINTON
    RT @RockCliffOne: Remember when the idea of a diabolical moron holding the world hostage was an idea for a funny movie? #Trump #GOP https:/…
    RT @HillaryClinton: "Every day, another Republican bemoans the rise of Donald Trump... but [he] didn’t come out of nowhere." —Hillary
    https…
    RT @Dodarey: @DR8801 @SykesCharlie Charlie, let's see you get a straight "yes" or "no" answer from Cruz a/b being unfaithful to his wife @T…
    RT @HillaryClinton: "Every day, another Republican bemoans the rise of Donald Trump... but [he] didn’t come out of nowhere." —Hillary
    https…
    RT @RockCliffOne: Remember when the idea of a diabolical moron holding the world hostage was an idea for a funny movie? #Trump #GOP https:/…
    RT @immigrant4trump: @immigrant4trump msm, cable news attacking trump all day, from 8am to 10pm today, then the reruns come on, repeating t…
    RT @immigrant4trump: @immigrant4trump msm, cable news attacking trump all day, from 8am to 10pm today, then the reruns come on, repeating t…
    RT @GlendaJazzey: Donald Trump’s Campaign Financing Dodge, @rrotunda https://t.co/L8flI4lswG via @VerdictJustia
    RT @TUSK81: LOUDER FOR THE PEOPLE IN THE BACK https://t.co/hlPVyNLXzx
    RT @loopzoop: Well...put it back https://t.co/8Yb7BDT5VM
    RT @claytoncubitt: Stop asking Bernie supporters if they’ll vote for Hillary against Trump. We got a plan to beat Trump already. Called Ber…
    RT @akaMaude13: Seriously can't make this up. What a joke. #NeverTrump  https://t.co/JkTx6mdRgC
"""





"""   
Bringing it all together (2)
100xp
Sometimes, we make mistakes when calling functions - even ones you made yourself. But don't fret! In this exercise, you will improve on your previous work with the count_entries() function in the last chapter by adding a try-except block to it. This will allow your function to provide a helpful message when the user calls your count_entries() function but provides a column name that isn't in the dataframe.

Once again, for your convenience, pandas has been imported as pd and the 'tweets.csv' file has been imported into the dataframe tweets_df. Parts of the code from your previous work are also provided.

Instructions
Add a try block so that when the function is called with the correct arguments, it processes the dataframe and returns a dictionary of results.
Add an except block so that when the function is called incorrectly, it displays an the following error message: 'The dataframe does not have a ' + col_name + ' column.'.
"""
# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Add try block
    try:
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

    # Add except block
    except:
        print('The dataframe does not have a ' + col_name + ' column.')

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Print result1
print(result1)

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'lang1')
""" sortie Ipython
<script.py> output:
    {'et': 1, 'und': 2, 'en': 97}
    The dataframe does not have a lang1 column.
"""






"""   
Bringing it all together (3)
100xp
In the previous exercise, you built on your function count_entries() to add a try-except block. This was so that users would get helpful messages when calling your count_entries() function and providing a column name that isn't in the dataframe. In this exercise, you'll instead raise a ValueError in the case that the user provides a column name that isn't in the DataFrame.

Once again, for your convenience, pandas has been imported as pd and the 'tweets.csv' file has been imported into the DatFrame tweets_df. Parts of the code from your previous work are also provided.

Instructions
If col_name is NOT a column in the DataFrame df, raise a ValueError 'The dataframe does not have a ' + col_name + ' column.'.
Call your new function count_entries() to analyze the 'lang' column of tweets_df. Hit Submit to check out the result, In the next exercise, you'll see that it raises the necessary ValueErrors.
"""
# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError('The dataframe does not have a ' + col_name + ' column.')

    # Initialize an empty dictionary: langs_count
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
# Print result1
print(result1)
""" sortie Ipython
<script.py> output:
    {'et': 1, 'und': 2, 'en': 97}
"""


""" question réponse :
Bringing it all together: testing your error handling skills
50xp
You have just written error handling into your count_entries() function so that, when the user passes the function a column (as 2nd argument) NOT contained in the DataFrame (1st argument), a ValueError is thrown. You're now going to play with this function: it is loaded into pre-exercise code, as is the DataFrame tweets_df. Try calling count_entries(tweets_df, 'lang') to confirm that the function behaves as it should. Then call count_entries(tweets_df, 'lang1'): what is the last line of the output?

Possible Answers
'ValueError: The dataframe does not have the requested column.' 1
'ValueError: The dataframe does not have a lang1 column.' 2
'TypeError: The dataframe does not have the requested column.'
"""

""" sortie Ipython
In [1]: count_entries(tweets_df, 'lang')
Out[1]: {'en': 97, 'et': 1, 'und': 2}

In [2]: count_entries(tweets_df, 'lang1')

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    count_entries(tweets_df, 'lang1')
  File "<stdin>", line 17, in count_entries
    raise ValueError('The dataframe does not have a ' + col_name + ' column.')
ValueError: The dataframe does not have a lang1 column.

"""
