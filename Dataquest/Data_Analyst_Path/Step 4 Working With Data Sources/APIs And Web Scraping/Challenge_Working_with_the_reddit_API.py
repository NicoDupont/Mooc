"""
03/2017
Dataquest : Data Analyst Path
Step 4: Working With Data Sources
SubStep : APIs And Web Scraping : Challenge: Working with the reddit API
"""


"""
1: Reddit

Over the past few missions, we learned how to make API requests, authenticate with an API server, and parse responses.
In this challenge, you'll pull these concepts together to explore trending posts and comments on reddit.

Reddit is a community-driven link-sharing site. Users submit links to articles, photos, and other content.
Other users upvote the submissions they like, and downvote the ones they dislike. Users can comment on submissions, and even upvote or downvote other people's comments.

Reddit consists of many smaller communities called subreddits where more focused communities can discuss niche posts.
For example, /r/python is a Python-focused community, and /r/sanfrancisco is for discussing issues relating to the city of San Francisco, CA.
The posts you submit to a subreddit will appear on the group's front page if enough users upvote them. Very popular subreddit posts may appear on reddit's home page.

Posts only stay on the main reddit and subreddit pages for a limited time.
You can search for older posts, but it can be hard to find what you're looking for.

In this challenge, you'll practice:

    Retrieving a list of trending posts on a particular subreddit
    Exploring the comments on a single article
    Posting our own comment on an article

"""





"""
2: Authenticating with the API

The reddit API requires authentication. You authenticated with a token in a previous mission, but in this challenge, you'll use OAuth.
OAuth can be fairly complex, but we've done some of the hard work already. You'll be using an authentication token, 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk, to authenticate in much the same way we did earlier, except that the header will look like this:

{"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk"}

Note that we'll need to use the string bearer instead of the string token we used in the previous mission.
That's because we're using OAuth this time. We'll cover OAuth in more depth in a later mission.

We'll also need to add a User-Agent header, which will identify us as Dataquest to the API:

{"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}

We've imported requests for you already, so please avoid doing it again in this mission.
Importing requests will overwrite some of the custom API logic we've developed for answer checking.

Instructions

    Retrieve the /r/python subreddit's top posts for the past day.
        Make a GET request to https://oauth.reddit.com/r/python/top using the get method of the requests library. See the documentation for the /r/python/top endpoint if you need help.
        Pass in the header information we showed you earlier in this section.
        To retrieve only the top posts for the past day, pass in a query parameter t (for "time") and set its value to the string day.
    Use the json method on the response to get the JSON response data.
    Assign the JSON response data to the variable python_top.

"""
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t": "day"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params=params)
python_top = response.json()





"""
3: Getting the Most Upvoted Post

The variable python_top is a dictionary containing information about all of the individual posts that users submitted during the past day.
However, the actual list of posts is buried inside a dictionary key, and you'll need to explore the dictionary to retrieve it.
You can read more about python_top's format here.

There's a dictionary for each individual post that looks like this:

{'data': {'approved_by': None,

     'archived': False,

     'author': 'ingvij',

     ...

     'ups': 43,

     'url': 'http://hkupty.github.io/2016/Functional-Programming-Concepts-Idioms-and-Philosophy/',

     'user_reports': [],

     'visited': False},

     'kind': 't3'}

We've truncated the representation, but you can see the ups field, which contains the number of people who upvoted the post.
The id field holds reddit's unique ID for the post.

Instructions

    Explore the python_top dictionary.
    Extract the list containing all of the posts, and assign it to python_top_articles.
    Find the post with the most upvotes.
    Assign the ID for the post with the most upvotes to most_upvoted.

"""
python_top_articles = python_top["data"]["children"]
print(type(python_top_articles))
print("------------------")
print("------------------")
print(python_top_articles[0:2])
print("------------------")
print("------------------")
most_upvoted = ""
upvotes = 0
for article in python_top_articles:
    if article["data"]["ups"] >= upvotes:
        most_upvoted = article["data"]["id"]
        upvotes = article["data"]["ups"]
