"""
02/2017
Dataquest : Data Analyst Path
Step 1: Introduction To Python
SubStep : Python Programming Intermediate : Variable Scopes
"""


"""
1: Introduction
Data scientists often need to parse strings to extract important information.
Suppose we have manually-entered data that includes dates, and need to extract the years from those dates.
The dates may look something like this:

- "Jan 17, 2012"
- "9/22/2005"
- "Spring 2007"
- "New Year's Eve 1999"
All of these strings contain the information we need, but in very different formats.
If we try to split the strings, what character would we split them on? In the resulting lists, which element would contain the year? We can handle a problem like this with regular expressions.

A regular expression (regex) is a sequence of characters that describes a search pattern. We can use regular expressions to search for and extract data.

In practice, we say that strings match a regular expression if the pattern exists anywhere within those strings (as substrings).
The simplest example of a regular expression is an ordinary sequence of characters that we specify.
We say that any string containing that sequence of characters, adjacent and in the same exact order, matches the regular expression. Here are a few examples:

see img7.png

This is the simplest form of a regex. We'll soon see that regular expressions can also contain special characters that denote particular patterns.

Instructions
In the code cell, assign to the variable regex a regular expression that's four characters long and matches every string in the list strings.
"""
strings = ["data science", "big data", "metadata"]
regex = "data"
""" Console Output or Results

"""



"""
2: Wildcards In Regular Expressions
We've seen that we can use regular expressions to find strings containing a simple pattern, but they can match much more complex patterns.

There are a number of special characters we can use with regular expressions to change the way a pattern is interpreted.
In Python, we use the re module to work with regular expressions.
The module's documentation provides a list of these special characters.

For instance, we use the special character "." to indicate that any character can be put in its place.
Here are a few examples of how you might use this placeholder:

see img8.png

Let's create a regular expression in the exercise on the next screen.

Instructions
Assign a regular expression that is three characters long and matches every string in strings to the variable regex.

"""
strings = ["bat", "robotics", "megabyte"]
regex = "b.t"
""" Console Output or Results

"""



"""
3: Searching The Beginnings And Endings Of Strings
We can use the caret symbol ("^") to match the beginning of a string, and the dollar sign ("$") to match the end of a string.

"^a" will match all strings that start with "a".

"a$" will match all strings that end with "a".

We can use any combination of special characters in a regex. Let's combine what we've learned so far to create some more advanced expressions.

Instructions
Assign a regular expression that's seven characters long and matches every string in strings (except for bad_string) to the variable regex.
"""
strings = ["better not put too much", "butter in the", "batter"]
bad_string = "We also wouldn't want it to be bitter"
regex = "^b.tter"
""" Console Output or Results

"""



"""
4: Introduction To The AskReddit Data Set
Reddit is a content and community website where users can submit links, text posts, and other types of content to groups of people with similar interests.
These groups are called subreddits, and each one specializes in a particular topic.

For example, AskReddit is a popular subreddit where you can pose questions to the entire Reddit community. Users answer the questions by commenting on them.

In this mission, we'll be working with a data set containing the top 1,000 questions users posted to AskReddit in 2015.
Reddit user P_S_Laplace created the data set, which has five columns that appear in the following order:

Title -- The title of the post
Score -- The number of upvotes the post received
Time -- When the post was posted
Gold -- How much Reddit Gold users gave the post
NumComs -- The number of comments the post received

"""





"""
5: Reading And Printing The Data Set
Let's use the csv module to read and print our data file, "askreddit_2015.csv".
Recall that we can use the csv module by performing the following steps:

Import csv.
Open the file that contains our CSV data in 'r' mode.
Call the csv.reader() function with the file object as input.
Convert the result to a list.
Instructions
Use the csv module to read our data set and assign it to posts_with_header.
Use list slicing to exclude the first row, which represents the column names. Assign this sliced data set to posts.
Use a for loop and string slicing to print the first 10 rows. See if you notice any patterns in this sample of the data set.
"""
import csv
posts_with_header = list(csv.reader(open("askreddit_2015.csv")))
posts = posts_with_header[1:len(posts_with_header)]

