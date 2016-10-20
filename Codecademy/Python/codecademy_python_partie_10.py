# Partie 10 :*
#  Advanced Topics in Python


# Iterators for Dictionaries


"""
Let's start with iterating over a dictionary. Recall that a dictionary is just a collection of keys and values.

d = {
    "Name": "Guido",
    "Age": 56,
    "BDFL": True
}
print d.items()
# => [('BDFL', True), ('Age', 56), ('Name', 'Guido')]

Note that the items() function doesn't return key/value pairs in any specific order. (For more on this, see the Hint.)
"""

my_dict ={"Prenom":"Nico","Age":30,"taille":1.8}
print my_dict.items()
my_dict ={"Prenom":"Nico","Age":30,"taille":1.8}
print my_dict.keys()
print my_dict.values()
# => ['taille', 'Age', 'Prenom']
#    [1.8, 30, 'Nico']



my_dict ={"Prenom":"Nico","Age":30,"taille":1.8}
print my_dict.keys()
print my_dict.values()
for key in my_dict:
    print key, my_dict[key]

# sortie :
"""	
['taille', 'Age', 'Prenom']
[1.8, 30, 'Nico']
taille 1.8
Age 30
Prenom Nico
"""

# Building Lists
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x**2 for x in range(1,11) if (x**2) % 2 == 0]

print even_squares

"""
[4, 16, 36, 64, 100]
"""

cubes_by_four = [x**3 for x in range(1,11) if x**3 % 4 == 0 ]
print cubes_by_four

"""
[8, 64, 216, 512, 1000]
"""

# List Slicing Syntax
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]


"""

Omitting Indices

If you don't pass a particular index to the list slice, Python will pick a default.

to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]
# prints ['D', 'E'] 

print to_five[:2]
# prints ['A', 'B']

print to_five[::2]
# print ['A', 'C', 'E']
"""

my_list = range(1, 11) # List of numbers 1 - 10

# Add your code below!
print my_list[::2]

[1, 3, 5, 7, 9]

#Reversing a List
my_list = range(1, 11)

# Add your code below!
backwards = my_list[::-1]


"""
Create a variable, backwards_by_tens, and set it equal to the result of going backwards through to_one_hundred by tens. 
Go ahead and print backwards_by_tens to the console.
"""
to_one_hundred = range(101)
# Add your code below!
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

to_21 = [x for x in range(1,22)]
#print to_21
odds = to_21[::2]
middle_third = to_21[7:14:1]


# Lambdas
"""

Anonymous Functions

One of the more powerful aspects of Python is that it allows for a style of programming called functional programming, which means that you're allowed to pass functions around just as if they were variables or values. Sometimes we take this for granted, but not all languages allow this!

Check out the code at the right. See the lambda bit? Typing

lambda x: x % 3 == 0

Is the same as

def by_three(x):
    return x % 3 == 0

Only we don't need to actually give the function a name; it does its work and returns a value without one. That's why the function the lambda creates is an anonymous function.

When we pass the lambda to filter, filter uses the lambda to determine what to filter, and the second argument (my_list, which is just the numbers 0 – 15) is the list it does the filtering on.
"""
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

"""[0, 3, 6, 9, 12, 15]
"""
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)

"""['Python']
"""

squares = [x**2 for x in range(1,11)]
print filter(lambda x:  30<=x<=70, squares)

"""[36, 49, 64]"""

movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}
print movies.items()

"""[("Monty Python's Life of Brian", 'Good'), ("Monty Python's Meaning of Life", 'Okay'), ('Monty Python and the Holy Grail', 'Great')]"""

threes_and_fives = [ x for x in range(1,16) if (x % 3 == 0) or (x % 5 == 0)]

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
#print backwards

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda mes : mes != "X",garbled)
print message
"""I am another secret message!"""



# Introduction to Bitwise Operators

# Binary representation

"""
Just a Little BIT

Welcome to an intro level explanation of bitwise operations in Python!

Bitwise operations might seem a little esoteric and tricky at first, but you'll get the hang of them pretty quickly.

Bitwise operations are operations that directly manipulate bits. In all computers, numbers are represented with bits, a series of zeros and ones. In fact, pretty much everything in a computer is represented by bits. This course will introduce you to the basic bitwise operations and then show you what you can do with them.

Bitwise operators often tend to puzzle and mystify new programmers, so don't worry if you are a little bit confused at first. To be honest, you aren't really going to see bitwise operators in your everyday program. However, they do pop up from time to time, and when they do, you should have a general idea of what is going on.
Instructions

In the editor are the 6 basic bitwise operations. Click Save & Submit Code and see what the console prints out. All of them will be explained in due time!

"""