""" Console Outputs or Results
Output
<class 'list'>
------------------
------------------
[{'kind': 't3', 'data': {'stickied': False, 'domain': 'hkupty.github.io', 'name': 't3_4b7w9u', 'title': 'Functional Philosophy and applying it to Python', 'removal_reason': None, 'from_kind': None, 'quarantine': False, 'distinguished': None, 'mod_reports': [], 'user_reports': [], 'suggested_sort': None, 'approved_by': None, 'url': 'http://hkupty.github.io/2016/Functional-Programming-Concepts-Idioms-and-Philosophy/', 'permalink': '/r/Python/comments/4b7w9u/functional_philosophy_and_applying_it_to_python/', 'secure_media_embed': {}, 'banned_by': None, 'locked': False, 'thumbnail': '', 'hide_score': False, 'over_18': False, 'subreddit': 'Python', 'visited': False, 'edited': False, 'clicked': False, 'selftext_html': None, 'author': 'ingvij', 'created': 1458515741.0, 'likes': None, 'author_flair_css_class': None, 'created_utc': 1458486941.0, 'secure_media': None, 'num_comments': 13, 'media_embed': {}, 'link_flair_text': None, 'downs': 0, 'author_flair_text': None, 'from_id': None, 'num_reports': None, 'subreddit_id': 't5_2qh0y', 'saved': False, 'selftext': '', 'id': '4b7w9u', 'archived': False, 'media': None, 'is_self': False, 'gilded': 0, 'score': 53, 'from': None, 'link_flair_css_class': None, 'hidden': False, 'report_reasons': None, 'ups': 53}}, {'kind': 't3', 'data': {'stickied': False, 'domain': 'self.Python', 'name': 't3_4b7gnk', 'title': 'SQL Injection demonstration on a local sqlite database', 'removal_reason': None, 'from_kind': None, 'quarantine': False, 'distinguished': None, 'mod_reports': [], 'user_reports': [], 'suggested_sort': None, 'approved_by': None, 'url': 'https://www.reddit.com/r/Python/comments/4b7gnk/sql_injection_demonstration_on_a_local_sqlite/', 'permalink': '/r/Python/comments/4b7gnk/sql_injection_demonstration_on_a_local_sqlite/', 'secure_media_embed': {}, 'banned_by': None, 'locked': False, 'thumbnail': '', 'hide_score': False, 'over_18': False, 'subreddit': 'Python', 'visited': False, 'edited': False, 'clicked': False, 'selftext_html': '&lt;!-- SC_OFF --&gt;&lt;div class="md"&gt;&lt;p&gt;Hey guys, &lt;/p&gt;\n\n&lt;p&gt;So I made a really simple demonstration of exploiting a local &lt;code&gt;SQLite&lt;/code&gt; database using &lt;code&gt;tkinter&lt;/code&gt; in &lt;code&gt;python&lt;/code&gt;&lt;/p&gt;\n\n&lt;p&gt;Thought I would share it with you guys&lt;/p&gt;\n\n&lt;hr/&gt;\n\n&lt;ul&gt;\n&lt;li&gt;Github link: &lt;a href="https://github.com/prodicus/thanos"&gt;https://github.com/prodicus/thanos&lt;/a&gt;&lt;/li&gt;\n&lt;li&gt;screenshots: \n\n&lt;ul&gt;\n&lt;li&gt;SQL injection: &lt;a href="http://i.imgur.com/qlzSCuP.jpg"&gt;http://i.imgur.com/qlzSCuP.jpg&lt;/a&gt;&lt;/li&gt;\n&lt;li&gt;mitigated threat: &lt;a href="http://i.imgur.com/42YhmpU.jpg"&gt;http://i.imgur.com/42YhmpU.jpg&lt;/a&gt;&lt;/li&gt;\n&lt;/ul&gt;&lt;/li&gt;\n&lt;/ul&gt;\n&lt;/div&gt;&lt;!-- SC_ON --&gt;', 'author': 'madboy1995', 'created': 1458508731.0, 'likes': None, 'author_flair_css_class': None, 'created_utc': 1458479931.0, 'secure_media': None, 'num_comments': 14, 'media_embed': {}, 'link_flair_text': None, 'downs': 0, 'author_flair_text': None, 'from_id': None, 'num_reports': None, 'subreddit_id': 't5_2qh0y', 'saved': False, 'selftext': 'Hey guys, \n\nSo I made a really simple demonstration of exploiting a local `SQLite` database using `tkinter` in `python`\n\nThought I would share it with you guys\n\n***\n\n- Github link: [https://github.com/prodicus/thanos](https://github.com/prodicus/thanos)\n- screenshots: \n  - SQL injection: http://i.imgur.com/qlzSCuP.jpg\n  - mitigated threat: http://i.imgur.com/42YhmpU.jpg', 'id': '4b7gnk', 'archived': False, 'media': None, 'is_self': True, 'gilded': 0, 'score': 18, 'from': None, 'link_flair_css_class': None, 'hidden': False, 'report_reasons': None, 'ups': 18}}]
------------------
------------------

"""




"""
4: Getting Post Comments

Now that you have the ID for the most upvoted post, you can retrieve the comments on it using the /r/{subreddit}/comments/{article} endpoint.
You'll need to replace the items that have brackets around them with the appropriate values: {subreddit} - The name of the subreddit the post appears in (omit the leading /r, because it already exists).
Use python for the python subreddit, for example. {article} - The ID for the post whose comments we want to retrieve.
It should look like this: 4b7w9u.

You'll need to include the API's base URL, https://oauth.reddit.com/, before this endpoint to generate the full URL for the request.

Instructions

    Get all of the comments on the /r/python subreddit's top post from the past day.
    Generate the full URL to query, using the subreddit name and post ID.
    Make a GET request to the URL.
    Get the response data using the response's json method.
    Assign the response data to the variable comments.

"""
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
response = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u", headers=headers)
comments = response.json()
""" Console Outputs or Results

"""




