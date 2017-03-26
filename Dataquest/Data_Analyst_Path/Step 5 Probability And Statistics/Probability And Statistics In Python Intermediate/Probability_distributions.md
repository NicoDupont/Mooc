03/2017  
Dataquest : Data Analyst Path  
Step 5: Probability and Statistics  
SubStep : Probability and Statistics in Python: Intermediate : Probability distributions    
lundi, 20. mars 2017 15:10       

---
# 1: The Dataset  

In the last mission, we looked at calculating probabilities. In this mission, we'll construct probability distributions. But first, let's look at the dataset we'll be using.  

In many countries, there are bikesharing programs where anyone can rent a bike from a depot, and return it at other depots throughout a city. There is one such program in Washington, D.C., in the US. We'll be looking at the number of bikes that were rented by day. Here are the relevant columns:  

 - dteday -- the date that we're looking at.
 - cnt -- the total number of bikes rented.
 
This data was collected by Hadi Fanaee-T at the University of Porto, and can be downloaded here.    

---
# 2: Binomial Distributions  

In the last mission, we defined pp as the probability of an outcome occurring, and qq as the probability of it not occurring, where q=1−pq=1−p. These types of probabilites are known as binomial -- there are two values, which add to 1 collectively. There's a 100% chance of one outcome or the other occurring.  

Many commonly occurring events can be expressed in terms of binomial outcomes -- a coin flip, winning a football game, the stock market going up, and more.  

When we deal with binomial probabilities, we're often interested in the chance of a certain outcome happening in a sequence. We want to know what the chances are of our favorite football team winning 5 of its next 6 games, and the stock market going up in 4 of the next 6 days.  

The same interest applies when we're analyzing data. Companies and researchers conduct experiments every day. These can range from testing whether changing the button color on your webpage increases conversion rate to seeing if a new drug increases patient recovery rate.  

The core of these tests is the idea of a binomial distribution -- we want to know how many visitors out of 100 would normally sign up for our website, and we want to know if changing our button color affected that probability.  

One easy way to visualize binomials is a binomial distribution. Given N events, it plots the probabilities of getting different numbers of successful outcomes.    


---
# 3: Bikesharing Distribution  

Let's say we're working for the mayor of Washington, DC, Muriel Bowser. She wants to know on how many days out of the next 30 we can expect more than 5000 riders.  

Rather than give her an exact number, which may not be accurate, we can hedge our bets with a probability distribution. This will show her all the possibilities, along with probabilities for each.  

First, we have to find the probability of there being more than 5000 riders in a single day.    

#### Instructions :

 - Find the probability of there being more than 5000 riders in a single day (using the cnt column).
	- Assign the result to prob_over_5000.
 
```python
import pandas
bikes = pandas.read_csv("bike_rental_day.csv")
days_over_threshold = bikes[bikes["cnt"] > 5000].shape[0]
total_days = bikes.shape[0]
prob_over_5000 = days_over_threshold / total_days
print(prob_over_5000)
```  

#### Results :  



---
# 4: Computing The Distribution  

We now know that the probability is about .39 that there are more than 5000 riders in a single day. In the last mission, we figured out how to find the probability of k outcomes out of N events occurring. We'll need to use this to build up a list of probabilities.  

The formula we used in the last mission was:   


see img/img6.png
(pk∗qN−k)∗N!k!(N−k)!


#### Instructions :

 - Using the knowledge from the last mission, create a function that can compute the probability of k outcomes out of N events occurring.
 - Use the function to find the probability of each number of outcomes in outcome_counts occurring.
	- An outcome is a day where there are more than 5000 riders, with p=.39p.  
	- You should have a list with 31 items, where the first item is the probability of 0 days out of 30 with more than 5000 riders, the second is the probability of 1 day out of 30, and so on, up to 30 days out of 30.
	- Assign the list to outcome_probs.
 
