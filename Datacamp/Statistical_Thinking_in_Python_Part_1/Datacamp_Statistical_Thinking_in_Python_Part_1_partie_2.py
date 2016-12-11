# Datacamp - Statistical Thinking in Python (Part 1)
# partie 2 : Quantitative exploratory data
# Python 3.X


"""  question réponse : 2
 Means and medians
50xp
Which one of the following statements is true about means and medians?

Possible Answers
An outlier can significantly affect the value of both the mean and the median. 1
An outlier can significantly affect the value of the mean, but not the median. 2
Means and medians are in general both robust to single outliers. 3
The mean and median are equal if there is an odd number of data points. 4
"""



""" 
 Computing means
100xp
The mean of all of all measurements gives an indication of the typical magnitude of a measurement. It is computed using np.mean().

Instructions
Compute the mean petal length of Iris versicolor from Anderson's classic data set. The variable versicolor_petal_length is provided in your namespace. Assign the mean to mean_length_vers.
Hit submit to print the result.
"""
# Compute the mean: mean_length_vers
mean_length_vers = np.mean(versicolor_petal_length)
# Print the result with some nice formatting
print('I. versicolor:', mean_length_vers, 'cm')
"""  sortie Ipython
<script.py> output:
    I. versicolor: 4.26 cm
"""




""" 
 Computing percentiles
100xp
In this exercise, you will compute the percentiles of petal length of Iris versicolor.

Instructions
Create percentiles, a Numpy array of percentiles you want to compute. These are the 2.5th, 25th, 50th, 75th, and 97.5th. You can do so by creating a list containing these ints/floats and convert the list to a Numpy array using np.array().
Use np.percentile() to compute the percentiles of the petal lengths from the Iris versicolor samples. The variable versicolor_petal_length is in your namespace.
Print the percentiles.
"""
# Specify array of percentiles: percentiles
percentiles = np.array([2.5,25, 50, 75, 97.5])

# Compute percentiles: ptiles_vers
ptiles_vers = np.percentile(versicolor_petal_length, percentiles)

# Print the result
print(ptiles_vers)
"""  sortie Ipython
In [1]: percentiles = np.array([2.5,25, 50, 75, 97.5])

In [2]: percentiles
Out[2]: array([  2.5,  25. ,  50. ,  75. ,  97.5])

<script.py> output:
    [ 3.3     4.      4.35    4.6     4.9775]
"""



""" 
 Comparing percentiles to ECDF
100xp
To see how the percentiles relate to the ECDF, you will plot the percentiles of Iris versicolor petal lengths you calculated in the last exercise on the ECDF plot you generated in chapter 1. The percentile variables from the previous exercise are available in the workspace as ptiles_vers and percentiles.

Note that to ensure the Y-axis of the ECDF plot remains between 0 and 1, you will need to rescale the percentiles array accordingly - in this case, dividing it by 100.

Instructions
Plot the percentiles as red diamonds on the ECDF. Pass the x and y co-ordinates as positional arguments. Use marker='D', color='red' and linestyle='none' keyword arguments.
Display the plot.
"""
# Plot the ECDF
_ = plt.plot(x_vers, y_vers, '.')
plt.margins(0.02)
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Overlay percentiles as red diamonds.
_ = plt.plot(ptiles_vers, percentiles/100, marker='D', color='red',
         linestyle='none')

# Show the plot
plt.show()
"""  sortie Ipython

"""



""" 
Box-and-whisker plot
100xp
Making a box plot for the petal lengths is unnecessary because the iris data set is not too large and the bee swarm plot works fine. However, it is always good to get some practice. Make a box plot of the iris petal lengths. You have a Pandas data frame, df, which contains the petal length data, in your namespace. Inspect the data frame df in the IPython shell using df.head() to make sure you know what the pertinent columns are.

For your reference, the code used to produce the box plot in the video is provided below:

_ = sns.boxplot(x='east_west', y='dem_share', data=df_all_states)

_ = plt.xlabel('region')

_ = plt.xlabel('percent of vote for Obama')

In the IPython Shell, you can use sns.boxplot? or help(sns.boxplot) for more details on how to make box plots using seaborn.

Instructions
The set-up is exactly the same as for the bee swarm plot; you just call sns.boxplot() with the same keyword arguments as you would sns.swarmplot().
Don't forget to label your axes!
Display the figure using the normal call. 
"""
# Create box plot with Seaborn's default settings
_ = sns.boxplot(x='species', y='petal length (cm)', data=df)

# Label the axes
_ = plt.xlabel('Species')
_ = plt.ylabel('petal length (cm)')

# Show the plot
plt.show()

"""  sortie Ipython

"""


""" 
 Computing the variance
100xp
It is important to have some understanding of what commonly-used functions are doing under the hood. Though you may already know how to compute variances, this is a beginner course that does not assume so. In this exercise, we will explicitly compute the variance of the petal length of Iris veriscolor using the equations discussed in the videos. We will then use np.var() to compute it.

Instructions
Create an array that is the difference between the petal lengths and the mean petal length. The variable versicolor_petal_length is already in your namespace as a NumPy array so you can take advantage of NumPy's vectorized operations.
Square each element in this array.
Compute the mean of the elements in this array.
Compute the variance using np.var().
Print both variance_explicit and variance_np in one print call to make sure they are consistent.
"""
# Array of differences to mean: differences
differences = versicolor_petal_length - np.mean(versicolor_petal_length)

