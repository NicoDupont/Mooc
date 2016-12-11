# Datacamp - Statistical Thinking in Python (Part 1)
# partie 1 : Graphical exploratory data analysis
# Python 3.X


"""  question réponse : 5
Tukey's comments on EDA
50xp
Even though you probably have not read Tukey's book, I suspect you already have a good idea about his viewpoint from the video introducing you to exploratory data analysis. Which of the following quotes is not directly from Tukey?

Possible Answers
Exploratory data analysis is detective work. 1
There is no excuse for failing to plot and look. 2
The greatest value of a picture is that it forces us to notice what we never expected to see. 3
It is important to understand what you can do before you learn how to measure how well you seem to have done it. 4
Often times EDA is too time consuming, so it is better to jump right in and do your hypothesis tests. 5
"""



"""  question réponse : 3
Advantages of graphical EDA
50xp
Which of the following is not true of graphical EDA?

Possible Answers
It often involves converting tabular data into graphical form. 1
If done well, graphical representations can allow for more rapid interpretation of data. 2
A nice looking plot is always the end goal of a statistical analysis. 3
There is no excuse for neglecting to do graphical EDA. 4
"""




"""  
Plotting a histogram of iris data
100xp
For the exercises in this section, you will use a classic data set collected by botanist Edward Anderson and made famous by Ronald Fisher, one of the most prolific statisticians in history. Anderson carefully measured the anatomical properties of samples of three different species of iris, Iris setosa, Iris versicolor, and Iris virginica. The full data set is available as part of scikit-learn. Here, you will work with his measurements of petal length.

Plot a histogram of the petal lengths of his 50 samples of Iris versicolor using matplotlib/seaborn's default settings. Recall that to specify the default seaborn style, you can use sns.set(), where sns is the alias that seaborn is imported as.

The subset of the data set containing the Iris versicolor petal lengths in units of centimeters (cm) is stored in the NumPy array versicolor_petal_length. In the video, Justin plotted the histograms by using the Pandas library and indexing the dataframe to extract the desired column. Here, however, you only need to use the provided NumPy array.

As Justin did in the video, be sure to assign your plotting statements (except for plt.show()) to the dummy variable _. This is in line with the Pythonic convention and prevents unnecessary output from being displayed.

Instructions
Import matplotlib.pyplot and seaborn as their usual aliases (plt and sns).
Use Seaborn to set the plotting defaults.
Plot a histogram of the Iris versicolor petal lengths using plt.hist() and the provided NumPy array versicolor_petal_length.
Show the histogram using plt.show().
"""
 # Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns


# Set default Seaborn style
sns.set()

# Plot histogram of versicolor petal lengths
_ = plt.hist(versicolor_petal_length)

# Show histogram
plt.show()
""" sortie Ipython
l'histograme est créé à partir du numpy array : versicolor_petal_length
"""




"""  
Axis labels!
100xp
In the last exercise, you made a nice histogram of petal lengths of Iris versicolor, but you didn't label the axes! That's ok; it's not your fault since we didn't ask you to. Now, add axis labels to the plot using plt.xlabel() and plt.ylabel(). Don't forget to add units and assign both statements to _. The packages matplotlib.pyplot and seaborn are already imported with their standard aliases. This will be the case in what follows, unless specified otherwise.

Instructions
Label the axes. Don't forget that you should always include units in your axis labels. Your yy-axis label is just 'count'. Your xx-axis label is 'petal length (cm)'. The units are essential!
Redraw the plot constructed in the above steps using plt.draw(). Like with plt.show(), you do not need to assign this to _.
"""
 
# Label axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')


# Show histogram
plt.draw()
""" sortie Ipython

"""






"""  
Adjusting the number of bins in a histogram
100xp
The histogram you just made had ten bins. This is the default of Matplotlib. The "square root rule" is a commonly-used rule of thumb for choosing number of bins: choose the number of bins to be the square root of the number of samples. Plot the histogram of Iris versicolor petal lengths again, this time using the square root rule for the number of bins. You specify the number of bins using the bins keyword argument of plt.hist().

The plotting utilities are already imported and the Seaborn defaults already set. The variable you defined in the last exercise, versicolor_petal_length, is already in your namespace.

Instructions
Import NumPy as np. This gives access to the square root function, np.sqrt().
Determine how many data points you have using len().
Compute the number of bins using the square root rule.
Be sure to convert the number of bins to an integer.
Generate the histogram and make sure to use the bins keyword argument and assign the result to _.
Hit submit to plot the figure and see the fruit of your labors!
"""
 # Import NumPy
import numpy as np

# Compute number of data: n_data
n_data = len(versicolor_petal_length)

# Number of bins is the square root of number of data points: n_bins
n_bins = np.sqrt(n_data)

# Convert number of bins to integer: n_bins
n_bins= int(n_bins)

# Plot the histogram
plt.hist(versicolor_petal_length, bins=n_bins)

# Label axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')

# Show histogram
plt.show()

""" sortie Ipython
In [1]: import numpy as np

In [2]: n_data = len(versicolor_petal_length)

In [3]: n_data
Out[3]: 50

In [4]: n_bins = np.sqrt(n_data)

In [5]: n_bins
Out[5]: 7.0710678118654755

In [6]: n_bins= int(n_bins)

In [7]: n_bins
Out[7]: 7
"""



