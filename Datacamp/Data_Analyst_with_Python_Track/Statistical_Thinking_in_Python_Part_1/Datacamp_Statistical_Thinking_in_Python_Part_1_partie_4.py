# Datacamp - Statistical Thinking in Python (Part 1)
# partie 3 : Thinking probabilistically-- Continuous variables
# Python 3.X


""" question réponse : 1
Interpreting PDFs
50xp

Consider the PDF shown to the right. Which is of the following is true?
Possible Answers

    x

is more likely than not less than 10.
1
x
is more likely than not greater than 10.
2
We cannot tell from the PDF if x
is more likely to be greater than or less than 10.
3
This is not a valid PDF because it has two peaks.
4
"""

""" 
Exercise Completed 50xp

Correct! The probability is given by the area under the PDF, and there is more area to the left of 10 than to the right.
"""





""" question réponse : 
Interpreting CDFs
50xp

At right is the CDF corresponding to the PDF you considered in the last exercise. Using the CDF, what is the probability that x

is greater than 10?
Possible Answers

    0.25
    1
    0.75
    2
    3.75
    3
    15
"""

""" 
Exercise Completed 50xp

Correct! The value of the CDF at x = 10 is 0.75, so the probability that x < 10 is 0.75. Thus, the probability that x > 10 is 0.25.
"""






"""
The Normal PDF
100xp

In this exercise, you will explore the Normal PDF and also learn a way to plot a PDF of a known distribution using hacker statistics. Specifically, you will plot a Normal PDF for various values of the variance.
Instructions

    Draw 100,000 samples from a Normal distribution that has a mean of 20 and a standard deviation of 1. Do the same for Normal distributions with standard deviations of 3 and 10, each still with a mean of 20. Assign the results to samples_std1, samples_std3 and samples_std10, respectively.
    Plot a histograms of each of the samples; for each, use 100 bins, also using the keyword arguments normed=True and histtype='step'. The latter keyword argument makes the plot look much like the smooth theoretical PDF. You will need to make 3 plt.hist() calls.
    Hit submit to make a legend, showing which standard deviations you used, and show your plot! There is no need to label the axes because we have not defined what is being described by the Normal distribution; we are just looking at shapes of PDFs.

"""
# Draw 100000 samples from Normal distribution with stds of interest: samples_std1, samples_std3, samples_std10
samples_std1 = np.random.normal(20, 1, size=100000)
samples_std3 = np.random.normal(20, 3, size=100000)
samples_std10 = np.random.normal(20, 10, size=100000)

# Make histograms
_ = plt.hist(samples_std1,bins=100,normed=True,histtype='step')
_ = plt.hist(samples_std3,bins=100,normed=True,histtype='step')
_ = plt.hist(samples_std10,bins=100,normed=True,histtype='step')



# Make a legend, set limits and show plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
plt.ylim(-0.01, 0.42)
plt.show()
""" 
Exercise Completed 100xp

Great work! You can see how the different standard deviations result in PDFS of different widths. The peaks are all centered at the mean of 20.
"""





"""
The Normal CDF
100xp

Now that you have a feel for how the Normal PDF looks, let's consider its CDF. Using the samples you generated in the last exercise (in your namespace as samples_std1, samples_std3, and samples_std10), generate and plot the CDFs.
Instructions

    Use your ecdf() function to generate x and y values for CDFs: x_std1, y_std1, x_std3, y_std3 and x_std10, y_std10, respectively.
    Plot all three CDFs as dots (do not forget the marker and linestyle keyword arguments!).
    Make a 2% margin in your plot.
    Hit submit to make a legend, showing which standard deviations you used, and to show your plot. There is no need to label the axes because we have not defined what is being described by the Normal distribution; we are just looking at shapes of CDFs.

"""
# Generate CDFs
x_std1, y_std1 = ecdf(samples_std1)
x_std3, y_std3 = ecdf(samples_std3)
x_std10, y_std10 = ecdf(samples_std10)


# Plot CDFs
_ = plt.plot(x_std1, y_std1, marker='.', linestyle='none')
_ = plt.plot(x_std3, y_std3, marker='.', linestyle='none')
_ = plt.plot(x_std10, y_std10, marker='.', linestyle='none')
# Make 2% margin
plt.margins(0.02)

