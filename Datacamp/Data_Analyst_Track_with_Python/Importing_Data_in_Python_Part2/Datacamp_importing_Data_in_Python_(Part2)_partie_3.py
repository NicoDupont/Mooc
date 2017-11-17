# Datacamp - Importing Data in Python (Part 2)
# partie 3 : Diving deep into the Twitter API  
# Python 3.X


""" 
API Authentication
100xp

The package tweepy is great at handling all the Twitter API OAuth Authentication details for you. All you need to do is to pass your authentication credentials to it. In this interactive exercise, we have created some mock authentication credentials (if you wanted to replicate this at home, you would need to create a Twitter App as Hugo detailed in the video). Your task is to pass these credentials to tweepy's OAuth handler.
Instructions

    Import the package tweepy.
    Pass the parameters consumer_key and consumer_secret to the function tweepy.OAuthHandler().
    Complete the passing of OAuth credentials to the OAuth handler auth by applying to it the method set_access_token(), along with arguments access_token and access_token_secret.

"""
# Import package
import tweepy

# Store OAuth authentication credentials in relevant variables
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
""" sortie Ipython

"""







""" 
Streaming tweets
100xp

Now that you have set up your authentication credentials, it is time to stream some tweets! In the pre-exercise code, we have already defined the Tweet Stream Listener Class, just as Hugo did in the introductory video. You can find the code for the Tweet Stream Listener Class here.

Your task is to create the Stream object and to filter tweets according to particular keywords.
Instructions

    Create your Stream object with authentication by passing to tweepy.Stream() the authentication handler auth and the Stream listener l;
    To filter Twitter Streams, pass to the track argument in stream.filter() a list containing the desired keywords 'clinton', 'trump', 'sanders', and 'cruz'.

"""
# Initialize Stream listener
l = MyStreamListener()

# Create you Stream object with authentication
stream = tweepy.Stream(auth, l)


# Filter Twitter Streams to capture data by the keywords:
stream.filter(track=['clinton','trump','sanders','cruz'])
""" sortie Ipython

"""








""" 
Load and explore your Twitter data
100xp

Now that you've got your Twitter data sitting locally in a text file, it's time to explore it! This is what you'll do in the next few interactive exercises. In this exercise, you'll read the Twitter data into a list tweets_data.
Instructions

    Assign the filename 'tweets.txt' to the variable tweets_data_path.
    Initialize tweets_data as an empty list to store the tweets in.
    Within the for loop initiated by for line in tweets_file:, load each tweet into a variable tweet using json.loads(), then append tweet to tweets_data using the append() method.
    Hit submit and check out the keys of the first tweet dictionary printed to the shell.

"""
# Import package
import json

# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    print(tweet)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())
""" sortie Ipython

"""







""" 
Twitter data to DataFrame
100xp

Now that you have the Twitter data in a list of dictionaries tweets_data, where each dictionary corresponds to a single tweet, it's time to extract the text of the tweets, along with the language of the tweet. The text in a tweet t1 is stored as the value t1['text']; similarly, the language is stored in t1['lang']. Your task is to build a DataFrame in which each row is a tweet and has two columns, one for text, the other for lang.
Instructions

    Use pd.DataFrame() to construct a DataFrame of tweet texts and languages: to do so, the first argument should be tweets_data, a list of dictionaries. The second argument to pd.DataFrame() is a list of the keys you wish to have as columns. Assign the result of the pd.DataFrame() call to df.
    Print the head of the DataFrame.

"""
# Import package
import pandas as pd

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text','lang'])

# Print head of DataFrame
print(df.head())
""" sortie Ipython
In [2]: print(tweets_data[0].keys())
dict_keys(['retweeted', 'timestamp_ms', 'retweet_count', 'truncated', 'possibly_sensitive', 'geo', 'is_quote_status', 'lang', 'in_reply_to_screen_name', 'created_at', 'in_reply_to_user_id', 'extended_entities', 'in_reply_to_status_id_str', 'in_reply_to_user_id_str', 'contributors', 'id', 'in_reply_to_status_id', 'favorite_count', 'user', 'favorited', 'text', 'place', 'coordinates', 'source', 'filter_level', 'retweeted_status', 'entities', 'id_str'])

<script.py> output:
                                                    text lang
    0  b"RT @bpolitics: .@krollbondrating's Christoph...   en
    1  b'RT @HeidiAlpine: @dmartosko Cruz video found...   en
    2  b'Njihuni me Zonj\\xebn Trump !!! | Ekskluzive...   et
    3  b"Your an idiot she shouldn't have tried to gr...   en
    4  b'RT @AlanLohner: The anti-American D.C. elite...   en

"""







""" 
A little bit of Twitter text analysis
100xp

Now that you have your DataFrame of tweets set up, you're going to do a bit of text analysis to count how many tweets contain the words 'clinton', 'trump', 'sanders' and 'cruz'. In the pre-exercise code, we have defined the following function word_in_text(), which will tell you whether the first argument (a word) occurs within the 2nd argument (a tweet).

import re

def word_in_text(word, tweet):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, tweet)

    if match:
        return True
    return False

You're going to iterate over the rows of the DataFrame and calculate how many tweets contain each of our keywords! The list of objects for each candidate has been initialized to 0.
Instructions

    Within the for loop for index, row in df.iterrows():, the code currently increases the value of clinton by 1 each time a tweet mentioning 'Clinton' is encountered; complete the code so that the same happens for trump, sanders and cruz.

"""
# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])
""" sortie Ipython

"""






""" 
Plotting your Twitter data
100xp

Now that you have the number of tweets that each candidate was mentioned in, you can plot a bar chart of this data and this is what you'll do in this final exercise. You'll use the statistical data visualization library seaborn, which you may not have seen before but we'll guide you through. You'll first import seaborn as sns; you'll then construct a barplot of the data using sns.barplot, passing it two arguments: (i) a list of labels and (ii) a list containing the variables you wish to plot (clinton, trump and so on.)

Hopefully, you'll see that Trump was unreasonably represented! In the pre-exercise code, we have run the previous exercise solutions.
Instructions

    Import both matplotlib.pyplot and seaborn, using the aliases plt and sns, respectively.
    Complete the arguments of sns.barplot: the first argument should be the labels to appear on the x-axis; the second argument should be the list of the variables you wish to plot, as produced in the previous exercise.

"""
# Import packages
import matplotlib.pyplot as plt
import seaborn as sns


# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Plot histogram
ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel="count")
plt.show()
""" sortie Ipython

"""






""" 

"""

""" sortie Ipython

"""
