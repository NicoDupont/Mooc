"""
03/2017
Dataquest : Data Analyst Path
Step 4: Working With Data Sources
SubStep : APIs And Web Scraping : Web Scraping
"""


"""
1: Introduction

A lot of data aren't accessible through data sets or APIs. They may exist on the Internet as Web pages, though.
One way to access the data without waiting for the provider to create an API is to use a technique called Web scraping.

Web scraping allows us to load a Web page into Python and extract the information we want.
We can then work with the data using standard analysis tools like pandas and numpy.

Before we can do Web scraping, we need to understand the structure of the Web page we're working with, then find a way to extract parts of that structure in a sensible way.

We'll use the requests library heavily as we learn about Web scraping. This library enables us to download a Web page.
We'll also use the beautifulsoup library to extract the relevant parts of the Web page.
"""


"""
2: Web Page Structure

Web pages use HyperText Markup Language (HTML). HTML isn't a programming language like Python.
It's a markup language with its own syntax and rules. When a Web browser like Chrome or Firefox downloads a Web page, it reads the HTML to determine how to render it and display it to you.

Here's the HTML for a very simple Web page:

see img/6ne0anS.png

You can see what this page looks like on our GitHub site.

HTML consists of tags. We open a tag like this:

Imgur

We close a tag like this:

Imgur

Anything in between the opening and closing of a tag is the content of that tag.
We can nest tags to create complex formatting rules. Here's an example:

Imgur

The b tag bolds the content inside it, and the p tag creates a new paragraph.
The HTML above will display as a bold paragraph because the b tag is inside the p tag. In other words, the b tag is nested within the p tag.

HTML documents contain a few major sections.
The head section contains information that's useful to the Web browser that's rendering the page; the user doesn't see it.
The body section contains the bulk of the content the user interacts with on the page.

Different tags have different purposes.
For example, the title tag tells the Web browser what page title to display at the top of your tab. T
he p tag indicates that the content inside it is a single paragraph.

We won't cover tags comprehensively here, but please read the Mozilla Developer Network's (MDN) article on HTML basics if you need more of a grounding on this topic.
Check out MDN's guide to the HTML element for a list of all possible HTML tags.
In order to do Web scraping effectively, you'll need a solid understanding of the various tags and how they work.

In this exercise, you'll make a GET request to http://dataquestio.github.io/web-scraping-pages/simple.html.
Instructions

    Make a GET request to http://dataquestio.github.io/web-scraping-pages/simple.html, and assign the result to the variable response.
    Use response.content to get the content of the response, and assign it to content.
    Note how the content is the same as the HTML above.


"""
# Write your code here.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
content = response.content
print(content)
""" Console Outputs or Results
Output
b'<!DOCTYPE html>\n<html>\n    <head>\n        <title>A simple example page</title>\n    </head>\n    <body>\n        <p>Here is some simple content for this page.</p>\n    </body>\n</html>'

"""




"""
3: Retrieving Elements from a Page

Downloading the page is the easy part. Let's say that we want to get the text in the first paragraph.
Now we need to parse the page and extract the information we want.

We'll use the BeautifulSoup library to parse the Web page with Python. This library allows us to extract tags from an HTML document.

We can think of HTML documents as "trees," and the nested tags as "branches" (similar to a family tree). BeautifulSoup works the same way.

If we look at this page, for example, the root of the "tree" is the html tag:

Imgur

The html tag contains two "branches," head and body. head contains one "branch," title. body contains one branch, p. Drilling down through these multiple branches is one way to parse a Web page.

To extract the text inside the p tag, we would first need to get the body element, then the p element, and then finally the text inside the p element.
Instructions

    Get the text inside the title tag, and assign the result to title_text.

"""
from bs4 import BeautifulSoup

# Initialize the parser, and pass in the content we grabbed earlier.
parser = BeautifulSoup(content, 'html.parser')

# Get the body tag from the document.
# Since we passed in the top level of the document to the parser, we need to pick a branch off of the root.
# With BeautifulSoup, we can access branches by using tag types as attributes.
body = parser.body

# Get the p tag from the body.
p = body.p

# Print the text inside the p tag.
# Text is a property that gets the inside text of a tag.
print(p.text)

title_text = parser.head.title.text
print(title_text)
""" Console Outputs or Results
Here is some simple content for this page.
A simple example page
"""




