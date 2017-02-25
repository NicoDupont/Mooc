"""
02/2017
Dataquest : Data Analyst Path
Step 2: Intermediate Python And Pandas
SubStep : Storytelling Through Data Visualization : Guided Project: Visualizing The Gender Gap In College Degrees
"""


"""
1: Introduction
In this guided project, we'll extend the work we did in the last two missions on visualizing the gender gap across college degrees.
So far, we mostly focused on the STEM degrees but now we will generate line charts to compare across all degree categories. In the last step of this guided project, we'll explore how to export the final diagram we create as an image file. You can download the solutions for this guided project here.

Instructions
Use the starter code in the notebook to get familiar with the data set and the visualization we created at the end of the last mission.
"""
# 1: Introduction
%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
cb_dark_blue = (0/255,107/255,164/255)
cb_orange = (255/255, 128/255, 14/255)
stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']

fig = plt.figure(figsize=(18, 3))

for sp in range(0,6):
    ax = fig.add_subplot(1,6,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")

    if sp == 0:
        ax.text(2005, 87, 'Men')
        ax.text(2002, 8, 'Women')
    elif sp == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2001, 35, 'Women')
plt.show()
""" Console Output or results

"""


"""
2: Comparing Across All Degrees
Because there are seventeen degrees that we need to generate line charts for, we'll use a subplot grid layout of 6 rows by 3 columns.
We can then group the degrees into STEM, liberal arts, and other, in the following way:


stem_cats = ['Psychology', 'Biology', 'Math and Statistics', 'Physical Sciences', 'Computer Science', 'Engineering', 'Computer Science']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']
Here's what the diagram will look like:

Comparing Across Degree Categories
see 149_comparing_across_categories.png

While in the last mission, the stem_cats list was ordered by ending gender gap, all three of these lists are ordered in descending order by the percentage of degrees awarded to women.
You may have also noticed that while stem_cats and other_cats have six degree categories as elements, lib_arts_cats only has five.
You'll need to not only modify the for loop to generate the STEM line charts that we wrote in the last mission but also add two new for loops to generate the line charts for liberal arts degrees and for other degrees.

Instructions
Generate a 6 row by 3 column grid of subplots.
In the first column:
Generate line charts for both male and female percentages for every degree in stem_cats.
Add text annotations for Women and Men in the topmost and bottommost plots.
In the second column:
Generate line charts for both male and female percentages for every degree in lib_arts_cats.
Add text annotations for Women and Men for only the topmost plot (since the lines overlap at the end in the bottommost plot).
In the third column:
Generate line charts for both male and female percentages for every degree in other_cats.
Add text annotations for Women and Men in the topmost and bottommost plots.
"""
# 2: Comparing Across All Degrees

stem_cats = ['Psychology', 'Biology', 'Math and Statistics', 'Physical Sciences', 'Computer Science', 'Engineering', 'Computer Science']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']
len_stem_cats = len(stem_cats)
len_lib_arts_cats = len(lib_arts_cats)
len_other_cats = len(other_cats)
print("------")
print(len_stem_cats)
print("------")
print(len_lib_arts_cats)
print("------")
print(len_other_cats)
print("---------------------------")
print("---------------------------")

list_col = [stem_cats,lib_arts_cats,other_cats]

fig = plt.figure(figsize=(25, 30))

i = 1
for row in range(0,6):
    for col in range (0,3):
        if (row == 5 and col == 1) == False:
            ax = fig.add_subplot(6,3,i)
            ax.plot(women_degrees['Year'], women_degrees[list_col[col][row]], c=cb_dark_blue, label='Women', linewidth=3)
            ax.plot(women_degrees['Year'], 100-women_degrees[list_col[col][row]], c=cb_orange, label='Men', linewidth=3)
            ax.spines["right"].set_visible(False)
            ax.spines["left"].set_visible(False)
            ax.spines["top"].set_visible(False)
            ax.spines["bottom"].set_visible(False)
            ax.set_xlim(1968, 2011)
            ax.set_ylim(0,100)
            ax.set_title(list_col[col][row])
            ax.tick_params(bottom="off", top="off", left="off", right="off")

            if row == 0:
                ax.text(2005, 87, 'Men')
                ax.text(2002, 8, 'Women')
            elif row == 5:
                ax.text(2005, 62, 'Men')
                ax.text(2001, 35, 'Women')
        i += 1

plt.show()
""" Console Output or results
see plot19.png
"""