"""  
Bee swarm plot
100xp
Make a bee swarm plot of the iris petal lengths. Your x-axis should contain each of the three species, and the y-axis the petal lengths. A data frame containing the data is in your namespace as df.

For your reference, the code Justin used to create the bee swarm plot in the video is provided below:

_ = sns.swarmplot(x='state', y='dem_share', data=df_swing)

_ = plt.xlabel('state')

_ = plt.ylabel('percent of vote for Obama')

plt.show()

In the IPython Shell, you can use sns.swarmplot? or help(sns.swarmplot) for more details on how to make bee swarm plots using seaborn.

Instructions
In the IPython Shell, inspect the dataframe df using df.head(). This will let you identify which column heading names you need to pass as the x and y keyword arguments in your call to sns.swarmplot().
Use sns.swarmplot() to make a bee swarm plot from the data frame containing the Fisher iris data set, df.
Label the axes.
Show your plot.
"""
 # Create bee swarm plot with Seaborn's default settings
sns.set()
_ = sns.swarmplot(x='species', y='petal length (cm)', data=df)

# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm)')

# Show the plot
plt.show()
""" sortie Ipython
In [1]: df.head()
Out[1]: 
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  \
0                5.1               3.5                1.4               0.2   
1                4.9               3.0                1.4               0.2   
2                4.7               3.2                1.3               0.2   
3                4.6               3.1                1.5               0.2   
4                5.0               3.6                1.4               0.2   

  species  
0  setosa  
1  setosa  
2  setosa  
3  setosa  
4  setosa  
"""




"""  question réponse :3
Interpreting a bee swarm plot
50xp
Which of the following conclusions could you draw from the bee swarm plot of iris petal lengths you generated in the previous exercise? For your convenience, the bee swarm plot is regenerated and shown to the right.

Possible Answers
All I. versicolor petals are shorter than I. virginica petals. 1
I. setosa petals have a broader range of lengths than the other two species. 2
I. virginica petals tend to be the longest, and I. setosa petals tend to be the shortest of the three species. 3
I. versicolor is a hybrid of I. virginica and I. setosa. 4
"""





"""  
Computing the ECDF
100xp
In this exercise, you will write a function that takes as input a 1D array of data and then returns the x and y values of the ECDF. You will use this function over and over again throughout this course and its sequel. ECDFs are among the most important plots in statistical analysis. You can write your own function, foo(x,y) according to the following skeleton:

def foo(a,b):
    """State what function does here"""
    # Computation performed here
    return x, y
The function foo() above takes two arguments a and b and returns two values x and y. The function header def foo(a,b): contains the function signature foo(a,b), which consists of the function name, along with its parameters. For more on writing your own functions, see DataCamp's course Python Data Science Toolbox (Part 1) here!

Instructions
Define a function with the signature ecdf(data). Within the function definition,
Compute the number of data points, n, using the len() function.
The xx-values are the sorted data. Use the np.sort() function to perform the sorting.
The yy data of the ECDF go from 1/n to 1 in equally spaced increments. You can construct this using np.arange() and then dividing by n.
The function returns the values x and y.
"""
 def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, len(x)+1) / len(x)

    return x, y




"""  
Plotting the ECDF
100xp
You will now use your ecdf() function to compute the ECDF for the petal lengths of Anderson's Iris versicolor flowers. You will then plot the ECDF. Recall that your ecdf() function returns two arrays so you will need to unpack them. An example of such unpacking is x, y = foo(data), for some function foo().

Instructions
Use ecdf() to compute the ECDF of versicolor_petal_length. Unpack the output into x_vers and y_vers.
Plot the ECDF as dots. Remember to include marker = '.' and linestyle = 'none' as arguments inside plt.plot(). Assign the result to _.
Set the margins of the plot with plt.margins() so that no data points are cut off. Use a 2% margin. Like plt.show() and plt.draw(), the plt.margins() does not need to be assigned to _.
Label the axes. You can label the y-axis 'ECDF'.
Show your plot.
"""
 # Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)

# Generate plot
_ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')

# Make the margins nice
plt.margins(0.02)

# Label the axes
_ = plt.xlabel('Petal length')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()




"""  
Comparison of ECDFs
100xp
ECDFs also allow you to compare two or more distributions (though plots get cluttered if you have too many). Here, you will plot ECDFs for the petal lengths of all three iris species. You already wrote a function to generate ECDFs so you can put it to good use!

To overlay all three ECDFs on the same plot, you can use plt.plot() three times, once for each ECDF. Remember to include marker='.' and linestyle=none as arguments inside plt.hist().

Instructions
Compute ECDFs for each of the three species using your ecdf() function. The variables setosa_petal_length, versicolor_petal_length, and virginica_petal_length are all in your namespace. Unpack the ECDFs into x_set, y_set, x_vers, y_vers and x_virg, y_virg, respectively.
Plot all three ECDFs on the same plot as dots. To do this, you will need three plt.plot() commands. Assign the result of each to _.
Specify 2% margins.
Hit submit to add a legend and axis labels and to see all ECDFs!
"""
 # Compute ECDFs
x_set, y_set = ecdf(setosa_petal_length)
x_vers, y_vers = ecdf(versicolor_petal_length)
x_virg, y_virg = ecdf(virginica_petal_length)

# Plot all ECDFs on the same plot
_ = plt.plot(x_set, y_set, marker='.', linestyle='none')
_ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')
_ = plt.plot(x_virg, y_virg, marker='.', linestyle='none')

# Make nice margins
plt.margins(0.02)

# Annotate the plot
plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()