"""
5: Getting the Most Upvoted Comment

Querying the comments endpoint at /r/{subreddit}/comments/{article} returns a list.
The first item in the list contains information about the post, and the second item contains information about the comments.

Reddit users can nest comments. That is, they can comment on comments. Here's an example.

This means that comments have one more key than posts do. The additional key, replies, contains the nested comments.
ou can read more about that structure in reddit's API documentation. Here's an example of a single comment that has nested comments:

{'data': {'approved_by': None,

      'archived': False,

      'author': 'larsga',

      ...

      'replies': {'data': {'after': None,

        'before': None,

        'children': [{'data': {'approved_by': None,

           'archived': False,

           'author': 'Deto',

           ...

           },

          ...

          ]

          }

          ...

          'url': 'https://www.reddit.com/r/Python/comments/4b6bew/using_pilpillow_with_mozjpeg/',

         'user_reports': [],

         'visited': False

         }

It's easier to focus on top-level comments only, and ignore the nested replies.
Instructions

    Find the most upvoted top-level comment in comments.
    Extract the comments list from the comments variable, and assign it to comments_list.
    Assign the ID for the comment with the most upvotes to most_upvoted_comment.

"""
print(len(comments))
print(type(comments))
print("------------------")
print("------------------")
print(comments[0])
print("------------------")
print("------------------")
print(comments[1])
comments_list = comments[1]["data"]["children"]
print(type(comments_list))
print("------------------")
print("------------------")
print(comments_list[0:1])
print("------------------")
print("------------------")
most_upvoted_comment = ""
upvotes = 0
for com in comments_list:
    if com["data"]["ups"] >= upvotes:
        most_upvoted_comment = com["data"]["id"]
        upvotes = com["data"]["ups"]
print(most_upvoted_comment)
""" Console Outputs or Results
Output
<class 'list'>
------------------
------------------
[{'data': {'removal_reason': None, 'banned_by': None, 'score': 8, 'num_reports': None, 'created_utc': 1458496526.0, 'downs': 0, 'score_hidden': False, 'user_reports': [], 'name': 't1_d16wtxk', 'body': "Increasingly I've been writing my Python libraries in a functional way but with an object-oriented API where methods just call the appropriate function.\n\nI was motivated to do this because I found classes with lots of lines of code difficult to work with.\n\nAlso it made tests easier to write.\n\nNamed tuples are also very useful (they're like immutable dicts/objects).", 'replies': '', 'mod_reports': [], 'edited': False, 'stickied': False, 'author_flair_css_class': None, 'parent_id': 't3_4b7w9u', 'subreddit': 'Python', 'author': 'mcilrain', 'gilded': 0, 'controversiality': 0, 'saved': False, 'archived': False, 'ups': 8, 'created': 1458525326.0, 'link_id': 't3_4b7w9u', 'approved_by': None, 'author_flair_text': None, 'likes': None, 'report_reasons': None, 'distinguished': None, 'id': 'd16wtxk', 'body_html': '&lt;div class="md"&gt;&lt;p&gt;Increasingly I&amp;#39;ve been writing my Python libraries in a functional way but with an object-oriented API where methods just call the appropriate function.&lt;/p&gt;\n\n&lt;p&gt;I was motivated to do this because I found classes with lots of lines of code difficult to work with.&lt;/p&gt;\n\n&lt;p&gt;Also it made tests easier to write.&lt;/p&gt;\n\n&lt;p&gt;Named tuples are also very useful (they&amp;#39;re like immutable dicts/objects).&lt;/p&gt;\n&lt;/div&gt;', 'subreddit_id': 't5_2qh0y'}, 'kind': 't1'}]
------------------
------------------
d16y4r
"""




"""
6: Upvoting a Comment

You can upvote a comment with the /api/vote endpoint. You'll need to pass in the following parameters:

    dir - Vote direction: 1, 0, or -1. 1 is an upvote, and -1 is a downvote.
    id - The ID for the post or comment to upvote.

Instructions

    Make a POST request to the /api/vote endpoint to upvote the most upvoted comment from the last screen.
    Assign the status code for the response to the variable status.

"""
payload = {"dir":1,"id":"d16y4ry"}

response = requests.post("https://oauth.reddit.com/api/vote", json=payload, headers=headers)
status = response.status_code
print(status)
""" Console Outputs or Results
Output
201

"""




"""
7: Next Steps

In this challenge, you authenticated with an API, then retrieved and parsed responses. In the next mission, we'll dive into Web scraping.
"""
