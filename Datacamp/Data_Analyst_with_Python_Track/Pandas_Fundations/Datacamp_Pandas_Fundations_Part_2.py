"""
Datacamp - Pandas Fundations
https://www.datacamp.com/courses/pandas-foundations
Part 2 : Exploratory data analysis
Python 3.X
"""



"""
Exploratory data analysis
Having learned how to ingest and inspect your data, the next step is to explore it visually as well as quantitatively.
This process, known as exploratory data analysis (EDA), is a crucial component of any data science project, and pandas has powerful methods that help with statistical and visual EDA.
In this chapter, you will learn how and when to apply these techniques.
"""



"""
pandas line plots
100xp
In the previous chapter, you saw that the .plot() method will place the Index values on the x-axis by default. In this exercise, you'll practice making line plots with specific columns on the x and y axes.

You will work with a dataset consisting of monthly stock prices in 2015 for AAPL, GOOG, and IBM. The stock prices were obtained from Yahoo Finance. Your job is to plot the 'Month' column on the x-axis and the AAPL and IBM prices on the y-axis using a list of column names.

All necessary modules have been imported for you, and the DataFrame is available in the workspace as df. Explore it using methods such as .head(), .info(), and .describe() to see the column names.

Instructions
Create a list of y-axis column names called y_columns consisting of 'AAPL' and 'IBM'.
Generate a line plot with x='Month' and y=y_columns as inputs.
Add a title to the plot.
Specify the y-axis label.
Display the plot.
"""
# Create a list of y-axis column names: y_columns
y_columns = ['AAPL','IBM']

# Generate a line plot
df.plot(x='Month', y=y_columns)

# Add the title
plt.title('Monthly stock prices')

# Add the y-axis label
plt.ylabel('Price ($US)')

# Display the plot
plt.show()
""" consol ouput or results

"""




"""
pandas scatter plots
100xp
Pandas scatter plots are generated using the kind='scatter' keyword argument. Scatter plots require that the x and y columns be chosen by specifying the x and y parameters inside .plot(). Scatter plots also take an s keyword argument to provide the radius of each circle to plot in pixels.

In this exercise, you're going to plot fuel efficiency (miles-per-gallon) versus horse-power for 392 automobiles manufactured from 1970 to 1982 from the UCI Machine Learning Repository.

The size of each circle is provided as a NumPy array called sizes. This array contains the normalized 'weight' of each automobile in the dataset.

All necessary modules have been imported and the DataFrame is available in the workspace as df.

Instructions
Generate a scatter plot with 'hp' on the x-axis and 'mpg' on the y-axis. Specify s=sizes.
Add a title to the plot.
Specify the x-axis and y-axis labels.
"""
# Generate a scatter plot
df.plot(kind='scatter', x='hp', y='mpg', s=sizes)

# Add the title
plt.title('Fuel efficiency vs Horse-power')

# Add the x-axis label
plt.xlabel('Horse-power')

# Add the y-axis label
plt.ylabel('Fuel efficiency (mpg)')

# Display the plot
plt.show()
""" consol ouput or results

"""




"""
pandas box plots
100xp
While pandas can plot multiple columns of data in a single figure, making plots that share the same x and y axes, there are cases where two columns cannot be plotted together because their units do not match. The .plot() method can generate subplots for each column being plotted. Here, each plot will be scaled independently.

In this exercise your job is to generate box plots for fuel efficiency (mpg) and weight from the automobiles data set. To do this in a single figure, you'll specify subplots=True inside .plot() to generate two separate plots.

All necessary modules have been imported and the automobiles dataset is available in the workspace as df.

Instructions
Make a list called cols of the column names to be plotted: 'weight' and 'mpg'. You can then access it using df[cols].
Generate a box plot of the two columns in a single figure. To do this, specify subplots=True.
"""
# Make a list of the column names to be plotted: cols
cols = ['weight','mpg']

# Generate the box plots
df[cols].plot(kind='box',subplots=True)

# Display the plot
plt.show()
""" consol ouput or results

"""




