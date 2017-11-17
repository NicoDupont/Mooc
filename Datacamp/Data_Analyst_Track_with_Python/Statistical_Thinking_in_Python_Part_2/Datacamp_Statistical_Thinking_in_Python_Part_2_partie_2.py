# Datacamp - Statistical Thinking in Python (Part 2)
# partie 2 : Bootstrap confidence intervals
# Python 3.X


""" question réponse : 2
Getting the terminology down
50xp

Getting tripped up over terminology is a common cause of frustration in students. Unfortunately, you often will read and hear other data scientists using different terminology for bootstrap samples and replicates. This is even more reason why we need everything to be clear and consistent for this course. So, before going forward discussing bootstrapping, let's get our terminology down. If we have a data set with n
repeated measurements, a bootstrap sample is an array of length n

that was drawn from the original data with replacement. What is a bootstrap replicate?
Possible Answers

    Just another name for a bootstrap sample.
    1
    A single value of a statistic computed from a bootstrap sample.
    2
    An actual repeat of the measurements.
    3
"""

""" 

"""



""" question réponse : 5

50xp

To help you gain intuition about how bootstrapping works, imagine you have a data set that has only three points, [-1, 0, 1]. How many unique bootstrap samples can be drawn (e.g., [-1, 0, 1] and [1, 0, -1] are unique), and what is the maximum mean you can get from a bootstrap sample? It might be useful to jot down the samples on a piece of paper.

(These are too few data to get meaningful results from bootstrap procedures, but this example is useful for intuition.)
Possible Answers

    There are 3 unique samples, and the maximum mean is 0.
    1
    There are 10 unique samples, and the maximum mean is 0.
    2
    There are 10 unique samples, and the maximum mean is 1.
    3
    There are 27 unique samples, and the maximum mean is 0.
    4
    There are 27 unique samples, and the maximum mean is 1.
    5
"""

""" 
Correct! There are 27 total bootstrap samples, and one of them, [1,1,1] has a mean of 1. Conversely, 7 of them have a mean of zero.
"""




"""
Visualizing bootstrap samples
100xp

In this exercise, you will generate bootstrap samples from the set of annual rainfall data measured at the Sheffield Weather Station in the UK from 1883 to 2015. The data are stored in the Numpy array rainfall in units of millimeters (mm). By graphically displaying the bootstrap samples with an ECDF, you can get a feel for how bootstrap sampling allows probabilistic descriptions of data.
Instructions

    Write a for loop to acquire 50 bootstrap samples of the rainfall data and plot their ECDF.
        Use np.random.choice() to generate a bootstrap sample. Be sure that the length of the resampled array is len(data).
        Use the function ecdf() that you wrote in the prequel to this course to generate the x and y values for the ECDF of the bootstrap sample, and plot them. Use the color='gray' (to make gray dots) and alpha=0.1 (to make them semi-transparent, since we are overlaying so many).
    Use ecdf() to generate x and y values for the ECDF of the original rainfall data and plot them as you normally plot ECDFs.
    Label your axes and specify a 2% margin.
    Show your plot.

"""
for i in range(50):
    # Generate bootstrap sample: bs_sample
    bs_sample = np.random.choice(rainfall, size=len(rainfall))

    # Compute and plot ECDF from bootstrap sample
    x, y = ecdf(bs_sample)
    _ = plt.plot(x, y, marker='.', linestyle='none',
                 color='gray', alpha=0.1)

# Compute and plot ECDF from original data
x, y = ecdf(rainfall)
_ = plt.plot(x, y, '.')

# Make margins and label axes
plt.margins(0.02)
_ = plt.xlabel('yearly rainfall (mm)')
_ = plt.xlabel('ECDF')

# Show the plot
plt.show()
""" 
Good job! Notice how the bootstrap samples give an idea of how the distribution of rainfalls is spread.
"""




"""
Generating many bootstrap replicates
100xp

The function bootstrap_replicate_1d() from the video is available in your namespace. Now you'll write another function, draw_bs_reps(data, func, size=1), which generates many bootstrap replicates from the data set. This function will come in handy for you again and again as you compute confidence intervals and later when you do hypothesis tests.

For your reference, the bootstrap_replicate_1d() function is provided below:

def bootstrap_replicate_1d(data, func):
    return func(np.random.choice(data, size=len(data)))

Instructions

    Define a function with call signature draw_bs_reps(data, func, size=1).
        Initialize an array, bs_replicates to hold all of the bootstrap replicates using np.empty().
        Write a for loop to compute a replicate using bootstrap_replicate_1d() and stores the replicate in bs_replicates.
        Return the array of replicates.

"""
def draw_bs_reps(data, func, size=1):
    """Draw bootstrap replicates."""

    # Initialize array of replicates: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data, func)

    return bs_replicates
""" 
Good job! This function will be a workhorse for you!
"""



