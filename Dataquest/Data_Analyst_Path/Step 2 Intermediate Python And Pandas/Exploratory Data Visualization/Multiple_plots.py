"""
02/2017
Dataquest : Data Analyst Path
Step 2: Intermediate Python And Pandas
SubStep : Exploratory Data Visualization : Multiple plots
"""


"""
1: Recap
In the previous mission, we explored how a visual representation of data can help us reach observations about data more quickly than a table representation of the same data.
We learned how to work with the pyplot module, which provides a high-level interface to the matplotlib library, to create and customize a line chart of unemployment data.
To look for potential seasonality, we started by creating a line chart of unemployment rates from 1948.

In this mission, we'll dive a bit deeper into matplotlib to learn how to create multiple line charts to help us compare monthly unemployment trends across time.
The unemployment dataset contains 2 columns:

DATE: date, always the first of the month. Examples:
1948-01-01: January 1, 1948.
1948-02-01: February 1, 1948.
1948-03-01: March 1, 1948.
1948-12-01: December 1, 1948.
VALUE: the corresponding unemployment rate, in percent.
Here's what the first 12 rows look like, which reflect the unemployment rate from January 1948 to December 1948:

DATE	VALUE
1948-01-01	3.4
1948-02-01	3.8
1948-03-01	4.0
1948-04-01	3.9
1948-05-01	3.5
1948-06-01	3.6
1948-07-01	3.6
1948-08-01	3.9
1948-09-01	3.8
1948-10-01	3.7
1948-11-01	3.8
1948-12-01	4.0
Let's practice what you learned in the previous mission.

Instructions
Read unrate.csv into a DataFrame and assign to unrate.
Use Pandas.to_datetime to convert the DATE column into a Series of datetime values.
Generate a line chart that visualizes the unemployment rates from 1948:
x-values should be the the first 12 values in the DATE column
y-values should be the first 12 values in the VALUE column
Use pyplot.xticks() to rotate the x-axis tick labels by 90 degrees.
Use pyplot.xlabel() to set the x-axis label to "Month".
Use pyplot.ylabel() to set the y-axis label to "Unemployment Rate".
Use pyplot.title() to set the plot title to "Monthly Unemployment Trends, 1948".
Display the plot.
"""
import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])

plt.plot(unrate['DATE'].loc[0:11],unrate['VALUE'].loc[0:11])
plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.show()
""" Console output or Results
see plot5.png
"""



"""
2: Matplotlib Classes
When we were working with a single plot, pyplot was storing and updating the state of that single plot.
We could tweak the plot just using the functions in the pyplot module.
When we want to work with multiple plots, however, we need to be more explicit about which plot we're making changes to.
This means we need to understand the matplotlib classes that pyplot uses internally to maintain state so we can interact with them directly.
Let's first start by understanding what pyplot was automatically storing under the hood when we create a single plot:

a container for all plots was created (returned as a Figure object)
a container for the plot was positioned on a grid (the plot returned as an Axes object)
visual symbols were added to the plot (using the Axes methods)
A figure acts as a container for all of our plots and has methods for customizing the appearance and behavior for the plots within that container.
Some examples include changing the overall width and height of the plotting area and the spacing between plots.

We can manually create a figure by calling pyplot.figure():


fig = plt.figure()
Instead of only calling the pyplot function, we assigned its return value to a variable (fig).
After a figure is created, an axes for a single plot containing no data is created within the context of the figure.
When rendered without data, the plot will resemble the empty plot from the previous mission.
The Axes object acts as its own container for the various components of the plot, such as:

values on the x-axis and y-axis
ticks on the x-axis and y-axis
all visual symbols, such as:
markers
lines
gridlines
While plots are represented using instances of the Axes class, they're also often referred to as subplots in matplotlib.
To add a new subplot to an existing figure, use Figure.add_subplot.
This will return a new Axes object, which needs to be assigned to a variable:


axes_obj = fig.add_subplot(nrows, ncols, plot_number)
If we want the figure to contain 2 plots, one above the other, we need to write:


ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
This will create a grid, 2 rows by 1 column, of plots.
Once we're done adding subplots to the figure, we display everything using plt.show():


import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()
Let's create a figure, add subplots to it, and display it.

Instructions
Use plt.figure() to create a figure and assign to fig.
Use Figure.add_subplot() to create two subplots above and below each other
Assign the top Axes object to ax1.
Assign the top Axes object to ax2.
Use plt.show() to display the resulting plot.
"""
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()
""" Console output or Results
see plot6.png
"""



