"""
01/2017
Dataquest : Data Analyst Path
Step 4: Working With Data Sources
SubStep : APIs And Web Scraping : Working With APIs
"""



"""
1: What's An API?
We've worked with data sets pretty extensively so far. While they're popular resources, there are many cases where it's impractical to use one.

Here are a few situations where data sets don't work well:

The data change frequently. It doesn't really make sense to regenerate a data set of stock prices, for example, and download it every minute. This approach would require a lot of bandwidth, and be very slow.
You only want a small piece of a much larger data set. Reddit comments are one example. What if you want to pull just your own comments from reddit? It doesn't make much sense to download the entire reddit database, then filter it for a few items.
It involves repeated computation. For example, Spotify has an API that can tell you the genre of a piece of music. You could theoretically create your own classifier and use it to categorize music, but you'll never have as much data as Spotify does.
In cases like these, an application program interface (API) is the right solution. An API is a set of methods and tools that allows different applications to interact with each other. Programmers use APIs to query and retrieve data dynamically (which they can then integrate with their own apps). A client can retrieve information quickly and effectively through an API.

Reddit, Spotify, Twitter, Facebook, and many other companies provide free APIs that enable developers to access the information they store on their servers; others charge for access to their APIs.

In this mission, we'll query a basic API to retrieve data about the International Space Station (ISS). Using an API will save us time and effort, instead of doing all the computation ourselves.
"""


"""
2: Introduction To API Requests
Organizations host their APIs on Web servers. When you type www.google.com in your browser's address bar, your computer is actually asking the www.google.com server for a Web page, which it then returns to your browser.

APIs work much the same way, except instead of your Web browser asking for a Web page, your program asks for data. The API usually returns this data in JavaScript Object Notation (JSON) format. We'll discuss JSON more later on in this mission.

We make an API request to the Web server we want to get data from. The server then replies and sends it to us. In Python, we use the requests library to do this.
"""




"""
3: Types Of Requests
There are many different types of requests. The most common is a GET request, which we use to retrieve data. We'll explore the other types in later missions.

We can use a simple GET request to retrieve information from the OpenNotify API.

OpenNotify has several API endpoints. An endpoint is a server route for retrieving specific data from an API. For example, the /comments endpoint on the reddit API might retrieve information about comments, while the /users endpoint might retrieve data about users.

The first endpoint we'll look at on OpenNotify is the iss-now.json endpoint. This endpoint gets the current latitude and longitude position of the ISS. A data set wouldn't be a great fit for this task because the information changes often, and involves some calculation on the server.

Check out the complete list of OpenNotify endpoints.

Instructions
The server will send a status code indicating the success or failure of your request. You can get the status code of the response from response.status_code.
Assign the status code to the variable status_code.
"""
# Make a get request to get the latest position of the ISS from the OpenNotify API.
response = requests.get("http://api.open-notify.org/iss-now.json")
status_code = response.status_code
print(status_code)
""" Console output or Results
Output
200
"""




"""
4: Understanding Status Codes
The request we just made returned a status code of 200. Web servers return status codes every time they receive an API request. A status code provides information about what happened with a request. Here are some codes that are relevant to GET requests:

200 - Everything went okay, and the server returned a result (if any).
301 - The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint's name has changed.
401 - The server thinks you're not authenticated. This happens when you don't send the right credentials to access an API (we'll talk about this in a later mission).
400 - The server thinks you made a bad request. This can happen when you don't send the information the API requires to process your request, among other things.
403 - The resource you're trying to access is forbidden; you don't have the right permissions to see it.
404 - The server didn't find the resource you tried to access.
Instructions
Make a GET request to http://api.open-notify.org/iss-pass.
Assign the status code of the response to status_code.
"""
# Enter your answer below.
status_code = requests.get("http://api.open-notify.org/iss-pass").status_code
print(status_code)
""" Console output or Results
Output
404
"""




