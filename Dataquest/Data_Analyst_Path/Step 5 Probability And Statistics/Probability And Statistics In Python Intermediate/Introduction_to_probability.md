03/2017  
Dataquest : Data Analyst Path  
Step 5: Probability and Statistics  
SubStep : Probability and Statistics in Python: Intermediate : Introduction to probability  
dimanche, 19. mars 2017 02:33   


---
# 1: Probability Basics  

We covered a bit of probability in the last mission, but we'll go more into depth here and build a strong foundation. Before we do that, let's introduce our dataset. Our dataset contains information on flags of countries around the world. Each row is a country. Here are the relevant columns:  

- name -- name of the country
- landmass -- which continent the country is in (1=N.America, 2=S.America, 3=Europe, 4=Africa, 4=Asia, 6=Oceania)
- area -- country area, in thousands of square kilometers
- population -- rounded to the nearest million
- bars -- Number of vertical bars in the flag
- stripes -- Number of horizontal stripes in the flag
- colors -- Number of different colours in the flag
- red, green, blue, gold, white, black, orange -- 0 if color absent, 1 if color present in the flag

This data was collected from Collins Gem Guide to Flags. It was written in 1986, so some flag information may be out of date!   


#### Instructions :

 - Find the country with the most bars in its flag. Assign the name of the country to most_bars_country.
 - Find the country with the highest population (as of 1986). Assign the name of the country to highest_population_country.
 
```python
# Print the first two rows of the data.
print(flags[:2])

most_bars_country = flags[["name","bars"]].sort_values("bars",ascending=False).iloc[0,0]
print(most_bars_country)

highest_population_country = flags[["name","population"]].sort_values("population",ascending=False).iloc[0,0]
print(highest_population_country)

# dataquest solution
# Print the first two rows of the data.
print(flags[:2])
bars_sorted = flags.sort_values("bars", ascending=[0])
most_bars_country = bars_sorted["name"].iloc[0]

population_sorted = flags.sort_values("population", ascending=[0])
highest_population_country = population_sorted["name"].iloc[0]

```  

#### Results :  

		  name  landmass  zone  area  population  language  religion  bars  \
	0  Afghanistan         5     1   648          16        10         2     0   
	1      Albania         3     1    29           3         6         6     0   

	   stripes  colors    ...     saltires  quarters  sunstars  crescent  \
	0        3       5    ...            0         0         1         0   
	1        0       3    ...            0         0         1         0   

	   triangle  icon  animate text  topleft  botright  
	0         0     1        0    0    black     green  
	1         0     0        1    0      red       red  

	[2 rows x 30 columns]
	St-Vincent
	China

---
# 2: Calculating Probability  

Now that we've explored the data a bit, let's get back to probability. Probability can roughly be described as "the percentage chance of an event or sequence of events occurring".  

If you think about a coin flip intuitively, there's a 50% chance of getting heads, and a 50% chance of getting tails. This is because there are only two possible outcomes, and each event is equally likely.  

We can apply the same principle to find how likely it is to select an element with certain characteristics from a sample. In this case, our sample is all the country flags. With a coin flip, it's already known that only two outcomes exist -- we need to compute the probability ourselves for the flags.  

We could compute the probability of a country flag having a certain characteristic by dividing how many flags have that characteristic by the total number of flags.   


#### Instructions :

 - Determine the probability of a country having a flag with the color orange in it. Assign the result to orange_probability.
 - Determine the probability of a country having a flag with more than 1 stripe in it. Assign the result to stripe_probability.
 
```python
total_countries = flags.shape[0]
orange_probability = len(flags[flags["orange"] == 1]) / len(flags) 
stripe_probability = len(flags[flags["stripes"] > 1]) / len(flags) 

#dataquest solution
total_countries = flags.shape[0]
orange_probability = flags[flags["orange"] == 1].shape[0] / total_countries

stripe_probability = flags[flags["stripes"] > 1].shape[0] / total_countries

```  

#### Results :  


	Variables
	 orange_probabilityfloat (<class 'float'>)
	0.13402061855670103
	 stripe_probabilityfloat (<class 'float'>)
	0.41237113402061853

---
# 3: Conjunctive Probabilities  

We just found the probability of a country having a flag with more than one stripe. This was fairly straightforward, as it only involved one probability.  

But let's say we have a coin that we flip 5 times, and we want to find the probability that it will come up heads every time. This is called a conjunctive probability, because it involves a sequence of events. We want to find the probability that the first flip is heads and the second flip is heads, and so on.  

Each event in this sequence is independent, as the outcome of the first flip won't have an impact on the outcome of the last flip. All we have to do to compute the probability of this sequence is multiply the individual probabilities of each event together. This is .5 * .5 * .5 * .5 * .5, which equals .03125, giving us a 3.125% chance that all 5 coin flips result in heads.  


