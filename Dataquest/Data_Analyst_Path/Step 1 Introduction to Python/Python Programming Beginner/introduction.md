1: Programming And Data Science
What is data science?

Data science is a new and exciting field, and involves working with data to perform analysis, visualization, make predictions and more. Data science can be used to draw interesting conclusions from business data, find valuable insights from sporting statistics, visualize crimes across a geographic region, predict whether a user will purchase your product and more.

Data Science Map

As data science techniques shifted from academic research to industry, many organizations started to contribute back to the data science ecosystem by building new tools for working with data. Many of these tools have been released as open source software and are free for anyone to work with. Before we can work with these tools, we need to learn the basics of programming, which is what this course is dedicated to.

Why learn programming?

To work with data effectively, you need to learn how to program. Programming is the process of creating structured programs by writing individual lines of code. You can think of code as the blueprint for an application. The web browser you're currently using is an example of a program and the code that powers the application was written by a large team of software engineers.

In this course, we'll focus on the Python programming language, which has become one of the most popular tools for doing data science. Engineers and data scientists use it to do everything from analyzing large datasets to building complex web applications, due to its incredible versatility. At Dataquest, we're strong believers in learning by doing. As you work through our content, you'll work with real data sets and receive immediate feedback.

Variables

Variables are a fundamental building block of most programming languages. We use variables to store values that we want to use later. Creating a variable involves deciding on a name, entering that name, and then assigning a value to that variable. We then can refer to that value using the variable name in our code. For example, if we know we're going to be using the value 365 often, we can store that value in a variable named days.

To assign the value 365 to the variable days, we enter the variable name, add an equals sign (=), and then enter the value you want that variable to store. This is known as an assignment statement:


days = 365
The equals sign (=) is called the assignment operator. because it's used to assign the value on the right to the variable on the left. An operator is a symbol that we use to express mathematical or logical operations between variables or values. In this case, the assignment operator assigns the value to the right of the equals sight to the variable name on the left.

Variable names in Python can't contain any spaces or special characters like * or |. The one special character that is allowed is the underscore (_), and it's recommended use is connecting multiple words in a single variable name:


number_of_days = 365
While you can also use numbers in the variable name, you can't start a variable name with a number. Here's the recommended way of using numbers in your variable names:


num_days_1 = 365
num_days_2 = 366
Lastly, Python contains a set of reserved words that can't be used as variable names like True, False, and is). You can find the full list of reserved words here.

In addition to assigning a value to a new variable, you can also use the assignment operator to assign a new value to an existing variable:


number_of_days = 365
number_of_days = 366
After the last line of code is executed, the variable number_of_days will refer to 366.

The Dataquest Interface

In most steps in a mission, you'll be asked to write code that accomplishes a specific task based on what you just learned. We then run your code, perform answer checking on the results, and give you feedback on your answer. This kind of deliberate practice at the time of learning helps you confirm your understanding and spot any weaknesses before moving on.

There are two ways to write and run code:

the code editor interface
the console interface
We'll focus on the code editor workflow in this step and discuss the console workflow later this mission. In the code editor workflow, you write your code in a single text file (named script.py), run the code to see the results, and receive feedback on your code. You write code in the section titled script.py and run code using the Check button:

DQ Interface Check Button

You can also run code using the relevant keyboard shortcut for your operating system. You can hover over each button to display the keyboard shortcut. For example, the shortcut to run code is Option + Enter on Mac OS X:

DQ Interface Keyboard Shortcuts

The Python interpreter is the program that reads and runs your code line by line. We walk through how to install the interpreter on your own computer in a later course. As you're learning the basics of Python on Dataquest, we'll handle running and displaying the results of code you write.

Once your code is finished running on our server, any variables you created will be displayed in the Variables inspector below the code editor interface along with feedback on your work. In the following screenshot, we receive feedback when we assigned 365 to number_of_days when the exercise actually asked us to assign 366 to number_of_days.

DQ Interface

Now it's your turn! In this step's exercise, we work with the hottest recorded temperatures, in Fahrenheit, for the three most populated countries in the world (China, India, and United States). These values are rounded to the nearest whole number.


