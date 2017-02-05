# 01/2017
# Dataquest : Complete Data Analyst Path
# Step 6 - Learning R
# SubStep : R Programming Beginner : Working with data frames

#------------------------------------------------------------------

#1: Functions
#We learned about data frames, a powerful way to represent and work with data, in the last mission.

#Before we dive more into data frames, lets take a look at functions.
#Functions are named chunks of code that take in inputs, and return some outputs.
#sum is a function that we used in the last mission -- it adds all of the values in a vector together.
#print is another function -- it displays a string on the screen.

#We use functions to save ourselves the trouble of writing the same code every time.
#For example, adding all the elements in a vector takes quite a few lines of code -- having a function to do it for us means that we can save ourselves some typing.

#sum and print are builtin functions -- they already exist whenever we start programming in R.
#We can also define our own functions to perform tasks.

#We can write functions like this:

#add <- function(a, b){
#    d <- a + b
#    return(d)
#}
#Let's deconstruct what you see above.
#We have add, which is a variable name. The <- denotes assignment, so we're assigning the function to the variable name.
#function is a special keyword that we use to define a function in R. a and b are the input arguments to the function.
#We separate them with a comma. A function have have any number of arguments, including zero.

#Once we define the arguments, we open the body of the function with a curly brace.
#Inside the function, we write whatever computations we want the functions to do.
#The input arguments are passed into the body of the function, so we can access them however we want.

#We choose to add a and b together, and assign the result to d. Then we return that result.
#The return function will return as output from the function whatever is passed to it.
#So the variable d will be returned as the output of the function.

#------------------------------------------------------------------

#2: Calling Functions
#We can call functions that we define the same way we've been calling builtin functions.
#We would just type add(1,2) to call our add function.
#In the function body, a would take on the value 1, and b would take on the value 2.
#This is because 1 is the first input to our add function, and 2 is the second input.
#a is the first variable in the function definition, and b is the second.
#Inputs are matched to variables by position -- the first is assigned to the first one in the function definition, the second to the second, and so on.

#Instructions
#Call the function add with the arguments 5 and 10 and assign the result to d.

# * ------------------------- *
# * Code *

# Define the add function.
add <- function(a, b){
    return(a + b)
}

# Call the add function with the arguments 1 and 2.
print(add(1, 2))
d <- add(5, 10)
print(d)

# * ------------------------- *
# * Log or Results *

#Output
#[1] 3
#[1] 15

#------------------------------------------------------------------

#3: Defining A Function
#Let's define a function to subtract two numbers.

#Instructions
#Define a function that takes two arguments, a and b:
#It should subtract b from a and return the result.
#Assign the function to the variable subtract.
#Call the function with the arguments 50 and 10 and assign the result to d.

# * ------------------------- *
# * Code *

# Enter your code here.
subtract <- function(a,b){
    return(a - b)
}
d <- subtract(50,10)
print(d)

# * ------------------------- *
# * Log or Results *

#Output
#[1] 40

#------------------------------------------------------------------

#4: Reading In The Data
#In this mission, we'll be using UFO sighting data. The data looks like this:

#date sighted,date reported,duration,city,state,geocode score,geocode precision,latitude,longitude
#20040616,20040617,1 minute, Willoughby Hills, OH,0.743,zip,25.3166667,85.2833333
#20021116,20021120,30 seconds, Halls Gap (near Melbourne) (NSW, Australia),0.768,zip,-37.8139965641595,144.963322877884
#19920615,19961203,2-3 mins, River Falls, WI,0.757,zip,39.3666667,22.9458333
#Each row corresponds to a report of a UFO sighting.
#There are 10000 rows, counting the header, and they were randomly sampled from a larger dataset.

#Here are descriptions of some of the columns:

#date sighted -- the date the ufo was seen.
#date reported -- the date the sighting was reported.
#duration -- how long the ufo was seen for.
#city -- the city the sighting happened in.
#state -- the state the sighting happened in.
#latitude -- the latitude of the sighting.
#longitude -- the longitude of the sighting.
#Instructions
#Read the data in ufo_sightings.csv and assign it to the variable ufos.

# * ------------------------- *
# * Code *