for i in range(0,10):
    print(posts[i])
""" Console Output or Results
Output
['What\'s your internet "white whale", something you\'ve been searching for years to find with no luck?', '11510', '1433213314.0', '1', '26195']
["What's your favorite video that is 10 seconds or less?", '8656', '1434205517.0', '4', '8479']
['What are some interesting tests you can take to find out about yourself?', '8480', '1443409636.0', '1', '4055']
["PhD's of Reddit. What is a dumbed down summary of your thesis?", '7927', '1440188623.0', '0', '13201']
['What is cool to be good at, yet uncool to be REALLY good at?', '7711', '1440082910.0', '0', '20325']
['[Serious] Redditors currently in a relationship, besides dinner and a movie, what are your favorite activities for date night?', '7598', '1439993280.0', '2', '5389']
["Parents of Reddit, what's something that your kid has done that you pretended to be angry about but secretly impressed or amused you?", '7553', '1439161809.0', '0', '11520']
['What is a good subreddit to binge read the All Time Top Posts of?', '7498', '1438822288.0', '0', '2780']
['What would the person who named Walkie Talkies have named other items?', '7501', '1447904351.0', '4', '6720']
["People who grew up in a different socioeconomic class as your significant others, what are the notable differences you've noticed and how does it affect your relationship (if at all)?", '7419', '1440358069.0', '0', '8603']
"""




"""
6: Counting Simple Matches In The Data Set With Re()
We mentioned the re module earlier, and now we'll begin to use it in our code. One useful function the module provides is re.search.

With re.search(regex, string), we can check whether string is a match for regex.
If it is, the expression will return a match object.
If it isn't, it will return None.
For now, we won't worry about returning the actual matches - we'll just compare the result to None to see whether we have a match or not.


if re.search("needle", "haystack") is not None:
    print("We found it!")
else:
    print("Not a match")
The code above will print Not a match, because "haystack" is not a match for the regex "needle".

You may have noticed that many of the posts in our AskReddit database are directed towards particular groups of people, using phrases like "Soldiers of Reddit".
These types of posts are common, and always follow a similar format. We can use regular expressions to count how many of them are in the top 1,000.

Let's do this in our next exercise.
We've already read the data set into the variable posts.

Instructions
Count the number of posts in our data set that match the regex "of Reddit".
Assign the count to of_reddit_count.

"""
import re

of_reddit_count = 0
for row in posts:
    if re.search("of Reddit", row[0]) is not None:
        of_reddit_count += 1
""" Console Output or Results

"""



"""
7: Using Square Brackets To Match Multiple Characters
If you look at the data set closely, you may notice that some posts use "of Reddit", and others use "of reddit".
While both versions have the same format, the capitalization of "Reddit" is different.
We can account for this inconsistency with square brackets.
We use square brackets in a regex to indicate that any character within them can fill the space.

For example, the regex "[bcr]at" would match the substrings "bat", "cat", and "rat", but nothing else.
We indicate that the first character in the regex can be either "b", "c" or "r".

Instructions
Use square bracket notation to make the code account for both capitalizations of "Reddit", and count how many posts contain "of Reddit" or "of reddit" in the title.
Assign the resulting count to of_reddit_count.
"""
import re

of_reddit_count_old = 0
for row in posts:
    if re.search("of Reddit", row[0]) is not None:
        of_reddit_count_old += 1

of_reddit_count = 0
for row in posts:
    if re.search("of [Rr]eddit", row[0]) is not None:
        of_reddit_count += 1

print(of_reddit_count_old)
print("------------------")
print(of_reddit_count)
""" Console Output or Results
Output
76
------------------
102
"""



