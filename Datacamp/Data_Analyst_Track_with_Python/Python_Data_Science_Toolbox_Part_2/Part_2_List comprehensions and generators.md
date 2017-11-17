05/2017  
Datcamp - Python Data Science Toolbox (Part 2)  

---
 
# Part 2 : List comprehensions and generators 

In this chapter, you'll build on your knowledge of iterators and be introduced to list comprehensions, which allow you to create complicated lists and lists of lists in one line of code! List comprehensions can dramatically simplify your code and make it more efficient, and will become a vital part of your Python Data Science toolbox. You'll then learn about generators, which are extremely helpful when working with large sequences of data that you may not want to store in memory but instead generate on the fly.  

## Write a basic list comprehension

In this exercise, you will practice what you've learned from the video about writing list comprehensions. You will write a list comprehension and identify the output that will be produced.  

The following list has been pre-loaded in the environment.  

doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
How would a list comprehension that produces a list of the first character of each string in doctor look like? Note that the list comprehension uses doc as the iterator variable. What will the output be?  


### Instructions :

Possible Answers

- The list comprehension is [for doc in doctor: doc[0]] and produces the list ['h', 'c', 'c', 't', 'w'].
- The list comprehension is [doc[0] for doc in doctor] and produces the list ['h', 'c', 'c', 't', 'w'].
- The list comprehension is [doc[0] in doctor] and produces the list ['h', 'c', 'c', 't', 'w'].

### Results :  

	3

---

## List comprehension over iterables

You know that list comprehensions can be built over iterables. Given the following objects below, which of these can we build list comprehensions over?  

```python
doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']

range(50)

underwood = 'After all, we are nothing more or less than what we choose to reveal.'

jean = '24601'

flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

valjean = 24601
```


### Instructions :

Possible Answers

-     You can build list comprehensions over all the objects except the string of number characters jean.
-     You can build list comprehensions over all the objects except the string lists doctor and flash.
-     You can build list comprehensions over all the objects except range(50).
-     You can build list comprehensions over all the objects except the integer object valjean.

### Results :  

	4
	In [4]: doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']

	In [5]: underwood = 'After all, we are nothing more or less than what we choose to reveal.'

	In [6]: jean = '24601'

	In [7]: flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

	In [8]: valjean = 24601

	In [9]: listc1 = [item for item in doctor]

	In [10]: listc2 = [item for item in range(50)]

	In [11]: listc1
	Out[11]: ['house', 'cuddy', 'chase', 'thirteen', 'wilson']

	In [12]: listc2
	Out[12]: 
	[0,
	 1,
	 2,
	 3,
	 4,
	 5,
	 6,
	 7,
	 8,
	 9,
	 10,
	 11,
	 12,
	 13,
	 14,
	 15,
	 16,
	 17,
	 18,
	 19,
	 20,
	 21,
	 22,
	 23,
	 24,
	 25,
	 26,
	 27,
	 28,
	 29,
	 30,
	 31,
	 32,
	 33,
	 34,
	 35,
	 36,
	 37,
	 38,
	 39,
	 40,
	 41,
	 42,
	 43,
	 44,
	 45,
	 46,
	 47,
	 48,
	 49]

	In [13]: listc3 = [item for item in underwood]

	In [14]: listc3
	Out[14]: 
	['A',
	 'f',
	 't',
	 'e',
	 'r',
	 ' ',
	 'a',
	 'l',
	 'l',
	 ',',
	 ' ',
	 'w',
	 'e',
	 ' ',
	 'a',
	 'r',
	 'e',
	 ' ',
	 'n',
	 'o',
	 't',
	 'h',
	 'i',
	 'n',
	 'g',
	 ' ',
	 'm',
	 'o',
	 'r',
	 'e',
	 ' ',
	 'o',
	 'r',
	 ' ',
	 'l',
	 'e',
	 's',
	 's',
	 ' ',
	 't',
	 'h',
	 'a',
	 'n',
	 ' ',
	 'w',
	 'h',
	 'a',
	 't',
	 ' ',
	 'w',
	 'e',
	 ' ',
	 'c',
	 'h',
	 'o',
	 'o',
	 's',
	 'e',
	 ' ',
	 't',
	 'o',
	 ' ',
	 'r',
	 'e',
	 'v',
	 'e',
	 'a',
	 'l',
	 '.']

	In [15]: listc4 = [item for item in jean]

	In [16]: listc4
	Out[16]: ['2', '4', '6', '0', '1']

	In [17]: listc5 = [item for item in flash]

	In [18]: listc5
	Out[18]: ['jay garrick', 'barry allen', 'wally west', 'bart allen']

	In [19]: listc6 = [item for item in valjean]
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	    listc6 = [item for item in valjean]
	TypeError: 'int' object is not iterable