"""
3: Hiding X-Axis Labels
With seventeen line charts in one diagram, the non-data elements quickly clutter the field of view.
The most immediate issue that sticks out is the titles of some line charts overlapping with the x-axis labels for the line chart above it.
If we remove the titles for each line chart, the viewer won't know what degree each line chart refers to.
Let's instead remove the x-axis labels for every line chart in a column except for the bottom most one.
We can accomplish this by modifying the call to Axes.tick_params() and setting labelbottom to off:


ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
This will disable the x-axis labels for all of the line charts. You can then enable the x-axis labels for the bottommost line charts in each column:


ax.tick_params(labelbottom='on')
Instructions
Disable the x-axis labels for all line charts except the bottommost line charts in each column.
Click here to see what the diagram should look like.
"""
# 3: Hiding X-Axis Labels
fig = plt.figure(figsize=(25, 30))

i = 1
for row in range(0,6):
    for col in range (0,3):
        if (row == 5 and col == 1) == False:
            ax = fig.add_subplot(6,3,i)
            ax.plot(women_degrees['Year'], women_degrees[list_col[col][row]], c=cb_dark_blue, label='Women', linewidth=3)
            ax.plot(women_degrees['Year'], 100-women_degrees[list_col[col][row]], c=cb_orange, label='Men', linewidth=3)
            ax.spines["right"].set_visible(False)
            ax.spines["left"].set_visible(False)
            ax.spines["top"].set_visible(False)
            ax.spines["bottom"].set_visible(False)
            ax.set_xlim(1968, 2011)
            ax.set_ylim(0,100)
            ax.set_title(list_col[col][row])
            ax.tick_params(bottom="off", top="off", left="off", right="off",labelbottom='off')

            if row == 0:
                ax.text(2005, 87, 'Men')
                ax.text(2002, 8, 'Women')
            elif row == 5:
                ax.text(2005, 62, 'Men')
                ax.text(2001, 35, 'Women')
        i += 1

plt.show()
""" Console Output or results
see plot20.png
"""




"""
4: Setting Y-Axis Labels
Removing the x-axis labels for all but the bottommost plots solved the issue we noticed with the overlapping text.
In addition, the plots are cleaner and more readable.
The trade-off we made is that it's now more difficult for the viewer to discern approximately which years some interesting changes in trends may have happened.
This is acceptable because we're primarily interested in enabling the viewer to quickly get a high level understanding of which degrees are prone to gender imbalance and how has that changed over time.

In the vein of reducing cluttering, let's also simplify the y-axis labels.
urrently, all seventeen plots have six y-axis labels and even though they are consistent across the plots, they still add to the visual clutter.
By keeping just the starting and ending labels (0 and 100), we can keep some of the benefits of having the y-axis labels to begin with.

We can use the Axes.set_yticks() method to specify which labels we want displayed.
The following code enables just the 0 and 100 labels to be displayed:


ax.set_yticks([0,100])
Instructions
For all plots:
Enable just the y-axis labels at 0 and 100.
Click here to see what the diagram should look like.
"""
# 4: Setting Y-Axis Labels
fig = plt.figure(figsize=(25, 30))

i = 1
for row in range(0,6):
    for col in range (0,3):
        if (row == 5 and col == 1) == False:
            ax = fig.add_subplot(6,3,i)
            ax.plot(women_degrees['Year'], women_degrees[list_col[col][row]], c=cb_dark_blue, label='Women', linewidth=3)
            ax.plot(women_degrees['Year'], 100-women_degrees[list_col[col][row]], c=cb_orange, label='Men', linewidth=3)
            ax.spines["right"].set_visible(False)
            ax.spines["left"].set_visible(False)
            ax.spines["top"].set_visible(False)
            ax.spines["bottom"].set_visible(False)
            ax.set_xlim(1968, 2011)
            ax.set_ylim(0,100)
            ax.set_yticks([0,100])
            ax.set_title(list_col[col][row])
            ax.tick_params(bottom="off", top="off", left="off", right="off",labelbottom='off')

            if row == 0:
                ax.text(2005, 87, 'Men')
                ax.text(2002, 8, 'Women')
            elif row == 5:
                ax.text(2005, 62, 'Men')
                ax.text(2001, 35, 'Women')
        i += 1

plt.show()
""" Console Output or results
see plot21.png
"""