"""
4: Using Find All

While it's nice to use the tag type as a property, it's not always a very robust way to parse a document.
It's usually better to be more explicit by using the find_all method.
This method will find all occurrences of a tag in the current element, and return a list.

If we only want the first occurrence of an item, we'll need to index the list to get it.
Aside from this difference, it behaves the same way as passing in the tag type as an attribute.
Instructions

    Apply the find_all method to get the text inside the title tag, and assign the result to title_text.

"""
parser = BeautifulSoup(content, 'html.parser')

# Get a list of all occurrences of the body tag in the element.
body = parser.find_all("body")

# Get the paragraph tag.
p = body[0].find_all("p")

# Get the text.
print(p[0].text)

title_text = parser.find_all("head")[0].find_all("title")[0].text
print(title_text)
""" Console Outputs or Results
Output
Here is some simple content for this page.
A simple example page

"""




"""
5: Element IDs

HTML allows elements to have IDs. Because they are unique, we can use an ID to refer to a specific element.

Here's an example page:

see img/WBG4aCQ.png

You can see the page here.

HTML uses the div tag to create a divider that splits the page into logical units.
We can think of a divider as a "box" that contains content. For example, different dividers hold a Web page's footer, sidebar, and horizontal menu.

There are two paragraphs on the page; the first is nested inside a div. Luckily, the paragraphs have IDs. This means we can access them easily, even through they're nested.

Let's use the find_all method to access those paragraphs, and pass in the additional id attribute.
Instructions

    Get the text of the second paragraph (what's inside the second p tag), and assign the result to second_paragraph_text.

"""
# Get the page content and set up a new parser.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_ids.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Pass in the ID attribute to only get the element with that specific ID.
first_paragraph = parser.find_all("p", id="first")[0]
print(first_paragraph.text)

second_paragraph_text = parser.find_all("p", id="second")[0].text
print(second_paragraph_text)
""" Console Outputs or Results
Output

                First paragraph.



                Second paragraph.



"""




"""
6: Element Classes

In HTML, elements can also have classes. Classes aren't globally unique.
In other words, many different elements belong to the same class, usually because they share a common purpose or characteristic.

For example, you may want to create three dividers to display three of your photographs.
You can create a common look and feel for these dividers, such as a border and caption style.

This is where classes come into play. You could create a class called "gallery," define a style for it once using CSS (which we'll talk about soon), and then apply that class to all of the dividers you'll use to display photos.
One element can even have multiple classes.

see img/T2TguLL.png

Take a look at this page to see how we've used classes to style paragraphs.

We can use find_all to select elements by class. We'll just need to pass in the class_ parameter.
Instructions

    Get the text in the second inner paragraph, and assign the result to second_inner_paragraph_text.
    Get the text of the first outer paragraph, and assign the result to first_outer_paragraph_text.

"""
# Get the website that contains classes.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Get the first inner paragraph.
# Find all the paragraph tags with the class inner-text.
# Then, take the first element in that list.
first_inner_paragraph = parser.find_all("p", class_="inner-text")[0]
print(first_inner_paragraph.text)

second_inner_paragraph = parser.find_all("p", class_="inner-text")[1]
second_inner_paragraph_text = second_inner_paragraph.text
print(second_inner_paragraph_text)

first_outer_paragraph = parser.find_all("p", class_="outer-text")[0]
first_outer_paragraph_text = first_outer_paragraph.text
print(first_outer_paragraph_text)
""" Console Outputs or Results
Output

                First paragraph.


                Second paragraph.



                First outer paragraph.



"""




"""
7: CSS Selectors

Cascading Style Sheets, or CSS, is a language for adding styles to HTML pages. You may have noticed that our simple HTML pages from the past few screens didn't have any styling; all of the paragraphs had black text and the same font size. Most Web pages use CSS to display a lot more than basic black text.

CSS uses selectors to add styles to the elements and classes of elements you specify. You can use selectors to add background colors, text colors, borders, padding, and many other style choices to the elements on HTML pages.

An in-depth lesson on CSS is outside the scope of this mission. If you'd like to learn more about it on your own, MDN's guide is a great place to start.

What we do need to know is how CSS selectors work.

This CSS will make all of the text inside all paragraphs red:

p{

    color: red

 }

You can see what this style looks like on our GitHub site.

This CSS will change the text color to red for any paragraphs that have the class inner-text. We select classes with the period or dot symbol (.):

p.inner-text{

    color: red

 }

You can see what the result looks like here.

This CSS will change the text color to red for any paragraphs that have the ID first. We select IDs with the pound or hash symbol (#):

p#first{

    color: red

 }

Take a look at the results on our GitHub site.

You can also style IDs and classes without using any specific tags. For example, this CSS will make the element with the ID first red (not just paragraphs):

#first{

    color: red

 }

This CSS will make any element with the class inner-text red:

.inner-text{

    color: red

 }

In the examples above, we used CSS selectors to select one or more elements, then apply styles to only those elements. CSS selectors are very powerful and flexible.

Perhaps not surprisingly, we also use CSS selectors to select elements when we do Web scraping.
"""