# Enter your code here.
ufos  <- read.csv("ufo_sightings.csv")

# * ------------------------- *
# * Log or Results *

#Variables
# ufosdata.frame (list)
#["'data.frame':	10000 obs. of  9 variables:"," $ date.sighted     : int  20040616 20021116 19920615 20050901 20060607 20050816 20040925 19990812 20070624 20080102 ..."," $ date.reported    : int  20040617 20021120 19961203 20050902 20060617 20050818 20040925 20050311 20070624 20080522 ..."," $ duration         : Factor w/ 2546 levels "","-","?","??",..: 602 1088 797 1257 711 2431 434 455 397 1892 ..."," $ city             : Factor w/ 5290 levels " 14 Island Lake (Canada)",..: 5164 1891 4008 1824 2841 5171 347 4587 4134 1952 ..."," $ state            : Factor w/ 198 levels ""," ."," 15 MILES SW of)",..: 126 21 191 98 67 149 187 126 32 97 ..."," $ geocode.score    : num  0.743 0.768 0.757 0.757 0.782 0.796 0.857 0.829 0.732 0.857 ..."," $ geocode.precision: Factor w/ 2 levels "unmatched","zip": 2 2 2 2 2 2 2 2 2 2 ..."," $ latitude         : num  25.3 -37.8 39.4 35.2 20.1 ..."," $ longitude        : num  85.3 145 22.9 24.9 -97 ..."]

#------------------------------------------------------------------

#5: Exploring The Data Frame
#If you want to quickly peek at a data frame, you can use the head function to see the beginning, and the tail function to see the end.

#Both functions take two arguments, first the data frame you want to explore, and second the number of rows you want to see.
#head will show that number of rows at the beginning of the dataframe, and tail will show that number of rows at the end.

#Instructions
#Print the last 5 rows of ufos, using the tail function.

# * ------------------------- *
# * Code *

# Print the first 5 rows in the data frame.
print(head(ufos, 5))
print("--------------")
print(tail(ufos, 5))

# * ------------------------- *
# * Log or Results *

#Output
#  date.sighted date.reported       duration                             city
#1     20040616      20040617       1 minute                 Willoughby Hills
#2     20021116      20021120     30 seconds  Halls Gap (near Melbourne) (NSW
#3     19920615      19961203       2-3 mins                      River Falls
#4     20050901      20050902 3 minutes each                      Great Falls
#5     20060607      20060617    20 minustes                     Martinsville
#        state geocode.score geocode.precision  latitude longitude
#1          OH         0.743               zip  25.31667  85.28333
#2  Australia)         0.768               zip -37.81400 144.96332
#3          WI         0.757               zip  39.36667  22.94583
#4          MT         0.757               zip  35.15585  24.89502
#5          IL         0.782               zip  20.06667 -97.05000
#[1] "--------------"
#      date.sighted date.reported        duration
#9996      20041230      20051202      15 minutes
#9997      20060209      20060209 5 to 10 minutes
#9998      20050401      20050411        1 minute
#9999      20000409      20000425        not sure
#10000     20061101      20061102       3 minutes
#                                              city state geocode.score
#9996                           High River (Canada)    AB         0.771
#9997                            Coeur d&apos;Alene    ID         0.743
#9998                                        Tucson    AZ         0.857
#9999   Singapore (Orchid Country Club golf course)               0.750
#10000                                       Adrian    MI         0.810
#      geocode.precision  latitude  longitude
#9996                zip 60.000000  -96.00000
#9997                zip 30.050000   31.25000
#9998                zip 32.221743 -110.92648
#9999                zip  1.293056  103.85583
#10000               zip 37.661754   14.83478

#------------------------------------------------------------------

#6: UFO Sighting Years
#Now that we've taken a look at the data, you may have noticed that the date.sighted column has the year, month, and day that the sighting happened.
#We can use this to figure out how many UFO sightings occured in each year.
#
#Unfortunately, the data is a little bit hard to work with because the year, month, and day are combined into one field.
#
#In order to process this field, we'll need to figure out what type it is.
#If it's a number, we'll need to process it differently than if it's a character.
#
#We can figure out the types of all the columns in a data frame with the str function.
#The str function will turn any R object into a human-readable form, with information about it.
#In the case of a data frame, it will display each column, and the type of that column.
#
#Instructions
#Use the str function on the ufos data frame.
#Use the print function to display ufos.

