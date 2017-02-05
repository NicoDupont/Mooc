"""
02/2017
Dataquest : Data Analyst Path
Step 1: Introduction To Python
SubStep : Python Programming Intermediate : Dates in Python
"""


"""
1: The Time Module
There are a few modules in Python's Standard Library that deal with dates and times.
One is the time module, which deals primarily with Unix timestamps.

A Unix timestamp is a floating point value with no explicit mention of day, month, or year.
This value represents the number of seconds that have passed since the "epoch", or the first second of the year 1970.
So, a timestamp of 0.0 would represent the epoch, and a timestamp of 60.0 would represent one minute after the epoch.
We can represent any date after 1970 this way.

To retrieve the current Unix timestamp, we use the time.time() function.

Instructions
Return the current timestamp and assign it to current_time.
Display current_time using the print() function.
"""
import time
current_time = time.time()
print(current_time)
""" Console Output or Results
Output
1478316702.508865
"""



"""
2: Converting Timestamps
We can convert a timestamp to a more human-readable form using the time.gmtime() function.
This function takes a timestamp as an argument, and returns an instance of the struct_time class.
struct_time instances have attributes that represent the current time in other ways.

Here are some of the attributes:

tm_year: The year of the timestamp
tm_mon: The month of the timestamp (1-12)
tm_mday: The day in the month of the timestamp (1-31)
tm_hour: The hour of the timestamp (0-23)
tm_min: The minute of the timestamp (0-59)
For example, we can retrieve the year value as an integer using the tm_year property:


current_time = time.time()
current_struct_time = time.gmtime()
current_year = current_time.tm_year
Instructions
Use the time.time() function assign the current Unix timestamp to a new variable current_time.
Convert current_time to a struct_time object and assign the resulting object to current_struct_time.
Assign the current hour to current_hour and display the value.
"""
import time

current_time = time.time()
current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour
print(current_hour)
""" Console Output or Results
Output
22
"""



"""
3: UTC
Note the value for the hour from the last screen.
The time module always results in a UTC time.
UTC stands for Coordinated Universal Time.
This is the accepted time standard within the programming community.
It corresponds to the mean solar time at 0° longitude, or Greenwich Mean Time, except that it doesn't follow daylight saving time.
While we can convert UTC to other time zones, we'll use UTC in this mission for simplicity.

The datetime module offers better support for working extensively with dates.
For example, it's easier to perform arithmetic on them (such as adding days), and to work with different time zones.

The datetime module has a datetime class that represents points in time.
datetime instances appear similar to struct_time instances, and have the following attributes:

year
month
day
hour
minute
second
microsecond
To get the current datetime, we use the datetime.now() function, which returns a datetime.datetime instance.

Instructions
Import the datetime module.
Assign the datetime object representation of the current time to a new variable current_datetime.
Assign the current year to current_year.
Assign the current month to current_month.
"""
from datetime import datetime
current_datetime =  datetime.datetime.now()
current_year = current_datetime.year
current_month = current_datetime.month
""" Console Output or Results

"""



"""
4: Timedelta
We know how to represent dates, but we'd also like to perform arithmetic on them. Since adding a day, week, month, etc. to a date can be tedious to do from scratch, the datetime module provides the timedelta class.
We can create an instance of this class that represents a span of time, then add or subtract it from instances of the datetime class.

When we create instances of the timedelta class, we can specify the following parameters:

weeks
days
hours
minutes
seconds
milliseconds
microseconds
Suppose we want to calculate the date for three weeks and two days from now.
We would first create an instance of the datetime class that represents today:


today = datetime.datetime.now()
Then, we could get an instance of the timedelta class that represents the span of time we're working with:


diff = datetime.timedelta(weeks = 3, days = 2)
Finally, we would add these two instances:


result = today + diff
If we wanted to, we could also subtract a timedelta instance from a datetime instance.
Let's use the timedelta class to retrieve datetime instances for both tomorrow and yesterday (at the current time).

Instructions
Create an instance of the datetime class that represents the current time and date. Assign this to a new variable today.
Create an instance of the timedelta class that represents one day.
Assign this to a new variable diff.
Assign the datetime instance for tomorrow to a new variable tomorrow, and the datetime instance for yesterday to a new variable yesterday.
"""
import datetime
today = datetime.datetime.now()
diff = datetime.timedelta(days = 1)
tomorrow = today + diff
yesterday =  today - diff
print(today)
print("--------")
print(tomorrow)
print("--------")
print(yesterday)
print("--------")
""" Console Output or Results
Output
2017-02-04 17:37:57.582976
--------
2017-02-05 17:37:57.582976
--------
2017-02-03 17:37:57.582976
--------
"""




