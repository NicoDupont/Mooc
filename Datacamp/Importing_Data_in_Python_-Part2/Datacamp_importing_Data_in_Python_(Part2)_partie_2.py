# Datacamp - Importing Data in Python (Part 2)
# partie 2 : Interacting with APIs to import data from the web 
# Python 3.X


""" question réponse : 4
Pop quiz: What exactly is a JSON?
50xp

Which of the following is not true of the JSON file format?
Possible Answers

    JSONs consist of key-value pairs.
    1
    JSONs are human-readable.
    2
    The JSON file format arose out of a growing need for real-time server-to-browser communication.
    3
    The function json.load() will load the JSON into Python as a list.
    4
    The function json.load() will load the JSON into Python as a dictionary.
"""




"""
Loading and exploring a JSON
100xp

Now that you know what a JSON is, you'll load one into your Python environment and explore it yourself. Herein, you'll load the JSON 'a_movie.json' into the variable json_data, which will be a dictionary. You'll then explore the JSON contents by printing the key-value pairs of json_data to the shell.
Instructions

    Load the JSON 'a_movie.json' into the variable json_data within the context provided by the with statement. To do so, use the function json.load() within the context manager.
    Use a for loop to print all key-value pairs in the dictionary json_data. Recall that you can access a value in a dictionary using the syntax: dictionary[key].

"""
# Load JSON: json_data
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])
""" sortie Ipython
<script.py> output:
    Year:  2010
    Metascore:  95
    imdbVotes:  485,392
    Country:  USA
    Director:  David Fincher
    imdbID:  tt1285016
    imdbRating:  7.7
    Poster:  https://images-na.ssl-images-amazon.com/images/M/MV5BMTM2ODk0NDAwMF5BMl5BanBnXkFtZTcwNTM1MDc2Mw@@._V1_SX300.jpg
    Runtime:  120 min
    Rated:  PG-13
    Awards:  Won 3 Oscars. Another 161 wins & 162 nominations.
    Language:  English, French
    Title:  The Social Network
    Released:  01 Oct 2010
    Writer:  Aaron Sorkin (screenplay), Ben Mezrich (book)
    Response:  True
    Actors:  Jesse Eisenberg, Rooney Mara, Bryan Barter, Dustin Fitzsimons
    Genre:  Biography, Drama
    Type:  movie
    Plot:  Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook, but is later sued by two brothers who claimed he stole their idea, and the co-founder who was later squeezed out of the business.

"""





""" question réponse : 3
Pop quiz: Exploring your JSON
50xp

Load the JSON 'a_movie.json' into a variable, which will be a dictionary. Do so by copying, pasting and executing the following code in the IPython Shell:

import json
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

Print the values corresponding to the keys 'Title' and 'Year' and answer the following question about the movie that the JSON describes:

Which of the following statements is true of the movie in question?
Possible Answers

    The title is 'Kung Fu Panda' and the year is 2010.
    1
    The title is 'Kung Fu Panda' and the year is 2008.
    2
    The title is 'The Social Network' and the year is 2010.
    3
    The title is 'The Social Network' and the year is 2008.
"""

""" sortie Ipython
In [1]: import json
... with open("a_movie.json") as json_file:
...     json_data = json.load(json_file)

In [2]: json_data['Title']
Out[2]: 'The Social Network'

In [3]: json_data['Year']
Out[3]: '2010'
"""





""" question réponse : 4
Pop quiz: What's an API?
50xp

Which of the following statements about APIs is NOT true?
Possible Answers

    An API is a set of protocols and routines for building and interacting with software applications.
    1
    API is an acronym and is short for Application Program interface.
    2
    It is common to pull data from APIs in the JSON file format.
    3
    All APIs transmit data only in the JSON file format.
    4
    An API is a bunch of code that allows two software programs to communicate with each other.
    5
"""






