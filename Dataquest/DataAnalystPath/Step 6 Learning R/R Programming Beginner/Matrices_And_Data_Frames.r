# 01/2017
# Dataquest : Complete Data Analyst Path
# Step 6 - Learning R
# SubStep : R Programming Beginner : Matrices And Data Frames

#------------------------------------------------------------------

#1: Introduction
#In the last mission, we looked at the basics of R. A key topic we looked at was vectors.
#Vectors are core to R, and most data in R is stored as a vector.

#We'll be looking more into vectors in this mission, along with other ways to structure data called matrices and data frames.

#For this mission, we'll be using a dataset of White House employee salaries, which you can find on whitehouse.gov.
#The data contains information on every White House employee, including their name, title, and salary.

#------------------------------------------------------------------

#2: Reading In Data
#A very common way to store data on a hard drive is in comma separated values format.
#This format has the file extension .csv. If you open a csv file, it will look something like this:


#Name,Status,Salary,Pay Basis,Position Title
#"Abdullah, Hasan A.",Detailee,105960,Per Annum,POLICY ADVISOR
#"Abraham, Sabey M.",Employee,55000,Per Annum,ENERGY AND ENVIRONMENT DIRECTOR FOR PRESIDENTIAL PERSONNEL
#The data has rows and columns.
#The first row of data is Name,Status,Salary,Pay Basis,Position Title.
#This is called a header row, and it tells you what the data in the rest of the rows means.
#This row contains multiple columns. Each column is a different datapoint.
#In this case, the first column of the row is Name, the second column is Status, and so on.
#One row goes across the data, left to right.

#The first column of the data is:

#Name
#"Abdullah, Hasan A."
#"Abraham, Sabey M."
#One column goes down the data, top to bottom.

#When we look at the second row -- "Abdullah, Hasan A.",Detailee,105960,Per Annum,POLICY ADVISOR, we can see that Name is "Abdullah, Hasan A.", Status is Detailee, Salary is 105960, Pay Basis is Per Annum, and Position Title is POLICY ADVISOR.

#Each row after the header row contains data on a single White House employee. As you can see, we separate each column within the rows with a , (comma).
#If you've used Excel before, this layout will look very familiar -- it's how spreadsheets look.

#We can read a csv file into R using the read.csv function.
#This will take a csv file, and split it properly into the right rows and columns.

#Instructions
#The file we'll be working with in this mission is called 2015_white_house.csv.
#Read this file into the variable whiteHouse.


# * ------------------------- *
# * Code *

congress <- read.csv("114_congress.csv")
whiteHouse <- read.csv("2015_white_house.csv")
print(class(whiteHouse))

# * ------------------------- *
# * Log or Results *

#Output
#[1] "data.frame"

#------------------------------------------------------------------

#3: Matrices
#When we read the 2015_white_house.csv file in, you may have noticed that it had both rows and columns of data.

#We can't store this kind of data as a vector, because vectors can only hold one dimension of data.
#For example: c(3,6,1) would be a vector. We call a vector one dimensional because it can only hold data going in one direction.
#All data in the vector has to be sequentially indexed. So a[1] would give you 3, a[2] would give you 6, and so on.

#But, how would we store something like this into a vector?


#Name   Status Salary Pay.Basis Position.Title
#           Abdullah, Hasan A. Detailee 105960 Per Annum POLICY ADVISOR
#            Abraham, Sabey M. Employee  55000 Per Annum ENERGY AND E..
#         Abraham, Yohannes A. Employee 121200 Per Annum SPECIAL ASSI..
#           Abramson, Jerry E. Employee 155035 Per Annum DEPUTY ASSIS..
#The problem is that not everything is sequential. If we start from the top left, at Name, some data points are below Name, and some are to the right.
#This means that we can't store everything in a vector.

#But, if you look closely at this data, you can see that each row is a vector. We could store the first row into a vector like this: row1 <- c("Name", "Status", "Salary", "Pay.Basis", "Position.Title"). And the second row like this: row2 <- c("Abdullah, Hasan A.", "Detailee", 105960, "Per Annum", "POLICY ADVISOR").

