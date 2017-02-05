# 01/2017
# Dataquest : Complete Data Analyst Path
# Step 6 - Learning R
# SubStep : R Programming Beginner : Introduction To R

#-----------------------

#1: Python And R
#Data scientists love debating whether Python or R is a better language for data analysis. 
#There are Quora threads, venn diagrams, and more on the subject.

#While both languages have their strengths and weaknesses, R is used more heavily by academics, and Python is used more often by companies. 
#The R language is popular in academia because of its similarity to MATLAB, a common academic data analysis tool. 
#R also has good advanced statistical analysis and data visualization support.

#Python integrates well with tools used in industry, such as web servers, and is used to build data pipelines. 
#Python has a large ecosystem of libraries developed by contributors outside of the data science industry, which means that learning Python allows you to build just about any piece of software you want.

#Why learn R

#At Dataquest, our mission is to help prepare people for data science roles in companies. This means that we mainly teach Python. However, due to its visualization and statistical libraries, R can augment your data science workflow and help you explore data more effectively.

#-----------------------

#2: Introduction To The Data
#For this lesson, we'll be using a dataset of White House employee salaries, which you can find on whitehouse.gov. 
#The data contains information on every White House employee, including their name, title, and salary.

#-----------------------

#3: Assignment
#A key part of most programming languages is the idea of assigning values to variables. Each variable has a name like x, y, or highestSalary. Variable names cannot have spaces or special characters in them. A value can be 1, 1.1, or "hello". There are many other types of values that we'll explore later on.

#Assigning a value to a variable allows you to store the value, and refer to it later easily. While in most languages, you use the = sign to assign values to variables, in R you use <-, also known as the "carrot". This is two separate characters, the less than sign (<), and a dash (-).

#The = sign is also supported by R. It's mostly equivalent to <-, and you can read this blog post for a full explanation of the differences. We'll use <- in our lessons because the Google Style Guide recommends it.

# Instructions
# Assign the value 10 to the variable dogAwesomeness.
# Assign the value 9.5 to the variable catAwesomeness.

# This is a comment, and so is any line that starts with a #
# Comments help provide information about the code.

# Assign the value 10 to the variable bearAwesomeness.
bearAwesomeness <- 10

# Assign the value 1.5 to the variable guineaPigAwesomeness.
guineaPigAwesomeness <- 1.5

dogAwesomeness <- 10
catAwesomeness <- 9.5

#------------------------------------------------------------------

#4: Print
#A key part of exploring data is being able to print your results. 
#Printing your results enables you to see what the data looks like, and see what your computations are doing. 
#In R, we can print using the print function.

#Functions :

#Functions are snippets of pre-written code that can take in a value and do some computations with it. 
#In this case, the print function prints out a value so we can see it.

#Functions are stored in variables, just like other values. 
#We call the function using parentheses. 
#For instance, to print the value 10, we would type print(10).

#Instructions
#Let's upgrade our lifeSavings.
#Assign the value 9999 to the variable lifeSavings and then print lifeSavings.

# * ------------------------- *
# * Code *

# We can print out values
print(10)

# We can also assign a value to a variable, then print the variable
lifeSavings <- 5.5
print(lifeSavings)
lifeSavings <- 9999
print(lifeSavings)

# * ------------------------- *
# * Log or Results *

#Output
#[1] 10
#[1] 5.5
#[1] 9999


#------------------------------------------------------------------

#5: Types Of Variables
#R treats 5.5 differently from "cat" since 5.5 is a number and cat is text. 
#Every variable in R has a type. 
#The type of a variable defines how it is stored, and how functions and other variables interact with it.

#When we assign a value (like 5.5) to a variable (like lifeSavings), the variable can be said to be of the type of the value.

#Two commonly occurring types in R are character, which holds text, and numeric, which holds a number. 
#To look up which type a specific variable is, we can use the class function.

#Instructions
#Assign the type of biggestDog to biggestDogType.
#Assign the type of mastiffCount to mastiffCountType.

# * ------------------------- *
# * Code *

# Assign the value 800 to the variable runDistance.
runDistance <- 800

# This is of type "numeric".
print(class(runDistance))

# Assign the value "Peanut Butter Cup" to favoriteDessert
favoriteDessert <- "Peanut Butter Cup"

# This is of type "character", because it contains text.
print(class(favoriteDessert))

biggestDog <- "Mastiff"
mastiffCount <- 50

