"""
02/2017
Dataquest : Data Analyst Path
Step 2: Intermediate Python And Pandas
SubStep : Exploratory Data Visualization : Guided Project: Visualizing Earnings Based On College Majors
"""




"""
1: Introduction
In this course, we've been creating plots using pyplot and matplotlib directly.
When we want to explore a new dataset by quickly creating visualizations, using these tools directly can be cumbersome.
Thankfully, pandas has many methods for quickly generating common plots from data in DataFrames.
Like pyplot, the plotting functionality in pandas is a wrapper for matplotlib.
This means we can customize the plots when necessary by accessing the underlying Figure, Axes, and other matplotlib objects.

In this guided project, we'll explore how using the pandas plotting functionality along with the Jupyter notebook interface allows us to explore data quickly using visualizations.
If you're new to either our guided projects or Jupyter notebook in general, you can learn more here.
You can find the solutions to this guided project here.

We'll be working with a dataset on the job outcomes of students who graduated from college between 2010 and 2012.
The original data on job outcomes was released by American Community Survey, which conducts surveys and aggregates the data.
FiveThirtyEight cleaned the dataset and released it on their Github repo.

Each row in the dataset represents a different major in college and contains information on gender diversity, employment rates, median salaries, and more.
Here are some of the columns in the dataset:

Rank - Rank by median earnings (the dataset is ordered by this column).
Major_code - Major code.
Major - Major description.
Major_category - Category of major.
Total - Total number of people with major.
Sample_size - Sample size (unweighted) of full-time.
Men - Male graduates.
Women - Female graduates.
ShareWomen - Women as share of total.
Employed - Number employed.
Median - Median salary of full-time, year-round workers.
Low_wage_jobs - Number in low-wage service jobs.
Full_time - Number employed 35 hours or more.
Part_time - Number employed less than 36 hours.
Using visualizations, we can start to explore questions from the dataset like:

Do students in more popular majors make more money?
Using scatter plots
How many majors are predominantly male? Predominantly female?
Using histograms
Which category of majors have the most students?
Using bar plots
We'll explore how to do these and more while primarily working in pandas.
Before we start creating data visualizations, let's import the libraries we need and remove rows contain null values.

Instructions
Let's setup the environment by importing the libraries we need and running the necessary Jupyter magic so that plots are displayed inline.
Import pandas and matplotlib into the environment.
Run the Jupyter magic %matplotlib inline so that plots are displayed inline.
Read the dataset into a DataFrame and start exploring the data.
Read recent-grads.csv into pandas and assign the resulting DataFrame to recent_grads.
Use DataFrame.iloc[] to return the first row formatted as a table.
Use DataFrame.head() and DataFrame.tail() to become familiar with how the data is structured.
Use DataFrame.describe() to generate summary statistics for all of the numeric columns.
Drop rows with missing values. Matplotlib expects that columns of values we pass in have matching lengths and missing values will cause matplotlib to throw errors.
Look up the number of rows in recent_grads and assign the value to raw_data_count.
Use DataFrame.dropna() to drop rows containing missing values and assign the resulting DataFrame back to recent_grads.
Look up the number of rows in recent_grads now and assign the value to cleaned_data_count. If you compare cleaned_data_count and raw_data_count, you'll notice that only one row contained missing values and was dropped.
"""
# 1: Introduction
# setup :
import pandas as pd
import matplotlib as plt
%matplotlib inline
# import data
recent_grads = pd.read_csv("recent-grads.csv")
print(recent_grads.head(2))
print("------------------")
print("------------------")
recent_grads.iloc[0]
print("------------------")
print("------------------")
# visualizing data
recent_grads.head(2)
recent_grads.tail(2)
recent_grads.describe()
# Drop rows with missing values
# Number of row in the dataframe :
raw_data_count = recent_grads.count()
print(raw_data_count)
raw_data_count = len(recent_grads.index)
print("---------------")
print(raw_data_count)
# dropna row axis=1
recent_grads = recent_grads.dropna(axis=0)
cleaned_data_count = recent_grads.count()
print(cleaned_data_count)
cleaned_data_count = len(recent_grads.index)
print("---------------")
print(cleaned_data_count)
""" Console output or Results
   Rank  Major_code                           Major   Total     Men  Women  \
0     1        2419           PETROLEUM ENGINEERING  2339.0  2057.0  282.0
1     2        2416  MINING AND MINERAL ENGINEERING   756.0   679.0   77.0

  Major_category  ShareWomen  Sample_size  Employed      ...        Part_time  \
0    Engineering    0.120564           36      1976      ...              270
1    Engineering    0.101852            7       640      ...              170

   Full_time_year_round  Unemployed  Unemployment_rate  Median  P25th   P75th  \
0                  1207          37           0.018381  110000  95000  125000
1                   388          85           0.117241   75000  55000   90000

   College_jobs  Non_college_jobs  Low_wage_jobs
0          1534               364            193
1           350               257             50

[2 rows x 21 columns]
------------------
------------------
------------------
------------------
	Rank	Major_code	Major	Total	Men	Women	Major_category	ShareWomen	Sample_size	Employed	...	Part_time	Full_time_year_round	Unemployed	Unemployment_rate	Median	P25th	P75th	College_jobs	Non_college_jobs	Low_wage_jobs
0	1	2419	PETROLEUM ENGINEERING	2339.0	2057.0	282.0	Engineering	0.120564	36	1976	...	270	1207	37	0.018381	110000	95000	125000	1534	364	193
1	2	2416	MINING AND MINERAL ENGINEERING	756.0	679.0	77.0	Engineering	0.101852	7	640	...	170	388	85	0.117241	75000	55000	90000	350	257	50
2 rows × 21 columns
	Rank	Major_code	Major	Total	Men	Women	Major_category	ShareWomen	Sample_size	Employed	...	Part_time	Full_time_year_round	Unemployed	Unemployment_rate	Median	P25th	P75th	College_jobs	Non_college_jobs	Low_wage_jobs
171	172	5203	COUNSELING PSYCHOLOGY	4626.0	931.0	3695.0	Psychology & Social Work	0.798746	21	3777	...	965	2738	214	0.053621	23400	19200	26000	2403	1245	308
172	173	3501	LIBRARY SCIENCE	1098.0	134.0	964.0	Education	0.877960	2	742	...	237	410	87	0.104946	22000	20000	22000	288	338	192
2 rows × 21 columns
	Rank	Major_code	Total	Men	Women	ShareWomen	Sample_size	Employed	Full_time	Part_time	Full_time_year_round	Unemployed	Unemployment_rate	Median	P25th	P75th	College_jobs	Non_college_jobs	Low_wage_jobs
count	173.000000	173.000000	172.000000	172.000000	172.000000	172.000000	173.000000	173.000000	173.000000	173.000000	173.000000	173.000000	173.000000	173.000000	173.000000	173.000000	173.000000	173.000000	173.000000
mean	87.000000	3879.815029	39370.081395	16723.406977	22646.674419	0.522223	356.080925	31192.763006	26029.306358	8832.398844	19694.427746	2416.329480	0.068191	40151.445087	29501.445087	51494.219653	12322.635838	13284.497110	3859.017341
std	50.084928	1687.753140	63483.491009	28122.433474	41057.330740	0.231205	618.361022	50675.002241	42869.655092	14648.179473	33160.941514	4112.803148	0.030331	11470.181802	9166.005235	14906.279740	21299.868863	23789.655363	6944.998579
min	1.000000	1100.000000	124.000000	119.000000	0.000000	0.000000	2.000000	0.000000	111.000000	0.000000	111.000000	0.000000	0.000000	22000.000000	18500.000000	22000.000000	0.000000	0.000000	0.000000
25%	44.000000	2403.000000	4549.750000	2177.500000	1778.250000	0.336026	39.000000	3608.000000	3154.000000	1030.000000	2453.000000	304.000000	0.050306	33000.000000	24000.000000	42000.000000	1675.000000	1591.000000	340.000000
50%	87.000000	3608.000000	15104.000000	5434.000000	8386.500000	0.534024	130.000000	11797.000000	10048.000000	3299.000000	7413.000000	893.000000	0.067961	36000.000000	27000.000000	47000.000000	4390.000000	4595.000000	1231.000000
75%	130.000000	5503.000000	38909.750000	14631.000000	22553.750000	0.703299	338.000000	31433.000000	25147.000000	9948.000000	16891.000000	2393.000000	0.087557	45000.000000	33000.000000	60000.000000	14444.000000	11783.000000	3466.000000
max	173.000000	6403.000000	393735.000000	173809.000000	307087.000000	0.968954	4212.000000	307933.000000	251540.000000	115172.000000	199897.000000	28169.000000	0.177226	110000.000000	95000.000000	125000.000000	151643.000000	148395.000000	48207.000000
Rank                    173
Major_code              173
Major                   173
Total                   172
Men                     172
Women                   172
Major_category          173
ShareWomen              172
Sample_size             173
Employed                173
Full_time               173
Part_time               173
Full_time_year_round    173
Unemployed              173
Unemployment_rate       173
Median                  173
P25th                   173
P75th                   173
College_jobs            173
Non_college_jobs        173
Low_wage_jobs           173
dtype: int64
---------------
173
Rank                    172
Major_code              172
Major                   172
Total                   172
Men                     172
Women                   172
Major_category          172
ShareWomen              172
Sample_size             172
Employed                172
Full_time               172
Part_time               172
Full_time_year_round    172
Unemployed              172
Unemployment_rate       172
Median                  172
P25th                   172
P75th                   172
College_jobs            172
Non_college_jobs        172
Low_wage_jobs           172
dtype: int64
---------------
172
"""