"""
Bootstrap replicates of the mean and the SEM
100xp

In this exercise, you will compute a bootstrap estimate of the probability distribution function of the mean annual rainfall at the Sheffield Weather Station. Remember, we are estimating the mean annual rainfall we would get if the Sheffield Weather Station could repeat all of the measurements from 1883 to 2015 over and over again. This is a probabilistic estimate of the mean. You will plot the PDF as a histogram, and you will see that it is Normal.

In fact, it can be shown theoretically that under not-too-restrictive conditions, the value of the mean will always be Normally distributed. (This does not hold in general, just for the mean and a few other statistics.) The standard deviation of this distribution, called the standard error of the mean, or SEM, is given by the standard deviation of the data divided by the square root of the number of data points. I.e., for a data set, sem = np.std(data) / np.sqrt(len(data)). Using hacker statistics, you get this same result without the need to derive it, but you will verify this result from your bootstrap replicates.
Instructions

    Draw 10,000 bootstrap replicates of the mean annual rainfall using your draw_bs_reps() function.
    Compute and print the standard error of the mean.
    Compute and print the standard deviation of your bootstrap replicates.
    Make a histogram of the replicates using the normed=True keyword argument and 50 bins. Be sure to label the axes.
    Show your plot.

"""
# Take 10,000 bootstrap replicates of the mean: bs_replicates
bs_replicates = draw_bs_reps(rainfall,np.mean,10000)

# Compute and print SEM
print(np.std(rainfall) / np.sqrt(len(rainfall)))

# Compute and print standard deviation of bootstrap replicates
print(np.std(bs_replicates))

# Make a histogram of the results
_ = plt.hist(bs_replicates, bins=50, normed=True)
_ = plt.xlabel('mean annual rainfall (mm)')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()
""" sortie Ipython
<script.py> output:
    10.5105491505
    10.4659270712

Great work! Notice that the SEM we got from the known expression and the bootstrap replicates is the same and the distribution of the bootstrap replicates of the mean is Normal.


"""



""" question réponse : 
Confidence intervals of rainfall data
50xp

A confidence interval gives bounds on the range of parameter values you might expect to get if we repeated our measurements. For named distributions, you can compute them analytically or look them up, but one of the many beautiful properties of the bootstrap method is that you can just take percentiles of your bootstrap replicates to get your confidence interval. Conveniently, you can use the np.percentile() function.

Using your bootstrap replicates you just generated to compute the 95% confidence interval. That is, give the 2.5th and 97.5th percentile of your bootstrap replicates stored as bs_replicates.
Possible Answers

    (765, 776) mm/year
    1
    (780, 821) mm/year
    2
    (761, 817) mm/year
    3
    (761, 841) mm/year
    4
"""

""" 
In [1]: conf_int = np.percentile(bs_replicates, [2.5, 97.5])

In [2]: conf_int
Out[2]: array([ 779.76992481,  820.95043233])

Correct! See, it's simple to get confidence intervals using bootstrap!

"""




"""
Bootstrap replicates of other statistics
100xp

We saw in a previous exercise the the mean is Normally distributed. This does not necessarily hold for other statistics, but no worry: as hackers, we can always take bootstrap replicates! Generate bootstrap replicates for the variance of the annual rainfall at the Sheffield Weather Station and plot the histogram of the replicates.

Here, you will make use of the draw_bs_reps() function you defined a few exercises ago. It is provided below for your reference:

def draw_bs_reps(data, func, size=1):
    return np.array([bootstrap_replicate_1d(data, func) for _ in range(size)])

Instructions

    Draw 10,000 bootstrap replicates of the variance in annual rainfall using your draw_bs_reps() function. Hint: Pass in np.var for computing the variance.
    Divide you variance replicates by 100 to put the variance in units of square centimeters for convenience.
    Make a histogram of the replicates using the normed=True keyword argument and 50 bins. Be sure to label the axes.
    Show your plot.

"""
# Generate 10,000 bootstrap replicates of the variance: bs_replicates
bs_replicates = draw_bs_reps(rainfall,np.var,10000)

# Put the variance in units of square centimeters
bs_replicates = bs_replicates / 100

# Make a histogram of the results
_ = plt.hist(bs_replicates , bins=50, normed=True)
_ = plt.xlabel('variance of annual rainfall (sq. cm)')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()
""" 
Great work! This is not normally distributed, as it has a longer tail to the right. Note that you can also compute a confidence interval on the variance, or any other statistic, using np.percentile() with your bootstrap replicates.
"""




"""
Confidence interval on the rate of no-hitters
100xp

Consider again the inter-no-hitter intervals for the modern era of baseball. Generate 10,000 bootstrap replicates of the optimal parameter τ

. Plot a histogram of your replicates and report a 95% confidence interval.
Instructions

    Generate 10,000 bootstrap replicates of τ

from the nohitter_times data using your draw_bs_reps() function. Recall that the the optimal τ
is calculated as the mean of the data.
Compute the 95% confidence interval.
Print the confidence interval.
Plot a histogram of your bootstrap replicates. Be sure to label your axes and use the normed=True keyword argument.
Show the plot.
"""
# Draw bootstrap replicates of the mean no-hitter time (equal to tau): bs_replicates
bs_replicates = draw_bs_reps(nohitter_times, np.mean, size=10000)
""" size?
"""