---

## Writing list comprehensions

You now have all the knowledge necessary to begin writing list comprehensions! Your job in this exercise is to write a list comprehension that produces a list of the squares of the numbers ranging from 0 to 9.  

### Instructions :

- Using the range of numbers from 0 to 9 as your iterable and i as your iterator variable, write a list comprehension that produces a list of numbers consisting of the squared values of i.  

```python
# Create list comprehension: squares
squares = [i**2 for i in range(0,10)]
print(squares)
```

### Results :  

	<script.py> output:
	    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

---


## Nested list comprehensions

Great! At this point, you have a good grasp of the basic syntax of list comprehensions. Let's push your code-writing skills a little further. In this exercise, you will be writing a list comprehension within another list comprehension, or nested list comprehensions. It sounds a little tricky, but you can do it!  

Let's step aside for a while from strings. One of the ways in which lists can be used are in representing multi-dimension objects such as matrices. Matrices can be represented as a list of lists in Python. For example a 5 x 5 matrix with values 0 to 4 in each row can be written as:  

```python
matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]
```

Your task is to recreate this matrix by using nested listed comprehensions. Recall that you can create one of the rows of the matrix with a single list comprehension. To create the list of lists, you simply have to supply the list comprehension as the output expression of the overall list comprehension:  

[[output expression] for iterator variable in iterable]  

Note that here, the output expression is itself a list comprehension.  


### Instructions :

- In the inner list comprehension - that is, the output expression of the nested list comprehension - create a list of values from 0 to 4 using range(). Use col as the iterator variable.
- In the iterable part of your nested list comprehension, use range() to count 5 rows - that is, create a list of values from 0 to 4. Use row as the iterator variable; note that you won't be needing this to create values in the list of lists.

```python
# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col  in range(5)] for row in range(5)]

# Print the matrix
for row in matrix:
    print(row)
```

### Results :  

	<script.py> output:
	    [0, 1, 2, 3, 4]
	    [0, 1, 2, 3, 4]
	    [0, 1, 2, 3, 4]
	    [0, 1, 2, 3, 4]
	    [0, 1, 2, 3, 4]

---


## Using conditionals in comprehensions (1)

You've been using list comprehensions to build lists of values, sometimes using operations to create these values.  

An interesting mechanism in list comprehensions is that you can also create lists with values that meet only a certain condition. One way of doing this is by using conditionals on iterator variables. In this exercise, you will do exactly that!  

Recall from the video that you can apply a conditional statement to test the iterator variable by adding an if statement in the optional predicate expression part after the for statement in the comprehension:  

[ output expression for iterator variable in iterable if predicate expression ].  

You will use this recipe to write a list comprehension for this exercise. You are given a list of strings fellowship and, using a list comprehension, you will create a list that only includes the members of fellowship that have 7 characters or more.  


### Instructions :

- Use member as the iterator variable in the list comprehension. For the conditional, use len() to evaluate the iterator variable. Note that you only want strings with 7 characters or more.  

```python
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member)>=7 ]

# Print the new list
print(new_fellowship)
```

### Results :  

	<script.py> output:
	    ['samwise', 'aragorn', 'legolas', 'boromir']
    
---

## Using conditionals in comprehensions (2)

In the previous exercise, you used an if conditional statement in the predicate expression part of a list comprehension to evaluate an iterator variable. In this exercise, you will use an if-else statement on the output expression of the list.   

You will work on the same list, fellowship and, using a list comprehension and an if-else conditional statement in the output expression, create a list that keeps members of fellowship with 7 or more characters and replaces others with an empty string. Use member as the iterator variable in the list comprehension.  