"""
API requests
100xp

Now it's your turn to pull some movie data down from the Open Movie Database (OMDB) using their API. The movie you'll query the API about is The Social Network. Recall that, in the video, to query the API about the movie Hackers, Hugo's query string was 'http://www.omdbapi.com/?t=hackers' and had a single argument t=hackers.
Instructions

    Import the requests package.
    Assign to the variable url the URL of interest in order to query 'http://www.omdbapi.com' for the data corresponding to the movie The Social Netork. The query string should have one argument t=social+network.
    Print the text of the reponse object r by using its text attribute and passing the result to the print() function.

"""
# Import requests package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?t=social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)
""" sortie Ipython
<script.py> output:
    {"Title":"The Social Network","Year":"2010","Rated":"PG-13","Released":"01 Oct 2010","Runtime":"120 min","Genre":"Biography, Drama","Director":"David Fincher","Writer":"Aaron Sorkin (screenplay), Ben Mezrich (book)","Actors":"Jesse Eisenberg, Rooney Mara, Bryan Barter, Dustin Fitzsimons","Plot":"Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook, but is later sued by two brothers who claimed he stole their idea, and the co-founder who was later squeezed out of the business.","Language":"English, French","Country":"USA","Awards":"Won 3 Oscars. Another 161 wins & 162 nominations.","Poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BMTM2ODk0NDAwMF5BMl5BanBnXkFtZTcwNTM1MDc2Mw@@._V1_SX300.jpg","Metascore":"95","imdbRating":"7.7","imdbVotes":"485,392","imdbID":"tt1285016","Type":"movie","Response":"True"}
"""






"""
JSON- from the web to Python
100xp

Wow, congrats! You've just queried your first API programmatically in Python and printed the text of the response to the shell. However, as you know your response is actually a JSON, you can do one step better and decode the JSON. You can then print the key-value pairs of the resulting dictionary. That's what you're going to do now!
Instructions

    Pass the variable url to the requests.get() function in order to send the relevant request and catch the response, assigning the resultant response message to the variable r.
    Apply the json() method to the response object r and store the resulting dictionary in the variable json_data.
    Hit Submit Answer to print the key-value pairs of the dictionary json_data to the shell.

"""
# Import package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?t=social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])
""" sortie Ipython
<script.py> output:
    Year:  2010
    Metascore:  95
    imdbVotes:  485,392
    Country:  USA
    Director:  David Fincher
    Released:  01 Oct 2010
    imdbRating:  7.7
    Poster:  https://images-na.ssl-images-amazon.com/images/M/MV5BMTM2ODk0NDAwMF5BMl5BanBnXkFtZTcwNTM1MDc2Mw@@._V1_SX300.jpg
    imdbID:  tt1285016
    Rated:  PG-13
    Awards:  Won 3 Oscars. Another 161 wins & 162 nominations.
    Language:  English, French
    Title:  The Social Network
    Runtime:  120 min
    Writer:  Aaron Sorkin (screenplay), Ben Mezrich (book)
    Response:  True
    Actors:  Jesse Eisenberg, Rooney Mara, Bryan Barter, Dustin Fitzsimons
    Genre:  Biography, Drama
    Type:  movie
    Plot:  Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook, but is later sued by two brothers who claimed he stole their idea, and the co-founder who was later squeezed out of the business.
"""







"""
Checking out the Wikipedia API
100xp

You're doing so well and having so much fun that we're going to throw one more API at you: the Wikipedia API, documented here. You'll figure out how to find and extract from the Wikipedia page for Pizza. What gets a bit wild here is that your query will return nested JSONs, that is, JSONs with JSONs, but Python can handle that because it will translate them into dictionaries within dictionaries.

The URL that requests the relevant query from the Wikipedia API is

https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza

Instructions

    Assign the relevant URL to the variable url.
    Apply the json() method to the response object r and store the resulting dictionary in the variable json_data.
    The variable pizza_extract holds the HTML of an extract from Wikipedia's Pizza page as a string; use the function print() to print this string to the shell.

"""
# Import package
import requests

# Assign URL to variable: url
url = "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza"

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)
""" sortie Ipython
<script.py> output:
    <p><b>Pizza</b> is a flatbread generally topped with tomato sauce and cheese and baked in an oven. It is commonly topped with a selection of meats, vegetables and condiments. The term was first recorded in the 10th century, in a Latin manuscript from Gaeta in Central Italy. The modern pizza was invented in Naples, Italy, and the dish and its variants have since become popular and common in many areas of the world.</p>
    <p>In 2009, upon Italy's request, Neapolitan pizza was safeguarded in the European Union as a Traditional Speciality Guaranteed dish. The Associazione Verace Pizza Napoletana (the True Neapolitan Pizza Association) is a non-profit organization founded in 1984 with headquarters in Naples. It promotes and protects the "true Neapolitan pizza".</p>
    <p>Pizza is sold fresh or frozen, either whole or in portions, and is a common fast food item in Europe and North America. Various types of ovens are used to cook them and many varieties exist. Several similar dishes are prepared from ingredients commonly used in pizza preparation, such as calzone and stromboli.</p>
    <p></p>
"""