"""
5: Formatting Dates
Suppose we'd like to output dates in human-readable formats.
If we use the print() function to display a datetime object, the output will look something like 2016-01-06 13:51:25.849719.
Instead of displaying the full timestamp down to the microsecond, we can use the datetime.strftime() method to specify how we'd like the string output to be formatted.

The datetime.datetime.strftime() method takes a format string as its input.
A format string contains special indicators, usually preceded by percent characters ("%"), that indicate where certain values should go.
For example, suppose we stored a timestamp from March 3, 2010 in the object march3.
If we want to format it nicely into the string "Mar 03, 2010", we can write the following code:


march3 = datetime.datetime(year = 2010, month = 3, day = 3)
pretty_march3 = march3.strftime("%b %d, %Y")
print(pretty_march3)
The format string argument in strftime() indicates that we want:

the abbreviated month name ("%b") followed by a space
the day of the month ("%d") followed by a comma and space
the full year ("%Y").
Thankfully, we don't have to memorize the string arguments and can refer to the documentation for the strftime() method, which provides a useful summary table of the different options.

Instructions
Using the datetime.datetime.strftime() method, display mystery_date, a datetime instance we've created for you, in the following format:
[12-hour time with minutes][AM/PM] on [Day of week] [Month full name] [Day of month], [Full year]
Here's an example in that format:
"11:00AM on Wednesday March 03, 2010"
Store this string in the new variable mystery_date_formatted_string and display using the print() function.
 Need a hint?
"""
import datetime

mystery_date_formatted_string = mystery_date.strftime("%I:%M%p on %A %B %d, %Y")
print(mystery_date_formatted_string)
""" Console Output or Results
Output
mystery_datedatetime (<class 'datetime.datetime'>)
datetime.datetime(2015, 12, 31, 0, 0)
12:00AM on Thursday December 31, 2015
"""




"""
6: Parsing Dates
Just as we can convert a datetime object into a formatted string, we can also do the reverse.
The datetime.datetime.strptime() function allows us to convert a string to a datetime instance:

The date string (e.g. "Mar 03, 2010")
The format string (e.g. "%b %d, %Y")
With just these two arguments, strptime() will return a datetime instance for March 3, 2010.
The one thing to remember is that datetime.datetime.strptime() is a function, not a method that's called on a specific object.


march3 = datetime.datetime.strptime("Mar 03, 2010", "%b %d, %Y")
This is useful if we have a date in a string format, and need to convert it to a datetime instance.
If we inspect the data and determine the format of every date, we can save ourselves a lot of manual string manipulation by using the datetime.datetime.strptime() function instead.
We could even use datetime.strptime() and datetime.strftime() together to convert a date string to a datetime object, and then convert it to a date string of a different format.

Instructions
Use the datetime.datetime.strptime() function to return a datetime instance that represents the timestamp associated with the string mystery_date_formatted_string:
mystery_date_formatted_string has the format: [Time][AM/PM] on [Day of week] [Month full name] [Day of month], [Full year].
March 3, 2010 at 11:00AM would look like "11:00AM on Wednesday March 3, 2010" in this format.
Assign the resulting datetime instance in mystery_date and display it using the print() function.
"""
import datetime

