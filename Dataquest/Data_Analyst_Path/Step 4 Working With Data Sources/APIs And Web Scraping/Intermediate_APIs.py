"""
03/2017
Dataquest : Data Analyst Path
Step 4: Working With Data Sources
SubStep : APIs And Web Scraping : Intermediate APIs
"""



"""
1: Introduction
We looked at a basic API in the last mission. That API didn't require authentication, but most do.
Imagine that you're using the reddit API to pull a list of your private messages.
It would be a huge privacy breach for reddit to give that information to anyone, so requiring authentication makes sense.

APIs also use authentication to perform rate limiting.
Developers typically use APIs to build interesting applications or services.
In order to ensure that it remains available and responsive for all users, an API will prevent you from making too many requests in too short a time.
We call this restriction rate limiting. It ensures that one user can't overload the API server by making too many requests too fast.

In this mission, we'll explore the GitHub API and use it to pull some interesting data on repositories and users.
GitHub is a site for hosting code.
If you haven't looked at it, you should - it's a great place to share a portfolio.

GitHub has user accounts (example), repositories that contain code (example), and organizations that companies can create (example).

Take a look at the documentation for the GitHub API, and specifically the authentication section.
"""




"""
2: API Authentication
To authenticate with the GitHub API, we'll need to use an access token.
An access token is a credential we can generate on GitHub's website.
The token is a string that the API can read and associate with your account.

Using a token is preferable to a username and password for a few reasons:

Typically, you'll be accessing an API from a script.
If you put your username and password in the script and someone manages to get their hands on it, they can take over your account.
In contrast, you can revoke an access token to cancel an unauthorized person's access if there's a security breach.
Access tokens can have scopes and specific permissions.
For instance, you can make a token that has permission to write to your GitHub repositories and make new ones.
Or, you can make a token that can only read from your repositories.
Using read-access-only tokens in potentially insecure or shared scripts gives you more control over security.
You'll need to pass your token to the GitHub API through an Authorization header.
Just like the server sends headers in response to our request, we can send the server headers when we make a request.
Headers contain metadata about the request. We can use Python's requests library to make a dictionary of headers, and then pass it into our request.

We need to include the word token in the Authorization header, followed by our access token. Here's an example of an Authorization header:

{"Authorization": "token 1f36137fbbe1602f779300dad26e4c1b7fbab631"}

In this case, our access token is 1f36137fbbe1602f779300dad26e4c1b7fbab631.
GitHub generated this token and associated it with the account of Vik Paruchuri.

You should never share your token with anyone you don't want to have access to your account.
We've revoked the token you'll be using throughout this mission, so it isn't valid anymore.
Consider a token somewhat equivalent to a password, and store it securely.

Instructions
Make an authenticated request to https://api.github.com/users/VikParuchuri/orgs.
This will give us a list of the organizations a GitHub user belongs to.
Assign the JSON content of the response to orgs (you can get this with response.json()).
"""
# Create a dictionary of headers containing our Authorization header.
headers = {"Authorization": "token 1f36137fbbe1602f779300dad26e4c1b7fbab631"}

# Make a GET request to the GitHub API with our headers.
# This API endpoint will give us details about Vik Paruchuri.
response = requests.get("https://api.github.com/users/VikParuchuri", headers=headers)

# Print the content of the response.  As you can see, this token corresponds to the account of Vik Paruchuri.
print(response.json())

response = requests.get("https://api.github.com/users/VikParuchuri/orgs", headers=headers)
orgs = response.json()
""" Console output or Results
Output
{'email': 'vik.paruchuri@gmail.com', 'public_repos': 60, 'disk_usage': 711120, 'gists_url': 'https://api.github.com/users/VikParuchuri/gists{/gist_id}', 'private_gists': 1, 'followers': 100, 'html_url': 'https://github.com/VikParuchuri', 'created_at': '2011-07-13T18:18:07Z', 'type': 'User', 'bio': None, 'site_admin': False, 'avatar_url': 'https://avatars.githubusercontent.com/u/913340?v=3', 'repos_url': 'https://api.github.com/users/VikParuchuri/repos', 'gravatar_id': '', 'location': 'Boston, MA', 'owned_private_repos': 17, 'blog': 'http://www.vikparuchuri.com', 'hireable': None, 'name': 'Vik Paruchuri', 'total_private_repos': 17, 'company': 'dataquest.io', 'public_gists': 9, 'collaborators': 4, 'updated_at': '2015-08-19T18:44:48Z', 'following': 10, 'followers_url': 'https://api.github.com/users/VikParuchuri/followers', 'organizations_url': 'https://api.github.com/users/VikParuchuri/orgs', 'following_url': 'https://api.github.com/users/VikParuchuri/following{/other_user}', 'starred_url': 'https://api.github.com/users/VikParuchuri/starred{/owner}{/repo}', 'login': 'VikParuchuri', 'plan': {'space': 976562499, 'collaborators': 0, 'name': 'medium', 'private_repos': 20}, 'id': 913340, 'received_events_url': 'https://api.github.com/users/VikParuchuri/received_events', 'url': 'https://api.github.com/users/VikParuchuri', 'subscriptions_url': 'https://api.github.com/users/VikParuchuri/subscriptions', 'events_url': 'https://api.github.com/users/VikParuchuri/events{/privacy}'}
"""