"""
8: Using CSS Selectors

We can use BeautifulSoup's .select method to work with CSS selectors. Here's the HTML we'll be working with on this screen:

see img/uOaCMeY.png

You may have noticed that the same element can have both an ID and a class. We can also assign multiple classes to a single element; we just separate the classes with a space.

Take a look at the Web page that corresponds to the HTML above.
Instructions

    Select all of the elements that have the class outer-text.
        Assign the text of the first paragraph that has the class outer-text to first_outer_text.

    Select all of the elements that have the ID second.
        Assign the text of the first paragraph that has the ID second to the variable second_text.

"""
# Get the website that contains classes and IDs.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Select all of the elements that have the first-item class.
first_items = parser.select(".first-item")

# Print the text of the first paragraph (the first element with the first-item class).
print(first_items[0].text)

first_outer_text = parser.select(".outer-text")[0].text
print(first_outer_text)

second_text = parser.select("#second")[0].text
print(second_text)

""" Console Outputs or Results
Output

                First paragraph.



                First outer paragraph.




                First outer paragraph.



"""




"""
9: Nesting CSS Selectors

We can nest CSS selectors similar to the way HTML nests tags.
For example, we could use selectors to find all of the paragraphs inside the body tag.
Nesting is a very powerful technique that enables us to use CSS to do complex Web scraping tasks.

This selector will target any paragraph inside a div tag:

div p

This selector will target any item inside a div tag that has the class first-item:

div .first-item

This one is even more specific. It selects any item that's inside a div tag inside a body tag, but only if it also has the ID first:

body div #first

This selector zeroes in on any items with the ID first that are inside any items with the class first-item:

.first-item #first

As you can see, we can nest CSS selectors in infinite ways. This allows us to extract data from websites with complex layouts.
You can test selectors by using the .select method as you write them.
Because it's easy to write a selector that doesn't work the way you expect, we highly recommend doing this.
"""





"""
10: Using Nested CSS Selectors

Now that we know about nested CSS selectors, let's try them out. We can use them with the same .select method we used for our CSS selectors.

We'll be practicing on this HTML:

see img/H34hK8I.png

It's an excerpt from a box score of the 2014 Super Bowl, a National Football League (NFL) game in which the New England Patriots played the Seattle Seahawks.
The box score contains information on how many yards each team gained, how many turnovers each team had, and so on. Check out the Web page this HTML renders.

The page renders as a table with column and row names.
The first column is for the Seattle Seahawks, and the second column is for the New England Patriots. Each row represents a different statistic.

Instructions

    Find the Total Plays for the New England Patriots, and assign the result to patriots_total_plays_count.

    Find the Total Yards for the Seahawks, and assign the result to seahawks_total_yards_count.

"""
# Get the Superbowl box score data.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/2014_super_bowl.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Find the number of turnovers the Seahawks committed.
turnovers = parser.select("#turnovers")[0]
seahawks_turnovers = turnovers.select("td")[1]
seahawks_turnovers_count = seahawks_turnovers.text
print(seahawks_turnovers_count)


totalplays = parser.select("#total-plays")[0]
patriots_total_plays = totalplays.select("td")[2]
patriots_total_plays_count = patriots_total_plays.text
print(patriots_total_plays_count)

totalyards = parser.select("#total-yards")[0]
seahawks_total_yards = totalyards.select("td")[1]
seahawks_total_yards_count = seahawks_total_yards.text
print(seahawks_total_yards_count)
""" Console Outputs or Results
Output
1
72
396

"""



"""
11: Beyond the Basics

We've covered the basics of HTML and how to select elements, which are key foundational blocks.

You may be wondering why Web scraping is useful, given that in most of our examples, we could easily have found the answer by looking at the page.
The real power of Web scraping lies in getting information from a large amount of pages very quickly.

Let's say we wanted to find the total number of yards each NFL team gained in every single NFL game over an entire season.
We could do this manually, but it would take days of boring drudgery.
We could write a script to automate this in a couple of hours instead, and have a lot more fun doing it.
"""