"""
3: Grid Positioning
For each subplot, matplotlib generated a coordinate grid that was similar to the one we generated in the last mission using the plot() function:

the x-axis and y-axis values ranging from 0.0 to 1.0
no gridlines
no data
The main difference is that this plot ranged from 0.0 to 1.0 instead of from -0.06 to 0.06, which is a quirk suggested by a difference in default properties.

Now that we have a basic understanding of the important matplotlib classes, we can create multiple plots to compare monthly unemployment trends.
If you recall, we need to specify the position of each subplot on a grid. Here's a diagram that demonstrates how a 2 by 2 subplot layout would look like:

see img1.png

When the first subplot is created, matplotlib knows to create a grid with 2 rows and 2 columns. As we add each subplot, we specify the plot number we want returned and the corresponding Axes object is created and returned.
In matplotlib, the plot number starts at the top left position in the grid (left-most plot on the top row), moves through the remaining positions in that row, then jumps to the left-most plot in the second row, and so forth.

see subplot_grid.png

If we created a grid of 4 subplots but don't create a subplot for each position in the grid, areas without axes are left blank:

see multiple_subplots_missing_one_plot.png


"""


"""
4: Adding Data
To generate a line chart within an Axes object, we need to call Axes.plot() and pass in the data you want plotted:


x_values = [0.0, 0.5, 1.0]
y_values = [10, 20, 40]
ax1.plot(x_values, y_values)
Like pyplot.plot(), the Axes.plot() will accept any iterable object for these parameters, including NumPy arrays and pandas Series objects.
It will also use generate a line chart by default from the values passed in.
Each time we want to generate a line chart, we need to call Axes.plot() and pass in the data we want to use in that plot.

Instructions
Create 2 line subplots in a 2 row by 1 column layout:
In the top subplot, plot the data from 1948.
For the x-axis, use the first 12 values in the DATE column.
For the y-axis, use the first 12 values in the VALUE column.
In the bottom subplot, plot the data from 1949.
For the x-axis, use the values from index 12 to 24 in the DATE column.
For the y-axis, use the values from index 12 to 24 in the VALUE column.
Use plt.show() to display all the plots.
"""
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
plt.show()
""" Console output or Results

"""




"""
5: Formatting And Spacing
One issue with the 2 plots is that the x-axis ticks labels are unreadable.
The other issue is that the plots are squeezed together vertically and hard to interpret.
Even though now we generated 2 line charts, the total plotting area for the figure remained the same:

see plotting_area_stays_same.png

This is because matplotlib used the default dimensions for the total plotting area instead of resizing it to accommodate the plots.
If we want to expand the plotting area, we have to specify this ourselves when we create the figure.
To tweak the dimensions of the plotting area, we need to use the figsize parameter when we call plt.figure():

This parameter takes in a tuple of floats:

fig = plt.figure(figsize=(width, height))
The unit for both width and height values is inches.
The dpi parameter, or dots per inch, and the figsize parameter determine how much space on your display a plot takes up.
By increasing the width and the height of the plotting area, we can address both issues.

Instructions
For the plot we generated in the last screen, set the width of the plotting area to 12 inches and the height to 6 inches.

"""
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()
""" Console output or Results
see plot8.png
"""