"""
3: Endpoints And Objects
APIs usually let us retrieve information about specific objects in a database.
On the previous screen, for example, we retrieved information about a specific user object, VikParuchuri.
We could also retrieve information about other GitHub users through the same endpoint.
For example, https://api.github.com/users/torvalds would get us information about Linus Torvalds.

Instructions
Use the endpoint https://api.github.com/users/torvalds with the same headers from before to get information about Linus Torvalds.
Use the response.json() method to get the JSON of the response.
Assign the result to torvalds.
"""
# We've loaded headers in.

response = requests.get("https://api.github.com/users/torvalds", headers=headers)
torvalds = response.json()
print(torvalds)
""" Console output or Results
Output
{'location': 'Portland, OR', 'type': 'User', 'organizations_url': 'https://api.github.com/users/torvalds/orgs', 'email': None, 'received_events_url': 'https://api.github.com/users/torvalds/received_events', 'html_url': 'https://github.com/torvalds', 'updated_at': '2015-06-11T00:46:13Z', 'events_url': 'https://api.github.com/users/torvalds/events{/privacy}', 'following_url': 'https://api.github.com/users/torvalds/following{/other_user}', 'name': 'Linus Torvalds', 'public_gists': 0, 'bio': None, 'avatar_url': 'https://avatars.githubusercontent.com/u/1024025?v=3', 'followers_url': 'https://api.github.com/users/torvalds/followers', 'followers': 29687, 'url': 'https://api.github.com/users/torvalds', 'repos_url': 'https://api.github.com/users/torvalds/repos', 'subscriptions_url': 'https://api.github.com/users/torvalds/subscriptions', 'company': 'Linux Foundation', 'hireable': None, 'site_admin': False, 'gravatar_id': '', 'blog': None, 'created_at': '2011-09-03T15:26:22Z', 'starred_url': 'https://api.github.com/users/torvalds/starred{/owner}{/repo}', 'login': 'torvalds', 'following': 0, 'id': 1024025, 'public_repos': 2, 'gists_url': 'https://api.github.com/users/torvalds/gists{/gist_id}'}
"""





"""
4: Other Objects
In addition to users, the GitHub API has a few other types of objects.
For example, https://api.github.com/orgs/dataquestio will retrieve information about the Dataquest organization on GitHub.
https://api.github.com/repos/octocat/Hello-World will give us information about the Hello-World repository that the user octocat owns.

GitHub offers full documentation for all of the API's endpoints.

Instructions
Make a GET request to the https://api.github.com/repos/octocat/Hello-World endpoint.
Assign the JSON result to hello_world.

"""
# Enter your answer here.

response = requests.get("https://api.github.com/repos/octocat/Hello-World", headers=headers)
hello_world = response.json()
print(hello_world)




"""
5: Pagination
Sometimes, a request can return a lot of objects.
This might happen when you're doing something like listing out all of a user's repositories, for example.
Returning too much data will take a long time and slow the server down.
For example, if a user has 1,000+ repositories, requesting all of them might take 10+ seconds.
his isn't a great user experience, so it's typical for API providers to implement pagination.
This means that the API provider will only return a certain number of records per page.
You can specify the page number that you want to access. To access all of the pages, you'll need to write a loop.

To get the repositories a user has starred (marked as interesting), we can use the following API endpoint:

https://api.github.com/users/VikParuchuri/starred

We can add two pagination query parameters to it - page, and per_page.
page is the page we want to access, and per_page is the number of records we want to see on each page.
Typically, API providers enforce a cap on how high per_page can be, because setting it to an extremely high value defeats the purpose of pagination.

Check out the Github API documentation on pagination.

Instructions
Get the second page of repositories that Vik Paruchuri starred from the https://api.github.com/users/VikParuchuri/starred endpoint.
Assign the JSON of the response to page2_repos.
"""
params = {"per_page": 50, "page": 1}
response = requests.get("https://api.github.com/users/VikParuchuri/starred", headers=headers, params=params)
page1_repos = response.json()
params = {"per_page": 50, "page": 2}
response = requests.get("https://api.github.com/users/VikParuchuri/starred", headers=headers, params=params)
page2_repos = response.json()





