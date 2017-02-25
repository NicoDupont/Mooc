"""
02/2017
Dataquest : Data Analyst Path
Step 2: Intermediate Python And Pandas
SubStep : Exploratory Data Visualization : Bar Plots And Scatter Plots
"""


"""
1: Recap
In the previous missions in this course, we explored trends in unemployment data using line charts.
The unemployment data we worked with had 2 columns:

DATE - monthly time stamp
VALUE - unemployment rate (in percent)
Line charts were an appropriate choise for visualizing this dataset because the rows had a natural ordering to it.
Each row reflected information about an event that occurred after the previous row. Changing the order of the rows would make the line chart inaccurate. The lines from one marker to the next helped emphasize the logical connection between the data points.

In this mission, we'll be working with a dataset that has no particular order.
Before we explore other plots we can use, let's get familiar with the dataset we'll be working with.
"""




"""
2: Introduction To The Data
To investigate how different movie review sites the potential bias that movie reviews site has, FiveThirtyEight compiled data for 147 films from 2015 that have substantive reviews from both critics and consumers.
Every time Hollywood releases a movie, critics from Metacritic, Fandango, Rotten Tomatoes, and IMDB review and rate the film.
They also ask the users in their respective communities to review and rate the film.
Then, they calculate the average rating from both critics and users and display them on their site.
Here are screenshots from each site:

see review_sites_screenshots.png

FiveThirtyEight compiled this dataset to investigate if there was any bias to Fandango's ratings.
In addition to aggregating ratings for films, Fandango is unique in that it also sells movie tickets, and so it has a direct commercial interest in showing higher ratings.
After discovering that a few films that weren't good were still rated highly on Fandango, the team investigated and published an article about bias in movie ratings.

We'll be working with the fandango_scores.csv file, which can be downloaded from the FiveThirtEight Github repo.
https://github.com/fivethirtyeight/data/tree/master/fandango

Here are the columns we'll be working with in this mission:

FILM - film name
RT_user_norm - average user rating from Rotten Tomatoes, normalized to a 1 to 5 point scale
Metacritic_user_nom - average user rating from Metacritc, normalized to a 1 to 5 point scale
IMDB_norm - average user rating from IMDB, normalized to a 1 to 5 point scale
Fandango_Ratingvalue - average user rating from Fandango, normalized to a 1 to 5 point scale
Fandango_Stars - the rating displayed on the Fandango website (rounded to nearest star, 1 to 5 point scale)
Instead of displaying the raw rating, the writer discovered that Fandango usually rounded the average rating to the next highest half star (next highest 0.5 value).
The Fandango_Ratingvalue column reflects the true average rating while the Fandango_Stars column reflects the displayed, rounded rating.

Let's read in this dataset, which allows us to compare how a movie fared across all 4 review sites.

Instructions
Read fandango_scores.csv into a Dataframe named reviews.
Select the following columns and assign the resulting Dataframe to norm_reviews:
FILM
RT_user_norm
Metacritic_user_nom (note the misspelling of norm)
IMDB_norm
Fandango_Ratingvalue
Fandango_Stars
Display the first row in norm_reviews
"""
import pandas as pd
norm_reviews = pd.read_csv("fandango_scores.csv")[["FILM","RT_user_norm","Metacritic_user_nom","IMDB_norm","Fandango_Ratingvalue","Fandango_Stars"]]
print(norm_reviews.head())
""" Console output or Results
Output
                             FILM  RT_user_norm  Metacritic_user_nom  \
0  Avengers: Age of Ultron (2015)           4.3                 3.55
1               Cinderella (2015)           4.0                 3.75
2                  Ant-Man (2015)           4.5                 4.05
3          Do You Believe? (2015)           4.2                 2.35
4   Hot Tub Time Machine 2 (2015)           1.4                 1.70

   IMDB_norm  Fandango_Ratingvalue  Fandango_Stars
0       3.90                   4.5             5.0
1       3.55                   4.5             5.0
2       3.90                   4.5             5.0
3       2.70                   4.5             5.0
4       2.55                   3.0             3.5
"""