print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT
"""
0
10
0
13
38
-89
"""

"""
Lesson I0: The Base 2 Number System

When we count, we usually do it in base 10. That means that each place in a number can hold one of ten values, 0-9. In binary we count in base two, where each place can hold one of two values: 0 or 1. The counting pattern is the same as in base 10 except when you carry over to a new column, you have to carry over every time a place goes higher than one (as opposed to higher than 9 in base 10).

For example, the numbers one and zero are the same in base 10 and base 2. But in base 2, once you get to the number 2 you have to carry over the one, resulting in the representation "10". Adding one again results in "11" (3) and adding one again results in "100" (4).

Contrary to counting in base 10, where each decimal place represents a power of 10, each place in a binary number represents a power of two (or a bit). The rightmost bit is the 1's bit (two to the zero power), the next bit is the 2's bit (two to the first), then 4, 8, 16, 32, and so on.

The binary number '1010' is 10 in base 2 because the 8's bit and the 2's bit are "on":

8's bit  4's bit  2's bit  1's bit
    1       0       1      0 
    8   +   0    +  2   +  0  = 10 

In Python, you can write numbers in binary format by starting the number with 0b. When doing so, the numbers can be operated on like any other number!
Instructions

Take a look at the examples in the editor. Really try to understand this pattern before moving on. Click Save & Submit Code when you're ready to continue.
"""

print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11

"""
1 2 3 4 5 6 7
******
4
9
"""

one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0B110
seven = 0b111
eight = 0B1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

print bin(1)
for n in range(2,6):
    print bin(n)
	
print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("0b11001001",2)


# Slide to the Left! Slide to the Right!

"""
Slide to the Left! Slide to the Right!

The next two operations we are going to talk about are the left and right shift bitwise operators. These operators work by shifting the bits of a number over by a designated number of slots.

The block below shows how these operators work on the bit level. Note that in the diagram, the shift is always a positive integer:

# Left Bit Shift (<<)  
0b000001 << 2 == 0b000100 (1 << 2 = 4)
0b000101 << 3 == 0b101000 (5 << 3 = 40)       

# Right Bit Shift (>>)
0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
0b0000010 >> 2 == 0b000000 (2 >> 2 = 0) 

This operation is mathematically equivalent to floor dividing and multiplying by 2 (respectively) for every time you shift, but it's often easier just to think of it as shifting all the 1s and 0s left or right by the specified number of slots.

Note that you can only do bitwise operations on an integer. Trying to do them on strings or floats will result in nonsensical output!
Instructions

Shift the variable shift_right to the right twice (>> 2) and shift the variable shift_left to the left twice (<< 2). Try to guess what the printed output will be!
"""

shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right)
print bin(shift_left)
"""
0b11
0b100
"""

"""

A BIT of This AND That

The bitwise AND (&) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if the corresponding bits of both numbers are 1. For example:

     a:   00101010   42
     b:   00001111   15       
===================
 a & b:   00001010   10

As you can see, the 2's bit and the 8's bit are the only bits that are on in both a and b, so a & b only contains those bits. Note that using the & operator can only result in a number that is less than or equal to the smaller of the two values.

So remember, for every given bit in a and b:

0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1

Therefore,

 0b111 (7) & 0b1010 (10) = 0b10

which equals two.
Instructions

print out the result of calling bin() on 0b1110 & 0b101.

See if you can guess what the output will be!
"""

res = 0b1110 & 0b101
print bin(res)
"""
res :
0b100
"""


"""
A BIT of This OR That

The bitwise OR (|) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of either number are 1. For example:

    a:  00101010  42
    b:  00001111  15       
================
a | b:  00101111  47

Note that the bitwise | operator can only create results that are greater than or equal to the larger of the two integer inputs.

So remember, for every given bit in a and b:

0 | 0 = 0
0 | 1 = 1 
1 | 0 = 1
1 | 1 = 1

Meaning

 110 (6) | 1010 (10) = 1110 (14)

Instructions

For practice, print out the result of using | on 0b1110 and 0b101 as a binary string. Try to do it on your own without using the | operator if you can help it.
"""

