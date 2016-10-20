# Classes

"""
Class basics
Classes can be very useful for storing complicated objects with their own methods and variables. Defining a class is much like defining a function, but we use the class keyword instead. We also use the word object in parentheses because we want our classes to inherit the object class. This means that our class has all the properties of an object, which is the simplest, most basic class. Later we'll see that classes can inherit other, more complicated classes. An empty class would look like this:

class ClassName(object):
    # class statements go here
Instructions
Define a new class named "Car". For now, since we have to put something inside the class, use the pass keyword.
"""

class Car(object):
    pass
	

"""
Create an instance of a class
We can use classes to create new objects, which we say are instances of those classes.

Creating a new instance of a class is as easy as saying:

newObject = ClassName()
Instructions
Below your Car class, create a new object named my_car that is an instance of Car.
"""

class Car(object):
    pass

my_car = Car()

"""
Class member variables
Classes can have member variables that store information about each class object. We call them member variables since they are information that belongs to the class object.

Creating member variables and assigning them initial values is as easy as creating any other variable:

class ClassName(object):
    memberVariable = "initialValue"
Instructions
Inside your Car class, replace the pass statement with a new member variable named condition and give it an initial value of the string "new".
"""

class Car(object):
    condition = "new"

my_car = Car()

"""
calling class member variables
Each class object we create has its own set of member variables. Since we've created an object my_car that is an instance of the Car class, my_car should already have a member variable named condition. This attribute gets assigned a value as soon as my_car is created.

Instructions
At the end of your code, use a print statement to display the condition of my_car.
"""

class Car(object):
    condition = "new"

my_car = Car()
print my_car.condition

"""
Initializing a class
There is a special function named __init__() that gets called whenever we create a new instance of a class. It exists by default, even though we don't see it. However, we can define our own __init__() function inside the class, overwriting the default version. We might want to do this in order to provide more input variables, just like we would with any other function.

The first argument passed to __init__() must always be the keyword self - this is how the object keeps track of itself internally - but we can pass additional variables after that.

In order to assign a variable to the class (creating a member variable), we use dot notation. For instance, if we passed newVariable into our class, inside the __init__() function we would say:

self.new_variable = new_variable
Instructions
Define the __init__() function of the Car class to take four inputs: self, model, color, and mpg. Assign the last three inputs to member variables of the same name by using the self keyword.

Then, modify the object my_car to provide the following inputs at initialization:

model = "DeLorean"
color = "silver"
mpg = 88
You don't need to include the self keyword when you create an instance of a class, because self gets added to the beginning of your list of inputs automatically by the class definition.
"""

class Car(object):
    condition = "new"
    
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

my_car = Car("DeLorean","silver",88)
print my_car.condition

# sortie :
"""new"""

"""
Referring to member variables
Calling class member variables works the same whether those values are created within the class (like our car's condition) or values are passed into the new object at initialization. We use dot notation to access the member variables of classes since those variables belong to the object.

For instance, if we had created a member variable named new_variable, a new instance of the class named new_object could access this variable by saying:

new_object.new_variable
Instructions
Now that you've created my_car print its member variables:

First print the model of my_car. Click "Stuck? Get a hint!" for an example.
Then print out the color of my_car.
Then print out the mpg of my_car.
"""

class Car(object):
    condition = "new"
    
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

my_car = Car("DeLorean","silver",88)
print my_car.condition
print my_car.model
print my_car.color
print my_car.mpg

#sortie :
"""
new
DeLorean
silver
88
"""


"""
Creating class methods
Besides member variables, classes can also have their own methods. For example:

class Square(object):
  def __init__(self, side):
    self.side = side

  def perimeter(self):
    return self.side * 4
The perimeter() class method is identical to defining any other function, except that it is written inside of the Square class definition.

Just like when we defined __init__(), you need to provide self as the first argument of any class method.

Instructions
Inside the Car class, add a method named display_car() to Car that will reference the Car's member variables to return the string, "This is a [color] [model] with [mpg] MPG." You can use the str() function to turn your mpg into a string when creating the display string.
Replace the individual print statements with a single print command that displays the result of calling my_car.display_car()
"""
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    
    def display_car(self):
        print "This is a %s %s with %s MPG." %(self.color, self.model, self.mpg)