"""
5: Hitting The Right Endpoint
iss-pass wasn't a valid endpoint, so the API's server sent us a 404 status code in response. We forgot to add .json at the end, like the API documentation tells us to do.

Instructions
Make a GET request to http://api.open-notify.org/iss-pass.json.
Assign the status code of the response to status_code.
"""
# Enter your answer below.
status_code = requests.get("http://api.open-notify.org/iss-pass.json").status_code
print(status_code)
""" Console output or Results
Output
400
"""



"""
6: Adding Query Parameters
You'll see that in the last example, we got a 400 status code, which indicates a bad request. If you look at the documentation for the OpenNotify API, we see that the ISS Pass endpoint requires two parameters.

This endpoint returns the next time the ISS will pass over a given location on the Earth.

To request this information, we'll need to pass the coordinates for a specific location to the API. We do this by passing in two parameters, latitude and longitude.

To accomplish this, we can add an optional keyword argument, params, to our request. In this case, we need to pass in two parameters:

lat - The latitude of the location
lon - The longitude of the location
We can make a dictionary that contains these parameters, and then pass them into the function.

We can also do the same thing directly by adding the query parameters to the url, like this:

http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74

It's almost always preferable to set up the parameters as a dictionary, because the requests library we mentioned earlier takes care of certain issues, like properly formatting the query parameters.

Instructions
Get a response for the latitude 37.78 and the longitude -122.41 (the coordinates of San Francisco).
Retrieve the content of the response with response.content.
Assign the content to the variable content.
"""
# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Print the content of the response (the data the server returned)
print(response.content)

# This gets the same data as the command above
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
print(response.content)

parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
content = response.content
print(content)
""" Console output or Results
Output
b'{\n  "message": "success", \n  "request": {\n    "altitude": 100, \n    "datetime": 1441417753, \n    "latitude": 40.71, \n    "longitude": -74.0, \n    "passes": 5\n  }, \n  "response": [\n    {\n      "duration": 330, \n      "risetime": 1441445639\n    }, \n    {\n      "duration": 629, \n      "risetime": 1441451226\n    }, \n    {\n      "duration": 606, \n      "risetime": 1441457027\n    }, \n    {\n      "duration": 542, \n      "risetime": 1441462894\n    }, \n    {\n      "duration": 565, \n      "risetime": 1441468731\n    }\n  ]\n}'
b'{\n  "message": "success", \n  "request": {\n    "altitude": 100, \n    "datetime": 1441417753, \n    "latitude": 40.71, \n    "longitude": -74.0, \n    "passes": 5\n  }, \n  "response": [\n    {\n      "duration": 329, \n      "risetime": 1441445639\n    }, \n    {\n      "duration": 629, \n      "risetime": 1441451226\n    }, \n    {\n      "duration": 606, \n      "risetime": 1441457027\n    }, \n    {\n      "duration": 542, \n      "risetime": 1441462894\n    }, \n    {\n      "duration": 565, \n      "risetime": 1441468731\n    }\n  ]\n}'
b'{\n  "message": "success", \n  "request": {\n    "altitude": 100, \n    "datetime": 1441417753, \n    "latitude": 37.78, \n    "longitude": -122.41, \n    "passes": 5\n  }, \n  "response": [\n    {\n      "duration": 369, \n      "risetime": 1441456672\n    }, \n    {\n      "duration": 626, \n      "risetime": 1441462284\n    }, \n    {\n      "duration": 581, \n      "risetime": 1441468104\n    }, \n    {\n      "duration": 482, \n      "risetime": 1441474000\n    }, \n    {\n      "duration": 509, \n      "risetime": 1441479853\n    }\n  ]\n}'
"""



"""
7: JSON Format
You may have noticed that the content of the API response we received earlier was a string. Strings are the way we pass information back and forth through APIs, but it's hard to get the information we want out of them. How do we know how to decode the string we receive and work with it in Python?

Luckily, there's a format we call JSON. We mentioned it earlier in the mission. This format encodes data structures like lists and dictionaries as strings to ensure that machines can read them easily. JSON is the primary format for sending and receiving data through APIs.

Python offers great support for JSON through its json library. We can convert lists and dictionaries to JSON, and vice versa. Our ISS Pass data, for example, is a dictionary encoded as a string in JSON format.

The JSON library has two main methods:

dumps -- Takes in a Python object, and converts it to a string
loads -- Takes a JSON string, and converts it to a Python object
Instructions
Use the JSON function loads to convert fast_food_franchise_string to a Python object.
Assign the resulting Python object to fast_food_franchise_2.
"""
# Make a list of fast food chains.
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
print(type(best_food_chains))