res = 0b1110 | 0b101
print bin(res)
"""
res :
0b1111
"""

"""
This XOR That?

The XOR (^) or exclusive or operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of the two numbers are 1, but not both.

    a:  00101010   42
    b:  00001111   15       
================
a ^ b:  00100101   37

Keep in mind that if a bit is off in both numbers, it stays off in the result. Note that XOR-ing a number with itself will always result in 0.

So remember, for every given bit in a and b:

0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0

Therefore:

 111 (7) ^ 1010 (10) = 1101 (13)

Instructions

For practice, print the result of using ^ on 0b1110 and 0b101 as a binary string. Try to do it on your own without using the ^ operator.
"""

res = 0b1110 ^ 0b101
print bin(res)
"""res : 0b1011"""


"""
See? This is NOT That Hard!

The bitwise NOT operator (~) just flips all of the bits in a single number. What this actually means to the computer is actually very complicated, so we're not going to get into it. Just know that mathematically, this is equivalent to adding one to the number and then making it negative.

And with that, you've seen all of the basic bitwise operators! We'll see what we can do with these in the next section.
Instructions

Click Save & Submit Code and observe what the console prints out.
"""

print ~1
print ~2
print ~3
print ~42
print ~123

"""
res :
-2
-3
-4
-43
-124
"""


"""
The Man Behind the Bit Mask

A bit mask is just a variable that aids you with bitwise operations. A bit mask can help you turn specific bits on, turn others off, or just collect data from an integer about which bits are on or off.

num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
    print "Bit was on"

In the example above, we want to see if the third bit from the right is on.

    First, we first create a variable num containing the number 12, or 0b1100.
    Next, we create a mask with the third bit on.
    Then, we use a bitwise-and operation to see if the third bit from the right of num is on.
    If desired is greater than zero, then the third bit of num must have been one.

Instructions

    Define a function, check_bit4, with one argument, input, an integer.
    It should check to see if the fourth bit from the right is on.
    If the bit is on, return "on" (not print!)
    If the bit is off, return "off".

Check the Hint for some examples!
"""

def check_bit4(nb):
    mask = 0b1000  #1000 => pour tester le 4eme, 0100 pour tester le 2eme,..
    if mask & nb > 0:
        return "on"
    else:
        return "off"
		
"""
Turn It On

You can also use masks to turn a bit in a number on using |. For example, let's say I want to make sure the rightmost bit of number a is turned on. I could do this:

a = 0b110 # 6
mask = 0b1 # 1
desired =  a | mask # 0b111, or 7

Using the bitwise | operator will turn a corresponding bit on if it is off and leave it on if it is already on.
Instructions

In the editor is a variable, a. Use a bitmask and the value a in order to achieve a result where the third bit from the right of a is turned on. Be sure to print your answer as a bin() string!
"""

a = 0b10111011
res = a | 0b100
print bin(res)
""" sortie : 0b10111111 """


"""

Just Flip Out

Using the XOR (^) operator is very useful for flipping bits. Using ^ on a bit with the number one will return a result where that bit is flipped.

For example, let's say I want to flip all of the bits in a. I might do this:

a = 0b110 # 6
mask = 0b111 # 7
desired =  a ^ mask # 0b1

Instructions

In the editor is the 8 bit variable a. Use a bitmask and the value a in order to achieve a result where all of the bits in a are flipped. Be sure to print your answer as a bin() string!
"""

a = 0b11101110
res = a ^ 0b11111111
print bin(res)
""" res : 0b10001 """

"""

Slip and Slide

Finally, you can also use the left shift (<<) and right shift (>>) operators to slide masks into place.

a = 0b101 
# Tenth bit mask
mask = (0b1 << 9)  # One less than ten 
desired = a ^ mask

Let's say that I want to turn on the 10th bit from the right of the integer a.

Instead of writing out the entire number, we slide a bit over using the << operator.

We use 9 because we only need to slide the mask nine places over from the first bit to reach the tenth bit.
Instructions

    Define a function called flip_bit that takes the inputs (number, n).
    Flip the nth bit (with the ones bit being the first bit) and store it in result.
    Return the result of calling bin(result).

?
Hint

Use the << operator to move your mask into place and the ^ operator to flip your desired bit.
"""



def flip_bit(number,n):
    mask = 0b1 << n-1
    print bin(mask)
    result = number ^ mask
    return bin(result)

flip_bit(0b111,2)
"""
res : 0b10
"""

		