"""
6: Comparing Across More Years
Instead of having to rotate the x-axis tick labels, we were able to horizontally extend the entire plotting area to make the labels more readable.
Because the goal is to be able to look for any visual similarities between the lines in the plots, we want the space between the 2 plots to be as small as possible.
If we had rotated the labels by 90 degrees instead, like we did in the last mission, we'd need to increase the spacing between the plots to keep them from overlapping.
Expanding the plotting area horizontally improved the readability of the x-axis tick labels and minimized the amount of space between the 2 line charts.

If you recall, we generated these 2 line charts because we were interested in looking for any seasonality in the monthly unemployment trends.
If you spend some time visually analyzing both line charts, you'll discover that there's no changes in unemployment trends that are occurring in the same month in both years.

Let's visualize data from a few more years to see if we find any evidence for seasonality between those years.

Instructions
Set the width of the plotting area to 12 inches and the height to 12 inches.
Generate a grid with 5 rows and 1 column and plot data from the individual years. Start with 1948 in the top subplot and end with 1952 in the bottom subplot.
Use plt.show() to display the plots.
"""
fig = plt.figure(figsize=(12, 12))

ax1 = fig.add_subplot(5,1,1)
ax2 = fig.add_subplot(5,1,2)
ax3 = fig.add_subplot(5,1,3)
ax4 = fig.add_subplot(5,1,4)
ax5 = fig.add_subplot(5,1,5)

ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax3.plot(unrate[24:36]['DATE'], unrate[24:36]['VALUE'])
ax4.plot(unrate[36:48]['DATE'], unrate[36:48]['VALUE'])
ax5.plot(unrate[48:60]['DATE'], unrate[48:60]['VALUE'])

plt.show()


# or

fig = plt.figure(figsize=(12,12))

for i in range(5):
    ax = fig.add_subplot(5,1,i+1)
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    ax.plot(subset['DATE'], subset['VALUE'])

plt.show()
""" Console output or Results
see plot9.png
"""





"""
7: Overlaying Line Charts
By adding more line charts, we can look across more years for seasonal trends.
This comes at a cost, unfortunately.
We now have to visually scan over more space, which is a limitation that we experienced when scanning the table representation of the same data.
If you recall, one of the limitations of the table representation we discussed in the previous mission was the amount of time we'd have to spend scanning the table as the number of rows increased significantly.

We can handle the visual overhead each additional plot adds by overlaying the line charts in a single subplot.
If we remove the year from the x-axis and just keep the month values, we can use the same x-axis values to plot all of the lines.
First, we'll explore how to extract just the month values from the DATE column, then we'll dive into generating multipe plots on the same coordinate grid.

To extract the month values from the DATE column and assign them to a new column, we can use the pandas.Series.dt accessor:


unrate['MONTH'] = unrate['DATE'].dt.month
Calling pandas.Series.dt.month returns a Series containing the integer values for each month (e.g. 1 for January, 2 for February, etc.).
Under the hood, pandas applies the datetime.date function over each datetime value in the DATE column, which returns the integer month value.
Let's now move onto generating multiple line charts in the same subplot.

In the last mission, we called pyplot.plot() to generate a single line chart.
Under the hood, matplotlib created a figure and a single subplot for this line chart.
If we call pyplot.plot() multiple times, matplotlib will generate the line charts on the single subplot.


plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'])
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'])
If we want to set the dimensions for the plotting area, we can create the figure ourselves first then plot the data.
This is because matplotlib first checks if a figure already exists before plotting data.
It will only create one if we didn't create a figure.


fig = plt.figure(figsize=(6,6)
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'])
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'])
By default, matplotlib will select a different color for each line.
To specify the color ourselves, use the c parameter when calling plot():


plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c='red')
You can read about the different ways we can specify colors in matplotlib here.

Instructions
Set the plotting area to a width of 6 inches and a height of 3 inches.
Generate 2 line charts in the base subplot, using the MONTH column for the x-axis instead of the DATE column:
One line chart using data from 1948, with the line color set to "red".
One line chart using data from 1949, with the line color set to "blue".
Use plt.show() to display the plots.
"""
unrate['MONTH'] = unrate['DATE'].dt.month
plt.figure(figsize=(6, 3))
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], color='red')
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'], color='blue')
plt.show()
""" Console output or Results
see plot10.png
"""