# Import the JSON library.
import json

# Use json.dumps to convert best_food_chains to a string.
best_food_chains_string = json.dumps(best_food_chains)
print(type(best_food_chains_string))

# Convert best_food_chains_string back to a list.
print(type(json.loads(best_food_chains_string)))

# Make a dictionary
fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

# We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
print(type(fast_food_franchise_string))

fast_food_franchise_2 = json.loads(fast_food_franchise_string)
print(fast_food_franchise_2)
""" Console output or Results
Output
<class 'list'>
<class 'str'>
<class 'list'>
<class 'str'>
{'Starbucks': 10821, 'Pizza Hut': 7600, 'McDonalds': 14098, 'Subway': 24722}
"""




"""
8: Getting JSON From A Request
We can get the content of a response as a Python object by using the .json() method on the response.

Instructions
Get the duration value of the ISS' first pass over San Francisco (this is the duration key of the first dictionary in the response list).
Assign the value to first_pass_duration.
"""
# Make the same request we did two screens ago.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a Python object.  Verify that it's a dictionary.
json_data = response.json()
print(type(json_data))
print(json_data)

first_pass_duration = json_data["response"][0]["duration"]
print(first_pass_duration)
""" Console output or Results
Output
<class 'dict'>
{'request': {'longitude': -122.41, 'altitude': 100, 'passes': 5, 'latitude': 37.78, 'datetime': 1441417753},
'response': [
{'risetime': 1441456672, 'duration': 369},
{'risetime': 1441462284, 'duration': 626},
{'risetime': 1441468104, 'duration': 581},
{'risetime': 1441474000, 'duration': 482},
{'risetime': 1441479853, 'duration': 509}],
'message': 'success'}
369
"""




"""
9: Content Type
The server sends more than a status code and the data when it generates a response.
It also sends metadata containing information on how it generated the data and how to decode it.
This information appears in the response headers. We can access it using the .headers property that responses have.

The headers will appear as a dictionary. For now, the content-type within the headers is the most important key.
It tells us the format of the response, and how to decode it.
For the OpenNotify API, the format is JSON, which is why we could decode it with JSON earlier.

Instructions
Get content-type from response.headers.
Assign the content type to the content_type variable.
"""
# Headers is a dictionary
print(response.headers)
content_type = response.headers["content-type"]
print("-------------")
print(content_type)
""" Console output or Results
Output
{'server': 'gunicorn/19.3.0', 'date': 'Sat, 05 Sep 2015 01:49:13 GMT', 'content-type': 'application/json', 'via': '1.1 vegur', 'content-length': '520', 'connection': 'keep-alive'}
-------------
application/json
"""




"""
10: Finding The Number Of People In Space
OpenNotify has one more API endpoint, astros.json. It tells us how many people are currently in space. You can find the format of the responses here.
"""
# Call the API here.
response = requests.get("http://api.open-notify.org/astros.json")
json_data = response.json()
print(json_data)
in_space_count = json_data["number"]
print("-------------")
print(in_space_count)
""" Console output or Results
Output
{'people':
[
{'craft': 'ISS', 'name': 'Gennady Padalka'}, {'craft': 'ISS', 'name': 'Mikhail Kornienko'},
{'craft': 'ISS', 'name': 'Scott Kelly'}, {'craft': 'ISS', 'name': 'Oleg Kononenko'},
{'craft': 'ISS', 'name': 'Kimiya Yui'}, {'craft': 'ISS', 'name': 'Kjell Lindgren'},
{'craft': 'ISS', 'name': 'Sergey Volkov'}, {'craft': 'ISS', 'name': 'Andreas Mogensen'},
{'craft': 'ISS', 'name': 'Aidyn Aimbetov'}],
'message': 'success',
'number': 9}
-------------
9
"""
