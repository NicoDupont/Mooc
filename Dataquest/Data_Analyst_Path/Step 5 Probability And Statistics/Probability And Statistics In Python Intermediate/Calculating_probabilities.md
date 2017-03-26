03/2017  
Dataquest : Data Analyst Path  
Step 5: Probability and Statistics  
SubStep : Probability and Statistics in Python: Intermediate : Introduction to probability  
dimanche, 19. mars 2017 15:42   

---
# 1: The Dataset  

In the last mission, we looked at probability, and the ideas of disjunctive, dependent, and conjunctive probabilities.    

We'll dive more into probability in this mission, and calculate more complex probabilities. But first, we'll look at the dataset we'll be using.    

In many countries, there are bikesharing programs where anyone can rent a bike from a depot, and return it at other depots throughout a city. There is one such program in Washington, D.C., in the US. We'll be looking at the number of bikes that were rented by day. Here are the relevant columns:  

 - dteday -- the date that we're looking at.
 - casual -- the number of casual riders (people who hadn't previously signed up with the bikesharing program) that rented bikes on the day.
 - registered -- the number of registered riders (people who signed up previously) that rented bikes.
 - cnt -- the total number of bikes rented.
 
This data was collected by Hadi Fanaee-T at the University of Porto, and can be downloaded here.    

---
# 2: Probability Of Renting Bikes  

Let's explore our data a bit, first by finding the probability that more than 2000 bikes will be rented on any given day.    


#### Instructions :

 - Find the probability that more than 4000 bikes were rented on any given day.
	- Assign the result to probability_over_4000.
 
```python
import pandas
bikes = pandas.read_csv("bike_rental_day.csv")

# Find the number of days the bikes rented exceeded the threshold.
days_over_threshold = bikes[bikes["cnt"] > 2000].shape[0]
# Find the total number of days we have data for.
total_days = bikes.shape[0]

# Get the probability that more than 2000 bikes were rented for any given day.
probability_over_2000 = days_over_threshold / total_days
print(probability_over_2000)


days_over_threshold = bikes[bikes["cnt"] > 4000].shape[0]
probability_over_4000 = days_over_threshold / total_days
print(probability_over_4000)
```  

#### Results :  

	Output
	0.86593707250342
	0.6183310533515732

---
# 3: Up To Or Greater  

Let's say we flip three coins, and we want to know the probability of getting 2 or more heads. In order to do this, we'd need to add the probability of getting exactly 2 heads with the probability of getting exactly 3 heads. The probability that any single coin will be heads is .5 (the probability that the coin will be tails is the same, .5).  

The probability of 3 heads is easy to calculate -- this can only happen in one situation, where all three coins are heads, or .5 * .5 * .5, which equals .125.  

The probability of 2 heads is a little trickier -- there are three different combinations that the three coins can configure themselves in to end up with 2 heads. We show this in the table below, using H for heads, and T for tails.  


	Coin 1    Coin 2    Coin 3
	H         H         T
	T         H         H
	H         T         H
	
Each one of these has a probability of .5 * .5 * .5, so we just multiply 3 * .125 to get .375, the probability that we'll get 2 heads.    

We then just have to add up the probability of getting 2 heads to the probability of getting 3 heads to get .5, the probability of getting 2 or more heads when we flip 3 coins.    


---
# 4: Calculating Probabilities  

Now that we know how to calculate probabilities for coins, let's calculate the probability that 1 coin out of 3 is heads.    

#### Instructions :

 - Find the probability that 1 coin out of 3 is heads.
	- Assign the result to coin_1_prob.
 
```python
# Enter your code here.
# There are three combinations in which we can have one coin heads.
# HTT, THT, TTH
# Each combination's probability is (.5 * .5 * .5)
combination_prob = (.5 * .5 * .5) 
# The probability for one combination is in combination_prob -- multiply by the three possible combinations.
coin_1_prob = 3 * combination_prob
```  

#### Results :  

	Variables
	 combination_probfloat (<class 'float'>)
	0.125
	 coin_1_probfloat (<class 'float'>)
	0.375

---
# 5: Number Of Combinations  

What we found in the last screen was that there were exactly 3 combinations of coins to get 2 out of the 3 coins to be heads. There was exactly 1 combination to get all three coins to be heads.  

Let's scale this example up a little bit. Let's say that we live in Los Angeles, CA, and the chance of any single day being sunny is .7. The chance of a day not being sunny is .3.  

If we have a sample of 5 days, and we want to find the chance that all 5 of them will be sunny, there's only one combination that allows this to happen -- the sunny outcome has to occur on all 5 days:  


	Day 1    Day 2    Day 3    Day 4    Day 5
	S        S        S        S        S

If we want to find the probability that only 4 days will be sunny, there are 5 possible combinations.  


	Day 1    Day 2    Day 3    Day 4    Day 5
	S        S        S        S        N
	S        S        S        N        S
	S        S        N        S        S
	S        N        S        S        S
	N        S        S        S        S
	
You may notice a pattern here. The most extreme cases -- a given outcome happening all the time or none of the time, can only occur in one combination. The next step lower, a given outcome happening every time except once, or a given outcome only happening once, can happen in as many combinations as there are total events.    

---
# 6: Calculating The Number Of Combinations  

Now that we've worked out some tables, let's practice a bit.    


#### Instructions :

 - Find the number of combinations in which 1 day will be sunny.
	- Assign the result to sunny_1_combinations.
 
```python
sunny_1_combinations = None
sunny_1_combinations = 5
```  

#### Results :  

	SUUUU
	USUUU
	UUSUU
	UUUSU
	UUUUS

---
# 7: Number Of Combinations Formula  

In fact, there's an easily quantifiable pattern with the number of combinations. We can calculate the number of combinations in which an outcome can occur k times in a set of events with a formula:  

N!k!(N−k)!N!k!(N−k)!  

In this formula, NN is the total number of events we have, and kk is the target number of times we want our desired outcome to occur. So if we wanted to find the number of combinations in which 4 out of 5 days can be sunny, we'd set NN to 5, and kk to 4. The !! symbol means factorial. A factorial means "multiply every number from 1 to this number together". So 4!4! is 1*2*3*4, which is 24.  

Plugging 4 and 5 into this formula gives us:  

5!4!(5−4)!=5!4!(5−4)!=1∗2∗3∗4∗51∗2∗3∗4(1!)=12024=55!4!(5−4)!=5!4!(5−4)!=1∗2∗3∗4∗51∗2∗3∗4(1!)=12024=5  

This matches our intuitive answer that we got earlier!   


---
# 8: Finding The Number Of Combinations  

We can calculate probabilities greater than or equal to a threshold with our bike sharing data. We found that the probability of having more riders than 4000 is about .6. We can use this to find the probability that in 10 days, 7 or more days have more than 4000 riders.  

But first, let's find the number of combinations in which 7 days out of 10 have more than 4000 rentals. We can repeat this process for 8 and 9 days.    


#### Instructions :

 - Find the number of combinations where 8 days out of 10 have more than 4000 rentals. Assign the result to combinations_8.
 - Find the number of combinations where 9 days out of 10 have more than 4000 rentals. Assign the result to combinations_9.
 
```python
import math
def find_outcome_combinations(N, k):
    # Calculate the numerator of our formula.
    numerator = math.factorial(N)
    # Calculate the denominator.
    denominator = math.factorial(k) * math.factorial(N - k)
    # Divide them to get the final value.
    return numerator / denominator

combinations_7 = find_outcome_combinations(10, 7)
combinations_8 = find_outcome_combinations(10, 8)
combinations_9 = find_outcome_combinations(10, 9)
print("combinations_7 : ",combinations_7)
print("combinations_8 : ",combinations_8)
print("combinations_9 : ",combinations_9)
```  

#### Results :  

	Output
	combinations_7 :  120.0
	combinations_8 :  45.0
	combinations_9 :  10.0

---
# 9: The Probability For Each Combination  

Let's go back to our example about the number of sunny days in Los Angeles. We can call the probability that a day will be sunny pp, and the probability that a day won't be sunny qq.  

pp is the probability that an outcome will occur, and qq is the complementary probability that the outcome won't happen -- 1−p=q1−p=q.  

When we calculate the number of combinations in which a given outcome can occur k times in N events, each of those combinations has a certain probability of occurring.  

Let's say that for sunny days in Los Angeles, pp is .7, and qq is .3. If we look at 5 days, there is one combination in which every day is sunny -- the probability for this combination is .7 * .7 * .7 * .7 * .7, which equals .168.  

There are 5 combinations in which only 4 days are sunny -- you can see our table earlier for a closer look. We can calculate the probability of the first combination with .7 * .7 * .7 * .7 * .3, which equals .072. The probability of the second combination is .7 * .7 * .7 * .3 * .7, which equals .072. We're multiplying all the same numbers, just in a different order, so this combination has the same probability as the first combination. The probability for each combination in which kk of the same outcome can happen in NN events is always the same.    

---
# 10: Calculating The Probability Of One Combination  

Now that we calculated the probability for a single combination occurring, let's practice the calculation a bit more.    


#### Instructions :

 - Find the probability of a single combination for finding 3 days out of 5 are sunny.
	- The combination is Sunny, Sunny, Sunny, Not Sunny, Not Sunny.
	- Assign the result to prob_combination_3.
 
```python
prob_combination_3 = None
prob_combination_3 = 0.7 * 0.7 * 0.7 * 0.3 * 0.3
```  

#### Results :  

	Variables
	 prob_combination_3float (<class 'float'>)
	0.03086999999999999

---
# 11: Per Combination Probability Formula  

As we learned earlier, the probability for each combination in which kk of the same outcome can happen in NN events is always the same. Given this, we can calculate the probability of a given outcome happening kk times in NN events by multiplying the number of combinations in which our result can occur by the probability of a single combination occurring.  

The probability of a single combination occurring is given by pk∗qN−kpk∗qN−k  (see img/img3.png). We can verify this with our sunny days example. First, let's find the probability of one combination in which there are 5 sunny days out of 5:  

(see img/img4.png)
.75∗.35−5=.168∗.30=.168∗1=.168.75∗.35−5=.168∗.30=.168∗1=.168  

Now, let's find the probability of one combination in which there are 4 sunny days out of 5:  

(see img/img5.png)
.74∗.35−4=.24∗.31=.24∗.3=.072.74∗.35−4=.24∗.31=.24∗.3=.072

This matches up perfectly with what we did earlier. To find the overall probabilty of 4 days out of 5 being sunny, we just multiply the number of combinations by the probability of any single combination occurring. This gives us .36.    


---
# 12: Function To Calculate The Probability Of A Single Combination  

Now we know enough to find the probability that within 10 days, 7 or more days have more than 4000 riders. The probability of having more than 4000 riders on any single day is about .6. This means that pp is .6, and qq is .4.    

#### Instructions :

 - Write a function to find the probability of a single combination occurring.
 - Use the function to calculate the probability of 8 days out of 10 having more than 4000 riders.
	- Assign the result to prob_8.
 - Use the function to calculate the probability of 9 days out of 10 having more than 4000 riders.
	- Assign the result to prob_9.
 - Use the function to calculate the probability of 10 days out of 10 having more than 4000 riders.
	- Assign the result to prob_10.
 
```python
p = .6
q = .4

def find_prob_single_combinations(p, q, k, n):
    prob = (p ** k) * (q ** (n-k))
    return prob

import math
def find_outcome_combinations(N, k):
    # Calculate the numerator of our formula.
    numerator = math.factorial(N)
    # Calculate the denominator.
    denominator = math.factorial(k) * math.factorial(N - k)
    # Divide them to get the final value.
    return numerator / denominator

combinations_8 = find_outcome_combinations(10, 8)
combinations_9 = find_outcome_combinations(10, 9)
combinations_10 = find_outcome_combinations(10, 10)

prob_8 = find_prob_single_combinations(p,q,8,10) * combinations_8
prob_9 = find_prob_single_combinations(p,q,9,10) * combinations_9
prob_10 = find_prob_single_combinations(p,q,10,10) * combinations_10
```  

#### Results :  

	Variables
	 prob_8float (<class 'float'>)
	0.12093235199999997
	 prob_10float (<class 'float'>)
	0.006046617599999997
	 prob_9float (<class 'float'>)
	0.04031078399999999
	 combinations_10float (<class 'float'>)
	1.0
	 combinations_9float (<class 'float'>)
	10.0
	 combinations_8float (<class 'float'>)
	45.0

---
# 13: Statistical Significance  

Let's say we've invented a weather control device that can make the weather sunny (if only!), and we decide to test it on Los Angeles. The device isn't perfect, and can't make every single day sunny -- it can only increase the chance that a day is sunny. We turn it on for 10 days, and notice that the weather is sunny in 8 of those.  

We touched on the question of statistical significance before -- it's the question of whether a result happened as the result of something we changed, or whether a result is a matter of random chance.  

Typically, researchers will use 5% as a significance threshold -- if an event would only happen 5% or less of the time by random chance, then it is statistically significant. If an event would happen more than 5% of the time by random chance, then it isn't statistically significant.  

In order to determine statistical significance, we need to determine the percentage chance that the number of outcomes we saw or greater could happen by random chance.  

In our case, there is 12% chance that the weather would be sunny 8 days out of 10 by random chance. We add this to 4% for 9 days out of 10, and .6% for 10 days out of 10 to get a 16.6% total chance of the sunny outcome happening 8 or more time in our 10 days. Our result isn't statistically significant, so we'd have to go back to the lab and spend some time adding more flux capacitors to our weather control device.  

Let's say we recalibrate our weather control device successfully, and observe for 10 more days, of which 9 of them are sunny. This only has a 4.6% chance of happening randomly (probability of 9 plus probability of 10). This is a statistically significant result, but it isn't a slam-dunk. It would require more investigation, including collecting results for more days, to get a more conclusive result.  

In practice, setting statistical significance thresholds is tricky, and can be highly variable. We'll be touching on how to set thresholds later on.    