"""
pandas hist, pdf and cdf
100xp
Pandas relies on the .hist() method to not only generate histograms, but also plots of PDFs and CDFs. In this exercise, you will work with a dataset consisting of restaurant bills that includes the amount customers tipped.

The original dataset is provided by the Seaborn package.

Your job is to plot a probability density function (PDF) and cumulative density function (CDF) for the 'fraction' column of the tips dataset. This column contains information about what fraction of the total bill comprised of the tip.

Remember, when plotting the PDF, you need to specify normed=True in your call to .hist(), and when plotting the CDF, you need to specify cumulative=True in addition to normed=True.

All necessary modules have been imported and the tips dataset is available in the workspace as df. Also, some formatting code has been written so that the plots you generate will appear on separate rows.

Instructions
Plot a PDF for the values in 'fraction' with 30 bins between 0 and 30%. The range has been taken care of for you. ax=axes[0] means that this plot will appear in the first row.
Note: For the system to accept your answer, you need to specify the parameters in the following order: ax, kind, normed, bins, range.
Plot a CDF for the values in 'fraction' with 30 bins between 0 and 30%. Again, the range has been specified for you. To make the CDF appear on the second row, you need to specify ax=axes[1].
Note: For the system to accept your answer, you need to specify the parameters in the following order: ax, kind, normed, cumulative, bins, range.
"""
# This formats the plots such that they appear on separate rows
fig, axes = plt.subplots(nrows=2, ncols=1)

# Plot the PDF
df['fraction'].plot(ax=axes[0], kind='hist',normed=True, bins=30,  range=(0,.3))
plt.show()

# Plot the CDF
df['fraction'].plot(ax=axes[1], kind='hist',normed=True, cumulative=True, bins=30,  range=(0,.3))
plt.show()
""" consol ouput or results

"""




""" question answer : 3
Fuel efficiency
50xp
From the automobiles data set, which value corresponds to the median value of the 'mpg' column? Your job is select the 'mpg' column and call the .median() method on it. The automobile DataFrame has been provided as df.

Possible Answers
29.0 1
23.45 2
22.75 3
32 4
"""

""" consol ouput or results
In [1]: df.describe()
Out[1]:
              mpg         cyl       displ          hp       weight  \
count  392.000000  392.000000  392.000000  392.000000   392.000000
mean    23.445918    5.471939  194.411990  104.469388  2977.584184
std      7.805007    1.705783  104.644004   38.491160   849.402560
min      9.000000    3.000000   68.000000   46.000000  1613.000000
25%     17.000000    4.000000  105.000000   75.000000  2225.250000
50%     22.750000    4.000000  151.000000   93.500000  2803.500000
75%     29.000000    8.000000  275.750000  126.000000  3614.750000
max     46.600000    8.000000  455.000000  230.000000  5140.000000

            accel          yr
count  392.000000  392.000000
mean    15.541327   75.979592
std      2.758864    3.683737
min      8.000000   70.000000
25%     13.775000   73.000000
50%     15.500000   76.000000
75%     17.025000   79.000000
max     24.800000   82.000000
"""



"""
Bachelor's degrees awarded to women
100xp
In this exercise, you will investigate statistics of the percentage of Bachelor's degrees awarded to women from 1970 to 2011. Data is recorded every year for 17 different fields. This data set was obtained from the Digest of Education Statistics.

Your job is to compute the minimum and maximum values of the 'Engineering' column and generate a line plot of the mean value of all 17 academic fields per year. To perform this step, you'll use the .mean() method with the keyword argument axis='columns'. This computes the mean across all columns per row.

The DataFrame has been pre-loaded for you as df with the index set to 'Year'.

Instructions
Print the minimum value of the 'Engineering' column.
Print the maximum value of the 'Engineering' column.
Construct the mean percentage per year with .mean(axis='columns'). Assign the result to mean.
Plot the average percentage per year. Since 'Year' is the index of df, it will appear on the x-axis of the plot. No keyword arguments are needed in your call to .plot().
"""
# Print the minimum value of the Engineering column
print(df['Engineering'].min())

# Print the maximum value of the Engineering column
print(df['Engineering'].max())

# Construct the mean percentage per year: mean
mean = df.mean(axis='columns')

