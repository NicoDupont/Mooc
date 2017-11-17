# Datacamp - Statistical Thinking in Python (Part 2)
# partie 1 : Parameter estimation by optimization
# Python 3.X


"""
How often do we get no-hitters?
100xp

The number of games played between each no-hitter in the modern era (1901-2015) of Major League Baseball is stored in the array nohitter_times.

If you assume that no-hitters are described as a Poisson process, then the time between no-hitters is Exponentially distributed. As you have seen, the Exponential distribution has a single parameter, which we will call τ
, the typical interval time. The value of the parameter τ

that makes the exponential distribution best match the data is the mean interval time (where time is in units of number of games) between no-hitters.

Compute the value of this parameter from the data. Then, use np.random.exponential() to "repeat" the history of Major League Baseball by drawing inter-no-hitter times from an exponential distribution with the τ

you found and plot the histogram as an approximation to the PDF.
Instructions

    Seed the random number generator with 42.
    Compute the mean time (in units of number of games) between no-hitters.
    Draw 100,000 samples from an Exponential distribution with the parameter you computed from the mean of the inter-no-hitter times.
    Plot the theoretical PDF using plt.hist(). Remember to use keyword arguments bins=50, normed=True, and histtype='step'. Be sure to label your axes.
    Show your plot.

"""
# Seed random number generator
np.random.seed(42)

# Compute mean no-hitter time: tau
tau = np.mean(nohitter_times)

# Draw out of an exponential distribution with parameter tau: inter_nohitter_time
inter_nohitter_time = np.random.exponential(tau, 100000)

# Plot the PDF and label axes
_ = plt.hist(inter_nohitter_time,
             bins=50, normed=True, histtype='step')
_ = plt.xlabel('Games between no-hitters')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()
""" 
Nice work! We see the typical shape of the Exponential distribution, going from a maximum at 0 and decaying to the right.
"""




"""
Do the data follow our story?
100xp

You have modeled no-hitters using an Exponential distribution. Create an ECDF of the real data. Overlay the theoretical CDF with the ECDF from the data. This helps you to verify that the Exponential distribution describes the observed data.

It may be helpful to remind yourself of the function you created in the previous course to compute the ECDF.
Instructions

    Compute an ECDF from the actual time between no-hitters (nohitter_times). You can use the ecdf() function you wrote in the prequel course.
    Create a CDF from the samples you took in the last exercise (inter_nohitter_time).
    Plot the CDF as a line. Then overlay the ECDF of the real data as points.
    Set a 2% margin on the plot and label the axes.
    Show the plot.

"""
# Create an ECDF from real data: x, y
x, y = ecdf(nohitter_times)

# Create a CDF from theoretical samples: x_theor, y_theor
x_theor, y_theor = ecdf(inter_nohitter_time)

# Overlay the plots
plt.plot(x_theor, y_theor)
plt.plot(x, y, marker='.', linestyle='none')

# Margins and axis labels
plt.margins(0.02)
plt.xlabel('Games between no-hitters')
plt.ylabel('CDF')

# Show the plot
plt.show()

""" 
It looks like no-hitters in the modern era of Major League Baseball are Exponentially distributed. Based on the story of the Exponential distribution, this suggests that they are a random process; when a no-hitter will happen is independent of when the last no-hitter was.

"""