# * ------------------------- *
# * Code *

# Enter your code here.
ufos <- str(ufos)
print(ufos)

# * ------------------------- *
# * Log or Results *

#Output
#'data.frame':	10000 obs. of  9 variables:
# $ date.sighted     : int  20040616 20021116 19920615 20050901 20060607 20050816 20040925 19990812 20070624 20080102 ...
# $ date.reported    : int  20040617 20021120 19961203 20050902 20060617 20050818 20040925 20050311 20070624 20080522 ...
# $ duration         : Factor w/ 2546 levels "","-","?","??",..: 602 1088 797 1257 711 2431 434 455 397 1892 ...
# $ city             : Factor w/ 5290 levels " 14 Island Lake (Canada)",..: 5164 1891 4008 1824 2841 5171 347 4587 4134 1952 ...
# $ state            : Factor w/ 198 levels ""," ."," 15 MILES SW of)",..: 126 21 191 98 67 149 187 126 32 97 ...
# $ geocode.score    : num  0.743 0.768 0.757 0.757 0.782 0.796 0.857 0.829 0.732 0.857 ...
# $ geocode.precision: Factor w/ 2 levels "unmatched","zip": 2 2 2 2 2 2 2 2 2 2 ...
# $ latitude         : num  25.3 -37.8 39.4 35.2 20.1 ...
# $ longitude        : num  85.3 145 22.9 24.9 -97 ...
#NULL

#------------------------------------------------------------------

#7: Converting Types
#It looks like the column is an int, which is short for integer.
#An integer is numeric, but it's stored slightly differently on the backend.
#It's generally safe to treat integers and numerics the same way, so we won't get too much into the distinction right now.
#You can read more about integers here.
#
#We only care about the year right now.
#When the type of the column is numeric, this will be very difficult, because we'll need to subtract the month and day to get just the year.
#This operation doesn't make much logical sense.
#An easier way to do it is the convert the date sighted to a character type, and then extract the first 4 characters, which will be the year.
#This is much simpler.
#
#We can convert between types using functions -- in this case, we need the date sighted to be a character vector so that we can process it more easily.
#We can do this conversion using the as.character function.
#
#Going forward, we'll sometimes use a slightly different indexing notation -- ufos$date.sighted will return the date.sighted column of ufos.
#This is equivalent to ufos[,"date.sighted"] -- it will return a vector.
#
#Instructions
#Convert the date.sighted column of ufos to the character type and assign the result to dateSighted.

# * ------------------------- *
# * Code *

dateReported <- as.character(ufos$date.reported)
dateSighted <- as.character(ufos$date.sighted)

# * ------------------------- *
# * Log or Results *



#------------------------------------------------------------------

#8: Substring Function
#We want to extract the year from our dates.
#Each of our dates looks like 20060620 -- we need to get from this to just 2006.
#This involves extracting just a few letters from our character type.

#In this case, we can use the substr (substring) function.
# Another name for character types is strings, and you'll commonly see them referred to this way.

#The substr function takes 3 arguments -- the character that we want to extract letters from, the letter index we want to start from, and the letter index we want to end at.

#date <- "20040415"
#substr(date, 1, 4)
#This code will start at the first letter in date, and go up to the fourth letter.
#It will pull out all the letters in between, inclusive of the ends, which are 2, 0, 0, and 4 (2004).
#So it will extract the year for us.

#Remember how single values in R are vectors by default?
#Because of this, our substr function is already working on a vector.
#We can use substr on a single value, or our entire dataSighted vector. Here's another example:

#dates <- c("20040415", "20080515")
#substr(dates, 1, 4)
#substr is actually working on each element of date.
#It does the exact same operation each time, and extracts the first four letters.
#Our result will be c("2004", "2008").

#Instructions
#Extract the year from each of the elements in dateSighted and assign the result to years.

# * ------------------------- *
# * Code *