"""
2: Pandas, Scatter Plots
Most of the plotting functionality in pandas is contained within the DataFrame.plot() method.
When we call this method, we specify the data we want plotted as well as the type of plot.
We use the kind parameter to specify the type of plot we want. We use x and y to specify the data we want on each axis.
ou can read about the different parameters in the documentation.


recent_grads.plot(x='Sample_size', y='Employed', kind='scatter')
If you create a new cell in jupyter notebook and run the above code, the scatter plot will be displayed immediately.
This functionality is a byproduct of running the jupyter magic %matplotlib inline.
This means we can write one line of code to generate a scatter plot, run the cell using a keyboard shortcut, inspect the plot, and repeat. The DataFrame.plot() method has a few parameters we can use for tweaking the scatter plot:


recent_grads.plot(x='Sample_size', y='Employed', kind='scatter', title='Employed vs. Sample_size', figsize=(5,10))
We can access the underlying matplotlib Axes object by assigning the return value to a variable:


ax = recent_grads.plot(x='Sample_size', y='Employed', kind='scatter')
ax.set_title('Employed vs. Sample_size')
When you run the code above in a jupyter notebook cell, the plot will be returned inline just like before.

Instructions
Generate scatter plots in separate jupyter notebook cells to explore the following relations:
Sample_size and Median
Sample_size and Unemployment_rate
Full_time and Median
ShareWomen and Unemployment_rate
Men and Median
Women and Median
Use the plots to explore the following questions:
Do students in more popular majors make more money?
Do students that majored in subjects that were majority female make more money?
Is there any link between the number of full-time employees and median salary?
"""
# 2: Pandas, Scatter Plots
recent_grads.plot(x="Sample_size",y="Median",kind='scatter')
recent_grads.plot(x="Sample_size",y="Unemployment_rate",kind='scatter')
recent_grads.plot(x="Full_time",y="Median",kind='scatter')
recent_grads.plot(x="ShareWomen",y="Unemployment_rate",kind='scatter')
recent_grads.plot(x="Men",y="Median",kind='scatter')
recent_grads.plot(x="Women",y="Median",kind='scatter')
""" Console output or Results
see plot24.png
see plot25.png
see plot26.png
see plot261.png
see plot27.png
see plot28.png
"""