# Plot the average percentage per year
mean.plot()

# Display the plot
plt.show()
""" consol ouput or results

"""




"""
Median vs mean
100xp
In many data sets, there can be large differences in the mean and median value due to the presence of outliers.

In this exercise, you'll investigate the mean, median, and max fare prices paid by passengers on the Titanic and generate a box plot of the fare prices. This data set was obtained from Vanderbilt University.

All necessary modules have been imported and the DataFrame is available in the workspace as df.

Instructions
Print summary statistics of the 'fare' column with .describe() and print().
Generate a box plot of the 'fare' column.
"""
# Print summary statistics of the fare column with .describe()
print(df['fare'].describe())

# Generate a box plot of the fare column
df['fare'].plot(kind='box')

# Show the plot
plt.show()
""" consol ouput or results
<script.py> output:
    count    1308.000000
    mean       33.295479
    std        51.758668
    min         0.000000
    25%         7.895800
    50%        14.454200
    75%        31.275000
    max       512.329200
    Name: fare, dtype: float64
"""




"""
Quantiles
100xp
In this exercise, you'll investigate the probabilities of life expectancy in countries around the world. This dataset contains life expectancy for persons born each year from 1800 to 2015. Since country names change or results are not reported, not every country has values. This dataset was obtained from Gapminder.

First, you will determine the number of countries reported in 2015. There are a total of 206 unique countries in the entire dataset. Then, you will compute the 5th and 95th percentiles of life expectancy over the entire dataset. Finally, you will make a box plot of life expectancy every 50 years from 1800 to 2000. Notice the large change in the distributions over this period.

The dataset has been pre-loaded into a DataFrame called df.

Instructions
Print the number of countries reported in 2015. To do this, use the .count() method on the '2015' column of df.
Print the 5th and 95th percentiles of df. To do this, use the .quantile() method with the list [0.05, 0.95].
Generate a box plot using the list of columns provided in years. This has already been done for you, so click on 'Submit Answer' to view the result!
"""
# Print the number of countries reported in 2015
print(df['2015'].count())

# Print the 5th and 95th percentiles
print(df.quantile([0.05, 0.95]))

# Generate a box plot
years = ['1800','1850','1900','1950','2000']
df[years].plot(kind='box')
plt.show()
""" consol ouput or results
<script.py> output:
    208
          Unnamed: 0   1800   1801   1802  1803  1804   1805   1806   1807  1808  \
    0.05       12.95  25.40  25.30  25.20  25.2  25.2  25.40  25.40  25.40  25.3
    0.95      246.05  37.92  37.35  38.37  38.0  38.3  38.37  38.37  38.37  38.0

           ...      2007   2008    2009    2010   2011    2012    2013   2014  \
    0.05   ...     53.07  53.60  54.235  54.935  55.97  56.335  56.705  56.87
    0.95   ...     80.73  80.93  81.200  81.365  81.60  81.665  81.830  82.00

            2015     2016
    0.05  57.855  59.2555
    0.95  82.100  82.1650

    [2 rows x 218 columns]
"""




"""
Standard deviation of temperature
100xp
Let's use the mean and standard deviation to explore differences in temperature distributions in Pittsburgh in 2013. The data has been obtained from Weather Underground.

In this exercise, you're going to compare the distribution of daily temperatures in January and March. You'll compute the mean and standard deviation for these two months. You will notice that while the mean values are similar, the standard deviations are quite different, meaning that one month had a larger fluctuation in temperature than the other.

The DataFrames have been pre-loaded for you as january, which contains the January data, and march, which contains the March data.

Instructions
Compute and print the means of the January and March data using the .mean() method.
Compute and print the standard deviations of the January and March data using the .std() method.
"""
# Print the mean of the January and March data
print(january.mean(), march.mean())

# Print the standard deviation of the January and March data
print(january.std(), march.std())
""" consol ouput or results
<script.py> output:
    28    32.5
    dtype: float64 28    35.233333
    dtype: float64
    28    13.790927
    dtype: float64 28    7.491067
    dtype: float64
"""