"""
8: Escaping Special Characters
Our data set contains a lot of posts that use the [Serious] tag.
AskReddit members use this tag to indicate that they're not looking for humorous responses, and that their question should be taken seriously.
We'd like to search through our data set to see how many posts have this tag, but the regex "[Serious]" doesn't do what we need.
Since square brackets serve a special function within regular expressions, "[Serious]" will match any string that contains "S", "e", "r", etc.

To deal with this sort of problem, we need to escape special characters.
In regular expressions, escaping a character means indicating that you don't want the character to do anything special, and that the interpreter should treat it just like any other character.
We use the backslash ("\") to escape characters in a regex.

Suppose we wanted to match all of the strings that end with a period.
If we used ".$", it would match all strings that contain any character, because "." has that special meaning.
Instead, we need to escape the "." with a backslash, so our regex becomes "\.$".

Instructions
Escape the square bracket characters to count the number of posts in our data set that contain the "[Serious]" tag.
Assign the count to serious_count.
"""
import re

serious_count = 0
for row in posts:
    if re.search("\[Serious\]", row[0]) is not None:
        serious_count += 1

print(serious_count)
""" Console Output or Results
Output
69
"""



"""
9: Combining Escaped Characters And Multiple Matches
Some people tag serious posts as "[Serious]", and others as "[serious]".
We should account for both capitalizations.

Instructions
Refine the code to count how many posts have either "[Serious]" or "[serious]" in the title.
Assign the count to serious_count.
"""
import re

serious_count_old = 0
for row in posts:
    if re.search("\[Serious\]", row[0]) is not None:
        serious_count_old += 1

serious_count = 0
for row in posts:
    if re.search("\[[Ss]erious\]", row[0]) is not None:
        serious_count += 1

print(serious_count_old)
print("----------------")
print(serious_count)
""" Console Output or Results
Output
69
----------------
77
"""




"""
10: Adding More Complexity To Your Regular Expression
On the previous screen, you saw that we can use square brackets as both special notation and escaped characters, all in the same regex.
We'll be using more brackets to refine our search.

In our data set, some users have tagged their posts with "(Serious)" or "(serious)", including the parentheses.
Therefore, we should account for both square brackets and parentheses.
We can do this by using square bracket notation, and escaping the "[", "]", "(", and ")" characters with the backslash.

Instructions
Refine the code so that it counts how many posts have the serious tag enclosed in either square brackets or parentheses.
Assign the count to serious_count.
"""
import re

serious_count_old = 0
for row in posts:
    if re.search("\[[Ss]erious\]", row[0]) is not None:
        serious_count_old += 1

serious_count = 0
for row in posts:
    if re.search("[\[\(][Ss]erious[\]\)]", row[0]) is not None:
        serious_count += 1

print(serious_count_old)
print("----------------")
print(serious_count)
""" Console Output or Results
Output
77
----------------
80
"""




"""
11: Combining Multiple Regular Expressions
We should consider a post serious only if the tag occurs at the beginning or end of the title.
To match titles with the tag at the beginning, we can use the "^" character in a regex.
To match titles with the tag at the end, we can use "$".
These characters produce two different regular expressions, and we'd like to identify all titles that match either of them.

To combine regular expressions, we use the "|" character.
For example, "cat|dog" would match "catfish" and "hotdog", because both of these strings match either "cat" or "dog".
Similarly, we can combine our regular expressions for the serious tags with the "|" operator to match all titles that either begin or end with the tag.

Instructions
Use the "^" character to count how many posts include the serious tag at the beginning of the title. Assign this count to serious_start_count.
Use the "$" character to count how many posts include the serious tag at the end of the title. Assign this count to serious_end_count.
Use the "|" character to count how many posts include the serious tag at either the beginning or end of the title. Assign this count to serious_count_final.
"""
import re

serious_start_count = 0
serious_end_count = 0
serious_count_final = 0

for row in posts:
    if re.search("^[\[\(][Ss]erious[\]\)]", row[0]) is not None:
        serious_start_count += 1

for row in posts:
    if re.search("[\[\(][Ss]erious[\]\)]$", row[0]) is not None:
        serious_end_count  += 1

for row in posts:
    if re.search("^[\[\(][Ss]erious[\]\)]|[\[\(][Ss]erious[\]\)]$", row[0]) is not None:
        serious_count_final += 1

print(serious_start_count)
print("--------")
print(serious_end_count)
print("--------")
print(serious_count_final)
""" Console Output or Results
Output
69
--------
11
--------
80
"""