# Make a legend and show the plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'), loc='lower right')
plt.show()
""" 
Exercise Completed 100xp

Great work! The CDFs all pass through the mean at the 50th percentile; the mean and median of a Normal distribution are equal. The width of the CDF varies with the standard deviation.
"""





""" question réponse : 
Gauss and the 10 Deutschmark banknote
50xp

What are the mean and standard deviation, respectively, of the Normal distribution that was on the 10 Deutschmark banknote, shown to the right?
Possible Answers

    mean = 3, std = 1
    1
    mean = 3, std = 2
    2
    mean = 0.4, std = 1
    3
    mean = 0.6, std = 6
    4
"""






"""
Are the Belmont Stakes results Normally distributed?
100xp

Since 1926, the Belmont Stakes is a 1.5 mile-long race of 3-year old thoroughbred horses. Secretariat ran the fastest Belmont Stakes in history in 1973. While that was the fastest year, 1970 was the slowest because of unusually wet and sloppy conditions. With these two outliers removed from the data set, compute the mean and standard deviation of the Belmont winners' times. Sample out of a Normal distribution with this mean and standard deviation using the np.random.normal() function and plot a CDF. Overlay the ECDF from the winning Belmont times. Are these close to Normally distributed?

Note: Justin scraped the data concerning the Belmont Stakes from the Belmont Wikipedia page.
Instructions

    Compute mean and standard deviation of Belmont winners' times with the two outliers removed. The NumPy array belmont_no_outliers has these data.
    Take 10,000 samples out of a normal distribution with this mean and standard deviation using np.random.normal().
    Compute the CDF of the theoretical samples and the ECDF of the Belmont winners' data, assigning the results to x_theor, y_theor and x, y, respectively.
    Hit submit to plot the CDF of your samples with the ECDF, label your axes and show the plot.

"""
# Compute mean and standard deviation: mu, sigma
mu = np.mean(belmont_no_outliers)
sigma = np.std(belmont_no_outliers)

# Sample out of a normal distribution with this mu and sigma: samples
samples = np.random.normal(mu, sigma, size=10000)

# Get the CDF of the samples and of the data
x_theor, y_theor = ecdf(samples)
x, y = ecdf(belmont_no_outliers)


# Plot the CDFs and show the plot
_ = plt.plot(x_theor, y_theor)
_ = plt.plot(x, y, marker='.', linestyle='none')
plt.margins(0.02)
_ = plt.xlabel('Belmont winning time (sec.)')
_ = plt.ylabel('CDF')
plt.show()
""" 
Exercise Completed 100xp

The theoretical CDF and the ECDF of the data suggest that the winning Belmont times are, indeed, Normally distributed. This also suggests that in the last 100 years or so, there have not been major technological or training advances that have significantly affected the speed at which horses can run this race.
"""






"""
What are the chances of a horse matching or beating Secretariat's record?
100xp

Assume that the Belmont winners' times are Normally distributed (with the 1970 and 1973 years removed), what is the probability that the winner of a given Belmont Stakes will run it as fast or faster than Secretariat?
Instructions

    Take 1,000,000 samples from the normal distribution from the previous problem. The mean mu and standard deviation sigma are already loaded into the namespace of your IPython instance. Make sure to use the size keyword argument.
    Compute the fraction of samples that have a time less than or equal to Secretariat's time of 144 seconds.
    Print the result.

"""
# Take a million samples out of the Normal distribution: samples
samples = np.random.normal(mu, sigma, size=1000000)

# Compute the fraction that are faster than 144 seconds: prob
prob = np.sum(samples <= 144) / len(samples)

# Print the result
print('Probability of besting Secretariat:', prob)
""" sortie Ipython
<script.py> output:
    Probability of besting Secretariat: 0.000635
"""
"""
Great work! We had to take a million samples because the probability of a fast time is very low and we had to be sure to sample enough. We get that there is only a 0.06% chance of a horse running the Belmont as fast as Secretariat.
"""