""" question answer : 2
Filtering and counting
50xp
How many automobiles were manufactured in Asia in the automobile data set? The DataFrame has been provided for you as df. Use filtering and the .count() member method to determine the number of rows where the 'origin' column has the value 'Asia'.

As an example, you can extract the rows that contain 'US' as the country of origin using df[df['origin'] == 'US'].

Possible Answers
68 1
79 2
245 3
392 4
"""

""" consol ouput or results
In [2]: df[df['origin'] == 'Asia'].info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 79 entries, 14 to 384
Data columns (total 9 columns):
mpg       79 non-null float64
cyl       79 non-null int64
displ     79 non-null float64
hp        79 non-null int64
weight    79 non-null int64
accel     79 non-null float64
yr        79 non-null int64
origin    79 non-null object
name      79 non-null object
dtypes: float64(3), int64(4), object(2)
memory usage: 6.2+ KB
"""






"""
Separate and summarize
100xp
Let's use population filtering to determine how the automobiles in the US differ from the global average and standard deviation. How the distribution of fuel efficiency (MPG) for the US differ from the global average and standard deviation?

In this exercise, you'll compute the means and standard deviations of all columns in the full automobile dataset. Next, you'll compute the same quantities for just the US population and subtract the global values from the US values.

All necessary modules have been imported and the DataFrame has been pre-loaded as df.

Instructions
Compute the global mean and global standard deviations of df using the .mean() and .std() methods. Assign the results to global_mean and global_std.
Filter the 'US' population from the 'origin' column and assign the result to us.
Compute the US mean and US standard deviations of us using the .mean() and .std() methods. Assign the results to us_mean and us_std.
Print the differences between us_mean and global_mean and us_std and global_std. This has already been done for you.
"""
# Compute the global mean and global standard deviation: global_mean, global_std
global_mean = df.mean()
global_std = df.std()

# Filter the US population from the origin column: us
us = df[df['origin'] == 'US']

# Compute the US mean and US standard deviation: us_mean, us_std
us_mean = us.mean()
us_std = us.std()

# Print the differences
print(us_mean - global_mean)
print(us_std - global_std)
""" consol ouput or results
<script.py> output:
    mpg        -3.412449
    cyl         0.805612
    displ      53.100255
    hp         14.579592
    weight    394.905612
    accel      -0.551122
    yr         -0.387755
    dtype: float64


    mpg       -1.364623
    cyl       -0.049788
    displ     -6.267657
    hp         1.406630
    weight   -54.055870
    accel     -0.022844
    yr        -0.023369
    dtype: float64
"""




"""
Separate and plot
100xp
Population filtering can be used alongside plotting to quickly determine differences in distributions between the sub-populations. You'll work with the Titanic dataset.

There were three passenger classes on the Titanic, and passengers in each class paid a different fare price. In this exercise, you'll investigate the differences in these fare prices.

Your job is to use Boolean filtering and generate box plots of the fare prices for each of the three passenger classes. The fare prices are contained in the 'fare' column and passenger class information is contained in the 'pclass' column.

When you're done, notice the portions of the box plots that differ and those that are similar.

The DataFrame has been pre-loaded for you as titanic.

Instructions
Inside plt.subplots(), specify the nrows and ncols parameters so that there are 3 rows and 1 column.
Filter the rows where the 'pclass' column has the values 1 and generate a box plot of the 'fare' column.
Filter the rows where the 'pclass' column has the values 2 and generate a box plot of the 'fare' column.
Filter the rows where the 'pclass' column has the values 3 and generate a box plot of the 'fare' column.
"""
# Display the box plots on 3 separate rows and 1 column
fig, axes = plt.subplots(nrows=3, ncols=1)

# Generate a box plot of the fare prices for the First passenger class
titanic.loc[titanic['pclass'] == 1].plot(ax=axes[0], y='fare', kind='box')

# Generate a box plot of the fare prices for the Second passenger class
titanic.loc[titanic['pclass'] == 2].plot(ax=axes[1], y='fare', kind='box')

# Generate a box plot of the fare prices for the Third passenger class
titanic.loc[titanic['pclass'] == 3].plot(ax=axes[2], y='fare', kind='box')

# Display the plot
plt.show()
""" consol ouput or results

"""