#### Instructions :

 - Find the probability that 10 flips in a row will all turn out heads. Assign the probability to ten_heads.
 - Find the probability that 100 flips in a row will all turn out heads. Assign the probability to hundred_heads.
 
```python
five_heads = .5 ** 5
ten_heads = 0.5 ** 10
hundred_heads = 0.5 ** 100
```  

#### Results :  


	Variables
	 hundred_headsfloat (<class 'float'>)
	7.888609052210118e-31
	 ten_headsfloat (<class 'float'>)
	0.0009765625
	 five_headsfloat (<class 'float'>)
	0.03125

---
# 4: Dependent Probabilities  

Let's say that we're picking countries from the sample, and removing them when we pick. Each time we pick a country, we reduce the sample size for the next pick. The events are dependent -- the number of countries available to pick depends on the previous pick. We can't just calculate the probability upfront and take a power in this case -- we need to recompute the probability after each selection happens.  

Let's simplify the example a bit by saying that we're eating some M&Ms. There are 10 M&Ms left in the bag: 5 are green, and 5 are blue. What are the odds of getting 3 blue candies in a row? The probability of getting the first blue candy is 5/10, or 1/2. When we pick a blue candy, though, we remove it from the bag, so the probability of getting another is 4/9. The probability of picking a third blue candy is 3/8. This means our final probability is 1/2 * 4/9 * 3/8, or .0833. So, there is an 8.3% chance of picking three blue candies in a row.  


#### Instructions :

 - Let's say that we're picking countries from our dataset, and removing each one that we pick.
 - What are the odds of picking three countries with red in their flags in a row? Assign the resulting probability to three_red.
 
```python
# Remember that whether a flag has red in it or not is in the `red` column.
nb_red = len(flags[flags["red"] == 1]) 
print(" Nb Flag with red : ",nb_red)
nb_tot = len(flags) 
print(" Nb Flag  : ",nb_tot)
three_red = (nb_red / nb_tot) * ((nb_red-1) / (nb_tot-1)) * ((nb_red-2) / (nb_tot-2))
print("Probabilty to get 3 red flag : ",three_red)
```  

#### Results :  

	Output
	 Nb Flag with red :  153
	 Nb Flag  :  194
	Probabilty to get 3 red flag :  0.4884855242775493

---
# 5: Disjunctive Probability  

Conjunctive probability is when something happens and something else happens. But sometimes, we want to know the probability of some event occurring or another event occurring. Let's say we're rolling a six-sided die -- the probability of rolling a 2 is 1/6.  

What if we want to know the probability of rolling a 2 or the probability of rolling a three? We actually can just add the probabilities, because both events are independent. Rolling a 2 doesn't change my odds of rolling a three next time around. Thus, the probability is 1/6 + 1/6, or 1/3.   


#### Instructions :

 - Let's say we have a random number generator that generates numbers from 1 to 18000.
 - What are the odds of getting a number evenly divisible by 100, with no remainder? (ie 100, 200, 300, etc). Assign the result to hundred_prob.
 - What are the odds of getting a number evenly divisible by 70, with no remainder? (ie 70, 140, 210, etc). Assign the result to seventy_prob.
 
```python
start = 1
end = 18000

cpt = 0
for i in range(1,18001):
    if (i % 100) == 0:
        cpt += 1
print(cpt)
hundred_prob = cpt/18000

cpt = 0
for i in range(1,18001):
    if (i % 70) == 0:
        cpt += 1
print(cpt)
seventy_prob = cpt/18000

# dataquest solution
start = 1
end = 18000
def count_evenly_divisible(start, end, div):
    divisible = 0
    for i in range(start, end+1):
        if (i % div) == 0:
            divisible += 1
    return divisible

hundred_prob = count_evenly_divisible(start, end, 100) / end
seventy_prob = count_evenly_divisible(start, end, 70) / end

```  

#### Results :  

	Variables
	 seventy_probfloat (<class 'float'>)
	0.014277777777777778
	 hundred_probfloat (<class 'float'>)
	0.01

---
# 6: Disjunctive Dependent Probabilities  

So we've covered disjunctive probabilities in the neat case where everything is mututally exclusive, and we can just add them up.  

But, let's think about a slightly more complex case with dependencies. What if we have a set of 10 cars -- 5 are red and 5 are blue. 5 of the 10 are convertibles, and 5 are sport utility vehicles.  

If we wanted to find cars that were red or were convertibles, we might try to add the probability of the car being red to the probability of the car being a convertible. This would give us 1/2 + 1/2 == 1. But, this is wrong, as it tells us that all 10 cars are either red or convertibles.  

It's wrong because it assumes that the two traits (color and vehicle type) are independent, when in fact they aren't. Some of the cars are red and convertibles. If we don't account for this overlap, we end up with a vastly inflated count.  

