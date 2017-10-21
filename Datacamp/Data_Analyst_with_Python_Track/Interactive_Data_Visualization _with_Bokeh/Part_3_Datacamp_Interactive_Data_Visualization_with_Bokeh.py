"""
Datacamp - Interactive Data Visualization with Bokeh
https://www.datacamp.com/courses/interactive-data-visualization-with-bokeh
Part 3 : High-level Charts
Python 3.X
"""



"""
In addition to versatile data-driven glyphs, Bokeh comes with a variety of high-level statistical chart types built in, so that you can get quick exploratory charts with very little code.
"""



"""
A basic histogram
100xp

Create a simple histogram with the Histogram() function. Again we'll use the fertility data set to plot the distribution of female literacy around the world.

As in the previous two chapters, you can interact with the figures you create in this chapter as well, and you may have to scroll down to view the lower portion of some of them.
Instructions

    Import Histogram, output_file, and show from bokeh.charts.
    Make a histogram called p with the Histogram() function using the 'female_literacy' column of df. You have to first specify df and then 'female_literacy'. Give the histogram a title of 'Female Literacy'.
    Set the x-axis label using p.xaxis.axis_label.
    Set the y-axis label using p.yaxis.axis_label.
    Specify the name 'histogram.html' for the output file and display the histogram p.

"""
# Import Histogram, output_file, and show from bokeh.charts
from bokeh.charts import Histogram, output_file, show

# Make a Histogram: p
p = Histogram(df, 'female_literacy', title='Female Literacy')

# Set the x axis label
p.xaxis.axis_label = 'Nb'

# Set the y axis label
p.xaxis.axis_label = 'Female Literacy'

# Specify the name of the output_file and show the result
output_file('histogram.html')
show(p)
""" Console Output or results
see plot25.png
Great work! In the next exercise, you will learn how to customize histograms by controlling the number of bins.
"""




"""
Controlling the number of bins
100xp

By default, Bokeh makes histograms with 10 bins. By controlling the bins parameter of the Histogram() function, we can adjust the number of bins.

Let's plot female literacy with 40 bins.
Instructions

    Import Histogram, output_file, and show from bokeh.charts
    Use the Histogram() function to make a histogram called p of the 'female_literacy' column of df with 40 bins.
    Specify a name for the output file and display the histogram p. This has already been done for you.

"""
# Import Histogram, output_file, and show from bokeh.charts
from bokeh.charts import Histogram, output_file, show

# Make the Histogram: p
p = Histogram(df, 'female_literacy', title='Female Literacy', bins=40)

# Set axis labels
p.xaxis.axis_label = 'Female Literacy (% population)'
p.yaxis.axis_label = 'Number of Countries'

# Specify the name of the output_file and show the result
output_file('histogram.html')
show(p)
""" Console Output or results
see plot26.png

"""





"""
Generating multiple histograms at once
100xp

Let's make separate histograms, each with 10 bins for each of the 6 continents.

To do this with Bokeh charts we pass a column name to the the color parameter of the Histogram() function. In this case, the 'Content' column contains the continent abbreviation that we'll use to group the female literacy values in each of the 6 continents.
Instructions

    Import Histogram, output_file, and show from bokeh.charts.
    Use the Histogram() function to make a histogram called p of the 'female_literacy' column of df. Specify the keyword argument color='Continent' to make separate histograms for each continent, and have the legend displayed on the 'top_left'.

"""
# Import Histogram, output_file, and show from bokeh.charts
from bokeh.charts import Histogram, output_file, show

# Make a Histogram: p
p = Histogram(df, 'female_literacy' , title='Female Literacy',
              color='Continent', legend='top_left')

# Set axis labels
p.xaxis.axis_label = 'Female Literacy (% population)'
p.yaxis.axis_label = 'Number of Countries'

# Specify the name of the output_file and show the result
output_file('hist_bins.html')
show(p)
""" Console Output or results
see plot27.png
"""





"""
A basic box plot
100xp

In this exercise, you'll make a box plot of female literacy per continent by setting values='female_literacy' and label='Continent' with the BoxPlot() function.
Instructions

    Import BoxPlot, output_file, and show from bokeh.charts.
    Use the BoxPlot() function to make a box plot called p of the 'female_literacy' column of df per 'Continent'. Have the legend displayed on the 'bottom_right'.
    Set the y-axis label to 'Female literacy (% population)' using p.yaxis.axis_label.

"""
# Import BoxPlot, output_file, and show from bokeh.charts
from bokeh.charts import BoxPlot, output_file, show

# Make a box plot: p
p = BoxPlot(df, values='female_literacy', label='Continent',
            title='Female Literacy (grouped by Continent)', legend='bottom_right')

# Set the y axis label
p.yaxis.axis_label = 'Female literacy (% population)'

