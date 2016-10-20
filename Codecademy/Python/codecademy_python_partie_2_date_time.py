#Date and Time



"""
The datetime Library

A lot of times you want to keep track of when something happened. We can do so in Python using datetime.

Here we'll use datetime to print the date and time in a nice format.
Instructions

Click Save & Submit Code to continue.
"""

from datetime import datetime




"""

Getting the Current Date and Time

We can use a function called datetime.now() to retrieve the current date and time.

from datetime import datetime

print datetime.now()

The first line imports the datetime library so that we can use it.

The second line will print out the current date and time.
Instructions

    Create a variable called now and store the result of datetime.now() in it.
    Then, print the value of now.
"""

from datetime import datetime
now = datetime.now()
print now


#sortie : 2016-10-17 19:56:28.985946




"""
Extracting Information

Notice how the output looks like 2013-11-25 23:45:14.317454. What if you don't want the entire date and time?

from datetime import datetime
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

You already have the first two lines.

In the third line, we take the year (and only the year) from the variable now and store it in current_year.

In the fourth and fifth lines, we store the month and day from now.
Instructions

    On a new line, print now.year. Make sure you do it after setting the now variable!
    Then, print out now.month.
    Finally, print out now.day.
"""


from datetime import datetime
now = datetime.now()
print now.year
print now.month
print now.day



"""

Hot Date

What if we want to print today's date in the following format? mm/dd/yyyy. Let's use string substitution again!

from datetime import datetime
now = datetime.now()

print '%s-%s-%s' % (now.year, now.month, now.day)
# will print: 2014-02-19

Remember that the % operator will fill the %s placeholders in the string on the left with the strings in the parentheses on the right.

In the above example, we print 2014-02-19 (if today is February 19th, 2014), but you are going to print out 02/19/2014.
Instructions

Print the current date in the form of mm/dd/yyyy.

    Change the string so that it uses a / character in between the %s placeholders instead of a - character.
    Re-arrange the parameters to the right of the % operator so that you print now.month, then now.day, then now.year.
"""

from datetime import datetime
now = datetime.now()

print '%s/%s/%s' % ( now.month, now.day, now.year)


# sortie : 10/17/2016



"""
Pretty Time

Nice work! Let's do the same for the hour, minute, and second.

from datetime import datetime
now = datetime.now()

print now.hour
print now.minute
print now.second

In the above example, we just printed the current hour, then the current minute, then the current second.

We can again use the variable now to print the time.
Instructions

Similar to the last exercise, print the current time in the pretty form of hh:mm:ss.

    Change the string that you are printing so that you have a : character in between the %s placeholders.
    Change the three things that you are printing from month, day, and year to now.hour, now.minute, and now.second.
"""

from datetime import datetime
now = datetime.now()

print '%s:%s:%s' % ( now.hour, now.minute, now.second)


# sortie : 19:57:45




"""
Grand Finale

We've managed to print the date and time separately in a very pretty fashion. Let's combine the two!

from datetime import datetime
now = datetime.now()

print '%s/%s/%s' % (now.month, now.day, now.year)
print '%s:%s:%s' % (now.hour, now.minute, now.second)

The example above will print out the date, then on a separate line it will print the time.

Let's print them all on the same line in a single print statement!
Instructions

Print the date and time together in the form: mm/dd/yyyy hh:mm:ss.

To start, change the format string to the left of the % operator.

    Ensure that it has 6 %s placeholders.

    Put slashes and colons and a space between the placeholders so that they fit the format above.

    Then, change the variables in the parentheses to the right of the % operator.
    """


from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

# sortie : 10/17/2016 19:58:18