# Compute the 95% confidence interval: conf_int
conf_int = np.percentile(bs_replicates, [2.5, 97.5])

# Print the confidence interval
print('95% confidence interval =', conf_int, 'games')

# Plot the histogram of the replicates
_ = plt.hist(bs_replicates, bins=50, normed=True)
_ = plt.xlabel(r'$\tau$ (games)')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()
""" 
This gives you an estimate of what the typical time between no-hitters is. It could be anywhere between 660 and 870 games.
"""




"""
A function to do pairs bootstrap
100xp

As discussed in the video, pairs bootstrap involves resampling pairs of data. Each collection of pairs fit with a line, in this case using np.polyfit(). We do this again and again, getting bootstrap replicates of the parameter values. To have a useful tool for doing pairs bootstrap, you will write a function to perform pairs bootstrap on a set of x,y data.
Instructions

    Define a function with call signature draw_bs_pairs_linreg(x, y, size=1) to perform pairs bootstrap estimates on linear regression parameters.
        Use np.arange() to set up an array of indices going from 0 to len(x). These are what you will resample and use them to pick values out of the x and y arrays.
        Initialize the slope and intercept replicate arrays.
        Write a for loop to:
            Resample the indices.
            Make new x

and y
arrays using the indices you resampled.
Use np.polyfit() on the new x
and y

    arrays and store the computed slope and intercept.

Return the pair bootstrap replicates of the slope and intercept.
"""
def draw_bs_pairs_linreg(x, y, size=1):
    """Perform pairs bootstrap for linear regression."""

    # Set up array of indices to sample from: inds
    inds = np.arange(len(x))

    # Initialize replicates: bs_slope_reps, bs_intercept_reps
    bs_slope_reps = np.empty(size)
    bs_intercept_reps = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_inds = np.random.choice(inds, len(inds))
        bs_x, bs_y = x[bs_inds], y[bs_inds]
        bs_slope_reps[i], bs_intercept_reps[i] = np.polyfit(bs_x, bs_y, 1)

    return bs_slope_reps, bs_intercept_reps
""" 
Great work! This will also be useful for you going forward.
"""



"""
Pairs bootstrap of literacy/fertility data
100xp

Using the function you just wrote, perform pairs bootstrap to plot a histogram describing the estimate of the slope from the illiteracy/fertility data. Also report the 95% confidence interval of the slope.

As a reminder, draw_bs_pairs_linreg() has a function signature of draw_bs_pairs_linreg(x, y, size=1), and it returns two values: bs_slope_reps and bs_intercept_reps.
Instructions

    Use your function to take 1000 bootstrap replicates of the slope and intercept.
    Compute and print the 95% bootstrap confidence interval for the slope.
    Plot and show a histogram of the slope replicates. Be sure to label your axes. This has been done for you, so click 'Submit Answer' to see your histogram!

"""
# Generate replicates of slope and intercept using pairs bootstrap
bs_slope_reps, bs_intercept_reps = draw_bs_pairs_linreg(illiteracy, fertility, size=1000)

# Compute and print 95% CI for slope
print(np.percentile(bs_slope_reps, [2.5, 97.5]))

# Plot the histogram
_ = plt.hist(bs_slope_reps, bins=50, normed=True)
_ = plt.xlabel('slope')
_ = plt.ylabel('PDF')
plt.show()
""" sortie Ipython
<script.py> output:
    [ 0.04378061  0.0551616 ]
"""




"""
Plotting bootstrap regressions
100xp

A nice way to visualize the variability we might expect in a linear regression is to plot the line you would get from each bootstrap replicate of the slope and intercept. Do this for the first 100 of your bootstrap replicates of the slope and intercept (stored as bs_slope_reps and bs_intercept_reps). Be sure to use the appropriate plt.plot() keyword arguments: linewidth=0.5, alpha=0.2, color='red'.
Instructions

    Generate an array of x

-values consisting of 0 and 100 for the plot of the regression lines. Use the np.array() function for this.
Write a for loop in which you plot a regression line with a slope and intercept given by the pairs bootstrap replicates. Do this for 100 lines.
Make a scatter plot of the illiteracy/fertility data.
Label the axes, set a 2% margin, and show the plot. This has been done for you.
"""
# Generate array of x-values for bootstrap lines: x
x = np.array([0, 100])

# Plot the bootstrap lines
for i in range(100):
    _ = plt.plot(x, bs_slope_reps[i] * x + bs_intercept_reps[i],
                 linewidth=0.5, alpha=0.2, color='red')

# Plot the data
_ = plt.plot(illiteracy, fertility, marker='.', linestyle='none')

# Label axes, set the margins, and show the plot
_ = plt.xlabel('illiteracy')
_ = plt.ylabel('fertility')
plt.margins(0.02)
plt.show()
""" sortie Ipython
Great work! You now have some serious chops for parameter estimation. Let's move on to hypothesis testing!
"""