"""
8: Adding More Lines
Let's visualize 5 years worth of unemployment rates on the same subplot.

Instructions
Set the plotting area to a width of 10 inches and a height of 6 inches.
Generate the following plots in the base subplot:
1948: set the line color to "red"
1949: set the line color to "blue"
1950: set the line color to "green"
1951: set the line color to "orange"
1952: set the line color to "black"
Use plt.show() to display the plots.

"""
plt.figure(figsize=(10, 6))

color = ["red","blue","green","orange","black"]

for i in range(0,5):
    start = i*12
    end = (i+1)*12
    col = color[i]
    plt.plot(unrate[start:end]['MONTH'], unrate[start:end]['VALUE'], color=col)

plt.show()
""" Console output or Results
see plot11.png
"""



"""
9: Adding A Legend
How colorful! By plotting all of the lines in one coordinate grid, we got a different perspective on the data.
The main thing that sticks out is how the blue and green lines span a larger range of y values (4% to 8% for blue and 4% to 7% for green) while the 3 plots below them mostly range only between 3% and 4%.
You can tell from the last sentence that we don't know which line corresponds to which year, because the x-axis now only reflects the month values.

To help remind us which year each line corresponds to, we can add a legend that links each color to the year the line is representing.
Here's what a legend for the lines in the last screen could look like:

see legend.png

When we generate each line chart, we need to specify the text label we want each color linked to.
The pyplot.plot() function contains a label parameter, which we use to set the year value:


plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c='red', label='1948')
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'], c='blue', label='1949')
We can create the legend using pyplot.legend and specify its location using the loc parameter:


plt.legend(loc='upper left')
If we're instead working with multiple subplots, we can create a legend for each subplot by mirroring the steps for each subplot.
When we use plt.plot() and plt.legend(), the Axes.plot() and Axes.legend() methods are called under the hood and parameters passed to the calls.
When we need to create a legend for each subplot, we can use Axes.legend() instead.

Let's now add a legend for the plot we generated in the last screen.

Instructions
Modify the code from the last screen that overlaid 5 plots to include a legend. Use the year value for each line chart as the label.
E.g. the plot of 1948 data that uses "red" for the line color should be labeled "1948" in the legend.
Place the legend in the "upper left" corner of the plot.
Display the plot using plt.show().

"""
fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
lab  = 1948
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=lab+i)

plt.legend(loc="upper left")
plt.show()
""" Console output or Results
see plot12.png
"""



"""
10: Final Tweaks
Instead of referring back to the code each time we want to confirm what subset each line corresponds to, we can focus our gaze on the plotting area and use the legend.
At the moment, the legend unfortunately covers part of the green line (which represents data from 1950).
Since the legend isn't critical to the plot, we should move this outside of the coordinate grid.
We'll explore how to do so in a later course because it requires a better understanding of some design principles as well as matplotlib.

Before we wrap up this mission, let's enhance the visualization by adding a title and labels for both axes. T
o set the title, we use pyplot.title() and pass in a string value:


plt.title("Monthly Unemployment Trends, 1948-1952")
To set the x-axis and y-axis labels, we use pyplot.xlabel() and pyplot.ylabel(). Both of these methods accept string values.

Instructions
Modify the code from the last screen:
Set the title to "Monthly Unemployment Trends, 1948-1952".
Set the x-axis label to "Month, Integer".
Set the y-axis label to "Unemployment Rate, Percent".
"""
fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc='upper left')
plt.title("Monthly Unemployment Trends, 1948-1952")
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")
plt.show()
""" Console output or Results
see plot13.png
"""




"""
11: Next Steps
In this mission, we learned about the important matplotlib building blocks and used them to experiment with creating multiple line charts.
In the next mission, we'll explore plots that allow us to visualize discrete data.
"""