print("----------")
print(mystery_date)
print("----------")
print(mystery_date_formatted_string)

mystery_date = datetime.datetime.strptime(mystery_date_formatted_string,"%I:%M%p on %A %B %d, %Y")

print("----------")
print(mystery_date)
""" Console Output or Results
Output
----------
2015-12-31 00:00:00
----------
12:00AM on Thursday January 02, 2003
----------
2003-01-02 00:00:00
"""



"""
7: AskReddit Data
Reddit is a content and community website where users can submit links, text posts, and other types of content to groups of people with similar interests.
These groups are called subreddits, and each one specializes in a particular topic.
One popular subreddit, AskReddit, is a place where users pose questions to the entire Reddit population.
Other users answer those questions in the comments section.

We'll be working with a data set of the top 1,000 posts on AskReddit from 2015.
Reddit user P_S_Laplace created the data set, which contains the following columns:

Title: The title of the post
Score: The number of upvotes the post received
Time: When the post appeared (timestamp)
Gold: How much Reddit Gold users gave the post
NumComs: The number of comments the post received
"""



"""
8: Reformatting Our Data
In the following code cell, we've read the AskReddit data into the posts variable for you as a list of lists. Each nested list represents an AskReddit post. Here's what the first few rows of the data set looks like:

see img9.png

Here's what the first three lists in posts looks like:


posts = [
            ['What\'s your internet "white whale", something you\'ve been searching for years to find with no luck?', '11510', '1433213314.0', '1', '26195'],
            ["What's your favorite video that is 10 seconds or less?", '8656', '1434205517.0', '4', '8479'],
            ['What are some interesting tests you can take to find out about yourself?', '8480', '1443409636.0', '1', '4055'],
            ...
        ]
The values in the Time column are formatted as Unix timestamps, not human-readable strings.
We can convert each Unix time stamp into datetime object using the datetime.datetime.fromtimestamp() function:


datetime_object = datetime.datetime.fromtimestamp(1433213314.0)
We'll convert the Unix timestamp for each row to a datetime object using datetime.datetime.fromtimestamp(), format the date with strftime(), and store the result back in the row, replacing the Unix timestamp.

Instructions
Loop through posts, and for each row:
Convert the value in the Time column (index 2 of each row) to a floating point number.
Convert the floating point number to a datetime instance using datetime.datetime.fromtimestamp().
Store the resulting datetime instance back in index 2 of the row, overwriting the original Unix timestamp value.

"""
import datetime

for row in posts:
    row[2] = datetime.datetime.fromtimestamp(float(row[2]))
""" Console Output or Results

"""



"""
9: Counting Posts From March
Now that we've converted our posts data set to contain datetime instances, we can count how many of the top 1,000 posts users submitted in the month of March.

Instructions
Loop through posts, and for each row:
Use the datetime.month attribute to check if the datetime instance at index 2 equals 3.
If so, increment march_count.
"""
march_count = 0
for row in posts:
    if row[2].month == 3:
        march_count += 1
print(march_count)
""" Console Output or Results
Output
59
"""




"""
10: Counting Posts From Any Month
Let's write a function that generalizes our counting logic and makes it works for any month.

Instructions
Write a function that takes in an integer value representing a month, and returns the number of posts users submitted during that month.
Use the function to return the number of posts users submitted in February (month value of 2), and assign the count to a new variable feb_count.
Use the function to return the number of posts users submitted in August (month value of 8), and assign the count to a new variable aug_count.
"""
march_count = 0

for row in posts:
    if row[2].month == 3:
        march_count += 1

def post_in_month(month):
    month_count = 0
    for row in posts:
        if row[2].month == month:
            month_count += 1
    return month_count

feb_count = post_in_month(2)
print(feb_count)
aug_count = post_in_month(8)
print(aug_count)
""" Console Output or Results
Output
46
94
"""