"""
3: Bar Plot
These sites use different scales for ratings.
Some use a 5 star scale while others use a 100 point scale. In addition, Metacritic and Rotten Tomatoes aggregate scores from both users and film critics while IMDB and Fandango aggregate only from their users.
We'll focus on just the average scores from users, because not all of the sites have scores from critics.

The RT_user_norm, Metacritic_user_nom, IMDB_norm, and Fandango_Ratingvalue columns contain the average user rating for each movie, normalized to a 0 to 5 point scale.
This allows us to compare how the users on each site rated a movie.
While using averages isn't perfect because films with a few reviews can skew the average rating, FiveThirtyEight only selected movies with a non-trivial number of ratings to ensure films with only a handful of reviews aren't included.

If you look at the first row, which lists the average user ratings for Avengers: Age of Ultron (2015), you'll notice that the Fandango ratings, both the actual and the displayed rating, are higher than those from the other sites for a given movie.
While calculating and comparing summary statistics give us hard numbers for quantifying the bias, visualizing the data using plots can help us gain a more intuitive understanding. We need a visualization that scales graphical objects to the quantitative values we're interested in comparing.
One of these visualizations is a bar plot.

see vertical_bar_plot.png

In the bar plot above, the x-axis represented the different ratings and the y-axis represented the actual ratings.
An effective bar plot uses categorical values on one axis and numerical values on the other axis.
Because bar plots can help us find the category corresponding to the smallest or largest values, it's important that we restrict the number of bars in a single plot.
Using a bar plot to visualize hundreds of values makes it difficult to trace the category with the smallest or largest value.

If the x-axis contains the categorical values and the rectangular bars are scaled vertically, this is known as a vertical bar plot.
A horizontal bar plot flips the axes, which is useful for quickly spotting the largest value.

see horizontal_bar_plot.png

An effective bar plot uses a consistent width for each bar.
This helps keep the visual focus on the heights of the bars when comparing.
Let's now learn how to create a vertical bar plot in matplotlib that represents the different user scores for Avengers: Age of Ultron (2015).
"""





"""
4: Creating Bars
When we generated line charts, we passed in the data to pyplot.plot() and matmplotlib took care of the rest.
Because the markers and lines in a line chart correspond directly with x-axis and y-axis coordinates, all matplotlib needed was the data we wanted plotted.
To create a useful bar plot, however, we need to specify the positions of the bars, the widths of the bars, and the positions of the axis labels.
Here's a diagram that shows the various values we need to specify:

see matplotlib_barplot_positioning.png

We'll focus on positioning the bars on the x-axis in this step and on positioning the x-axis labels in the next step.
We can generate a vertical bar plot using either pyplot.bar() or Axes.bar(). We'll use Axes.bar() so we can extensively customize the bar plot more easily.
We can use pyplot.subplots() to first generate a single subplot and return both the Figure and Axes object. This is a shortcut from the technique we used in the previous mission:


fig, ax = plt.subplots()
The Axes.bar() method has 2 required parameters, left and height. We use the left parameter to specify the x coordinates of the left sides of the bar.
We use the height parameter to specify the height of each bar. Both of these parameters accept a list-like object:


# Positions of the left sides of the bars. [0.75, 1.75, 2.75, 3.75, 4.75]
from numpy import arange
bar_positions = arange(5) + 0.75
​
# Heights of the bars.  In our case, the average rating for the first movie in the dataset.
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews.ix[0, num_cols].values
​
ax.bar(bar_positions, bar_heights)
We can also use the width parameter to specify the width of each bar.
This is an optional parameter and the width of each bar is set to 0.8 by default. The following code sets the width parameter to 1.5:


ax.bar(bar_positions, bar_heights, 1.5)
Instructions
Create a single subplot and assign the returned Figure object to fig and the returned Axes object to ax.
Generate a bar plot with:
left set to bar_positions
height set to bar_heights
width set to 0.5
Use plt.show() to display the bar plot.

"""
import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_heights = norm_reviews.ix[0, num_cols].values
bar_positions = arange(5) + 0.75

fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, 0.5)

plt.show()
""" Console output or Results
see plot14.png
"""




"""
5: Aligning Axis Ticks And Labels
By default, matplotlib sets the x-axis tick labels to the integer values the bars spanned on the x-axis (from 0 to 6).
We only need tick labels on the x-axis where the bars are positioned.
We can use Axes.set_xticks() to change the positions of the ticks to [1, 2, 3, 4, 5]:


tick_positions = range(1,6)
ax.set_xticks(tick_positions)
Then, we can use Axes.set_xticklabels() to specify the tick labels:


num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
ax.set_xticklabels(num_cols)
If you look at the documentation for the method, you'll notice that we can specify the orientation for the labels using the rotation parameter:


ax.set_xticklabels(num_cols, rotation=90)
Rotating the labels by 90 degrees keeps them readable.
In addition to modifying the x-axis tick positions and labels, let's also set the x-axis label, y-axis label, and the plot title.

Instructions
Create a single subplot and assign the returned Figure object to fig and the returned Axes object to ax.
Generate a bar plot with:
left set to bar_positions
height set to bar_heights
width set to 0.5
Set the x-axis tick positions to tick_positions.
Set the x-axis tick labels to num_cols and rotate by 90 degrees.
Set the x-axis label to "Rating Source".
Set the y-axis label to "Average Rating".
Set the plot title to "Average User Rating For Avengers: Age of Ultron (2015)".
Use plt.show() to display the bar plot.
"""
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews.ix[0, num_cols].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)

fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, 0.5)
ax.set_xticks(tick_positions)
ax.set_xticklabels(num_cols,rotation=90)
plt.xlabel("Rating Source")
plt.ylabel("Average Rating")
plt.title("Average User Rating For Avengers: Age of Ultron (2015)")

plt.show()
""" Console output or Results
see plot15.png
"""




"""
6: Horizontal Bar Plot
We can create a horizontal bar plot in matplotlib in a similar fashion.
Instead of using Axes.bar(), we use Axes.barh(). This method has 2 required parameters, bottom and width.
We use the bottom parameter to specify the y coordinate for the bottom sides for the bars and the width parameter to specify the lengths of the bars:


bar_widths = norm_reviews.ix[0, num_cols].values
bar_positions = arange(5) + 0.75
ax.barh(bar_positions, bar_widths, 0.5)
To recreate the bar plot from the last step as horizontal bar plot, we essentially need to map the properties we set for the y-axis instead of the x-axis.
We use Axes.set_yticks() to set the y-axis tick positions to [1, 2, 3, 4, 5] and Axes.set_yticklabels() to set the tick labels to the column names:


tick_positions = range(5) + 1
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
ax.set_yticks(tick_positions)
ax.set_yticklabels(num_cols)
Instructions
Create a single subplot and assign the returned Figure object to fig and the returned Axes object to ax.
Generate a bar plot with:
bottom set to bar_positions
width set to bar_widths
height set to 0.5
Set the y-axis tick positions to tick_positions.
Set the y-axis tick labels to num_cols.
Set the y-axis label to "Rating Source".
Set the x-axis label to "Average Rating".
Set the plot title to "Average User Rating for Avengers: Age of Ultron (2015)".
Use plt.show() to display the bar plot.
"""
import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_widths = norm_reviews.ix[0, num_cols].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)

fig, ax = plt.subplots()
ax.barh(bar_positions,bar_widths, 0.5)
ax.set_yticks(tick_positions)
ax.set_yticklabels(num_cols)
plt.ylabel("Rating Source")
plt.xlabel("Average Rating")
plt.title("Average User Rating for Avengers: Age of Ultron (2015)")