Let's say that we have 3 cars that are red and convertibles. Our probability for red or convertible then comes out to (1/2 + 1/2) - 3/10. We subtract 3/10 to account for the cars we double counted when we computed (1/2 + 1/2). This gives us a .7 probability of a car being a convertible or red.  


#### Instructions :

 - Find the probability of a flag having red or orange as a color. Assign the result to red_or_orange.
 - Find the probability of a flag having at least one stripes or at least one bars. Assign the result to stripes_or_bars.
 
```python
stripes_or_bars = None
red_or_orange = None

nb_red = len(flags[flags["red"] == 1]) 
print(" Nb Flag with red : ",nb_red)
nb_orange = len(flags[flags["orange"] == 1]) 
print(" Nb Flag with orange : ",nb_orange)
nb_red_and_orange = len(flags[(flags["red"] == 1) & (flags["orange"] == 1)]) 
print(" Nb Flag with red and orange  : ",nb_red_and_orange)
print("-------------------")

nb_bars = len(flags[flags["bars"] > 0]) 
print(" Nb Flag with a least one bars : ",nb_bars)
nb_stripes = len(flags[flags["stripes"] > 0]) 
print(" Nb Flag with a least one stripes : ",nb_stripes)
nb_bars_and_stripes = len(flags[(flags["stripes"] >= 1) & (flags["bars"] >= 1)]) 
print(" Nb Flag with bars and stripes  : ",nb_bars_and_stripes)
print("-------------------")
nb_tot = len(flags) 
print(" Nb Flag  : ",nb_tot)
print("-------------------")
red_or_orange = (nb_red/nb_tot) + (nb_orange/nb_tot) - (nb_red_and_orange/nb_tot)
stripes_or_bars = (nb_bars/nb_tot) + (nb_stripes/nb_tot) - (nb_bars_and_stripes/nb_tot)
print("red_or_orange : ",red_or_orange)
print("stripes_or_bars : ",stripes_or_bars)

# dataquest solution
stripes_or_bars = None
red_or_orange = None
red = flags[flags["red"] == 1].shape[0] / flags.shape[0]
orange = flags[flags["orange"] == 1].shape[0] / flags.shape[0]
red_and_orange = flags[(flags["red"] == 1) & (flags["orange"] == 1)].shape[0] / flags.shape[0]

red_or_orange = red + orange - red_and_orange

stripes = flags[flags["stripes"] > 0].shape[0] / flags.shape[0]
bars = flags[flags["bars"] > 0].shape[0] / flags.shape[0]
stripes_and_bars = flags[(flags["stripes"] > 0) & (flags["bars"] > 0)].shape[0] / flags.shape[0]

stripes_or_bars = stripes + bars - stripes_and_bars
```  

#### Results :  

	Output
	 Nb Flag with red :  153
	 Nb Flag with orange :  26
	 Nb Flag with red and orange  :  19
	-------------------
	 Nb Flag with a least one bars :  35
	 Nb Flag with a least one stripes :  84
	 Nb Flag with bars and stripes  :  4
	-------------------
	 Nb Flag  :  194
	-------------------
	red_or_orange :  0.8247422680412371
	stripes_or_bars :  0.5927835051546392


---
# 7: Disjunctive Probabilities With Multiple Conditions  

We've looked at disjunctive probabilities in cases where there are only two conditions (A or B). But what if we have three or more conditions?  

Let's say we have 10 cars again. 5 are red and 5 are blue. 5 are convertibles and 5 are sport utility vehicles. 5 have a top speed of 130mph, and 5 have a top speed of 110mph.  

Let's say we want to find all cars that are red or convertibles or have a top speed of 130mph. Let's say 2 cars meet all three criteria. We would end up with 1/2 + 1/2 + 1/2 - 1/5, or a 1.3 probability if we tried to apply the formula from before. This is clearly false, as we can't have a probability greater than 1.  
 
One easy way to solve for cases like this is to find everything that doesn't match our criteria first. In this case, we'd look for blue sport utility vehicles with a top speed of 110mph. We would then subtract that probability from 1 to get the probability of red or convertible or 130mph top speed. Let's say there are 2 vehicles that are blue and sport utility vehicles and have a 110mph top speed. We would get a 1 - .2 or .8 probability for red or convertible or 130mph top speed.   


#### Instructions :

 - Let's say we have a coin that we're flipping. Find the probability that at least one of the first three flips comes up heads. Assign the result to heads_or.

 
```python
heads_or = None
heads_or = 1 - (0.5**3)

#dataquest solution
heads_or = None
all_three_tails = (1/2 * 1/2 * 1/2)
heads_or = 1 - all_three_tails

```  

#### Results :  

	Variables
	 heads_orfloat (<class 'float'>)
	0.875