# This extracts "2004" from our string.
date <- "20040415"
print(substr(date, 1, 4))

# This extracts the year from each string in the vector.
dates <- c("20040415", "20080515")
print(substr(dates, 1, 4))

years <- substr(dateSighted, 1, 4)
print(class(dateSighted))
print(class(years))
print(years[1:5])
#print(years) ok

# * ------------------------- *
# * Log or Results *

#Output
#[1] "2004"
#[1] "2004" "2008"
#[1] "character"
#[1] "character"
#[1] "2004" "2002" "1992" "2005" "2006"

#------------------------------------------------------------------

#9: Making A Table
#We now have a vector of years. It looks like this:

#[1] "2004" "2002" "1992" "2005" "2006" "2005" "2004" "1999" "2007" "2008"
#   [11] "2008" "1998" "2002" "2004" "2007" "2009" "2007" "2004" "2000" "2005"
#The above is truncated, but we have 10000 years, which matches the number of ufo sightings in our data.

#We want to find how many ufo sightings are in each year.
#To do this, we can use the table function in R.
#It goes through the vector, finds the unique values, and then figures out how many times each unique value occurs in the vector.
#This will do exactly what we want, and give us a count of how many sightings occured in each year.

#Instructions
#Create a table of the years variable, and print it out.

# * ------------------------- *
# * Code *

# Create a small vector with a few years
selectedYears <- c("2004", "2002", "1992", "2005", "2006", "2005", "2004")

# Create and print a table
print(table(selectedYears))
print("----------")
print(table(years))

# * ------------------------- *
# * Log or Results *

#Output
#selectedYears
#1992 2002 2004 2005 2006
#   1    1    2    2    1
#[1] "----------"
#years
#   0 1400 1790 1880 1899 1905 1914 1933 1936 1941 1942 1944 1945 1946 1947 1948
#  36    1    1    1    1    1    1    1    2    1    1    2    1    1    8    4
#1949 1950 1951 1952 1953 1954 1955 1956 1957 1958 1959 1960 1961 1962 1963 1964
#   6    4    4    7    9    8    8    7   14    7    9   14    5    5   14   14
#1965 1966 1967 1968 1969 1970 1971 1972 1973 1974 1975 1976 1977 1978 1979 1980
#  22   38   34   37   28   20   19   25   38   49   43   57   51   60   48   34
#1981 1982 1983 1984 1985 1986 1987 1988 1989 1990 1991 1992 1993 1994 1995 1996
#  32   31   17   27   27   34   44   32   38   38   34   42   52   56  225  174
#1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010
# 192  317  482  498  562  615  672  796  750  654  748  831  738  441

#------------------------------------------------------------------

#10: Working With Dates
#Let's try to find the difference between the date a ufo was sighted, and the date is was reported.
#To do this, we'll first have to convert date.sighted and date.reported to a different data type -- the date type.
#
#If we left them as numerics and subtracted them, we'd end up with nonsensical results -- 20150515 - 20150510 would give us 5, which makes sense -- the dates are 5 days aparts. But, 20150515 - 20150415 would give us 100, which makes no sense -- they aren't separated by 100 days.
#
#We'll first convert the columns to strings.
#Then, to convert a string to a date, we'll need to use the as.Date function. When you store dates as strings, it can be in many different ways -- 2015/04/15, or 04/15/2015, or 20150415.
#All of these are the same date, but humans write dates in many different ways.
#To solve this problem, there's a concept known as date formatting.
#Date formatting enables you to specify how your date looks -- R is then able to figure out which parts of the string are the year, month, and day, and convert to a Date type properly.
#
#For example, if you wanted to convert 04/15/2015 to a Date type, you would run as.Date("04/15/2015", "%m/%d/%Y").
#This tells R that in the string, the month comes first (04), then a forward slash (/), then the day (15), then another forward slash, then the full, 4-digit year (2015).
#
#If we wanted to convert 2015-04-15 to a date, we would use as.Date("2015-04-15", "%Y-%m-%d").
#This tells R that the 4 digit year comes first, then a dash (-), then the month, then another dash, then the day.
#
#%Y means 4-digit year, %m means numeric month, and %d means numeric day.
#All of these are known as conversion specifications -- they indicate how to convert a string into a date.
#There are other conversion specifications -- for example %y means two-digit year. A full list is here.
#
#For now, let's convert date.sighted and date.reported.
#
#Instructions
#Convert the date.reported column in ufos to a Date and assign the result to dateReported.
# link about : Date-time Conversion Functions to and from Character
#https://stat.ethz.ch/R-manual/R-devel/library/base/html/strptime.html