plt.show()
""" Console output or Results
see plot16.png
"""



"""
7: Scatter Plot
From the horizontal bar plot, we can more easily determine that the 2 average scores from Fandango users are higher than those from the other sites.
While bar plots help us visualize a few data points to quickly compare them, they aren't good at helping us visualize many data points.
Let's look at a plot that can help us visualize many points.

In the previous mission, the line charts we generated always connected points from left to right.
This helped us show the trend, up or down, between each point as we scanned visually from left to right.
Instead, we can avoid using lines to connect markers and just use the underlying markers. A plot containing just the markers is known as a scatter plot.

see scatter_plot_intro.png

A scatter plot helps us determine if 2 columns are weakly or strongly correlated. While calculating the correlation coefficient will give us a precise number, a scatter plot helps us find outliers, gain a more intuitive sense of how spread out the data is, and compare more easily.

To generate a scatter plot, we use Axes.scatter(). The scatter() method has 2 required parameters, x and y, which matches the parameters of the plot() method. The values for these parameters need to be iterable objects of matching lengths (lists, NumPy arrays, or pandas series).

Let's start by creating a scatter plot that visualizes the relationship between the Fandango_RatingValue and RT_user_norm columns. We're looking for at least a weak correlation between the columns.

Instructions
Create a single subplot and assign the returned Figure object to fig and the returned Axes object to ax.
Generate a scatter plot with the Fandango_Ratingvalue column on the x-axis and the RT_user_norm column on the y-axis.
Set the x-axis label to "Fandango" and the y-axis label to "Rotten Tomatoes".
Use plt.show() to display the resulting plot.

"""
fig, ax = plt.subplots()
ax.scatter(norm_reviews["Fandango_Ratingvalue"],norm_reviews["RT_user_norm"])
plt.ylabel("Rotten Tomatoes")
plt.xlabel("Fandango")
plt.show()
""" Console output or Results
see plot17.png
"""



"""
8: Switching Axes
The scatter plot suggests that there's a weak, positive correlation between the user ratings on Fandango and the user ratings on Rotten Tomatoes.
The correlation is weak because for many x values, there are multiple corresponding y values.
The correlation is positive because, in general, as x increases, y also increases.

When using scatter plots to understand how 2 variables are correlated, it's usually not important which one is on the x-axis and which one is on the y-axis.
This is because the relationship is still captured either way, even if the plots look a little different.
If you want to instead understand how an independent variable affects a dependent variables, you want to put the independent one on the x-axis and the dependent one on the y-axis.
Doing so helps emphasize the potential cause and effect relation.

In our case, we're not exploring if the ratings from Fandango influence those on Rotten Tomatoes and we're instead looking to understand how much they agree.
Let's see what happens when we flip the columns.

Instructions
For the subplot associated with ax1:
Generate a scatter plot with the Fandango_Ratingvalue column on the x-axis and the RT_user_norm column on the y-axis.
Set the x-axis label to "Fandango" and the y-axis label to "Rotten Tomatoes".
For the subplot associated with ax2:
Generate a scatter plot with the RT_user_norm column on the x-axis and the Fandango_Ratingvalue column on the y-axis.
Set the x-axis label to "Rotten Tomatoes" and the y-axis label to "Fandango".
Use plt.show() to display the resulting plot.
"""
fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.scatter(norm_reviews["Fandango_Ratingvalue"],norm_reviews["RT_user_norm"])
ax1.set_xlabel('Fandango')
ax1.set_ylabel('Rotten Tomatoes')

ax2.scatter(norm_reviews["RT_user_norm"],norm_reviews["Fandango_Ratingvalue"])
ax2.set_ylabel('Fandango')
ax2.set_xlabel('Rotten Tomatoes')
plt.show()
""" Console output or Results
see plot18.png
"""