```python
import math

# Each item in this list represents one k, starting from 0 and going up to and including 30.
outcome_counts = list(range(31))

p = 0.39
q = 1 - p

def find_prob_single_combinations(p, q, k, n):
    prob = (p ** k) * (q ** (n-k))
    return prob

def find_outcome_combinations(N, k):
    # Calculate the numerator of our formula.
    numerator = math.factorial(N)
    # Calculate the denominator.
    denominator = math.factorial(k) * math.factorial(N - k)
    # Divide them to get the final value.
    return numerator / denominator

len_outcome = 30

outcome_probs = []
for outcome in outcome_counts:
    term_1 = find_outcome_combinations(len_outcome, outcome)
    term_2 = find_prob_single_combinations(p,q,outcome,len_outcome)
    outcome_probs.append(term_1*term_2)
    
#Dataquest solution :

# Each item in this list represents one k, starting from 0 and going up to and including 30.
outcome_counts = list(range(31))
def find_probability(N, k, p, q):
    # Find the probability of any single combination.
    term_1 = p ** k
    term_2 = q ** (N-k)
    combo_prob = term_1 * term_2
    
    # Find the number of combinations.
    numerator = math.factorial(N)
    denominator = math.factorial(k) * math.factorial(N - k)
    combo_count = numerator / denominator
    
    return combo_prob * combo_count

outcome_probs = [find_probability(30, i, .39, .61) for i in outcome_counts]
```  

#### Results :  



---
# 15: Plotting The Distribution  

You may have noticed that outcome_counts in the previous screen was 31 items long when N was only 30. This is because we need to account for 0. There's a chance of having k=0k=0, where the outcome we want doesn't happen at all. This data point needs to be on our charts. We'll always want to add 1 to N when figuring out how many points to plot.  

Our data is in terms of whole days. Either 1 day has more than 5000 riders, or 2 days have more than 5000 riders. It doesn't make sense to talk about the probability of 1.5 days having more than 5000 riders. The points in our data are discrete and not continuous, so we use a bar chart when plotting.  

Now that we've computed the distribution, we can easily plot it out using matplotlib. This will show us a nice distribution of our probabilities, along with the most likely outcomes.   

#### Instructions :

 - 
 
```python
import matplotlib.pyplot as plt

# The most likely number of days is between 10 and 15.
plt.bar(outcome_counts, outcome_probs)
plt.show()
```  

#### Results :  

see img/img7.png  

---
# 6: Simplifying The Computation  

To construct our distribution, we had to write our own custom function, and a decent amount of code. We can instead use the binom.pmf function from SciPy to do this faster.  

Here's a usage example:  

```python
from scipy import linspace
from scipy.stats import binom
​
# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31)
​
# Create the binomial probabilities, one for each entry in outcome_counts.
dist = binom.pmf(outcome_counts,30,0.39)
```

The pmf function in SciPy is an implementation of the mathematical probability mass function. The pmf will give us the probability of each k in our outcome_counts list occurring.  

A binomial distribution only needs two parameters. A parameter is the statistical term for a number that summarizes data for the entire population. For a binomial distribution, the parameters are:  

- N, the total number of events,
- p, the probability of the outcome we're interested in seeing.

The SciPy function pmf matches this and takes in the following parameters:  

- x: the list of outcomes,
- n: the total number of events,
- p: the probability of the outcome we're interested in seeing.

Because we only need two parameters to describe a distribution, it doesn't matter whether we want to know if it will be sunny 5 days out of 5, or if 5 out of 5 coin flips will turn up heads. As long as the outcome that we care about has the same probability (pp), and NN is the same, the binomial distribution will look the same.   

#### Instructions :

 - Generate a binomial distribution, and then find the probabilities for each value in outcome_counts.
	- Use N=30, and p=.39, as we're doing this for the bikesharing data.
 - Plot the resulting data as a bar chart.
 
```python
import scipy
from scipy import linspace
from scipy.stats import binom

# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31)

# Create the binomial probabilities, one for each entry in outcome_counts.
dist = binom.pmf(outcome_counts,30,0.39)
plt.bar(outcome_counts,dist)
plt.show()
```  

#### Results :  

see img/img8.png  


---
# 7: How To Think About A Probability Distribution  

Looking at a probability distribution might not be extremely intuitive. One way to think about it is that "if we repeatedly look at samples, the expected number of outcomes will follow the probability distribution".  

If we repeatedly look at 30 days of bikesharing data, we'll find that 10 of the days had more than 5000 riders about 12.4% of the time. We'll find that 12 of the days had more than 5000 riders about 14.6% of the time.  