# * ------------------------- *
# * Code *

dateSighted <- as.character(ufos$date.sighted)
dateSighted <- as.Date(dateSighted, "%Y%m%d")

dateReported <- as.character(ufos$date.reported)
dateReported <- as.Date(dateReported, "%Y%m%d")

print(class(dateSighted))
print("-------------------")
print(class(dateReported))
print("-------------------")
print(dateSighted[5])
print("-------------------")
print(dateReported[5])

# * ------------------------- *
# * Log or Results *

#Output
#[1] "Date"
#[1] "-------------------"
#[1] "Date"
#[1] "-------------------"
#[1] "2006-06-07"
#[1] "-------------------"
#[1] "2006-06-17"

#------------------------------------------------------------------

#11: Subtracting Vectors
#Since R works with vectors by default, mathematical operations automatically work on vectors.
#
#If you have two vectors, a <- c(3,4,5), and b <- c(3,2,1), doing a-b will subtract the first element in b from the first element in a, the second element in b from the second element in a, and so on.
#You'll end up with a vector that looks like this -- c(0,2,4).
#Any mathematical operation on a vector will do this -- it will perform the operation on the vector elements at each position, and create a new vector with the result.
#
#One major caveat is that this only works like that when vectors are the same length.
#If the vectors aren't the same length, R does something called recycling.
#Let's say you have these two vectors -- a <- c(3,4,5), and b <- 1. If you do a-b, R will recycle the elements in b, because a is longer.
#So the first element in b will be subtracted from the first element in a, the first element in b will be subtracted from the second element in a, and so on.
#You'll end up with c(2,3,4) -- every element in a will have one subtracted.
#
#When recycling gets really tricky is when one vector has more than one element, but less elements that the other vector.
#Let's say we have these two vectors -- a <- c(3,4,5,6,7), and b <- c(1,2). If we do a-b, the first element in b will be subtracted from the first element in a.
#Then the second element in b will be subtracted from the second element in a.
#Then we run out of elements in b, so we go back to the beginning.
#The first element in b will be subtracted from the third element in a, the second element in b will be subtracted from the fourth element in a.
#We then run out of elements in b again, so we go back to the beginning again.
#The first element in b is subtracted from the fifth element in a.
#We end up with c(2,2,4,4,6).
#
#R will recycle elements of a shorter vector however many times is necessary to perform the operation on all the elements of the longer vector.
#This can be extremely confusing, and lead to unexpected behavior, so be careful about vector lengths when doing operations on them.
#
#Instructions
#Subtract dateSighted from dateReported and assign the result to the variable delay.

# * ------------------------- *
# * Code *

# Enter your code here.
delay <- dateReported - dateSighted
print(delay[1])
print(delay[2])
print(delay[3])
print(delay[4])
print(delay[5])

# * ------------------------- *
# * Log or Results *

#Output
#Time difference of 1 days
#Time difference of 4 days
#Time difference of 1632 days
#Time difference of 1 days
#Time difference of 10 days

#------------------------------------------------------------------

#12: Making A Table Of Delays
#Subtracting two date vectors gives you date differences, in days. We can make a table to summarize the results.

#Instructions
#Make a summary table of the delay vector.
#Make sure to print the table

# * ------------------------- *
# * Code *

# Enter your code here.
print(table(delay))

# * ------------------------- *
# * Log or Results *

#Output
#delay
#  -120    -37    -27    -20    -17     -7     -5     -4     -2     -1      0
#     1      1      2      1      1      2      1      2      3    133   2549
#     1      2      3      4      5      6      7      8      9     10     11
#  1582    564    319    242    188    154    139     84     86     73     67
#    12     13     14     15     16     17     18     19     20     21     22
#    51     45     52     47     42     33     28     29     29     30     18
#    23     24     25     26     27     28     29     30     31     32     33
#    12     21     16     22     26     21     22     18     25     18     24
#    34     35     36     37     38     39     40     41     42     43     44
#    12     13     19      9     11     12     12      8      7     11      8
#    45     46     47     48     49     50     51     52     53     54     55