#It would be impractical to make a separate vector for each row, though -- we'd have to deal with many different variables.
#A far easier way to store this is as a matrix. A matrix is said to be two-dimensional -- it can store data in rows (one dimension), and columns (another dimension).

#------------------------------------------------------------------

#4: Creating A Matrix
#In R, we can create matrices with the matrix function.
#We turn a vector into a matrix by specifying the number of columns and rows we want the final data to have.

#For example, the vector c(1,2,3,4,5,6) could be turned into a matrix with 2 rows and 3 columns:


#1 3 5
#2 4 6
#It can also be turned into a matrix with 3 rows and 2 columns:


#1 4
#2 5
#3 6
#The number of elements in a matrix is equal to the number of rows times the number of columns.
#So, if we want to turn a vector into a matrix, the row and column count we want has to match the number of elements in the vector.

#We can create a matrix with the matrix function. The function takes 3 inputs, or arguments.
#The first argument is the vector we want to turn into a matrix. The second argument is the number of rows we want the resulting matrix to have.
#The third argument is the number of columns we want the resulting matrix to have.

#Instructions
#Create a matrix C from the vector c("Rambo", "Chuck Norris", "Arnold", "Steven Seagal", "John Wayne", "Steve McQueen").
#C should have 2 rows and 3 columns.

# * ------------------------- *
# * Code *

# Create a simple matrix with 3 rows and 2 columns.
B <- matrix(c(1,2,3,4,5,6), 3, 2)
print(B)
C <- matrix(c("Rambo", "Chuck Norris", "Arnold", "Steven Seagal", "John Wayne", "Steve McQueen"),2,3)
print(C)

# * ------------------------- *
# * Log or Results *

#Output
#     [,1] [,2]
#[1,]    1    4
#[2,]    2    5
#[3,]    3    6
#     [,1]           [,2]            [,3]
#[1,] "Rambo"        "Arnold"        "John Wayne"
#[2,] "Chuck Norris" "Steven Seagal" "Steve McQueen"

#------------------------------------------------------------------

#5: Getting A Matrix Element
#Just like with vectors, it's useful to be able to get values out of a matrix to do computations on.
#Because a matrix is two-dimensional, we need two numbers to index it and get elements out.
#The first number is the row that we want to get, and the second number is the column within the row that we want.

#We can index a matrix C and get the value in the first column of the first row with C[1,1]. The first number is the row number, followed by a comma, then the column number.

#C[2,3] will get the third column of the second row.

#Instructions
#Retrieve the element in the second column and second row of C and assign it to c22.
#Retrieve the element in the third column and the first row of C and assign the value to c13.

# * ------------------------- *
# * Code *

# Print the first column of the second row.
print(C[2,1])

# Print the third column of the second row.
print(C[2,3])

c22 <- C[2,2]
c13 <- C[1,3]
print(c22)
print(c13)

# * ------------------------- *
# * Log or Results *

#Output
#[1] "Chuck Norris"
#[1] "Steve McQueen"
#[1] "Steven Seagal"
#[1] "John Wayne"

#------------------------------------------------------------------

#6: Getting Rows And Columns
#Sometimes, we want a whole row or a whole column from a matrix, not just a single element (a whole row or column would be a vector).
#When we want to do this, we can leave off a column or row number.

#For example, C[1,] will get the whole first row of the matrix C, and C[,1] will get the whole first column of the matrix.

#Instructions
#Assign the second row of C to c20.
#Assign the third column of C to c03.

# * ------------------------- *
# * Code *

# The first row of C.
print(C[1,])

# The first column of C.
print(C[,1])

c20 <- C[2,]
c03 <- C[,3]
print(c20)
print(c03)

# * ------------------------- *
# * Log or Results *

#Output
#[1] "Rambo"      "Arnold"     "John Wayne"
#[1] "Rambo"        "Chuck Norris"
#[1] "Chuck Norris"  "Steven Seagal" "Steve McQueen"
#[1] "John Wayne"    "Steve McQueen"

#------------------------------------------------------------------