my_car = Car("DeLorean", "silver", 88)
print my_car.display_car()

#sortie :
"""
This is a silver DeLorean with 88 MPG.
"""


"""
Modifying member variables
We can modify variables that belong to a class the same way that we initialize those member variables. This can be useful when we want to change the value a variable takes on based on something that happens inside of a class method.

Instructions
Inside the Car class, add a method drive_car() that sets self.condition to the string "used".
Remove the call to my_car.display_car() and instead print only the condition of your car.
Then drive your car by calling the drive_car() method.
Finally, print the condition of your car again to see how its value changes.
"""
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    
    def display_car(self):
        print "This is a %s %s with %s MPG." %(self.color, self.model, self.mpg)
    
    def drive_car(self):
        self.condition = "used"

my_car = Car("DeLorean", "silver", 88)
print my_car.condition
my_car.drive_car()
print my_car.condition
"""
sortie :
new
used
"""

"""
Inheritance
One of the benefits of classes is that we can create more complicated classes that inherit variables or methods from their parent classes. This saves us time and helps us build more complicated objects, since these child classes can also include additional variables or methods.

We define a "child" class that inherits all of the variables and functions from its "parent" class like so:

class ChildClass(ParentClass):
    # new variables and functions go here
Normally we use object as the parent class because it is the most basic type of class, but by specifying a different class, we can inherit more complicated functionality.

Instructions
Create a class ElectricCar that inherits from Car. Give your new class an __init__() method of that includes a "battery_type" member variable in addition to the model, color and mpg.

Then, create an electric car named "my_car" with a "molten salt" battery_type. Supply values of your choice for the other three inputs (model, color and mpg).
"""
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    
    def display_car(self):
        print "This is a %s %s with %s MPG." %(self.color, self.model, self.mpg)
    
    def drive_car(self):
        self.condition = "used"

my_car = Car("DeLorean", "silver", 88)
print my_car.condition
my_car.drive_car()
print my_car.condition

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg   = mpg
        self.battery_type = battery_type
        
my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
"""
sortie :
new
used
"""

"""
Overriding methods
Since our ElectricCar is a more specialized type of Car, we can give the ElectricCar its own drive_car() method that has different functionality than the original Car class's.

Instructions
Inside ElectricCar add a new method drive_car() that changes the car's condition to the string "like new".
Then, outside of ElectricCar, print the condition of my_car
Next, drive my_car by calling the drive_car() function
Finally, print the condition of my_car again
"""
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    
    def display_car(self):
        print "This is a %s %s with %s MPG." %(self.color, self.model, self.mpg)
    
    def drive_car(self):
        self.condition = "used"

my_car = Car("DeLorean", "silver", 88)
print my_car.condition
my_car.drive_car()
print my_car.condition

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg   = mpg
        self.battery_type = battery_type
    
    def drive_car(self):
        self.condition = "like new"
        
my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
print my_car.condition
my_car.drive_car()
print my_car.condition

"""
sortie:
new
used
new
like new
"""


"""
Building useful classes
Chances are, you won't be designing Car classes in the real world anytime soon. Usually, classes are most useful for holding and accessing abstract collections of data.

One useful class method to override is the built-in __repr__() method, which is short for representation; by providing a return value in this method, we can tell Python how to represent an object of our class (for instance, when using a print statement).

Instructions
Define a Point3D class that inherits from object
Inside the Point3D class, define an __init__() function that accepts self, x, y, and z, and assigns these numbers to the member variables self.x, self.y, self.z
Define a __repr__() method that returns "(%d, %d, %d)" % (self.x, self.y, self.z). This tells Python to represent this object in the following format: (x, y, z).
Outside the class definition, create a variable named my_point containing a new instance of Point3D with x=1, y=2, and z=3.
Finally, print my_point.
"""

class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)
        
my_point = Point3D(1,2,3)
print my_point

"""
sortie :
(1, 2, 3)
"""