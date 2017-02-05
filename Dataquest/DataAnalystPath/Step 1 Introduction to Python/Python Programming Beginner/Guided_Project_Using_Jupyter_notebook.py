""" 01/2017
Dataquest : Data Analyst Path
Step 1: Introduction To Python
SubStep : Python Programming: Beginner : Guided Project: Using Jupyter notebook
"""


"""
"""


"""
1: How Guided Projects Work
So far in this course, you've been learning the basics of programming in the Python language through missions. Missions contain instructional content, a console, and a text editor to learn and practice concepts. Missions are highly structured and your work is answer checked every step of the way.

Guided projects, on the other hand, are less structured and focus more on exploration. Guided projects help you synthesize concepts learned during the Dataquest missions and start building a portfolio. Guided projects bridge the gap between learning using the Dataquest missions, and applying the knowledge on your own computer.

In this guided project, we'll walk through how to work in the Jupyter environment. Jupyter is a widely used data science environment that combines a rich text editor with a console. The Jupyter project was originally called IPython, and focused on supporting just the Python language. Over time, support for other languages like R and Julia were added and the project was renamed to Jupyter.

Jupyter notebook is built around a typical data analysis workflow and it's very different from a standard integrated development environment, such as Pycharm, which focus more on just working with code. In Jupyter, you work with notebooks, which mix plain text, code, and code outputs in one view. Here's what a notebook looks like:

Jupyter Notebook Preview

As you can see, notebooks allow you to interleave code and text explanations, enabling you to easily explore data, create visualizations, and share your results. Jupyter is widely used in data science, scientific research, and other applications where it's important to be able to explain the methodology. Here are some of the organizations that use Jupyter:

Jupyter Used In Organizations

Instructions
For now, just hit Next to get started with the project!


"""




"""
2: Displaying Output
Just like in the console, running code that assigns a value to a variable doesn't display any output. If your code generates output, using print statements, it will show up below the output below:

Jupyter Print Output

Instead of using a print statement, you can also add a line to the end of a cell that just refers to the variable name and it will be displayed. In the following screenshot, we read in a CSV file and display the resulting string by referring to the string variable in the last line:

Jupyter Notebook One Cell

When displaying a string value, the print statement acknowledges the new-line delimiter and separates each line in the string while Jupyter doesn't. Each display option has it's own use case and it helps to know when to use which.

You can also run code by pressing Shift + Enter, or the Shift key and the Enter key at the same time. If this cell was the last one in the notebook, a new cell will be created below it and the cursor will advance to that cell. This allows you to rapidly write a short segment of code in one cell, see the output, write more code in the next cell, and so on, all without leaving the keyboard.

Instructions
Display the string object containing the contents of the file and scroll to look at all of the contents.
See if you can figure out how to expand the output cell to display the full contents.
Using only the keyboard:
In a new code cell, split the string on the new-line character ("\n") and display the resulting list.
In a new new code cell, write a for loop that iterates through the list of strings, splits each string on the comma delimiter, and displays the line using a print statement.


"""

""" results or consol output

"""




"""
3: Execution order

When you create a notebook, you can specify the type of kernel that you want to use. The kernel defines the programming language that the code in the notebook will be written in. If you look in the top right of the notebook, you'll see that the kernel in this notebook is a Python 3 kernel.

When you create a new Jupyter notebook or open an existing notebook, a new kernel session is created (unless one is already running). Think of this session as a blank slate -- no variables have been defined, and no modules have been imported. When you run code, it's executed inside the kernel session. Any variables defined in the code are created inside the session. Because the kernel session is shared across the cells, you can access functions and variables you've defined in this session in other cells.

The order in which you execute cells is very important. Take a look at this diagram:
ExampleNotebookCodecellsKernelsessionvariablesa=10a=101b=10b=10c=a*10a=102b=10c=100b=5a=53a=5b=5d=a*bc=100d=25

If we tried to run cell 2 without having first run cell 1, we'd get an error, because a and b wouldn't be defined. We could run cell 3 without first having run cells 1 and 2, though, because it doesn't depend on any variables to be stored in the session.

We could execute the above cells in the order 1 -> 2 -> 3, or in the order 3 -> 2 -> 1, or 3 -> 1 -> 2. Usually, you'll want to execute cells in the order of the notebook, but when loading an existing notebook, it's important to understand which cells need to be executed before others. Usually, you'll need to execute all of the cells in a new notebook before you can add more cells and start working.

You can restart the current session by clicking the Restart button in the Kernel menu or by clicking the corresponding icon:

Jupyter Restart Session

When you restart a session, there are no variables or functions defined and the environment is a blank slate.
Instructions

    Restart the session.
    Try running some of the later cells without running the previous cells and get familiar with the execution flow.



"""
"""

"""