biggestDogType <- class(biggestDog)
mastiffCountType <- class(mastiffCount)

print(class(biggestDog))
print(biggestDogType)
print(class(mastiffCount))
print(mastiffCountType)

# * ------------------------- *
# * Log or Results *

#Output
#[1] "numeric"
#[1] "character"
#[1] "character"
#[1] "character"
#[1] "numeric"
#[1] "numeric"

#------------------------------------------------------------------

#6: Vectors
#Vectors are the primary way that values are stored in R. 
#Vectors are collections of values of the same type. 
#Vectors in R are different than mathematical vectors.

#If you've worked with other programming languages, you'll be familiar with lists and arrays -- vectors are similar.

#The reason why vectors are the core way to store data in R is that most data is naturally represented as a vector. 
#For example, consider looking at the stock price of Apple on 3 consecutive days. 
#You might end up with the values 114, 113, and 115. It would make sense to store these 3 values together, in a vector, as you analyze stock prices.

#⎡⎣⎢114113115⎤⎦⎥[114113115]
#Without the vector, we'd need to create three separate variables, price1, price2, and price3. 
#This would make our code needlessly complex. 
#Imagine if you wanted to explore and analyze the full history of Apple's stock price; you'd need thousands of separate variables for the thousands of values.

#We can define vectors, or collections of elements, using the c function. To create a vector containing just the value 1, you would write c(1). 
#To create a vector with two elements, 1 then 2, in that order, you would write c(1,2). 
#Each value in a vector is called an element.

#Instructions
#Create a vector with the elements 0, 1, 1, and 2 and assign it to the variable fibonacci.

# * ------------------------- *
# * Code *

# Store a vector of Russian presidents.
russianPresidents <- c("Mikhail Gorbachev", "Boris Yeltsin", "Vladimir Putin")

# Store a vector of stock prices on consecutive days.
applePrices <- c(113, 114, 115)

fibonacci <- c(0,1,1,2)
print(fibonacci)

# * ------------------------- *
# * Log or Results *

#Output
#[1] 0 1 1 2

#------------------------------------------------------------------

#7: Vectors And Single Values
#R stores almost every value as a vector. 
#This may be surprising to you, but when we were assigning single values to variables earlier, R actually stored those values in vectors. a <- 1 will create a vector with only one element in it. 
#R doesn't force us to write c(1) every time we want to create a vector with a single value.

#This property simplifies a lot of computations in R, and lets us treat all variables the same way.

#We can verify that this is true by comparing equality. We can use the identical function to check if two variables are exactly identical (i.e. they contain the same value). 
#The identical function will return a value of type boolean, which has to be either TRUE, or FALSE. 
#If the two objects are equal, the function will return TRUE, and if they're not, it'll return FALSE. We'll explore the boolean type more in the future.

#Instructions
#This step is a demo. Play around with code or advance to the next step.

# * ------------------------- *
# * Code *

dogCount <- 1
catCount <- c(1)

# We can see that these two assignments are identical.  dogCount is a vector, as is catCount.
print(identical(dogCount, catCount))

# * ------------------------- *
# * Log or Results *

#Output
#[1] TRUE

#------------------------------------------------------------------

#8: Indexing Vectors
#When a vector only has a single element, like we saw in the beginning of this mission, it's relatively easy to work with. 
#When a vector contains multiple elements, as most vectors do, we need a way to extract and work with the individual elements.

#This is where vector indexing comes in. 
#Indexing allows us retrieve individual elements from a vector. Here's a quick example:

#a <- c(3,5)
#a[1]
#a[2]
#R is a 1-indexed language. 
#This means that to access the first element in the vector, we use the index 1. a[1] will get the first element in a, and a[2] will get the second element in a.

#In the code area below, we've loaded the White House salaries data into the variable salaries. salaries is a vector containing all of the values for the salaries.

#Instructions
#Assign the 10th element in the vector salaries to a new variable named salary10.

# * ------------------------- *
# * Code *

# Print the first element in salaries.
print(salaries[1])

# Print the 50th element in salaries
print(salaries[50])

print(salaries[10])
salary10 <- salaries[10]
print(salary10)

# * ------------------------- *
# * Log or Results *

#Output
#[1] 105960
#[1] 50500
#[1] 103000
#[1] 103000

#------------------------------------------------------------------