"""
3: Pandas, Histograms
To explore the distribution of values in a column, we can select it from the DataFrame, call Series.plot(), and set the kind parameter to hist:


recent_grads['Sample_size'].plot(kind='hist')
The DataFrame.plot() and Series.plot() methods have many of the same parameters but are used for different use cases.
We use Series.plot() to plot a specific column and DataFrame.plot() to generate plots that use values from multiple columns.
For example, because scatter plots are generated using 2 sets of values (one for each axis), we can't create a scatter plot using Series.plot().

Unfortunately, Series.plot() doesn't contain parameters for tweaking a histogram because it was implemented to handle generating standard plots with default settings quickly.
If we want to control the binning strategy of a histogram, we should use Series.hist() instead, which contains parameters specific to customizing histograms:


recent_grads['Sample_size'].hist(bins=25, range=(0,5000))
Instructions
Generate histograms in separate jupyter notebook cells to explore the distributions of the following columns:
Sample_size
Median
Employed
Full_time
ShareWomen
Unemployment_rate
Men
Women
We encourage you to experiment with different bin sizes and ranges when generating these histograms.
Use the plots to explore the following questions:
What percent of majors are predominantly male? Predominantly female?
What's the most common median salary range?
"""
# 3: Pandas, Histograms
def hist(column):
    recent_grads[column].plot(kind='hist')
hist("Sample_size")
hist("Median")
hist("Employed")
hist("Full_time")
hist("ShareWomen")
hist("Unemployment_rate")
hist("Men")
hist("Women")
""" Console output or Results
see plot29.png
see plot30.png
see plot31.png
see plot32.png
see plot33.png
see plot34.png
see plot35.png
see plot36.png
"""