#------------------------------------------------------------------

#13: Cleaning Up The Data
#The table we just made is extremely messy -- there are some values that are greater than 10 years.
#There are also some negative values.
#
#It will take a few steps to clean up the data and generate a good table. First, let's get rid of the negative values.
#These happens when dateReported is less than dateSighted -- this obviously makes no sense, as you can't tell someone about something you haven't seen yet.
#
#Before we do this, we'll combine dateReported and dateSighted into one date frame to make them easier to work with.
#
#You can do this with the data.frame function. You just pass in all of the vectors you want to have in your data frame, and it creates a new data frame where each of those vectors are columns.
#
#Instructions
#Use the data.frame function to create a data frame with dateReported and dateSighted as columns (in that order) and assign the result to dates.

# * ------------------------- *
# * Code *

# Enter your code here.
dates <- data.frame(dateReported,dateSighted)
print(class(dates))
print("---------------")
print(head(dates,3))

# * ------------------------- *
# * Log or Results *

#Output
#[1] "data.frame"
#[1] "---------------"
#  dateReported dateSighted
#1   2004-06-17  2004-06-16
#2   2002-11-20  2002-11-16
#3   1996-12-03  1992-06-15

#------------------------------------------------------------------

#14: Booleans
#One of the nice things about R is that you can easily filter data frames and vectors. This filtering is done with something called booleans.

#Booleans are a special type that can only have the value TRUE, or the FALSE. We generate booleans with truth statements that compare equality.
#These statements assert whether something is TRUE or FALSE. For example, this statement -- 5 == 10 will return FALSE, because 5 and 10 are not equal.

#There are a few ways to compare equality in R, but the double equals sign (==) is the first one we'll look at. == checks whether two values, are the exact same.
#It returns TRUE when they are, and FALSE when they aren't.
#There are some caveats around equality that we'll get into later, but you can read about here if you want to explore more now.

#If you compare equality across a vector, == will return a vector. For example, we can do this:


#a <- c(1,2,3)
#b <- c(5,2,5)
#a == b
#This will return a vector c(FALSE, TRUE, FALSE). It will compare the first elements in each array, then the second elements, then the third elements.
#The same rules about vector recycling from before apply to the double equals statement.

#We can also compare things besides exact equality. We can use the less than sign (<) to check if a value is less than another.
#For example, we can do this:

#a <- c(1,2,3)
#b <- c(5,2,5)
#a < b
#This will compare the first element in a to the first element in b, and check if the element in a is smaller.
#It will then do the same comparison for the other elements. It will result in c(TRUE, FALSE, TRUE).
#
#We can do the same thing with the greater than sign (>).
#
#Instructions
#Generate a boolean vector that indicates when delay is greater than 0 and assign the result to positiveDelays.

# * ------------------------- *
# * Code *

a <- c(1,2,3)
b <- c(5,2,5)

# Find when each element in a is greater than the corresponding element in b.
print(a > b)

positiveDelays <- delay > 0
print(positiveDelays)

# * ------------------------- *
# * Log or Results *

#Output
#[1] FALSE FALSE FALSE
#    [1]  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE  TRUE FALSE  TRUE FALSE  TRUE
#   [13] FALSE FALSE FALSE FALSE  TRUE  TRUE FALSE  TRUE  TRUE  TRUE  TRUE  TRUE
#   [25]  TRUE FALSE  TRUE  TRUE  TRUE  TRUE FALSE  TRUE  TRUE  TRUE  TRUE FALSE
#   [37]  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE  TRUE FALSE  TRUE
#   [49] FALSE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE  TRUE
#   [61]  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE FALSE FALSE  TRUE  TRUE  TRUE
#   [73]  TRUE FALSE  TRUE  TRUE  TRUE FALSE  TRUE FALSE FALSE  TRUE FALSE  TRUE
#   ....