# Specify the name of the output_file and show the result
output_file('boxplot.html')
show(p)
""" Console Output or results
see plot28.png
Great work! In the next exercise, you will learn how to customize box plots using color.
"""




"""
Color different groups differently
100xp

Like the Histogram() function, we can use the color parameter of the BoxPlot() function to color the box plot of each continent separately.

In this exercise, you'll distinguish between the six continents by setting set the color parameter of the BoxPlot() function to 'Continent'.
Instructions

    Import BoxPlot, output_file, and show from bokeh.charts.
    Use the BoxPlot() function to make a box plot called p of the 'female_literacy' column of df per 'Continent'. Have the box plot for each continent colored differently by specifying the color parameter of BoxPlot(). As before, have the legend display on the 'bottom_right'.

"""
# Import BoxPlot, output_file, and show
from bokeh.charts import BoxPlot, output_file, show

# Make a box plot: p
p = BoxPlot(df, values='female_literacy', label='Continent', color='Continent',
            title='Female Literacy (grouped by Continent)', legend='bottom_right')

# Set y-axis label
p.yaxis.axis_label = 'Female literacy (% population)'

# Specify the name of the output_file and show the result
output_file('boxplot.html')
show(p)
""" Console Output or results
see plot29.png
"""




""" answer : 4
Understanding different Bokeh APIs
50xp

The high level Scatter in bokeh.charts is similar to marker plots from bokeh.plotting, but differs in important ways. What is a reason to consider using Scatter?
Possible Answers

    For drawing different markers automatically based on groups in the data.
    1
    To choose colors automatically based on groups in the data.
    2
    You want to work directly with Pandas DataFrame.
    3
    All of the above.
    4
"""

""" Console Output or results
Correct. Scatter provides quick and easy charts from DataFrames, including handling colors and markers for groupings.
"""




"""
A basic scatter plot
100xp

In this exercise, you'll make a simple scatter plot of female literacy on the y axis and population on x axis.
Instructions

    Import Scatter, output_file, and show from bokeh.charts.
    Use the Scatter() function to make a scatter plot called p with 'population' on the x-axis and 'female_literacy' on the y-axis.
    Set the x-axis label with p.xaxis.axis_label.
    Set the y-axis label with p.yaxis.axis_label.

"""
# Import Scatter, output_file, and show from bokeh.charts
from bokeh.charts import Scatter, output_file, show

# Make a scatter plot: p
p = Scatter(df, x='population', y='female_literacy',
            title='Female Literacy vs Population')

# Set the x-axis label
p.xaxis.axis_label = 'Population'

# Set the y-axis label
p.yaxis.axis_label = 'Female literacy'

# Specify the name of the output_file and show the result
output_file('scatterplot.html')
show(p)
""" Console Output or results
see plot30.png
"""





"""
Using colors to group data
100xp

Just like we've seen with other Bokeh charts you'll use the color parameter to the Scatter() function to color each circle by its 'Continent' in the plot of Female Literacy vs Population.
Instructions

    Import Scatter, output_file, and show from bokeh.charts.
    Make a scatter plot called p like you did in the previous exercise. This time, also color each circle by its 'Continent'. To do this, specify the color parameter of the Scatter() function.

"""
# Import Scatter, output_file, and show from bokeh.charts
from bokeh.charts import Scatter, output_file, show

# Make a scatter plot such that each circle is colored by its continent: p
p = Scatter(df, x='population', y='female_literacy', color='Continent',
            title='Female Literacy vs Population')

# Set x-axis and y-axis labels
p.xaxis.axis_label = 'Population (millions)'
p.yaxis.axis_label = 'Female literacy (% population)'

# Specify the name of the output_file and show the result
output_file('scatterplot.html')
show(p)
""" Console Output or results
see plot31.png
Great work! In addition to color, you can also use markers to group data in scatter plots. You will learn how to do this in the next exercise.
"""





"""
Using shapes to group data
100xp

Like the color parameter, the marker type can be set to a column of categorical data to select a different marker for each value.

Here you'll plot Female Literacy vs Population and set a different marker for each of the 6 continents using the marker parameter of the Scatter() function.
Instructions

    Import Scatter, output_file, and show from bokeh.charts.
    Make a scatter plot called p like you did in the previous exercise. This time, also add a different marker for each 'Continent'. To do this, specify the marker parameter of the Scatter() function.

"""
# Import Scatter, output_file, and show from bokeh.charts
from bokeh.charts import Scatter, output_file, show

# Make a scatter plot such that each continent has a different marker type: p
p = Scatter(df, x='population', y='female_literacy', marker='Continent', color='Continent',
            title='Female Literacy vs Population')

# Set x-axis and y-axis labels
p.xaxis.axis_label = 'Population (millions)'
p.yaxis.axis_label = 'Female literacy (% population)'

# Specify the name of the output_file and show the result
output_file('scatterplot.html')
show(p)
""" Console Output or results
see plot32.png
"""