A probability distribution is a great way to visualize data, but bear in mind that it's not dealing in absolute values. A probability distribution can only tell us which values are likely, and how likely they are.  

---
# 8: Computing The Mean Of A Probability Distribution  

Sometimes we'll want to be able to tell people the expected value of a probability distribution -- the most likely result of a single sample that we look at.  

To compute this, we just multiply NN by pp.   

#### Instructions :

 - Compute the mean for the bikesharing data, where N=30N=30, and p=.39p=.39.
	- Assign the result to dist_mean.

 
```python
dist_mean = None
dist_mean = 30 * 0.39
```  

#### Results :  

	Variables
	 dist_meanfloat (<class 'float'>)
	11.700000000000001

---
# 9: Computing The Standard Deviation  

Just as we can compute the mean, we can also compute the standard deviation of a probability distribution. This helps us find how much the actual values will vary from the mean when we take a sample.  

Going back to the bikesharing example, we know that the actual values will be around 11.7 (from the last screen). But, we'll need a standard deviation to explain how much the actual values can vary from this expectation.  

The formula for standard deviation of a probability distribution is:  

see img/img9.png  
N∗p∗q‾‾‾‾‾‾‾‾‾√ 

#### Instructions :

 - Compute the standard deviation for the bikesharing data, where N=30N=30, and p=.39p=.39.
	- Assign the result to dist_stdev.
 
```python
dist_stdev = None
dist_stdev = (30 * 0.39 * (1-0.39)) ** 0.5
```  

#### Results :  

	Variables
	 dist_stdevfloat (<class 'float'>)
	2.671516423307182

---
# 10: A Different Plot

Just like we did with histograms and sampling a few missions ago, we can vary the parameters to change the distribution. Let's see what the plot would look like with only 10 events, or 100 events.   

#### Instructions :

- Generate a binomial distribution, with N=10, and p=.39.
	- Find the probabilities for each value in outcome_counts.
	- Plot the resulting data as a bar chart.
- Generate a binomial distribution, with N=100, and p=.39.
	- Find the probabilities for each value in outcome_counts.
	- Plot the resulting data as a bar chart.
 
```python
# Enter your answer here.
outcome_counts = linspace(0,10,11)
dist = binom.pmf(outcome_counts,10,0.39)
plt.bar(outcome_counts,dist)
plt.show()

outcome_counts = linspace(0,100,101)
dist = binom.pmf(outcome_counts,100,0.39)
plt.bar(outcome_counts,dist)
plt.show()

#dataquest solution :

# Enter your answer here.
outcome_counts = linspace(0,10,11)
outcome_probs = binom.pmf(outcome_counts,10,0.39)
plt.bar(outcome_counts, outcome_probs)
plt.show()

outcome_counts = linspace(0,100,101)
outcome_probs = binom.pmf(outcome_counts,100,0.39)
plt.bar(outcome_counts, outcome_probs)
plt.show()
```  

#### Results :  

see img/img10.png
see img/img11.png

---
# 11: The Normal Distribution  

From the last screen, the more events we looked at, the closer our distribution was to being normal. With N=10N=10, we saw some rightward skew, but when we got up to N=100N=100, the skew disappeared.  

This is because the distribution got narrower relative to the x-axis range the more examples you add. With N=10N=10, there's a reasonable chance that 8 to 10 days could have over 5000 riders. But, when we get up to N=100N=100, it's statistically almost impossible that more than 60 days have over 5000 riders. This makes the distribution narrower.  

As the distribution gets narrower, it gets more similar to the normal distribution. In the code cell, we plot a line chat instead of a bar chart and it looks almost exactly like a normal distribution.   

#### Instructions :

 - 
 
```python
# Create a range of numbers from 0 to 100, with 101 elements (each number has one entry).
outcome_counts = scipy.linspace(0,100,101)

# Create a probability mass function along the outcome_counts.
outcome_probs = binom.pmf(outcome_counts,100,0.39)

# Plot a line, not a bar chart.
plt.plot(outcome_counts, outcome_probs)
plt.show()
```  

#### Results :  

see img/img12.png

---
# 12: Cumulative Density Function  

So far, we've looked at the probability that single values of k will occur. What we can look at instead is the probability that k or less will occur. These probabilities can be generated by the cumulative density function.  