"""
9: Benchmarking Correlation
The second scatter plot is a mirror reflection of the first second scatter plot.
The nature of the correlation is still reflected, however, which is the important thing.
Let's now generate scatter plots to see how Fandango ratings correlate with all 3 of the other review sites.

When generating multiple scatter plots for the purpose of comparison, it's important that all plots share the same ranges in the x-axis and y-axis.
In the 2 plots we generated in the last step, the ranges for both axes didn't match. We can use Axes.set_xlim() and Axes.set_ylim() to set the data limits for both axes:


ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
By default, matplotlib uses the minimal ranges for the data limits necessary to display all of the data we specify.
By manually setting the data limits ranges to specific ranges for all plots, we're ensuring that we can accurately compare.
We can even use the methods we just mentioned to zoom in on a part of the plots.
For example, the following code will constrained the axes to the 4 to 5 range:


ax.set_xlim(4, 5)
ax.set_ylim(4, 5)
This makes small changes in the actual values in the data appear larger in the plot.
A difference of 0.1 in a plot that ranges from 0 to 5 is hard to visually observe.
A difference of 0.1 in a plot that only ranges from 4 to 5 is easily visible since the difference is 1/10th of the range.

Instructions
For the Subplot associated with ax1:
Generate a scatter plot with the Fandango_Ratingvalue column on the x-axis and the RT_user_norm column on the y-axis.
Set the x-axis label to "Fandango" and the y-axis label to "Rotten Tomatoes".
Set the x-axis and y-axis data limits to range from 0 and 5.
For the Subplot associated with ax2:
Generate a scatter plot with the Fandango_Ratingvalue column on the x-axis and the Metacritic_user_nom column on the y-axis.
Set the x-axis label to "Fandango" and the y-axis label to "Metacritic".
Set the x-axis and y-axis data limits to range from 0 and 5.
For the Subplot associated with ax3:
Generate a scatter plot with the Fandango_Ratingvalue column on the x-axis and the IMDB_norm column on the y-axis.
Set the x-axis label to "Fandango" and the y-axis label to "IMDB".
Set the x-axis and y-axis data limits to range from 0 and 5.
Use plt.show() to display the plots.
"""
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.scatter(norm_reviews["Fandango_Ratingvalue"],norm_reviews["RT_user_norm"])
ax1.set_xlabel("Fandango")
ax1.set_ylabel("Rotten Tomatoes")
ax1.set_xlim(0, 5)
ax1.set_ylim(0, 5)

ax2.scatter(norm_reviews["Fandango_Ratingvalue"],norm_reviews["Metacritic_user_nom"])
ax2.set_xlabel("Fandango")
ax2.set_ylabel("Metacritic")
ax2.set_xlim(0, 5)
ax2.set_ylim(0, 5)

ax3.scatter(norm_reviews["Fandango_Ratingvalue"],norm_reviews["IMDB_norm"])
ax3.set_xlabel("Fandango")
ax3.set_ylabel("Metacritic")
ax3.set_xlim(0, 5)
ax3.set_ylim(0, 5)

plt.show()
""" Console output or Results
see plot19.png
"""




"""
10: Next Steps
From the scatter plots, we can conclude that user ratings from IMDB and Fandango are the most similar.
In addition, user ratings from Metacritic and Rotten Tomatoes have positive but weak correlations with user ratings from Fandango.
We can also notice that user ratings from Metacritic and Rotten Tomatoes span a larger range of values than those from IMDB or Fandango.
User ratings from Metacritic and Rotten Tomatoes range from 1 to 5.
User ratings from Fandango range approximately from 2.5 to 5 while those from IMDB range approximately from 2 to 4.5.

The scatter plots unfortunately only give us a cursory understanding of the distributions of user ratings from each review site.
For example, if a hundred movies had the same average user rating from IMDB and Fandango in the dataset, we would only see a single marker in the scatter plot.
In the next mission, we'll learn about two types of plots that help us understand distributions of values.
"""
