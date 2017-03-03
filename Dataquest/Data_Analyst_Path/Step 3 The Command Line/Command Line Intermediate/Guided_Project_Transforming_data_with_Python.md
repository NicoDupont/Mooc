02/2017  
Dataquest : Data Analyst Path  
Step 3: The Command Line  
SubStep : Command Line: Intermediate : Guided Project: Transforming data with Python  
dimanche, 26. février 2017 02:54 


---
#1: How Guided Projects Work
Welcome to the first Dataquest guided project! Guided projects are a way to help you synthesize concepts learned during the Dataquest missions, and start building a portfolio. Guided projects go above and beyond regular projects by providing an in-browser coding experience, along with help and hints. Guided projects bridge the gap between learning using the Dataquest missions, and applying the knowledge on your own computer.  

Guided projects help you develop key skills that you'll need to perform data science work in the "real world". Doing well on these projects is slightly different from doing well in the missions, where there is a "right" answer. In the guided projects, you'll need to think up and create solutions on your own (although we'll be there to help along the way).  

The guided project interface is structured much like an IDE on your local machine would be. This area contains text and instructions. You can advance between steps in the project whenever you want -- since there's no "right" answer for any screen, the text is mainly for you to use as a reference and guide as you build the project. To the right is a file browser interface, where you can view, create, and edit files. Under the file browser is a terminal window, where you can run shell commands.  

Note: Only files stored in the project folder, in this case /home/dq/scripts, will be saved! If you make changes to files elsewhere, they won't be saved.  

As you go through this project, Google, StackOverflow, and the documentation for various packages will help you along the way. All data scientists make extensive use of these and other resources as they write code, and so should you.  

We'd love to hear your feedback as you go through this project, and we hope it's a great experience!  



##Instructions  
- For now, just hit "Next" to get started with the project!





---
#2: The Dataset
In this project, you'll be working with a dataset of submissions to Hacker News from 2006 to 2015. Hacker News is a site where users can submit articles from across the internet (usually about technology and startups), and others can "upvote" the articles, signifying that they like them. The more upvotes a submission gets, the more popular it was in the community. Popular articles get to the "front page" of Hacker News, where they're more likely to be seen by others.  

The dataset you'll be using was compiled by Arnaud Drizard using the Hacker News API, and can be found here. We've sampled 10000 rows from the data randomly, and removed all extraneous columns. Our dataset only has four columns:  

 - submission_time -- when the story was submitted.
 - upvotes -- number of upvotes the submission got.
 - url -- the base domain of the submission.
 - headline -- the headline of the submission. Users can edit this, and it doesn't have to match the headline of the original article.

You'll be writing scripts to answer some main questions:  

 - What words appear most often in the headlines?
 - What domains were submitted most often to Hacker News?
 - At what times are the most articles submitted?

You'll be answering these questions by writing command line scripts, instead of using IPython notebook. IPython notebooks are great for quick data visualization and exploration, but Python scripts are the way to put anything we learn into production. Let's say you want to make a website to help people write headlines that get as many upvotes as possible, and submit articles at the right time. To do this, you'll need scripts.  


---
#3: Reading The Data
There should be a file called read.py already open. You can run this from the command line by being in the same folder, and typing python read.py. Of course, there's nothing in the file right now. You might recall from the last mission that you can put this into a file to run it from the command line:  

```python
if __name__ == "__main__":
        print("Welcome to a Python script")
```        
        
This will print Welcome to a Python script on the command line if you put it into a file and run it.

We can also add functions into a file by writing them like normal:

```python
def load_data():
        pass
​
    if __name__ == "__main__":
        # This will call load_data if you run the script from the command line.
        load_data()
```
Function definitions should come before the if __name__ == "__main__" line. These functions can be imported from other files.  

We'll be adding some code to the read.py file that will help us load in the dataset and do some initial processing. We'll then be able to import the code to read in the dataset from other scripts we develop.  



##Instructions  
- In the read.py file, read the hn_stories.csv file into a Pandas Dataframe.
- There is no header row in the data, so the columns don't have names. See this stackoverflow thread for how to add column names. Add the column names from the last screen (submission_time, upvotes, url, and headline) to the Dataframe.
- Create a function called load_data that takes no inputs, but contains the code to read in and process the dataset. load_data should return a Pandas Dataframe with the column names set correctly.

As you work on these steps, you should be running your script on the command line every so often and verifying that things are working. You can run read.py from the command line by calling python read.py. The first verification is to make sure that you don't see any errors. The second one is to call print at key points in your code, and make sure that the output looks like what you expect. You might want to do this after each step above. This is a good general rule of thumb to follow when writing new code.  

####Results: 

```python 
import numpy as np
import pandas as pd
def load_data():
    data = pd.read_csv("hn_stories.csv")
    print(data.head())
    print("--------------")
    print("--------------")
    data.columns = ["submission_time","upvotes", "url", "headline"]
    print(data.head())
    print("--------------")
    print("--------------")

if __name__ == "__main__":
        # This will call load_data if you run the script from the command line.
        load_data()
```

```bash
home/dq/scripts$ python read.py                                                
  2014-06-24T05:50:40.000Z   1            flux7.com  \                          
0     2010-02-17T16:57:59Z   1  blog.jonasbandi.net                             
1     2014-02-04T02:36:30Z   1        blogs.wsj.com                             
2     2011-10-26T07:11:29Z   1       threatpost.com                             
3     2011-04-03T15:43:44Z  67     algorithm.com.au                             
4     2013-01-13T16:49:20Z   1      winmacsofts.com                             
                                                                                
              8 Ways to Use Docker in the Real World                            
0  Software: Sadly we did adopt from the construc...
1   Google’s Stock Split Means More Control for L...                            
2  SSL DOS attack tool released exploiting negoti...                            
3       Immutability and Blocks Lambdas and Closures                            
4         Comment optimiser la vitesse de Wordpress?                            
--------------                                                                  
--------------                                                                  
        submission_time  upvotes                  url  \                        
0  2010-02-17T16:57:59Z        1  blog.jonasbandi.net                           
1  2014-02-04T02:36:30Z        1        blogs.wsj.com                           
2  2011-10-26T07:11:29Z        1       threatpost.com                           
3  2011-04-03T15:43:44Z       67     algorithm.com.au
4     2013-01-13T16:49:20Z   1      winmacsofts.com                             
                                                                                
              8 Ways to Use Docker in the Real World                            
0  Software: Sadly we did adopt from the construc...                            
1   Google’s Stock Split Means More Control for L...                            
2  SSL DOS attack tool released exploiting negoti...                            
3       Immutability and Blocks Lambdas and Closures                            
4         Comment optimiser la vitesse de Wordpress?                            
--------------                                                                  
--------------                                                                  
        submission_time  upvotes                  url  \
0  2010-02-17T16:57:59Z        1  blog.jonasbandi.net                           
1  2014-02-04T02:36:30Z        1        blogs.wsj.com                           
2  2011-10-26T07:11:29Z        1       threatpost.com                           
3  2011-04-03T15:43:44Z       67     algorithm.com.au                           
4  2013-01-13T16:49:20Z        1      winmacsofts.com                           
                                                                                
                                            headline                            
0  Software: Sadly we did adopt from the construc...                            
1   Google’s Stock Split Means More Control for L...                            
2  SSL DOS attack tool released exploiting negoti...                            
3       Immutability and Blocks Lambdas and Closures
4         Comment optimiser la vitesse de Wordpress?                            
--------------                                                                  
--------------
```





---
#4: Which Words Appear In The Headlines Often?
We now want to figure out which words appear most often in the headlines. We'll be developing another script, called count.py to accomplish this. We'll need to import our load_data function from read.py into count.py so we can use it.  

You'll recall that if you have a folder with two files, read.py and count.py, you can use the function load_data in read.py from count.py by writing the following code in count.py:  

```python
import read
df = read.load_data()
```

##Instructions  
Writing the script for this will require a series of steps:  

 - Make a file called count.py, using the file browser, or the command line.
 - Import load_data from read.py, and call the function to read in the dataset.
 - The order in which you do the below two steps is up to you, but it's suggested to first combine all the headlines (you can use a for loop for this, among other methods), and then split everything into words.
 	 - Combine all of the headlines together into one long string. You'll want to leave a space between each headline when you combine them. Here's a good reference on joining strings.
	 - Figure out how to split the long string into words. Each headline is a string, such as Anticlimax As Motivation Killer. Combining that with Swype acquired by Nuance for 100 million would look like Anticlimax As Motivation Killer Swype acquired by Nuance for 100 million. Adding more headlines would make a longer string. You'll need to figure out a way to split the long string, so you end up with a list of words. The documentation for str might help here.
 - You might want to think about lowercasing each word, so Hello and hello aren't treated as different words when you do a count.
 - Find a way to count up how many times each word occurs in the list. The Counter class might help you.
 - Add code to print the 100 words that occur the most in your data.


```bash  
touch count.py
```
read.py :  

```python
import numpy as np
import pandas as pd
def load_data():
    data = pd.read_csv("hn_stories.csv")
    print(data.head())
    print("--------------")
    data.columns = ["submission_time","upvotes", "url", "headline"]
    print(data.head())
    return data

if __name__ == "__main__":
        # This will call load_data if you run the script from the command line.
        load_data()
```

count.py :  

```python
import read
import collections

df = read.load_data()

combine_headline = ""
for row in df.iterrows():
    combine_headline += str(df["headline"]).lower()

word_list = combine_headline.split(" ")
print(word_list[0:5])

cnt = collections.Counter()
for wd in word_list:
    cnt[wd] += 1
    
word100 = cnt.most_common(100)
print(word100)
```


####Results: 

```bash  
['0', '', '', '', '']                                                           
[('', 10078992), ('for', 79992), ('is', 59994), ('what', 49995), ('in', 49995), 
('to', 39996), ('how', 39996), ('a', 39996), ('ask', 39996), ('hn:', 39996), ('y
ou', 39996), ('the', 29997), ('-', 29997), ('of', 29997), ('and', 29997), ('or',
 19998), ('de', 19998), ('split', 19998), ('amazon', 19998), ('silicon', 19998),
 ('valley', 19998), ('at', 19998), ('google', 19998), ('via', 19998), ('android'
, 19998), ('good', 19998), ('new', 19998), ('editor', 19998), ('desktop', 19998)
...
```




---
#5: Which Domains Were Submitted Most Often?
You can now move on to our second question, and explore which domains were submitted most often. We'll want to make a separate script, called domains.py, for this.  

##Instructions  
Here are the steps:  

 - Make a file called domains.py, using the file browser, or the command line.
 - Add in the code to read the file hn_stories.csv, and add column names.
 - You can think of each domain name as a "word". A domain will look like scala-lang.org, or blog.iweb.com.
	- You can use the value_counts method in pandas to count the number of occurrences of each value in a column. Here are the docs.
 - Print the 100 most submitted domains.

By default, Pandas only prints 10 rows of a Dataframe or Series. There is a pandas option to make it print more rows (see this thread on Stackoverflow), but there are bugs with it and Series. Instead, just loop through the series and print the index value, and the total. Here's some sample code:


```python  
for name, row in domains.items():
    print("{0}: {1}".format(name, row))
```

####Results: 

domains.py :  

```python  
import read
import collections

df = read.load_data()

print(df.head())

print(df["url"].value_counts(sort=True, ascending=False)[0:100])
```



---
#6: When Are The Most Articles Submitted?
We want to know when the most articles are submitted. One easy way to reframe this is to look at what hour articles are submitted. To figure this out, we'll need to use the submission_time column.  

The submission_time column contains timestamps, which look like this: 2011-11-09T21:56:22Z. These times are expressed in UTC, which is a universal time zone used by most software for consistency (imagine a database populated with times all having different timezones; it would be a huge pain to work with).  

To get hour from a timestamp, we can use the dateutil library. The parser module in dateutil contains the parse function, which can take in a timestamp, and return a datetime object. Here's a link to the documentation. After parsing the timestamp, the hour property of the resulting date object will tell you the hour the article was submitted.  



##Instructions  

 - Make a file called times.py to find the submission times.
 - Write a function to extract the hour from a timestamp. This function should first use dateutil.parser.parse to parse the timestamp, then extract the hour from the resulting datetime object, then return the hour.
 - Use the pandas apply method to make a column of submission hours.
 - Use the value_counts method to find the number of occurences of each hour.
 - Print out the results.

You can repeat this procedure to find how many articles were submitted on each day of the month, year, minute, day of the week, and so on.

times.py

```python  
import read
import collections
from dateutil.parser import parse

df = read.load_data()

def extract_hour(str):
    date = parse(str)
    return date.hour
    

df["Hour"] = df["submission_time"].apply(extract_hour)
print(df["Hour"].value_counts())

def extract_month(str):
    date = parse(str)
    return date.month

print("-------------")
print("-------------")
df["Month"] = df["submission_time"].apply(extract_month)
print(df["Month"].value_counts())
```

####Results: 

```bash  
-------------                                                                   
3     980                                                                       
4     924                                                                       
1     916                                                                       
2     867                                                                       
5     836                                                                       
10    829                                                                       
8     814                                                                       
6     796                                                                       
11    788                                                                       
12    767                                                                       
9     758
7     724                                                                       
Name: Month, dtype: int64
```




---
#7: Next Steps
That's all for the guided steps, but feel free to keep going through the data and answering questions. We encourage you to think of your own questions, and to be creative in exploring the dataset!  

If you can't think of any questions, some interesting ones are:  

What headline length leads to the most upvotes?  
What submission time leads to the most upvotes?  
How are the total numbers of upvotes changing over time?  
You can write scripts and explore here, or download the code to your computer using the download icon to the right. You'll then be able to run the scripts on your own computer.  

Hope this guided project has been a good experience, and please email us at hello@dataquest.io if you want to share your work -- we'd love to see it!  