# Square the differences: diff_sq
diff_sq = differences ** 2

# Compute the mean square difference: variance_explicit
variance_explicit = np.mean(diff_sq)

# Compute the variance using Numpy: variance_np
variance_np = np.var(versicolor_petal_length)

# Print the results
print(variance_explicit, variance_np)
"""  sortie Ipython
<script.py> output:
    0.2164 0.2164
"""




""" 
 The standard deviation and the variance
100xp
As mentioned in the video, the standard deviation is the square root of the variance. You will see this for yourself by computing the standard deviation using np.std() and comparing it to what you get by computing the variance with np.var() and then computing the square root.

Instructions
Compute the variance of the data in the versicolor_petal_length array using np.var().
Print the square root of this value.
Compute the standard deviation of the data in the versicolor_petal_length array using np.std() and print the result.
"""
# Compute the variance: variance
variance = np.var(versicolor_petal_length)

# Print the square root of the variance
print(np.sqrt(variance))

# Print the standard deviation
print(np.std(versicolor_petal_length))
"""  sortie Ipython
<script.py> output:
    0.465188133985
    0.465188133985
"""



""" 
 Scatter plots
100xp
When you made bee swarm plots, box plots, and ECDF plots in previous exercises, you compared the petal lengths of different species of iris. But what if you want to compare two properties of a single species? This is exactly what we will do in this exercise. We will make a scatter plot of the petal length and width measurements of Anderson's Iris versicolor flowers. If the flower scales (that is, it preserves its proportion as it grows), we would expect the length and width to be correlated.

For your reference, the code used to produce the scatter plot in the video is provided below:

_ = plt.plot(total_votes/1000, dem_share, marker='.', linestyle='none')

_ = plt.xlabel('total votes (thousands)')

_ = plt.ylabel('percent of vote for Obama')

Instructions
Use plt.plot() with the appropriate keyword arguments to make a scatter plot of versicolor petal length (x-axis) versus petal width (y-axis). The variables versicolor_petal_length and versicolor_petal_width are already in your namespace. Do not forget to use the marker and linestyle keyword arguments.
Specify 2% margins so no data are cut off.
Label the axes.
Display the plot.
"""
# Make a scatter plot
_ = plt.plot(versicolor_petal_length, versicolor_petal_width, marker='.', linestyle='none')


# Set margins
_ = plt.margins(0.02)

# Label the axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('petal width (cm)')

# Show the result
plt.show()
"""  sortie Ipython

"""




""" question réponse : 3
 Variance and covariance by looking
50xp
Consider four scatter plots of xx-yy data, appearing to the right. Which has, respectively,

the highest variance in the variable xx,
the highest covariance,
negative covariance?
Possible Answers
a, c, b 1
d, c, a 2
d, c, b 3
d, d, b 4
"""



""" 
 Computing the covariance
100xp
The covariance may be computed using the Numpy function np.cov(). For example, we have two sets of data x and y, np.cov(x, y) returns a 2D array where entries [0,1] and [1,0] are the covariances. Entry [0,0] is the variance of the data in x, and entry [1,1] is the variance of the data in y. This 2D output array is called the covariance matrix, since it organizes the self- and covariance.

To remind you how the I. versicolor petal length and width are related, we include the scatter plot you generated in a previous exercise.

Instructions
Use np.cov() to compute the covariance matrix for the petal length and width of I. versicolor. The Numpy arrays versicolor_petal_length and versicolor_petal_width are in your namespace.
Print the covariance matrix.
Extract the covariance from entry [0,1] of the covariance matrix. Note that by symmetry, entry [1,0] is the same as entry [0,1].
Print the covariance.
"""
# Compute the covariance matrix: covariance_matrix
covariance_matrix = np.cov(versicolor_petal_length,versicolor_petal_width)

# Print covariance matrix
print(covariance_matrix)

# Extract covariance of length and width of petals: petal_cov
petal_cov = covariance_matrix[0,1]

# Print the length/width covariance
print(petal_cov)
"""  sortie Ipython
<script.py> output:
    [[ 0.22081633  0.07310204]
     [ 0.07310204  0.03910612]]
    0.0731020408163
"""




""" 
 Computing the Pearson correlation coefficient
100xp
As mentioned in the video, the Pearson correlation coefficient, also called the Pearson r, is often easier to interpret than the covariance. It is computed using the np.corrcoef() function. Like np.cov(), it takes two arrays as arguments and returns a 2D array. Entries [0,0] and [1,1] are necessarily equal to 1 (can you think about why?), and the value we are after is entry [0,1].

In this exercise, you will write a function, pearson_r(x, y) that takes in two arrays and returns the Pearson correlation coefficient. You will then use this function to compute it for the petal lengths and widths of I. versicolor.

Again, we include the scatter plot you generated in a previous exercise to remind you how the petal width and length are related.

Instructions
Define a function with signature pearson_r(x, y).
Use np.corrcoef() to compute the correlation matrix of x and y (pass them to np.corrcoef() in that order).
The function returns entry [0,1] of the correlation matrix.
Compute the Pearson correlation between the data in the arrays versicolor_petal_length and versicolor_petal_width.
Print the result.
"""
def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x,y) 

    # Return entry [0,1]
    return corr_mat[0,1]

# Compute Pearson correlation coefficient for I. versicolor: r
r = pearson_r(versicolor_petal_length, versicolor_petal_width)

# Print the result
print(r)
"""  sortie Ipython
<script.py> output:
    0.786668088523
"""