### Instructions :

- In the output expression, keep the string as-is if the number of characters is >= 7, else replace it with an empty string - that is, '' or "".

```python
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) >= 7 else "" for member in fellowship]

# Print the new list
print(new_fellowship)
```

### Results :  

	<script.py> output:
	    ['', 'samwise', '', 'aragorn', 'legolas', 'boromir', '']

---

## Dict comprehensions

Comprehensions aren't relegated merely to the world of lists. There are many other objects you can build using comprehensions, such as dictionaries, pervasive objects in Data Science. You will create a dictionary using the comprehension syntax for this exercise. In this case, the comprehension is called a dict comprehension.  

Recall that the main difference between a list comprehension and a dict comprehension is the use of curly braces {} instead of []. Additionally, members of the dictionary are created using a colon :, as in key:value.  

You are given a list of strings fellowship and, using a dict comprehension, create a dictionary with the members of the list as the keys and the length of each string as the corresponding values.  

### Instructions :

- Create a dict comprehension where the key is a string in fellowship and the value is the length of the string. Remember to use the syntax key:value in the output expression part of the comprehension to create the members of the dictionary. Use member as the iterator variable.

```python
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = { member: len(member) for member in fellowship }

# Print the new list
print(new_fellowship)
```

### Results :  

	<script.py> output:
	    {'legolas': 7, 'merry': 5, 'aragorn': 7, 'samwise': 7, 'gimli': 5, 'frodo': 5, 'boromir': 7}

---


## List comprehensions vs generators

You've seen from the videos that list comprehensions and generator expressions look very similar in their syntax, except for the use of parentheses () in generator expressions and brackets [] in list comprehensions.  

In this exercise, you will recall the difference between list comprehensions and generators. To help with that task, the following code has been pre-loaded in the environment:  

```python
# List of strings
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# List comprehension
fellow1 = [member for member in fellowship if len(member) >= 7]

# Generator expression
fellow2 = (member for member in fellowship if len(member) >= 7)
```
Try to play around with fellow1 and fellow2 by figuring out their types and printing out their values. Based on your observations and what you can recall from the video, select from the options below the best description for the difference between list comprehensions and generators.  


### Instructions :

Possible Answers

- List comprehensions and generators are not different at all; they are just different ways of writing the same thing.
- A list comprehension produces a list as output, a generator produces a generator object.
- A list comprehension produces a list as output that can be iterated over, a generator produces a generator object that can't be iterated over.

### Results :  

	2

---

## Write your own generator expressions

You are familiar with what generators and generator expressions are, as well as its difference from list comprehensions. In this exercise, you will practice building generator expressions on your own.  

Recall that generator expressions basically have the same syntax as list comprehensions, except that it uses parentheses () instead of brackets []; this should make things feel familiar! Furthermore, if you have ever iterated over a dictionary with .items(), or used the range() function, for example, you have already encountered and used generators before, without knowing it! When you use these functions, Python creates generators for you behind the scenes.  

Now, you will start simple by creating a generator object that produces numeric values.  

### Instructions :

- Create a generator object that will produce values from 0 to 30. Assign the result to result and use num as the iterator variable in the generator expression.
- Print the first 5 values by using next() appropriately in print().
- Print the rest of the values by using a for loop to iterate over the generator object.

```python
# Create generator object: result
result = (num for num in range(31))

# Print the first 5 values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# Print the rest of the values
for value in result:
    print(value)
```

### Results :  


---

## Changing the output in generator expressions

Great! At this point, you already know how to write a basic generator expression. In this exercise, you will push this idea a little further by adding to the output expression of a generator expression. Because generator expressions and list comprehensions are so alike in syntax, this should be a familiar task for you!  

You are given a list of strings lannister and, using a generator expression, create a generator object that you will iterate over to print its values.  

### Instructions :

- Write a generator expression that will generate the lengths of each string in lannister. Use person as the iterator variable. Assign the result to lengths.
- Supply the correct iterable in the for loop for printing the values in the generator object.

```python
# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = (len(person) for person in lannister)

# Iterate over and print the values in lengths
for value in lengths:
    print(value)
```

