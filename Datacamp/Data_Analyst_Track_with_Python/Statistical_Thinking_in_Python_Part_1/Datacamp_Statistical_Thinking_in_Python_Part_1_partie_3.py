# Datacamp - Statistical Thinking in Python (Part 1)
# partie 3 : Thinking probabilistically-- Discrete variables
# Python 3.X


"""  question réponse : 4
What is the goal of statistical inference?
50xp

Why do we do statistical inference?
Possible Answers

    To draw probabilistic conclusions about what we might expect if we collected the same data again.
    1
    To draw actionable conclusions from data.
    2
    To draw more general conclusions from relatively few data or observations.
    3
    All of these. 4
"""




"""  question réponse : 2
Why do we use the language of probability?
50xp

Which of the following is not a reason why we use probabilistic language in statistical inference?
Possible Answers

    Probability provides a measure of uncertainty.
    1
    Probabilistic language is not very precise.
    2
    Data are almost never exactly the same when acquired again, and probability allows us to say how much we expect them to vary.
    3
"""




""" 
Generating random numbers using the np.random module
100xp

We will be hammering the np.random module for the rest of this course and its sequel. Actually, you will probably call functions from this module more than any other while wearing your hacker statistician hat. Let's start by taking its simplest function, np.random.random() for a test spin. The function returns a random number between zero and one. Call np.random.random() a few times in the IPython shell. You should see numbers jumping around between zero and one.

In this exercise, we'll generate lots of random numbers between zero and one, and then plot a histogram of the results. If the numbers are truly random, all bars in the histogram should be of (close to) equal height.
Instructions

    Seed the random number generator using the seed 42.
    Initialize an empty array, random_numbers, of 100,000 entries to store the random numbers. Make sure you use np.empty(100000) to do this.
    Write a for loop to draw 100,000 random numbers using np.random.random(), storing them in the random_numbers array. To do so, loop over range(100000).
    Plot a histogram of random_numbers. It is not necessary to label the axes in this case because we are just checking the random number generator.
    Hit Submit to show your plot.

"""
# Seed the random number generator
np.random.seed(42)

# Initialize random numbers: random_numbers
random_numbers = np.empty(100000) 

# Generate random numbers by looping over range(100000)
for i in range(100000):
    random_numbers[i] = np.random.random()

# Plot a histogram
_ = plt.hist(random_numbers)

# Show the plot
plt.show()

""" sortie Ipython
 
"""




""" 
The np.random module and Bernoulli trials
100xp

You can think of a Bernoulli trial as a flip of a possibly biased coin. Specifically, each coin flip has a probability p
of landing heads (success) and probability 1−p

of landing tails (failure). In this exercise, you will write a function to perform n Bernoulli trials, perform_bernoulli_trials(n, p), which returns the number of successes out of n Bernoulli trials, each of which has probability p of success. To perform each Bernoulli trial this, use the np.random.random() function, which returns a random number between zero and one.
Instructions

    Define a function with signature perform_bernoulli_trials(n, p).
        Initialize to zero a variable n_success the counter of Trues, which are Bernoulli trial successes.
        Write a for loop where you perform a Bernoulli trial in each iteration and increment the number of success if the result is True. Perform n iterations by looping over range(n).
            To perform a Bernoulli trial, choose a random number between zero and one using np.random.random(). If the number you chose is less than p, increment n_success (use the += 1 operator to achieve this).
        The function returns the number of successes n_success.

"""
def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with success probability p
    and return number of successes."""
    # Initialize number of successes: n_success
    n_success = 0


    # Perform trials
    for i in range(n):
        # Choose random number between zero and one: random_number
        random_number = np.random.random()

        # If less than p, it's a success so add one to n_success
        if random_number < p:
            n_success += 1

    return n_success
""" sortie Ipython
 
"""




""" 
How many defaults might we expect?
100xp

Let's say a bank made 100 mortgage loans. It is possible that anywhere between 0 and 100 of the loans will be defaulted upon. You would like to know the probability of getting a given number of defaults, given that the probability of a default is p = 0.05. To investigate this, you will do a simulation. You will perform 100 Bernoulli trials using the perform_bernoulli_trials() function you wrote in the previous exercise and record how many defaults we get. Here, a success is a default. (Remember that the word "success" just means that the Bernoulli trial evaluates to True, i.e., did the load recipient default?) You will do this for another 100 Bernoulli trials. And again and again until we have tried it 1000 times. Then, you will plot a histogram describing the probability of the number of defaults.
Instructions

    Seed the random number generator to 42.
    Initialize n_defaults, an empty array, using np.empty(). It should contain 1000 entries, since we are doing 1000 simulations.
    Write a for loop to compute the number of defaults per 100 loans using the perform_bernoulli_trials() function you wrote. On each loop store the result in an entry of n_defaults.
    Plot a histogram of the results with the default number of bins. Use the normed=True keyword argument so that the height of the bars of the histogram indicate probability. Be sure to label your axes.
    Show your plot.