"""
12: Using Regular Expressions To Substitute Strings
We've looked at one way we can account for inconsistencies in data; now let's examine another approach.
The re module provides a sub() function that takes the following parameters (in order):


1. pattern - The regex to match
2. repl    - The string that should replace the substring matches
3. string  - The string containing the pattern we want to search
If we were to call re.sub("yo", "hello", "yo world"), the function will replace the "yo" in "yo world" with "hello", producing the result "hello world".
If it doesn't find a pattern, the re.sub() function simply returns the original string.

Let's use re.sub() to convert all serious tags to the format "[Serious]".

Instructions
Replace "[serious]", "(Serious)", and "(serious)" with "[Serious]" for all of the titles in posts.
You should only need to use one call to sub(), and one regex.
Recall that the repl argument is an ordinary string. It's not a regex, so you don't need to escape characters like "[".
Append each formatted row to posts_new.
"""
import re
posts_new = []
for row in posts:
    row[0] = re.sub("[\[\(][Ss]erious[\]\)]", "[Serious]", row[0])
    posts_new.append(row)
""" Console Output or Results

"""



"""
13: Matching Years With Regular Expressions
Let's return to the example from the beginning of our mission.
Suppose we need to extract years from strings.
An intuitive way to do this would be to match any string that contains four consecutive integers.
We can indicate that we're looking for integers in a pattern by using square brackets ("[" and "]"), along with a dash ("-").
For example, "[0-9]" will match any character that falls between 0 and 9 (all of which will be one-digit integers).
Similarly, "[a-z]" would match any lowercase letter. We can also specify smaller ranges like "[3-5]" or "[d-g]".

Since we want to match four consecutive integers, our regex could be "[0-9][0-9][0-9][0-9]".
This would work, but let's also add the condition that we only want to match years after year 999 and before year 3000 (any other four-digit numbers in a string are probably not years).

Instructions
We've loaded a number of strings into the strings variable for you.
Loop through strings and use re.search() to determine whether each string contains a year between 1000 and 2999.
Store every string that contains a year in year_strings. The .append() function will help here.
"""
import re

year_strings = []
for year in strings:
    if re.search("[1-2][0-9][0-9][0-9]",year) is not None:
        year_strings.append(year)
print(strings)
print("------------")
print(year_strings)
""" Console Output or Results
Output
['War of 1812', 'There are 5280 feet to a mile', 'Happy New Year 2016!']
------------
['War of 1812', 'Happy New Year 2016!']
"""



"""
14: Repeating Characters In Regular Expressions
On the previous screen, we used the regex "[1-2][0-9][0-9][0-9]", which looks a bit repetitive.
Luckily, there's a better way to do it!

We can use curly brackets ("{" and "}") to indicate that a pattern should repeat.
To match any four-digit number, for example, we could repeat the pattern "[0-9]" four times by writing "[0-9]{4}".

Instructions
We've loaded a number of strings into the strings variable for you.
Loop through strings and use re.search() to determine whether each string contains a year between 1000 and 2999. Use a regex that takes advantage of curly brackets.
Store every string that contains a year in year_strings. The .append() function will help here.
"""
import re

year_strings = []
for year in strings:
    if re.search("[1-2][0-9]{3}",year) is not None:
        year_strings.append(year)
print(strings)
print("------------")
print(year_strings)
""" Console Output or Results
Output
['War of 1812', 'There are 5280 feet to a mile', 'Happy New Year 2016!']
------------
['War of 1812', 'Happy New Year 2016!']
"""




"""
15: Challenge: Extracting All Years
Finally, let's extract years from a string.
The re module contains a findall() function that returns a list of substrings matching the regex. re.findall("[a-z]", "abc123") would return ["a", "b", "c"], because those are the substrings that match the regex.

Instructions
Use re.findall() to generate a list of all years between 1000 and 2999 in the string years_string.
Assign the result to years.
"""
import re

years = []
years = re.findall("[1-2][0-9]{3}",years_string)

print(years_string)
print("------------")
print(years)
""" Console Output or Results
Output
2015 was a good year, but 2016 will be better!
------------
['2015', '2016']
"""