"""
How is this parameter optimal?
100xp

Now sample out of an exponential distribution with τ
being twice as large as the optimal τ. Do it again for τ half as large. Make CDFs of these samples and overlay them with your data. You can see that they do not reproduce the data as well. Thus, the τ

you computed from the mean inter-no-hitter times is optimal in that it best reproduces the data.

Note: In this and all subsequent exercises, the random number generator is pre-seeded for you to save you some typing.
Instructions

    Take 10,000 samples out of an Exponential distribution with parameter τ1/2=τ/2

.
Take 10,000 samples out of an Exponential distribution with parameter τ2=2τ
.
Generate CDFs from these to sets of samples.
Add these two CDFs as lines to your plot.
Show the plot.
"""
# Plot the theoretical CDFs
plt.plot(x_theor, y_theor)
plt.plot(x, y, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('Games between no-hitters')
plt.ylabel('CDF')

# Take samples with half tau: samples_half
samples_half = np.random.exponential(tau/2, 10000)

# Take samples with double tau: samples_double
samples_double = np.random.exponential(tau*2, 10000)

# Generate CDFs from these samples
x_half, y_half = ecdf(samples_half)
x_double, y_double = ecdf(samples_double)

# Plot these CDFs as lines
_ = plt.plot(x_half, y_half)
_ = plt.plot(x_double, y_double)

# Show the plot
plt.show()
""" 
Great work! Notice how the value of tau given by the mean matches the data best. In this way, tau is an optimal parameter.
"""




"""
EDA of literacy/fertility data
100xp

In the next few exercises, we will look at the correlation between female literacy and fertility (defined as the average number of children born per woman) throughout the world. For ease of analysis and interpretation, we will work with the illiteracy rate.

It is always a good idea to do some EDA ahead of our analysis. To this end, plot the fertility versus illiteracy and compute the Pearson correlation coefficient. The Numpy array illiteracy has the illiteracy rate among females for most of the world's nations. The array fertility has the corresponding fertility data.

Here, it may be useful to refer back to the function you wrote in the previous course to compute the Pearson correlation coefficient.
Instructions

    Plot fertility (y-axis) versus illiteracy (x-axis) as a scatter plot.
    Set a 2% margin.
    Compute and print the Pearson correlation coefficient between illiteracy and fertility.

"""
# Plot the illiteracy rate versus fertility
_ = plt.plot(illiteracy, fertility, marker='.', linestyle='none')

# Set the margins and label axes
plt.margins(0.02)
_ = plt.xlabel('percent illiterate')
_ = plt.ylabel('fertility')

# Show the plot
plt.show()

# Show the Pearson correlation coefficient
print(pearson_r(illiteracy, fertility))
""" sortie Ipython
You can see the correlation between illiteracy and fertility by eye, and by the substantial Pearson correlation coefficient of 0.8. It is difficult to resolve in the scatter plot, but there are many points around near-zero illiteracy and about 1.8 children/woman.
"""




"""
Linear regression
100xp

We will assume that fertility is a linear function of the female illiteracy rate. That is, i=af+b
, where a is the slope and b

is the intercept. We can think of the intercept as the minimal fertility rate, probably somewhere between one and two. The slope tells us how the fertility rate varies with illiteracy. We can find the best fit line using np.polyfit().

Plot the data and the best fit line. Print out the slope and intercept. (Think: what are their units?)
Instructions

    Compute the slope and intercept of the regression line using np.polyfit().
    Print out the slope and intercept from the linear regression.
    To plot the best fit line, choose x values that consist of 0 and 100 using np.array(). Then, compute the theoretical values of y based on your regression parameters. I.e., y = a * x + b.
    Plot the data and the regression line on the same plot. Be sure to label your axes.
    Hit submit to display your plot.

"""
# Plot the illiteracy rate versus fertility
_ = plt.plot(illiteracy, fertility, marker='.', linestyle='none')
plt.margins(0.02)
_ = plt.xlabel('percent illiterate')
_ = plt.ylabel('fertility')

# Perform a linear regression using np.polyfit(): a, b
a, b = np.polyfit(illiteracy,fertility,1)

# Print the results to the screen
print('slope =', a, 'children per woman / percent illiterate')
print('intercept =', b, 'children per woman')

# Make theoretical line to plot
x = np.array([0,100])
y = a * x + b

# Add regression line to your plot
_ = plt.plot(x, y)

# Draw the plot
plt.show()
""" sortie Ipython
<script.py> output:
    slope = 0.0497985480906 children per woman / percent illiterate
    intercept = 1.88805061064 children per woman
"""




"""
How is it optimal?
100xp

The function np.polyfit() that you used to get your regression parameters finds the optimal slope and intercept. It is optimizing the sum of the squares of the residuals, also known as RSS (for residual sum of squares). In this exercise, you will plot the function that is being optimized, the RSS, versus the slope parameter a. To do this, fix the intercept to be what you found in the optimization. Then, plot the RSS vs. the slope. Where is it minimal?
Instructions

    Specify which values of the slope for which to compute the RSS. Use np.linspace() to get 200 points in the range between 0 and 0.1.
    Initialize an array, rss, to contain the RSS using np.empty_like().
    Write a for loop to compute the sum of RSS of the slope. Hint: the RSS is given by np.sum((y_data - a * x_data - b)**2). The variable b you computed in the last exercise is already in your namespace.
    Plot the RSS versus slope. Be sure to label your axes.
    Show your plot.

"""
# Specify slopes to consider: a_vals
a_vals = np.linspace(0,0.1,200)

# Initialize sum of square of residuals: rss
rss = np.empty_like(a_vals)

# Compute sum of square of residuals for each value of a_vals
for i, a in enumerate(a_vals):
    rss[i] = np.sum((fertility - a * illiteracy - b)**2)

# Plot the RSS
plt.plot(a_vals, rss, '-')
plt.xlabel('slope (children per woman / percent illiterate)')
plt.ylabel('sum of square of residuals')

plt.show()
""" sortie Ipython
Great work! Notice that the minimum on the plot, that is the value of the slope that gives the minimum sum of the square of the residuals, is the same value you got when performing the regression.
"""




""" question réponse : 4
The importance of EDA
50xp

Why should exploratory data analysis be the first step in an analysis of data (after getting your data imported and cleaned, of course)?
Possible Answers

    You can be protected from misinterpretation of the type demonstrated by Anscombe's quartet.
    1
    EDA provides a good starting point for planning the rest of your analysis.
    2
    EDA is not really any more difficult than any of the subsequent analysis, so there is no excuse for not exploring the data.
    3
    All of these reasons!
    4
"""

""" 
Yes! Always do EDA as you jump into a data set.
"""




"""
Linear regression on appropriate Anscombe data
100xp

For practice, perform a linear regression on the data set from Anscombe's quartet that is most reasonably interpreted with linear regression.
Instructions

    Compute the parameters for the slope and intercept using np.polyfit(). The Anscombe data are stored in the arrays x and y.
    Print the slope and intercept.
    Generate theoretical x

and y data from the linear regression. Your x
values should consist of 3 and 15.
Plot the Anscombe data as a scatter plot and the theoretical line.
Label the axes (just x
and y
will do).
Show your plot.
"""
# Perform linear regression: a, b
a, b = np.polyfit(x,y,1)

# Print the slope and intercept
print(a, b)

# Generate theoretical x and y data: x_theor, y_theor
x_theor = np.array([3, 15])
y_theor = a * x_theor + b

# Plot the Anscombe data and theoretical line
_ = plt.plot(x, y,marker='.', linestyle='none')
_ = plt.plot(x_theor, y_theor)

# Label the axes
plt.xlabel('x')
plt.ylabel('y')

# Show the plot
plt.show()
""" sortie Ipython
<script.py> output:
    0.500090909091 3.00009090909

 Great work! You're getting to be a linear regression pro!
"""




"""
Linear regression on all Anscombe data
100xp

Now, to verify that all four of the Anscombe data sets have the same slope and intercept from a linear regression, you will compute the slope and intercept for each set. The data are stored in lists; anscombe_x = [x1, x2, x3, x4] and anscombe_y = [y1, y2, y3, y4], where, for example, x2 and y2 are the x
and y

values for the second Anscombe data set.
Instructions

    Write a for loop to do the following for each Anscombe data set.
        Compute the slope and intercept.
        Print the slope and intercept.

"""
# Iterate through x,y pairs
for x, y in zip(anscombe_x, anscombe_y):
    # Compute the slope and intercept: a, b
    a, b = np.polyfit(x,y,1)

    # Print the result
    print('slope:', a, 'intercept:', b)

""" 
Great work! Indeed, they all have the same slope and intercept.

<script.py> output:
    slope: 0.500090909091 intercept: 3.00009090909
    slope: 0.5 intercept: 3.00090909091
    slope: 0.499727272727 intercept: 3.00245454545
    slope: 0.499909090909 intercept: 3.00172727273


"""