"""
4: Editing cells

One of the great features of Jupyter notebook is that you can edit and re-run cells as many times as you want. In real-world data analysis, it's common to try many different techniques on a dataset in order to explore what works. In these cases, being able to edit your code and re-run is critical, because it lets you iteratively analyze your data.

Execution order is important to keep in mind as you edit and re-run. In the below diagram, you can see that the execution orders 3 -> 2 -> 1 and 3 -> 1 -> 2 will lead to different results being printed in cell 2.
ExampleNotebookCodecellsKernelsessionvariablesa=10a=101b=10b=10c=a*10a=102b=10c=100b=5a=53a=5b=5d=a*bc=100d=25

If you go back to edit and re-run an earlier cell, it's important to understand if any of the variables in the session have different values than you expect.
Instructions

    Run all of the existing cells in the notebook.
    In a new code cell, add code that returns a dictionary containing the total number of births for each unique day of the week.
        The result should be a dictionary where the keys are the unique day_of_week values and the associated values are the total number of births. Here's how the dictionary should be formatted:

days_counts = {
    0: 10000,
    1: 10000,
    2: 10000,
    ...
}

    Here are the steps:
        Create an empty dictionary,
        Select all but the header row and assign to a new list object,
        Iterate through this new list,
            Split each line on the comma delimiter,
            Extract the day_of_week value and the births value for each line,
            If the day_of_week value already exists as a key in the dictionary, add the births value to the existing, associated value.
            If the day_of_week value doesn't exist as a key, add it to the dictionary and set the associated value to the births value for that line.
        Outside the loop, display the dictionary.
    If you run into any errors, edit this existing code cell and iterate on the code until your code works properly. In the last step of this guided project, we've added a link to the solutions.



"""

# coding: utf-8

# In[1]:

f = open("births.csv","r")
f


# In[2]:

text = f.read()


# In[15]:

rows = text.split("\n")
days_counts = {}
births_list = []
for row in rows:
    births_list.append(row.split(','))
births_list[0:5]


# In[16]:

head_list = births_list[0]
head_list


# In[17]:

clean_births_list = births_list[1:len(births_list)]
clean_births_list[0:5]


# In[21]:

for list in clean_births_list:
    # print(list[3])
    if list[3] not in days_counts:
        days_counts[list[3]] = int(list[4])
    else:
        days_counts[list[3]] = days_counts[list[3]] + int(list[4])
days_counts


# In[ ]:
"""
"""







"""
5: Markdown cells

We can also add in markdown cells in order to explain our methodology further. Markdown is a standard for formatting plain text developed by John Gruber. Typing regular text will work fine in Markdown, but there are ways to make text bold, add lists, display images, and add links that can allow you to create a richer explanation. For example, you can prefix a line of text with a single hash symbol (#) to set it as the title and two hash symbols (##) to set it the line as the subtitle. You can read more about the Markdown standard on John Gruber's site.

In the following screenshot, we add a subtitle and a paragraph of text describing the data set.

Jupyter Markdown

Markdown cells can be run just like code cells. When a Markdown cell is run, the Markdown content is rendered:

Jupyter Rendered Markdown

To change the cell type from code to Markdown, click the dropdown menu that currently reads Code and select Markdown:

Jupyter Notebook Change Type
Instructions

    Add a new cell, change the type to Markdown, and then type a short explanation of what we've done so far.
    Add information on the column descriptions, which you can read more about here.



"""

""" results or consol output

"""




"""
6: Saving and downloading

When working with Jupyter notebooks, your work will be periodically auto-saved. You can also save manually by clicking the File menu, then the Save and Checkpoint button. This will create a Checkpoint of your work that you can then go back to by clicking the File menu, then the Revert to Checkpoint button.

You can also download notebooks in various formats by clicking on the File menu then the Download as button.

    If you download the notebook as a Notebook file, you can open it on your own computer after installing Jupyter.
    If you download as a Python file, with the .py extension, you'll be able to open the file locally using any text editor. This file will behave like a normal Python script.
    If you download as any of the other formats, like HTML, you can only view but not edit the contents in the notebook. These formats are helpful when you want to export your work for others to view.

Above the Jupyter notebook interface, we've added some buttons to restart the session, download the files, and restore the original files. Clicking the Download button will download a zip file, also known as an archive, to your computer containing the notebook and corresponding data sets.

Jupyter DQ Download

This zip file will have a .tar file extension and you won't be able to access the files contained within it without unzipping it first. If you're on a Mac or Linux computer, double clicking the zip file should unzip the files contained in the archive into a new folder. If you're on a Windows computer, you need to download a free unzip tool like 7-Zip and then double click the zip file.


"""





"""
7: Next Steps

In this guided project, we explored the Jupyter notebook interface and observed how it allows us to mix code and text effectively. The solutions for this guided project can be found here.

Next in this course is another guided project where we'll build on the work we did in this one to explore and analyze the U.S. births data set.


"""