"""
# Seed random number generator
np.random.seed(42)

# Initialize the number of defaults: n_defaults
n_defaults = np.empty(1000) 

# Compute the number of defaults
for i in range(1000):
    n_defaults[i] = perform_bernoulli_trials(100, 0.05)


# Plot the histogram with default number of bins; label your axes
_ = plt.hist(n_defaults, normed=True)
_ = plt.xlabel('n defaults / 100 for 1000')
_ = plt.ylabel('%')


# Show the plot
plt.show()
""" sortie Ipython
 
"""




""" 
Will the bank fail?
100xp

Plot the number of defaults you got from the previous exercise, in your namespace as n_defaults, as a CDF. The ecdf() function you wrote in the first chapter is available.

If interest rates are such that the bank will lose money if 10 or more of its loans are defaulted upon, what is the probability that the bank will lose money?
Instructions

    Compute the x and y values for the ECDF.
    Plot the ECDF, making sure to label the axes. Remember to include marker = '.' and linestyle = 'none'.
    Show the plot.
    Compute the total number of entries in your n_defaults array that were greater than or equal to 10. To do so, compute a boolean array that tells you whether a given entry of n_defaults is >= 10. Then sum all the entries in this array.
    The probability that the bank loses money is the fraction of n_defaults that are greater than or equal to 10. Print this result by hitting submit!

"""
# Compute ECDF: x, y
x, y = ecdf(n_defaults)

# Plot the ECDF with labeled axes
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.xlabel('Defaults')
_ = plt.ylabel('ECDF')



# Show the plot
plt.show()

# Compute the number of 100-loan simulations with 10 or more defaults: n_lose_money
n_lose_money = np.sum(n_defaults >= 10)

# Compute and print probability of losing money
print('Probability of losing money =', n_lose_money / len(n_defaults))
""" sortie Ipython
 <script.py> output:
    Probability of losing money = 0.022
In [1]: n_lose_money = np.sum(n_defaults >= 10)

In [2]: n_lose_money
Out[2]: 22

In [3]: len(n_defaults)
Out[3]: 1000
"""





""" 
Sampling out of the Binomial distribution
100xp

Compute the probability mass function for the number of defaults we would expect for 100 loans as in the last section, but instead of simulating all of the Bernoulli trials, perform the sampling using np.random.binomial(). This is identical to the calculation you did in the last set of exercises using your custom-written perform_bernoulli_trials() function, but far more computationally efficient. Given this extra efficiency, we will take 10,000 samples instead of 1000. After taking the samples, plot the CDF as last time. This CDF that you are plotting is that of the Binomial distribution.

Note: For this exercise and all going forward, the random number generator is pre-seeded for you (with np.random.seed(42)) to save you typing that each time.
Instructions

    Draw samples out of the Binomial distribution using np.random.binomial(). You should use parameters n = 100 and p = 0.05, and set the size keyword argument to 10000.
    Compute the CDF using your previously-written ecdf() function.
    Plot the CDF with axis labels. The x-axis here is the number of defaults out of 100 loans, while the y-axis is the CDF.
    Show the plot.

"""
# Take 10,000 samples out of the binomial distribution: n_defaults
n_defaults = np.random.binomial(100, 0.05, size=10000)

# Compute CDF: x, y
x, y = ecdf(n_defaults)

# Plot the CDF with axis labels
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.xlabel('Number of successes')
_ = plt.ylabel('CDF')



# Show the plot
plt.show()

""" sortie Ipython
 
"""



""" 
Plotting the Binomial PMF
100xp

As mentioned in the video, plotting a nice looking PMF requires a bit of Matplotlib trickery that we will not go into here. Instead, we will plot the PMF of the Binomial distribution as a histogram with skills you have already learned. The trick is setting up the edges of the bins to pass to plt.hist() via the bins keyword argument. We want the bins centered on the integers. So, the edges of the bins should be -0.5, 0.5, 1.5, 2.5, ... up to max(n_defaults)+0.5. You can generate an array like this using np.arange() and then subtracting 0.5 from the array.

You have already sampled out of the Binomial distribution during your exercises on loan defaults, and the resulting samples are in the Numpy array n_defaults.
Instructions

    Compute the bin edges and store the array in the variable bins.
    Use plt.hist() to plot the histogram of n_defaults with the normed=True and bins=bins keyword arguments. Assign the statement to _.
    Leave a 2% margin.
    Label your axes. Make sure to assign your plot label statements to _.
    Show the plot.