#7: Data Frames
#One problem with matrices that makes it hard to represent our White House data as a matrix is the fact that in R, matrix elements have to all have the same data type.
#Remember how we couldn't make a vector like c(1,"hello",5)? R will automatically convert 1 and 5 in that vector to character types, because we can't mix numeric and character types in one vector.

#A matrix is much the same -- all the values in a matrix can only be of one type.

#Our white house data looks like this:


#Name   Status Salary Pay.Basis
#           Abdullah, Hasan A. Detailee 105960 Per Annum
#            Abraham, Sabey M. Employee  55000 Per Annum
#         Abraham, Yohannes A. Employee 121200 Per Annum
#           Abramson, Jerry E. Employee 155035 Per Annum
#Of these, the Name, Status, and Pay.Basis columns are all character types.
#But the Salary column is a numeric type. We could read Salary in as a character, but if we want to, for example, add up all of the salaries, it won't be possible, because you can't add up character types.
#This makes sense -- you can't add hello and bye and expect a reasonable result -- addition is a mathematical operation, after all.

#We'll need the Salary column to be numeric. Luckily, R has a type called a data frame.
#Conceptually, a data frame is very similar to a matrix -- it holds two dimensions of data. However, the critical advantage of a data frame is that each column of a data frame can be a different type.
#A data frame will allow us to make Name, Status, and Pay.Basis into character types, and Salary a numeric type.

#When you're working with datasets, a data frame is the most common data type you'll be using.

#------------------------------------------------------------------

#8: Data Frame Columns
#When you read in a data file using read.csv, it's by default read in as a data frame.
#This means that our whiteHouse data from earlier is a data frame. read.csv will automatically figure out the right type to assign to each column -- in our case, Salary is numeric already.

#Data frames have a few other advantages over matrices. One is that header rows are automatically detected and used as column names.
#Another is that you can get a column by name instead of using the number.

#whiteHouse[1,"Salary"] will get the salary of the first employee in our data.

#whiteHouse["Salary"] will get the whole "Salary" column from our data frame.

#Instructions
#Assign the "Name" column of whiteHouse to whiteHouseNames.
#Assign the Status column of the fifth row to status5.

# * ------------------------- *
# * Code *

# Get the salary column from the whitehouse data
salary <- whiteHouse["Salary"]

# Get the salary of the first employee in our data (salary column of the first row)
firstSalary <- whiteHouse[1,"Salary"]

whiteHouseNames <- whiteHouse["Name"]
status5 <- whiteHouse[5,"Status"]

print(whiteHouseNames)
print(status5)

# * ------------------------- *
# * Log or Results *

#Output
#                         Name
#1          Abdullah, Hasan A.
#2           Abraham, Sabey M.
#3        Abraham, Yohannes A.
#4          Abramson, Jerry E.
#5          Adler, Caroline E.
#6            Aiyer, Vikrum D.
#...
#[1] Employee
#Levels: Detailee Employee

#------------------------------------------------------------------

#9: Finding Average Salary
#Now that we understand data frames better, we can calculate the average salary of all White House employees.
#To do this, we just have to find the sum of all the salaries, and divide by the number of employees.

#We can use the nrow function to find the number of White House employees.
#This function will find the number of rows in a matrix or data frame.

#We can use the sum function to add all the elements in a numeric vector or matrix.

#Instructions
#Calculate the average salary by:
#Using the sum function to find the sum of all the values in the Salary column of whiteHouse.
#Use the nrow function to find the number of White House employees.
#Divide the sum of the salaries by the number of employees.
#Assign the result to averageSalary.

# * ------------------------- *
# * Code *

# Enter your code here.
salarysum <- sum(whiteHouse["Salary"])
nbrow <- nrow(whiteHouse["Salary"])
averageSalary <- salarysum / nbrow
print(averageSalary)

# * ------------------------- *
# * Log or Results *

#Output
#[1] 84864.12

#------------------------------------------------------------------

#10: Finding The Highest/Lowest Salary
#We can find the highest value in a numeric vector or matrix using the max function.
#We can find the lowest value using the min function.