#------------------------------------------------------------------

#15: Filtering With Booleans
#Now that we have a boolean vector, we can use it to filter a dataframe or vector.
#Filtering will only keep elements in rows where the boolean vector at the same position is TRUE.
#It will discard anything in a position where the vector is FALSE.


#filter <- c(TRUE, FALSE, TRUE, FALSE)
#bestPlanets <- c("Earth", "Mars", "Jupiter", "Venus")
#bestPlanets[filter]
#This will only select the elements in bestPlanets where filter is TRUE. We'll end up with c("Earth", "Jupiter").

#Here's another example:


#filter <- c(FALSE, FALSE, TRUE, TRUE)
#bestIceCreamFlavors <- c("Peanut Butter Oreo", "Cookie Dough", "Mint Chocolate Chip", "Peanut Butter Cup")
#bestIceCreamFlavors[filter]
#This will result in c("Mint Chocolate Chip", "Peanut Butter Cup").

#To do the same thing with a data frame, we also have to specify which columns we want:
##
#
#filter <- c(FALSE, FALSE, TRUE, TRUE)
#bestIceCreamFlavors <- data.frame(c("Peanut Butter Oreo", "Cookie Dough", "Mint Chocolate Chip", "Peanut Butter Cup"))
#bestIceCreamFlavors[filter,]
#The above code will select all columns of bestIceCreamFlavors, and only the last two rows.

#Instructions
#Use the positiveDelays vector to filter dates and assign the result to positiveDates.

# * ------------------------- *
# * Code *

filter <- c(FALSE, FALSE, TRUE, TRUE)
bestIceCreamFlavors <- data.frame(c("Peanut Butter Oreo", "Cookie Dough", "Mint Chocolate Chip", "Peanut Butter Cup"))
twoFlavors <- bestIceCreamFlavors[filter,]
print(twoFlavors)

positiveDates <- dates[positiveDelays,]
print(head(positiveDates,3))

# * ------------------------- *
# * Log or Results *

#Output
#[1] Mint Chocolate Chip Peanut Butter Cup
#4 Levels: Cookie Dough Mint Chocolate Chip ... Peanut Butter Oreo
#  dateReported dateSighted
#1   2004-06-17  2004-06-16
#2   2002-11-20  2002-11-16
#3   1996-12-03  1992-06-15

#------------------------------------------------------------------

#16: Null Values
#In our original data, not all of the rows had a date.reported and a date.sighted.
#In cases like this, R assigns the symbol NA to indicate that the value isn't available.
#This is called missing data. One simple way to deal with missing data is to remove any rows with any missing columns.

#We can do this with the na.omit function.
#It will remove any rows from the dataframe where NA values are encountered.
#This will make our results more useful.

#na.omit is called with only one argument -- the data frame you want to remove the NA values from.
#It will return a new dataframe without the rows containing missing data.

#Instructions
#Use the na.omit function to remove the missing data from positiveDates and assign the result to cleanDates.

# * ------------------------- *
# * Code *

# Enter your code here.
cleanDates <- na.omit(positiveDates)

# * ------------------------- *
# * Log or Results *



#------------------------------------------------------------------

#17: Remaking Our Table
#Now, we can redo our table with only accurate data. We'll just have to subtract the two columns of cleanDates.

#Instructions
#Subtract the dateSighted column of cleanDates from the dateReported column.
#Make a table of the resulting vector and use the print function to display delay.

# * ------------------------- *
# * Code *

# Enter your code here.
delay <- cleanDates$dateReported - cleanDates$dateSighted
print(table(delay))

# * ------------------------- *
# * Log or Results *

#Output
#delay
#     1      2      3      4      5      6      7      8      9     10     11
#  1582    564    319    242    188    154    139     84     86     73     67
#    12     13     14     15     16     17     18     19     20     21     22
#    51     45     52     47     42     33     28     29     29     30     18
#    23     24     25     26     27     28     29     30     31     32     33
#    12     21     16     22     26     21     22     18     25     18     24
#    34     35     36     37     38     39     40     41     42     43     44
#    12     13     19      9     11     12     12      8      7     11      8
#    ...