"""
5: Adding A Horizontal Line
While removing most of the y-axis labels definitely reduced clutter, it also made it hard to understand which degrees have close to 50-50 gender breakdown.
While keeping all of the y-axis labels would have made it easier, we can actually do one better and use a horizontal line across all of the line charts where the y-axis label 50 would have been.

We can generate a horizontal line across an entire subplot using the Axes.axhline() method.
The only required parameter is the y-axis location for the start of the line:


ax.axhline(50)
Let's use the next color in the Color Blind 10 palette for this horizontal line, which has an RGB value of (171, 171, 171).
Because we don't want this line to clutter the viewing experience, let's increase the transparency of the line.
We can set the color using the c parameter and the transparency using the alpha parameter.
The value passed in to the alpha parameter must range between 0 and 1:


ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
Instructions
For all plots:
Generate a horizontal line with the following properties:
Starts at the y-axis position 50
Set to the third color (light gray) in the Color Blind 10 palette
Has a transparency of 0.3
Click here to see what the diagram should look like.
"""
# 5: Adding A Horizontal Line
fig = plt.figure(figsize=(25, 30))

i = 1
for row in range(0,6):
    for col in range (0,3):
        if (row == 5 and col == 1) == False:
            ax = fig.add_subplot(6,3,i)
            ax.plot(women_degrees['Year'], women_degrees[list_col[col][row]], c=cb_dark_blue, label='Women', linewidth=3)
            ax.plot(women_degrees['Year'], 100-women_degrees[list_col[col][row]], c=cb_orange, label='Men', linewidth=3)
            ax.spines["right"].set_visible(False)
            ax.spines["left"].set_visible(False)
            ax.spines["top"].set_visible(False)
            ax.spines["bottom"].set_visible(False)
            ax.set_xlim(1968, 2011)
            ax.set_ylim(0,100)
            ax.set_yticks([0,100])
            ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
            ax.set_title(list_col[col][row])
            ax.tick_params(bottom="off", top="off", left="off", right="off",labelbottom='off')

            if row == 0:
                ax.text(2005, 87, 'Men')
                ax.text(2002, 8, 'Women')
            elif row == 5:
                ax.text(2005, 62, 'Men')
                ax.text(2001, 35, 'Women')
        i += 1

plt.show()
""" Console Output or results
see plot22.png
"""




"""
6: Exporting To A File
If you recall, matplotlib can be used many different ways.
It can be used within a Jupyter Notebook interface (like this one), from the command line, or in an integrated development environment.
Many of these ways of using matplotlib vary in workflow and handle the rendering of images differently as well.
o help support these different use cases, matplotlib can target different outputs or backends.
If you import matplotlib and run matplotlib.get_backend(), you'll see the specific backend you're currently using.

With the current backend we're using, we can use Figure.savefig() or pyplot.savefig() to export all of the plots contained in the figure as a single image file.
Note that these have to be called before we display the figure using pyplot.show().:


plt.plot(women_degrees['Year'], women_degrees['Biology'])
plt.savefig('biology_degrees.png')
In the above code, we saved a line chart as a PNG file. You can read about the different popular file types for images here.
The image will be exported into the same folder that your Jupyter Notebook server is running.

Exporting plots we create using matplotlib allows us to use them in Word documents, Powerpoint presentations, and even in emails.

Instructions
Export the figure containing all of the line charts to "gender_degrees.png".
"""
# 6: Exporting To A File
fig = plt.figure(figsize=(25, 30))

i = 1
for row in range(0,6):
    for col in range (0,3):
        if (row == 5 and col == 1) == False:
            ax = fig.add_subplot(6,3,i)
            ax.plot(women_degrees['Year'], women_degrees[list_col[col][row]], c=cb_dark_blue, label='Women', linewidth=3)
            ax.plot(women_degrees['Year'], 100-women_degrees[list_col[col][row]], c=cb_orange, label='Men', linewidth=3)
            ax.spines["right"].set_visible(False)
            ax.spines["left"].set_visible(False)
            ax.spines["top"].set_visible(False)
            ax.spines["bottom"].set_visible(False)
            ax.set_xlim(1968, 2011)
            ax.set_ylim(0,100)
            ax.set_yticks([0,100])
            ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
            ax.set_title(list_col[col][row])
            ax.tick_params(bottom="off", top="off", left="off", right="off",labelbottom='off')

            if row == 0:
                ax.text(2005, 87, 'Men')
                ax.text(2002, 8, 'Women')
            elif row == 5:
                ax.text(2005, 62, 'Men')
                ax.text(2001, 35, 'Women')
        i += 1

plt.savefig('gender_degrees.png')
plt.show()
""" Console Output or results
see plot23.png
"""




"""

"""

""" Console Output or results

"""




"""

"""

""" Console Output or results

"""