#Instructions
#Find the highest salary in the Salary column and assign the result to highestSalary.
#Find the lowest salary in the Salary column and assign the result to lowestSalary.

# * ------------------------- *
# * Code *

# Enter your code here.
highestSalary <- max(whiteHouse["Salary"])
lowestSalary <- min(whiteHouse["Salary"])
print("highestSalary :")
print(highestSalary)
print("lowestSalary :")
print(lowestSalary)

# * ------------------------- *
# * Log or Results *

#Output
#[1] "highestSalary :"
#[1] 173922
#[1] "lowestSalary :"
#[1] 0

#------------------------------------------------------------------

#11: Subtle Differences
#You may have noticed that there are two ways to get a column -- you can use whiteHouse["Salary"], or whiteHouse[,"Salary"].
#Both of these will get the column, but they will do it in different ways.
#It's critical to know exactly what's happening, or you could end up with code that doesn't work properly.

#whiteHouse["Salary"] will return a data frame object.
#It will take just one column of the existing data frame, and create a new data frame with only that column.
#You could even type whiteHouse["Salary"]["Salary"] (or add ["Salary"] as many times as you want), and keep getting the same data frame, with just one column.

#whiteHouse[,"Salary"] will return a vector, with only the data in the Salary column.
#This is because using matrix indexing on a dataframe (two numbers separated by a comma) will always return a vector.

#R has many little things like this to be aware of -- if you want a full explanation of what gets returned with what kind of dataframe indexing, read this.

#It's very important to always use the indexing method that returns what you expect.

#Instructions
#Assign a data frame with only the column Name to whiteHouseNames.
#Assign a vector with all the names in the Name column to whiteHouseNamesVector.

# * ------------------------- *
# * Code *

# Returns a data frame.
salaryFrame <- whiteHouse["Salary"]

# Returns a vector
salaryVector <- whiteHouse[,"Salary"]

whiteHouseNames <- whiteHouse["Name"]
whiteHouseNamesVector <- whiteHouse[,"Name"]

# * ------------------------- *
# * Log or Results *

#------------------------------------------------------------------

#12: Minimum/Maximum Index
#We found the highest and lowest salaries earlier, but what if we wanted to find the names of the people who had those salaries?
#We'd need to find the row with the maximum and minimum salaries, and then find the value of the Name column.

#To do this, we can use the which.min and which.max functions.
#These functions find the index of the lowest and highest values, respectively, in a vector.

#Once we find that index, we can use it to grab the right row from the whiteHouse data frame, and then get the name we want.

#Instructions
#Find the White House employee with the highest salary and assign the result to highestEarner.

# * ------------------------- *
# * Code *

# Find the index of the person with the lowest salary.
# This is where knowing what kind of indexing returns what value comes in handy!  We need a vector.
minimumIndex <- which.min(whiteHouse[,"Salary"])
# Extract the row of the lowest salary.
minimumSalaryRow <- whiteHouse[minimumIndex,]
# Get the name column from that row.
lowestEarner <- minimumSalaryRow["Name"]
# Print the name of the white house employee who earned the least.
print(lowestEarner)

# index with the highest salary
maxsalaryindex <- which.max(whiteHouse[,"Salary"])
print("max salary index")
print(maxsalaryindex)
# row with the highest salary
maxsalaryrow <- whiteHouse[maxsalaryindex,]
print("max salary row")
print(maxsalaryrow)
maxsalary <- maxsalaryrow["Name"]
print("max salary name")
print(maxsalary)

highestEarner <- maxsalary

# * ------------------------- *
# * Log or Results *

#Output
#                   Name
#244 Leary, Kimberlyn R.
#[1] "max salary index"
#[1] 53
#[1] "max salary row"
#                     Name   Status Salary Pay.Basis
#53 Breckenridge, Anita J. Employee 173922 Per Annum
#                                                        Position.Title
#53 ASSISTANT TO THE PRESIDENT AND DEPUTY CHIEF OF STAFF FOR OPERATIONS
#[1] "max salary name"
#                     Name
#53 Breckenridge, Anita J.

#------------------------------------------------------------------