"""
# Compute bin edges: bins
bins = np.arange(0, max(n_defaults)+0.5) - 0.5

# Generate histogram
_ = plt.hist(n_defaults, normed=True, bins=bins)


# Set margins
plt.margins(0.02)

# Label axes
_ = plt.xlabel('N Succes')
_ = plt.ylabel('%')


# Show the plot
plt.show()

""" sortie Ipython
 
"""



""" 
Relationship between Binomial and Poisson distributions
100xp

You just heard that the Poisson distribution is a limit of the Binomial distribution for rare events. This makes sense if you think about the stories. Say we do a Bernoulli trial every minute for an hour, each with a success probability of 0.1. We would do 60 trials, and the number of successes is Binomially distributed, and we would expect to get about 6 successes. This is just like the Poisson story we discussed in the video, where we get on average 6 hits on a website per hour. So, the Poisson distribution with arrival rate equal to np
approximates a Binomial distribution for n Bernoulli trials with probability p of success (with n large and p

small). Importantly, the Poisson distribution is often simpler to work with because it has only one parameter instead of two for the Binomial distribution.

Let's explore these two distributions computationally. You will compute the mean and standard deviation of samples from a Poisson distribution with an arrival rate of 10. Then, you will compute the mean and standard deviation of samples from a Binomial distribution with parameters n
and p such that np=10

.
Instructions

    Draw 10,000 samples from a Poisson distribution with a mean of 10.
    Make a list of the n and p values to consider for the Binomial distribution. Choose n = [20, 100, 1000] and p = [0.5, 0.1, 0.01] so that np

is always 10.
Using np.random.binomial(), draw 10,000 samples from a Binomial distribution with each n, p pair and print the mean and standard deviation of the samples.
"""
# Draw 10,000 samples out of Poisson distribution: samples_poisson
samples_poisson = np.random.poisson(10, size=10000)

# Print the mean and standard deviation
print('Poisson:     ', np.mean(samples_poisson),
                       np.std(samples_poisson))

# Specify values of n and p to consider for Binomial: n, p
n = [20, 100, 1000]
p = [0.5, 0.1, 0.01]

# Draw 10,000 samples for each n,p pair: samples_binomial
for i in range(3):
    samples_binomial = np.random.binomial(n[i],p[i],size=10000)

    # Print results
    print('n =', n[i], 'Binom:', np.mean(samples_binomial),
                                 np.std(samples_binomial))
""" sortie Ipython
 <script.py> output:
    Poisson:      10.0186 3.14481383233
    n = 20 Binom: 9.9637 2.21634435727
    n = 100 Binom: 9.9947 3.01358124331
    n = 1000 Binom: 9.9985 3.13937856112
"""




"""  question réponse :  4
How many no-hitters in a season?
50xp

In baseball, a no-hitter is a game in which a pitcher does not allow the other team to get a hit. This is a rare event, and since the beginning of the so-called modern era of baseball (starting in 1901), there have only been 251 of them through the 2015 season in over 200,000 games. The ECDF of the number of no-hitters in a season is shown to the right. Which probability distribution would be appropriate to describe the number of no-hitters we would expect in a given season?

Note: The no-hitter data set was scraped and calculated from the data sets available at retrosheet.org (license).
Possible Answers

    Discrete uniform
    1
    Binomial
    2
    Poisson
    3
    Both Binomial and Poisson, though Poisson is easier to model and compute.
    4
    Both Binomial and Poisson, though Binomial is easier to model and compute.
    5
"""
"""
Exercise Completed 50xp

Correct! When we have rare events (low p, high n), the Binomial distribution is Poisson. This has a single parameter, the mean number of successes per time interval, in our case the mean number of no-hitters per season.
"""





""" 
Was 2015 anomalous?
100xp

1990 and 2015 featured the most no-hitters of any season of baseball (there were seven). Given that there are on average 251/115 no-hitters per season, what is the probability of having seven or more in a season?
Instructions

    Draw 10,000 samples from a Poisson distribution with a mean of 251/115 and assign to n_nohitters.
    Determine how many of your samples had a result greater than or equal to 7 and assign to n_large.
    Compute the probability, p_large, of having seven or more no-hitters by dividing by the total number of samples (10,000).
    Hit submit to print the probability that you calculated.

"""
# Draw 10,000 samples out of Poisson distribution: n_nohitters
n_nohitters = np.random.poisson(251/115, size=10000)

# Compute number that samples that are seven or greater: n_large
n_large = np.sum(n_nohitters >=7) 

# Compute probability of getting seven or more: p_large
p_large = n_large / len(n_nohitters)

# Print the result
print('Probability of seven or more no-hitters:', p_large)
""" sortie Ipython
 <script.py> output:
    Probability of seven or more no-hitters: 0.0067

"""
"""
Chapter Completed 100xp

The result is about 0.007. This means that it is not that improbable to see a 7-or-more no-hitter season in a century. We have seen two in a century and a half, so it is not unreasonable.
"""