#9: Vector Length
#Let's figure out how many White House staffers we have salaries for. 
#We can look this up by calculating the length of the salaries vector. 
#The length of a vector is the number of elements it contains. 
#The length function in R returns the number of elements in a vector.

#Instructions
#Find the length of the salaries vector and assign the result to salariesLength.

# * ------------------------- *
# * Code *

# Initialize the runDistances vector
runDistances <- c(20, 10.5, 30)

# Print the length of the vector.
print(length(runDistances))

# The salaries variable has been loaded in.
salariesLength <- length(salaries)
print(salariesLength)

# * ------------------------- *
# * Log or Results *

#Output
#[1] 3
#[1] 474

#------------------------------------------------------------------

#10: Vector Math
#In R, performing math operations on a vector will perform the same operation on each element of the vector. 
#We can use all the standard mathematical operators, + for addition, - for subtraction, * for multiplication, and / for division.

#a <- c(2, 4, 5)
#a + 2
#a + 2 will create a new vector that is the result of adding two to every element in a. 
#This will not change the value of a unless we assign it back to the a variable.

#Instructions
#Divide salaries by 3 and assign the result to lowerSalaries.

# * ------------------------- *
# * Code *

# Create a vector of stock prices.
stockPrices <- c(10, 9, 11, 15)

# This results in a new vector.  See how every element has had 2 added to it.
# Every time you do math on a vector, it will change all the elements of the vector.
print(stockPrices + 2)

# But stockPrices is unaffected.
print(stockPrices)

print(salaries)
lowerSalaries <- salaries / 3
print(lowerSalaries)

# * ------------------------- *
# * Log or Results *

#Output
#[1] 12 11 13 17
#[1] 10  9 11 15

#[1] 105960  55000 121200 155035 114000 134662  65650  42000  50000 103000
#[11]  42844  97000  42420 116804 126250 101000 155035  42000 160085  73225

#[1] 35320.00 18333.33 40400.00 51678.33 38000.00 44887.33 21883.33 14000.00
#[9] 16666.67 34333.33 14281.33 32333.33 14140.00 38934.67 42083.33 33666.67

#-------------------------------------------------------------------

#11: Overwriting Variables
#In the last screen, we discussed the following code snippet:

#a <- c(2, 4, 5)
#a + 2
#What if we want to store the result of a + 2 back into a? 
#We would need to overwrite the variable a and store the new value. 
#You can overwrite a variable using the same <- carrot operator:

#a <- a + 2
#This will add 2 to every element in a and overwrite the original value. 
#This is very commonly done when analyzing data.

#Instructions
#Subtract 5000 from every value in salaries and overwrite the variable salaries.

# * ------------------------- *
# * Code *

# Initialize our list of stock prices again.
stockPrices <- c(10, 9, 11, 15)

# Multiply every stock price by two, and overwrite the variable.
stockPrices <- stockPrices * 2
print(stockPrices)

salaries <- salaries - 5000

# * ------------------------- *
# * Log or Results *

#Output
#[1] 20 18 22 30

#------------------------------------------------------------------

#12: Vector Types
#Vectors in R can only contain elements of the same type. 
#You can't, for example, mix character elements and numeric elements in the same vector. 
#If you try to, all of the numeric elements will be converted to character elements.

#Instructions
#This step is a demo. Play around with code or advance to the next step.

# * ------------------------- *
# * Code *

mixedVector <- c("Fifteen", 15, 0)

# Everything in mixedVector is a character value.
print(mixedVector)

# mixedVector is of type character.
print(class(mixedVector))

# * ------------------------- *
# * Log or Results *

#Output
#[1] "Fifteen" "15"      "0"      
#[1] "character"

#------------------------------------------------------------------

#13: Getting Help
#If you ever need help with any R function, use the function help to get more information. 
#For example, if you wanted to learn more about the class function, you would type help(class).

#Instructions
#Try using the help function to get help with the class function.

# * ------------------------- *
# * Code *

# Enter your code here.
help(class)

# * ------------------------- *
# * Log or Results *



#------------------------------------------------------------------

#14: Next Steps
#We've learned a lot of the basics of R, and now that they're out of the way, we're ready to really dive into analyzing a dataset. 
#In the next mission, we'll dive more into the White House salaries data, and do some exploration.

#As always, if you have feedback on this mission or Dataquest in general, please reach out to us at hello@dataquest.io. 
#If you'd like to discuss Python or R, join our Slack community.