""" question réponse 2
Matching a story and a distribution.
50xp

How might we expect the time between Major League no-hitters to be distributed? Be careful here: a few exercises ago, we considered the probability distribution for the number of no-hitters in a season. Now, we are looking at the probability distribution of the time between no hitters.
Possible Answers

    Normal
    1
    Exponential
    2
    Poisson
    3
    Uniform
    4
"""



""" question réponse 4
Waiting for the next Secretariat
50xp

Unfortunately, Justin was not alive when Secretariat ran the Belmont in 1973. Do you think he will get to see a performance like that? To answer this, you are interested in how many years you would expect to wait until you see another performance like Secretariat's. How is the waiting time until the next performance as good or better than Secretariat's distributed? Choose the best answer.
Possible Answers

    Normal, because the distribution of Belmont winning times are Normally distributed.
    1
    Normal, because there is a most-expected waiting time, so there should be a single peak to the distribution.
    2
    Exponential: It is very unlikely for a horse to be faster than Secretariat, so the distribution should decay away to zero for high waiting time.
    3
    Exponential: A horse as fast as Secretariat is a rare event, which can be modeled as a Poisson process, and the waiting time between arrivals of a Poisson process is Exponentially distributed.
    4
"""

""" 
Correct! The Exponential distribution describes the waiting times between rare events, and Secretariat is rare!
"""






"""
If you have a story, you can simulate it!
100xp

Sometimes, the story describing our probability distribution does not have a named distribution to go along with it. In these cases, fear not! You can always simulate it. We'll do that in this and the next exercise.

In earlier exercises, we looked at the rare event of no-hitters in Major League Baseball. Hitting the cycle is another rare baseball event. When a batter hits the cycle, he gets all four kinds of hits, a single, double, triple, and home run, in a single game. Like no-hitters, this can be modeled as a Poisson process, so the time between hits of the cycle are also Exponentially distributed.

How long must we wait to see both a no-hitter and a batter hit the cycle? The idea is that we have to wait some time for the no-hitter, and then after the no-hitter, we have to wait for hitting the cycle. Stated another way, what is the total waiting time for the arrival of two different Poisson processes? The total waiting time is the time waited for the no-hitter, plus the time waited for the hitting the cycle.

Now, you will write a function to sample out of the distribution described by this story.
Instructions

    Define a function with call signature successive_poisson(tau1, tau2, size=1) that samples the waiting time for a no-hitter and a hit of the cycle.
        Draw waiting times (size number of samples) for the no-hitter out of an exponential distribution and assign to t1.
        Draw waiting times (size number of samples) for hitting the cycle out of an exponential distribution and assign to t2.
        The function returns the sum of the waiting times for the two events.

"""
def successive_poisson(tau1, tau2, size=1):
    # Draw samples out of first exponential distribution: t1
    t1 = np.random.exponential(tau1, size=size)

    # Draw samples out of first exponential distribution: t2
    t2 = np.random.exponential(tau2, size=size)

    return t1 + t2
""" 
Great work! We'll put the function to use in the next exercise.
"""





"""
Distribution of no-hitters and cycles
100xp

Now, you'll use your sampling function to compute the waiting time to observer a no-hitter and hitting of the cycle. The mean waiting time for a no-hitter is 764 games, and the mean waiting time for hitting the cycle is 715 games.
Instructions

    Use your successive_poisson() function to draw 100,000 out of the distribution of waiting times for observing a no-hitter and a hitting of the cycle.
    Plot the PDF of the waiting times using the step histogram technique of a previous exercise. Don't forget the necessary keyword arguments. You should use bins=100, normed=True, and histtype='step'.
    Label axes.
    Show your plot.

"""
# Draw samples of waiting times: waiting_times
waiting_times = successive_poisson(764,715,100000)

# Make the histogram
_ = plt.hist(waiting_times,bins=100, normed=True, histtype='step')


# Set margins and label axes
plt.margins(0.02)
_ = plt.xlabel('Waiting Time in game')
_ = plt.ylabel('PDF')


# Show the plot
plt.show()
""" sortie Ipython

"""
"""
Great work! Notice that the PDF is peaked, unlike the waiting time for a single Poisson process. For fun (and enlightenment), I encourage you to also plot the CDF.
"""