"""
6: User-Level Endpoints

So far, we've looked at endpoints where we need to explicitly provide the username of the person whose information we're looking up.
For example, we used https://api.github.com/users/VikParuchuri/starred to pull up the repositories that VikParuchuri starred.

Since we've authenticated with our token, the system knows who we are, and can show us some relevant information without our having to specify our username.

Making a GET request to https://api.github.com/user will give us information about the user the authentication token is for.

There are other endpoints that behave like this.
They automatically provide information or allow us to take actions as the authenticated user.

Instructions

    Make a GET request to the "https://api.github.com/user" endpoint.
        Assign the JSON of the result to the user variable.

"""
# Enter your code here.
response = requests.get("https://api.github.com/user", headers=headers)
user = response.json()






"""
7: POST Requests

So far, we've been making GET requests. We use GET requests to retrieve information from a server (hence the name GET).
There are a few other types of API requests.

For example, we use POST requests to send information (instead of retrieve it), and to create objects on the API's server.
With the GitHub API, we can use POST requests to create new repositories.

Different API endpoints choose what types of requests they will accept. Not all endpoints will accept a POST request, and not all will accept a GET request.
You'll have to consult the API's documentation to figure out which endpoints accept which types of requests.

We can make POST requests using requests.post.
POST requests almost always include data, because we need to send the data the server will use to create the new object.

We pass in the data in a way that's very similar to what we do with query parameters and GET requests:

payload = {"name": "test"}
requests.post("https://api.github.com/user/repos", json=payload)

The code above will create a new repository named test under the account of the currently authenticated user.
It will convert the payload dictionary to JSON, and pass it along with the POST request.

Check out GitHub's API documentation for repositories to see a full list of what data we can pass in with this POST request. Here are just a couple data points:

    name -- Required, the name of the repository
    description -- Optional, the description of the repository

A successful POST request will usually return a 201 status code indicating that it was able to create the object on the server.
Sometimes, the API will return the JSON representation of the new object as the content of the response.

Instructions

    Create a repository named learning-about-apis.
    Assign the status code of the response to the status variable.

"""
# Create the data we'll pass into the API endpoint.  While this endpoint only requires the "name" key, there are other optional keys.
payload = {"name": "test"}

# We need to pass in our authentication headers!
response = requests.post("https://api.github.com/user/repos", json=payload, headers=headers)
print(response.status_code)

payload = {"name": "learning-about-apis"}

# We need to pass in our authentication headers!
response = requests.post("https://api.github.com/user/repos", json=payload, headers=headers)
status = response.status_code
print(status)
""" Console output or Results
Output
201
201

"""





"""
8: PUT/PATCH Requests

Sometimes we want to update an existing object, rather than create a new one. This is where PATCH and PUT requests come into play.

We use PATCH requests when we want to change a few attributes of an object, but don't want to resend the entire object to the server.
Maybe we just want to change the name of our repository, for example.

We use PUT requests to send the complete object we're revising as a replacement for the server's existing version.

In practice, API developers don't always respect this convention.
Sometimes API endpoints that accept PUT requests will treat them like PATCH requests, and not require us to send the whole object back.

We send a payload of data with PATCH requests, the same way we do with POST requests:

payload = {"description": "The best repository ever!", "name": "test"}
response = requests.patch("https://api.github.com/repos/VikParuchuri/test", json=payload)

The code above will change the description of the test repository to The best repository ever! (we didn't specify a description when we created it).

A successful PATCH request will usually return a 200 status code.

Instructions

Make a PATCH request to the https://api.github.com/repos/VikParuchuri/learning-about-apis endpoint that changes the description to Learning about requests!.
Assign the status code of the response to status.

"""
payload = {'description': 'The best repository ever!', 'name': 'test'}
response = requests.patch('https://api.github.com/repos/VikParuchuri/test', json=payload, headers=headers)
print(response.status_code)

payload = {'description': 'Learning about requests!', 'name': 'learning-about-apis'}
response = requests.patch('https://api.github.com/repos/VikParuchuri/learning-about-apis', json=payload, headers=headers)
status = response.status_code
print(status)

""" Console output or Results
Output
200
200
"""



"""
9: delete Requests
The final major request type is the delete request. The delete request removes objects from the server. We can use the delete request to remove repositories.

response = requests.delete("https://api.github.com/repos/VikParuchuri/test")

The above code will delete the test repository from GitHub.

A successful delete request will usually return a 204 status code indicating that it successfully deleted the object.

Use delete requests carefully - it's very easy to remove something important by accident.
Instructions

Make a delete request to the https://api.github.com/repos/VikParuchuri/learning-about-apis endpoint.
Assign the status_code of the response to the variable status.
"""

response = requests.delete("https://api.github.com/repos/VikParuchuri/test", headers=headers)
print(response.status_code)

response = requests.delete("https://api.github.com/repos/VikParuchuri/learning-about-apis", headers=headers)
status=response.status_code
print(status)

""" Console output or Results
Output
204
204

"""




"""
10: Further Exploration

That's it for the major points of working with APIs, but feel free to continue exploring with your own API token. Then, consult the API documentation to find good endpoints to query.
"""
