#Taking a Vacation

"""
Before We Begin

Let's first quickly review functions in Python.

def bigger(first, second):
    print max(first, second)
    return True

In the example above:

    We define a function called bigger that has two arguments called first and second.
    Then, we print out the larger of the two arguments using the built-in function max.
    Finally, the bigger function returns True.

Now try creating a function yourself!
Instructions

Write a function called answer that takes no arguments and returns the value 42.

Even without arguments, you will still need parentheses.

Don't forget the colon at the end of the function definition!
"""

def answer():
    return 42


"""
Planning Your Trip

When planning a vacation, it's very important to know exactly how much you're going to spend.

def wages(hours):
    # If I make $8.35/hour...
    return 8.35 * hours

The above example is just a refresher in how functions are defined.

Let's use functions to calculate your trip's costs.
Instructions

    Define a function called hotel_cost with one argument nights as input.
    The hotel costs $140 per night. So, the function hotel_cost should return 140 * nights.
"""


def hotel_cost(nights):
    return 140 * nights


"""

Getting There

You're going to need to take a plane ride to get to your location.

def fruit_color(fruit):
    if fruit == "apple":
        return "red"
    elif fruit == "banana":
        return "yellow"
    elif fruit == "pear":
        return "green"

    The example above defines the function fruit_color that accepts a string as the argument fruit.
    The function returns a string if it knows the color of that fruit.

Instructions

    Below your existing code, define a function called plane_ride_cost that takes a string, city, as input.
    The function should return a different price depending on the location, similar to the code example above. Below are the valid destinations and their corresponding round-trip prices.

"Charlotte": 183
"Tampa": 220
"Pittsburgh": 222
"Los Angeles": 475
"""

def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if city.lower() == "charlotte":
        return 183
    elif city.lower() == "tampa":
        return 220
    elif city.lower() == "pittsburgh":
        return 222
    elif city.lower() == "los angeles":
        return 475
    else:
        return False


"""

Transportation

You're also going to need a rental car in order for you to get around.

def finish_game(score):
    tickets = 10 * score
    if score >= 10:
        tickets += 50
    elif score >= 7:
        tickets += 20
    return tickets

In the above example, we first give the player 10 tickets for every point that the player scored. Then, we check the value of score multiple times.

    First, we check if score is greater than or equal to 10. If it is, we give the player 50 bonus tickets.
    If score is just greater than or equal to 7, we give the player 20 bonus tickets.
    At the end, we return the total number of tickets earned by the player.

Remember that an elif statement is only checked if all preceding if/elif statements fail.
Instructions

    Below your existing code, define a function called rental_car_cost with an argument called days.
    Calculate the cost of renting the car:
        Every day you rent the car costs $40.
        if you rent the car for 7 or more days, you get $50 off your total.
        Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total.
        You cannot get both of the above discounts.
    Return that cost.

Just like in the example above, this check becomes simpler if you make the 7-day check an if statement and the 3-day check an elif statement.
"""


def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if city.lower() == "charlotte":
        return 183
    elif city.lower() == "tampa":
        return 220
    elif city.lower() == "pittsburgh":
        return 222
    elif city.lower() == "los angeles":
        return 475
    else:
        return False
        
def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    
    return cost


"""
Pull it Together

Great! Now that you've got your 3 main costs figured out, let's put them together in order to find the total cost of your trip.

def double(n):
    return 2 * n
def triple(p):
    return 3 * p

def add(a, b):
    return double(a) + triple(b)

    We define two simple functions, double(n) and triple(p) that return 2 times or 3 times their input. Notice that they have n and p as their arguments.
    We define a third function, add(a, b) that returns the sum of the previous two functions when called with a and b, respectively.

Instructions

    Below your existing code, define a function called trip_cost that takes two arguments, city and days.
    Like the example above, have your function return the sum of calling the rental_car_cost(days), hotel_cost(days), and plane_ride_cost(city) functions.

It is completely valid to call the hotel_cost(nights) function with the variable days. Just like the example above where we call double(n) with the variable a, we pass the value of days to the new function in the argument nights.
"""

def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if city.lower() == "charlotte":
        return 183
    elif city.lower() == "tampa":
        return 220
    elif city.lower() == "pittsburgh":
        return 222
    elif city.lower() == "los angeles":
        return 475
    else:
        return 0
        
def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    
    return cost
    
def trip_cost(city,days):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)


"""

Hey, You Never Know!

You can't expect to only spend money on the plane ride, hotel, and rental car when going on a vacation. There also needs to be room for additional costs like fancy food or souvenirs.
Instructions

    Modify your trip_cost function definition. Add a third argument, spending_money.
    Modify what the trip_cost function does. Add the variable spending_money to the sum that it returns.


"""
def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if city.lower() == "charlotte":
        return 183
    elif city.lower() == "tampa":
        return 220
    elif city.lower() == "pittsburgh":
        return 222
    elif city.lower() == "los angeles":
        return 475
    else:
        return 0
        
def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    
    return cost
    
def trip_cost(city,days,spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money



"""

Plan Your Trip!

Nice work! Now that you have it all together, let's take a trip.

What if we went to Los Angeles for 5 days and brought an extra 600 dollars of spending money?
Instructions

After your previous code, print out the trip_cost( to "Los Angeles" for 5 days with an extra 600 dollars of spending money.

Don't forget the closing ) after passing in the 3 previous values!
"""

def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if city.lower() == "charlotte":
        return 183
    elif city.lower() == "tampa":
        return 220
    elif city.lower() == "pittsburgh":
        return 222
    elif city.lower() == "los angeles":
        return 475
    else:
        return 0
        
def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    
    return cost
    
def trip_cost(city,days,spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    
print trip_cost("Los Angeles",5,600)