Let's say we flip a coin 3 times -- N=3N=3, and p=.5p=.5. When this happens, here are the probabilities:  


	k    probability
	​
	0    .125
	1    .375
	2    .375
	3    .125
	
A cumulative distribution would look like this:  


	k    probability
	​
	0    .125
	1    .5
	2    .875
	3    1
	
For each k, we fill in the probability that we'll see k outcomes or less. By the end of the distribution, we should get 1, because all the probabilities add to 1 (if we flip 3 coins, either 0, 1, 2, or 3 of them must be heads).  

We can calculate this with binom.cdf in scipy.  

```python
from scipy import linspace
from scipy.stats import binom
​
# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31)
​
# Create the cumulative binomial probabilities, one for each entry in outcome_counts.
dist = binom.cdf(outcome_counts,30,0.39) 
```

#### Instructions :

 - Create a cumulative distribution where N=30N=30 and p=.39p=.39 and generate a line plot of the distribution.
 
```python
outcome_counts = linspace(0,30,31)
dist = binom.cdf(outcome_counts,30,0.39)
plt.plot(dist)
plt.show()
```  

#### Results :  

see img/img13.png

---
# 13: Calculating Z-Scores  

We can calculate z-scores (the number of standard deviations away from the mean a probability is) fairly easily. These z-scores can then be used how we used z-scores earlier -- to find the percentage of values to the left and right of the value we're looking at.  

To make this more concrete, say we had 16 days where we observed more than 5000 riders. Is this likely? Unlikely? Using a z-score, we can figure out exactly how common this event is.  

This is because every normal distribution, as we learned in an earlier mission, has the same properties when it comes to what percentage of the data is within a certain number of standard deviations of the mean. You can look these up in a standard normal table. About 68% of the data is within 1 standard deviation of the mean, 95% is within 2, and 99% is within 3.  

We can calculate the mean (μμ) and standard deviation (σσ) of a binomial probability distribution using the formulas from earlier:  

see img/img14.png
μ=N∗pμ=N∗p
σ=N∗p∗q‾‾‾‾‾‾‾‾‾√σ=N∗p∗q

If we want to figure out the number of standard deviations from the mean a value is, we just do:  

see img/img15.png
k−μσk−μσ

If we wanted to find how many standard deviations from the mean 16 days is:  

see img/img16.png
16−μσ=16−(30∗.39)16∗.39∗.61√=4.31.95=2.216−μσ=16−(30∗.39)16∗.39∗.61=4.31.95=2.2

Based on the standard z-score table, this is unlikely -- a 2.78% chance. This tells us that 97.22% of the data is within 2.2 standard deviations of the mean, so so a result to be as different from the mean as this, there is a 2.78% probability that it occurred by chance.  

Note that this means both "sides" of the distribution. There's a 1.39% chance that a value is 2.2 standard deviations or more above the mean (to the right of the mean), and there's a 1.39% chance that a value is 2.2 standard devitation below the mean (to the left).   


---
# 14: Faster Way To Calculate Likelihood  

We don't want to have to use a z-score table every time we want to see how likely or unlikely a probability is. A much faster way is to use the cumulative distribution fuction (cdf) like we did earlier. This won't give us the exact same values as using z-scores, because the distribution isn't exactly normal, but it will give us the actual amount of probability in a distribution to the left of a given k.  

To use it, we can run:  

```python
# The sum of all the probabilities to the left of k, including k.
left = binom.cdf(k,N,p)
​
# The sum of all probabilities to the right of k.
right = 1 - left
```

This will return the sum of all the probabilities to the left of and including k. If we subtract this value from 1, we get the sum of all the probabilities to the right of k.   

#### Instructions :

 - Find the probability to the left of k=16k=16 (including 16) when N=30N=30 and p=.39p=.39.
	- Assign the result to left_16.
 - Find the probability to the right of k=16k=16 when N=30N=30 and p=.39p=.39.
	- Assign the result to right_16.
 
```python
left_16 = None
right_16 = None

left_16 = binom.cdf(16,30,0.39)
right_16 = 1 - left_16
```  

#### Results :  

	Variables
	 right_16float64 (<class 'numpy.float64'>)
	0.037699623394511717
	 left_16float64 (<class 'numpy.float64'>)
	0.96230037660548828