### Results :  

	<script.py> output:
	    6
	    5
	    5
	    6
	    7

---

## Build a generator

In previous exercises, you've dealt mainly with writing generator expressions, which uses comprehension syntax. Being able to use comprehension syntax for generator expressions made your work so much easier!  

Now, recall from the video that not only are there generator expressions, there are generator functions as well. Generator functions are functions that, like generator expressions, yield a series of values, instead of returning a single value. A generator function is defined as you do a regular function, but whenever it generates a value, it uses the keyword yield instead of return.  

In this exercise, you will create a generator function with a similar mechanism as the generator expression you defined in the previous exercise:  

```python
lengths = (len(person) for person in lannister)
```

### Instructions :

- Complete the function header for the function get_lengths() that has a single parameter, input_list.
- In the for loop in the function definition, yield the length of the strings in input_list.
- Complete the iterable part of the for loop for printing the values generated by the get_lengths() generator function. Supply the call to get_lengths(), passing in the list lannister.

```python
# Create a list of strings
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)

# Print the values generated by get_lengths()
for value in get_lengths(lannister):
    print(value)
```

### Results :  

	<script.py> output:
	    6
	    5
	    5
	    6
	    7

---


## List comprehensions for time-stamped data

You will now make use of what you've learned from this chapter to solve a simple data extraction problem. You will also be introduced to a data structure, the pandas Series, in this exercise. We won't elaborate on it much here, but what you should know is that it is a data structure that you will be working with a lot of times when analyzing data from pandas DataFrames. You can think of DataFrame columns as single-dimension arrays called Series.  

In this exercise, you will be using a list comprehension to extract the time from time-stamped Twitter data. The pandas package has been imported as pd and the file 'tweets.csv' has been imported as the df DataFrame for your use.  

### Instructions :

- Extract the column 'created_at' from df and assign the result to tweet_time. Fun fact: the extracted column in tweet_time here is a Series data structure!
- Create a list comprehension that extracts the time from each row in tweet_time. Each row is a string that represents a timestamp, and you will access the 12th to 18th characters in the string to extract the time. Use entry as the iterator variable and assign the result to tweet_clock_time. Remember that Python uses 0-based indexing!

```python
# Extract the created_at column from df: tweet_time
tweet_time = df.created_at

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time]

# Print the extracted times
print(tweet_clock_time)
```

### Results :  

	<script.py> output:
	    ['23:40:17', '23:40:17', '23:40:17', '23:40:17', '23:40:17', '23:40:17', '23:40:18', '23:40:17', '23:40:18', '23:40:18', '23:40:18', '23:40:17', '23:40:18', '23:40:18', '23:40:17', '23:40:18', '23:40:18', '23:40:17', '23:40:18', '23:40:17', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:17', '23:40:18', '23:40:18', '23:40:17', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:18', '23:40:19', '23:40:18', '23:40:18', '23:40:18', '23:40:19', '23:40:19', '23:40:19', '23:40:18', '23:40:19', '23:40:19', '23:40:19', '23:40:18', '23:40:19', '23:40:19', '23:40:19', '23:40:18', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19']

---

## Conditional list comprehesions for time-stamped data

Great, you've successfully extracted the data of interest, the time, from a pandas DataFrame! Let's tweak your work further by adding a conditional that further specifies which entries to select.  

In this exercise, you will be using a list comprehension to extract the time from time-stamped Twitter data. You will add a conditional expression to the list comprehension so that you only select the times in which entry[17:19] is equal to '19'. The pandas package has been imported as pd and the file 'tweets.csv' has been imported as the df DataFrame for your use.  

### Instructions :


- Extract the column 'created_at' from df and assign the result to tweet_time.
- Create a list comprehension that extracts the time from each row in tweet_time. Each row is a string that represents a timestamp, and you will access the 11th to 18th characters in the string to extract the time. Use entry as the iterator variable and assign the result to tweet_clock_time. Additionally, add a conditional expression that checks whether entry[17:19] is equal to '19'.


```python
# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

# Print the extracted times
print(tweet_clock_time)
```

### Results :  

	<script.py> output:
	    ['23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19']