"""
4: Pandas, Scatter Matrix Plot
In the last 2 steps, we created individual scatter plots to visualize potential relationships between columns and histograms to visualize the distributions of individual columns.
A scatter matrix plot combines both scatter plots and histograms into one grid of plots and allows us to explore potential relationships and distributions simultaneously.
A scatter matrix plot consists of n by n plots on a grid, where n is the number of columns, the plots on the diagonal are histograms, and the non-diagonal plots are scatter plots.

Scatter Matrix Plot
see scatterplot_matrix_intro.png

Because scatter matrix plots are frequently used in the exploratory data analysis, pandas contains a function named scatter_matrix() that generates the plots for us.
This function is part of the pandas.tools.plotting module and needs to be imported separately.
To generate a scatter matrix plot for 2 columns, select just those 2 columns and pass the resulting DataFrame into the scatter_matrix() function.


scatter_matrix(recent_grads[['Women', 'Men']], figsize=(10,10))
While passing in a DataFrame with 2 columns returns a 2 by 2 scatter matrix plot (4 plots total), passing in one with 3 returns a 3 by 3 scatter matrix plot (16 plots total).
This means that the number of plots generated scales exponentially by a factor of 2, not linearly.
If you increase the number of columns to 4 or more, the resulting grid of plots becomes unreadable and difficult to interpret (even if you increase the plotting area using the figsize parameter).

Unfortunately, the documentation for scatter_matrix() is missing from the pandas website.
If you want to read more about the parameters the function accepts, read the comments in the source code for the function.

Instructions
Import scatter_matrix from pandas.tools.plotting
Create a 2 by 2 scatter matrix plot using the Sample_size and Median columns.
Create a 3 by 3 scatter matrix plot using the Sample_size, Median, and Unemployment_rate columns.
Explore the questions from the last few steps using these scatter matrix plots. You may need to create more scatter matrix plots.
"""
# 4: Pandas, Scatter Matrix Plot
from pandas.tools.plotting import scatter_matrix
scatter_matrix(recent_grads[['Sample_size', 'Median', 'Unemployment_rate']], figsize=(10,10))
""" Console output or Results
see plot37.png
"""




"""
5: Pandas, Bar Plots
To create bar plots in matplotlib, we had to specify many aspects of the bar plot ourselves.
We had to specify the locations, labels, lengths, and widths of the bars.
When creating bar plots using pandas, we only need specify the data we want the bars to represent and the labels for each bar.
The following code returns a bar plot of the first 5 values in the Women column:


recent_grads[:5]['Women'].plot(kind='bar')
By default, pandas will use the default labels on the x-axis for each bar (1 to n) from matplotlib.
If we instead use the DataFrame.plot.bar() method, we can use the x parameter to specify the labels and the y parameter to specify the data for the bars:

recent_grads[:5].plot(x='Major', y='Women')
Instructions
Use bar plots to compare the percentages of women (ShareWomen) from the 10 highest paying majors and from the 10 lowest paying majors.
Use bar plots to compare the unemployment rate (Unemployment_rate) from the 10 highest paying majors and from the 10 lowest paying majors.
"""
# 5: Pandas, Bar Plots
# Use bar plots to compare the percentages of women (ShareWomen) from the 10 highest paying majors and from the 10 lowest paying majors.
recent_grads[:10].plot.bar(x='Major', y='ShareWomen', legend=False)
recent_grads[163:].plot.bar(x='Major', y='ShareWomen', legend=False)
# Use bar plots to compare the unemployment rate (Unemployment_rate) from the 10 highest paying majors and from the 10 lowest paying majors.
recent_grads[:10].plot.bar(x='Major', y='Unemployment_rate', legend=False)
recent_grads[163:].plot.bar(x='Major', y='Unemployment_rate', legend=False)
""" Console output or Results
see plot37.png
see plot38.png
see plot39.png
see plot40.png

"""




"""
6: Next Steps
In this guided project, we learned how to use the plotting tools built into pandas to explore data on job outcomes.
If you head over to the documentation on plotting in pandas, you'll notice that there's built in support for many more plots.

We encourage you to keep exploring these other visualizations on your own. Here are some ideas:

Use a grouped bar plot to compare the number of men with the number of women in each category of majors.
Use a box plot to explore the distributions of median salaries and unemployment rate.
Use a hexagonal bin plot to visualize the columns that had dense scatter plots from earlier in the project.
"""
