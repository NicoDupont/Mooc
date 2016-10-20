# Partie 3:
# Conditionals & Control Flow  // Boolean Operators  and if

def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()


"""
Compare Closely!

Let's start with the simplest aspect of control flow: comparators. There are six:

    Equal to (==)
    Not equal to (!=)
    Less than (<)
    Less than or equal to (<=)
    Greater than (>)
    Greater than or equal to (>=)

Comparators check if a value is (or is not) equal to, greater than (or equal to), or less than (or equal to) another value.

Note that == compares whether two things are equal, and = assigns a value to a variable.
"""

"""Set each variable to True or False depending on what you think the result will be. For example, 1 < 2 will be True, because one is less than two.

    Set bool_one equal to the result of 17 < 328
    Set bool_two equal to the result of 100 == (2 * 50)
    Set bool_three equal to the result of 19 <= 19
    Set bool_four equal to the result of -22 >= -18
    Set bool_five equal to the result of 99 != (98 + 1)
"""


# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = False

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = False



"""
Let's run through the comparators again with more complex expressions. Set each variable to True or False depending on what you think the result will be.

    Set bool_one to the result of (20 - 10) > 15
    Set bool_two to the result of (10 + 17) == 3**16
    Set bool_three to the result of 1**2 <= -1
    Set bool_four to the result of 40 * 4 >= -4
    Set bool_five to the result of 100 != 10**2
"""

# Assign True or False as appropriate on the lines below!

# (20 - 10) > 15
bool_one = False    # We did this one for you!

# (10 + 17) == 3**16
# Remember that ** can be read as 'to the power of'. 3**16 is about 43 million.
bool_two = False

# 1**2 <= -1
bool_three = False

# 40 * 4 >= -4
bool_four = True

# 100 != 10**2
bool_five = False


# Create comparative statements as appropriate on the lines below!

# Make me true!
bool_one = 3 < 5  # We already did this one for you!

# Make me false!
bool_two = 3 == 5

# Make me true!
bool_three = 4 != 5

# Make me false!
bool_four = 6 > 7

# Make me true!
bool_five = 4 < 5



#algebre de bool
"""
Boolean Operators
------------------------      True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True
"""
"""
Let's practice with and. Assign each variable to the appropriate boolean value.

    Set bool_one equal to the result of False and False
    Set bool_two equal to the result of -(-(-(-2))) == -2 and 4 >= 16**0.5
    Set bool_three equal to the result of 19 % 4 != 300 / 10 / 10 and False
    Set bool_four equal to the result of -(1**2) < 2**0 and 10 % 10 <= 20 - 10 * 2
    Set bool_five equal to the result of True and True
"""
# AND
bool_one = 1 > 2 and 1 == 2
bool_two = False and True
bool_three = False and 1 == 2
bool_four = True and True
bool_five = 1 == 1 and 2 != 1

"""
Time to practice with or!

    Set bool_one equal to the result of 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'
    Set bool_two equal to the result of True or False
    Set bool_three equal to the result of 100**0.5 >= 50 or False
    Set bool_four equal to the result of True or True
    Set bool_five equal to the result of 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1
"""
# OR
bool_one = True or False
bool_two = 1 == 1 or 1 > 2
bool_three = False or 1 != 1
bool_four = 1 == 1 or 2 == 2
bool_five = False or False

"""
Not

The boolean operator not returns True for false statements and False for true statements.

For example:

    not False will evaluate to True, while not 41 > 40 will return False.

Instructions

Let's get some practice with not.

    Set bool_one equal to the result of not True
    Set bool_two equal to the result of not 3**4 < 4**3
    Set bool_three equal to the result of not 10 % 3 <= 10 % 2
    Set bool_four equal to the result of not 3**2 + 4**2 != 5**2
    Set bool_five equal to the result of not not False
"""

bool_one = 1 > 2
bool_two = True
bool_three = True
bool_four = True
bool_five = 1 > 2

"""
This and That (or This, But Not That!)

Boolean operators aren't just evaluated from left to right. Just like with arithmetic operators, there's an order of operations for boolean operators:

    not is evaluated first;
    and is evaluated next;
    or is evaluated last.

For example, True or not False and False returns True. If this isn't clear, look at the Hint.

Parentheses () ensure your expressions are evaluated in the order you want. Anything in parentheses is evaluated as its own unit.
Instructions

Assign True or False as appropriate for bool_one through bool_five.

    Set bool_one equal to the result of False or not True and True
    Set bool_two equal to the result of False and not True or True
    Set bool_three equal to the result of True and not (False or False)
    Set bool_four equal to the result of not not True or False and not True
    Set bool_five equal to the result of False or not (True and True)

"""

bool_one = False
bool_two = True
bool_three = True
bool_four = True
bool_five = False


"""
Mix 'n' Match

Great work! We're almost done with boolean operators.

# Make me false
bool_one = (2 <= 2) and "Alpha" == "Bravo"

Instructions

This time we'll give the expected result, and you'll use some combination of boolean operators to achieve that result.

Remember, the boolean operators are and, or, and not. Use each one at least once!
"""

# Use boolean expressions as appropriate on the lines below!
# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!
# Make me true!
bool_two = 2 <= 2 or not 2 == 2
# Make me false!
bool_three = 2 <= 2 and 2 < 1
# Make me true!
bool_four = not 1 != 1 or not 1 == 1
# Make me true!
bool_five = 1 == 1 and 2 == 2


#partie IF
# Conditional Statement Syntax 

response = "Y" 

answer = "Left"
if answer == "Left":
    print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    
# Will the above print statement print to the console?
# Set response to 'Y' if you think so, and 'N' if you think not.

def using_control_once():
    if 1 < 2:
        return "Success #1"

def using_control_again():
    if 2 == 2:
        return "Success #2"

print using_control_once()
print using_control_again()

answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return False       # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return False       # Make sure this returns False
		
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)


# Make sure that the_flying_circus() returns True
def the_flying_circus():
    if 3 > 2 and 3 > 1:    # Start coding here!
        return True
    elif 3 < 2:
        return False
    else:
        return False
