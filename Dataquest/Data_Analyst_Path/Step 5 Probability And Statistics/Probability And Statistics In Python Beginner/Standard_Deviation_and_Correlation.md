03/2017  
Dataquest : Data Analyst Path  
Step 5: Probability and Statistics  
SubStep : Probability and Statistics in Python: Beginner : Standard Deviation and Correlation  
mercredi, 15. mars 2017 10:16 


---
# 1: Introduction  

In this mission, we'll be calculating statistics using data from the National Basketball Association (NBA). Here are the first few rows of the CSV file we'll explore:  


	player,pos,age,bref_team_id,g,gs,mp,fg,fga,fg.,x3p,x3pa,x3p.,x2p,x2pa,x2p.,efg.,ft,fta,ft.,orb,drb,trb,ast,stl,blk,tov,pf,pts,season,season_end
	Quincy Acy,SF,23,TOT,63,0,847,66,141,0.468,4,15,0.266666666666667,62,126,0.492063492063492,0.482,35,53,0.66,72,144,216,28,23,26,30,122,171,2013-2014,2013
	Steven Adams,C,20,OKC,81,20,1197,93,185,0.503,0,0,NA,93,185,0.502702702702703,0.503,79,136,0.581,142,190,332,43,40,57,71,203,265,2013-2014,2013

Each row holds data on a single player for a single season. It contains the player's team, the total number of points the player scored, and other information.  

Here are some of the interesting columns:  

- player - The player's name
- pts - The total number of points the player scored
- ast - The player's total number of assists
- fg. - The player's field goal percentage for the season

On the next few screens, we'll explore this data set by calculating a few summary statistics.   



---
# 2: The Mean As The Center  

While we've looked at the mean briefly before, it has an interesting property we'd like to point out here.  

If we subtract the mean of a set of numbers from each of the numbers within that set, the overall total of all of the differences will always add up to zero.  

That's because the mean is the "center" of the data. All of the differences that are negative will always cancel out all of the differences that are positive. Let's look at some examples to verify this.  

Let's also become familiar with the mathematical symbol for the mean:  

	x¯

This symbol means "the average of all of the values in x." The fact that x is lowercase and in bold indicates that it's a vector. The bar over the top indicates "the average of".  


#### Instructions :

 - Find the median of the values list. Assign the result to values_median.
 - Subtract the median from each element in values. Sum up all of the differences, and assign the result to median_difference_sum.
 
```python
# Make a list of values
values = [2, 4, 5, -1, 0, 10, 8, 9]
# Compute the mean of the values
values_mean = sum(values) / len(values)
# Find the difference between each of the values and the mean by subtracting the mean from each value.
differences = [i - values_mean for i in values]
# This equals 0.  If you'd like, try changing the values around to verify that it still equals 0.
print(sum(differences))

# We can use the median function from numpy to find the median.
# The median is the "middle" value in a set of values. If we sort the values in order, it's the one in the center (or the average of the two in the center if there are an even number of items in the set).
# You'll see that the differences from the median don't always add up to 0.  You might want to play around with this and think about why that is.
from numpy import median
values_median = median(values)
median_difference_sum = sum([i - values_median for i in values])
print(median_difference_sum)
```  

#### Results :  

	Output
	0.0
	1.0

---
# 3: Finding Variance  

Let's look at variance in the data. Variance tells us how concentrated or "spread out" the data is around the mean.  

We looked at kurtosis earlier, which measures the shape of a distribution. Variance directly measures how far the average data point is from the mean.  

We calculate variance by subtracting every value from the mean, squaring the results, and then averaging them. Mathemically, this looks like this:  

see img/img23.png

σ2=∑i=1n(xi−x¯)2nσ2=∑i=1n(xi−x¯)2n  

σ2σ2 is variance, and ∑ni=1∑i=1n means "the sum from 1 to n", where n is the number of elements in a vector.  

This formula goes through the exact same process we just described, and is the most common way to represent it.  

Let's complete an exercise to solidify what we've learned.  

The data set's "pf" column contains the total number of personal fouls each player committed during the season. Let's look at its variance.  


#### Instructions :

 - Compute the variance of the data set's "pts" column, which holds the total number of points each player scored.
 - Assign the result to point_variance.
 
```python
import matplotlib.pyplot as plt
import pandas as pd
# We've already loaded the NBA data into the nba_stats variable.
# Find the mean value of the column.
pf_mean = nba_stats["pf"].mean()
# Initialize variance at zero.
variance = 0
# Loop through each item in the "pf" column.
for p in nba_stats["pf"]:
    # Calculate the difference between the mean and the value.
    difference = p - pf_mean
    # Square the difference. This ensures that the result isn't negative.
    # If we didn't square the difference, the total variance would be zero.
    # ** in python means "raise whatever comes before this to the power of whatever number is after this."
    square_difference = difference ** 2
    # Add the difference to the total.
    variance += square_difference
# Average the total to find the final variance.
variance = variance / len(nba_stats["pf"])


pts_mean = nba_stats["pts"].mean()
variance = 0
for p in nba_stats["pts"]:

    difference = p - pts_mean
    square_difference = difference ** 2
    variance += square_difference

point_variance = variance / len(nba_stats["pts"])
print(point_variance)
```  

#### Results :  

	Output
	220836.995855

---
# 4: Understanding The Order Of Operations  

We've been multiplying and dividing values, but we haven't really discussed the order of operations yet.  

The order of operations defines the sequence in which mathematical operations occur. You may recall learning this in your primary school math classes.  

Think about the statement 2 * 5 - 1. The result will be different if we do the multiplication first, rather than the subtraction.  

If we multiply first, we get 10 - 1, which equals 9.  

If we subtract first, we get 2 * 4, which equals 8.  

We definitely want the results of these operations to be consistent; we don't want to get 8 one time and 9 the next. A default "order of operations" exists for this reason.  

Exponents occur first. That means if we raise something to a power (x ** y), that operation will execute before anything else. Multiplication (x * y) and division (x / y) occur next. They are equal to each other in priority. Addition (x + y) and subtraction (x - y) will occur last. They are also equal to each other in priority.  

So raising something to a power will always happen first, then any multiplication/division, and finally any addition/subtraction.  

Let's practice with these types of statements to get a better feel for the order of operations.    


#### Instructions :

 - Change the mathematical operations around so that c equals 25 and d equals .5.
 
```python
# You may be wondering why multiplication and division are on the same level.
# It doesn't matter whether we do the multiplication or division first; the answer here will always be the same.
# In this case, we need to think of division as multiplication by a fraction. Otherwise, we'll be dividing more than we want to.
# Create a formula
a = 5 * 5 / 2
# Multiply by 1/2 instead of dividing by 2. The result is the same (2/2 == 2 * 1/2).
a_subbed = 5 * 5 * 1/2
a_mul_first = 25 * 1/2
a_div_first = 5 * 2.5
print(a_mul_first == a_div_first)

# The same is true for subtraction and addition.
# In this case, we need to convert subtraction into adding a negative number. If we don't we'll end up subtracting more than we expect.
b = 10 - 8 + 5
# Add -8 instead of subtracting 8.
b_subbed = 10 + -8 + 5
b_sub_first = 2 + 5
b_add_first = 10 + -3
print(b_sub_first == b_add_first)

c = 10 * 2 + 5
d = (3 - 1) / (2 * 2)
```  

#### Results :  



---
# 5: Using Parentheses To Change The Order Of Operations  

We can use parentheses to override the order of operations and make something happen first.  

For example, 10 - 2 / 2 will equal 9, because the division occurs before the subtraction.  

If we write (10 - 2) / 2 instead, the parentheses "force" the operation inside to occur first, so we end up with 8/2.    


#### Instructions :

 - Use parentheses to make b equal 1100.
 - Use parentheses to make c equal 200.
 
```python
a = 50 * 50 - 10 / 5
a_paren = 50 * (50 - 10) / 5
# If we put multiple operations inside parentheses, the interpreter will use the order of operations to determine the sequence in which it should execute them.
a_paren = 50 * (50 - 10 / 5)

b = 10 * (10 + 100)
c = (8 - 6) * 100
```  

---
# 6: Fractional Powers  

Before we explore variance in greater depth, let's take a quick look at exponents.  

We wrote difference ** 2 on a previous screen. This code squared the difference between the mean and the value in the pf column. It calculates the equivalent of difference * difference.  

We could cube the difference by writing difference ** 3. This calculation is equal to difference * difference * difference.  

The same pattern holds true as we raise to higher powers like 4, 5, and so on.  

We can also take the roots of numbers using the same syntax.  

difference ** (1/2) will take the square root. We need to put the fraction in parentheses because raising a value to a power is the operation that would normally occur first.  

difference ** (1/3) will take the cube root. We can even continue with even smaller fractions.    


#### Instructions :

 - Raise 11 to the fifth power. Assign the result to e.
 - Take the fourth root of 10000. Assign the result to f.
 
```python
a = 5 ** 2
# Raise to the fourth power
b = 10 ** 4

# Take the square root ( 3 * 3 == 9, so the answer is 3)
c = 9 ** (1/2)

# Take the cube root (4 * 4 * 4 == 64, so 4 is the cube root)
d = 64 ** (1/3)

e = 11 ** 5
f = 10000 ** (1/4)
```  

---
# 7: Calculating Standard Deviation  

Standard deviation is the most common way to refer to the distance between data points and the mean. It's a very useful concept and a great way to measure the density of a data set.  

While it may sound complicated, standard deviation is fairly straightforward; it's the square root of the variance.  

Here's the mathematical formula for standard deviation:    

see img/img24.png

Statisticians and data scientists typically measure the percentage of data that falls within one or two standard deviations of the mean.  

#### Instructions :

 - Write a function that calculates the standard deviation of a given column in the nba_stats data.
 - Use the new function to calculate the standard deviation of the minutes played column ("mp"). Assign the results to mp_dev.
 - Use the function to calculate the standard deviation of the assists column ("ast"). Assign the results to ast_dev.
 
```python
# We've already loaded the NBA stats into the nba_stats variable.
import numpy as np

def calc_std_dev(data):
    n = len(data)
    mean = np.mean(data)
    sumdiffsquare = 0
    for d in data:
        sumdiffsquare += (d - mean) ** 2      
    std = (sumdiffsquare/n) ** (1/2)
    return std

mp_dev = calc_std_dev(nba_stats["mp"])
ast_dev = calc_std_dev(nba_stats["ast"])

print("-------")
print(mp_dev)
print("-------")
print(ast_dev)
print("-------")
```  

#### Results :  

	Output
	-------
	896.32565278
	-------
	130.883290708
	-------

---
# 8: Finding Standard Deviation Distance  

The standard deviation is very useful because it lets us compare the points in a distribution to the mean.  

We can say that a certain point is "two standard deviations away from the mean," for example. This gives us a way to compare data density across different charts.    


#### Instructions :

 - Find how many standard deviations away from the mean point_10 is. Assign the result to point_10_std.
 - Find how many standard deviations away from the mean point_100 is. Assign the result to point_100_std.
 
```python
import matplotlib.pyplot as plt

plt.hist(nba_stats["pf"])
mean = nba_stats["pf"].mean()
plt.axvline(mean, color="r")
# We can calculate standard deviation by using the std() method on a pandas series.
std_dev = nba_stats["pf"].std()
# Plot a line one standard deviation below the mean.
plt.axvline(mean - std_dev, color="g")
# Plot a line one standard deviation above the mean.
plt.axvline(mean + std_dev, color="g")

# We can see how many of the data points fall within one standard deviation of the mean.
# The more that fall into this range, the more dense the data is.
plt.show()

# We can calculate how many standard deviations a data point is from the mean by doing some subtraction and division.
# First, we find the total distance by subtracting the mean.
total_distance = nba_stats["pf"][0] - mean
# Then we divide by standard deviation to find how many standard deviations away the point is.
standard_deviation_distance = total_distance / std_dev

point_10 = nba_stats["pf"][9]
point_100 = nba_stats["pf"][99]

point_10_std = (point_10 - mean) / std_dev
point_100_std = (point_100 - mean) / std_dev

print(point_10_std)
print(point_100_std)
```  

#### Results :  

	Output
	0.212473057275
	0.49331818107

see img/img25.png

---
# 9: Working With The Normal Distribution  

The normal distribution is a special kind of distribution. You might recognize it more commonly as a bell curve.  

The normal distribution is found in a variety of natural phenomena. If we made a histogram of the heights of everyone on the planet, for example, it would be more or less a normal distribution.  

We can generate a normal distribution by using a probability density function.    


#### Instructions :

 - Make a normal distribution across the range that starts at -10, ends at 10, and has the step .1.
 - The distribution should have a mean of 0 and standard deviation of 2.
 
```python
import numpy as np
import matplotlib.pyplot as plt
# The norm module has a pdf function (pdf stands for probability density function)
from scipy.stats import norm

# The arange function generates a numpy vector
# The vector below will start at -1, and go up to, but not including 1
# It will proceed in "steps" of .01.  So the first element will be -1, the second -.99, the third -.98, all the way up to .99.
points = np.arange(-1, 1, 0.01)

# The norm.pdf function will take the points vector and convert it into a probability vector
# Each element in the vector will correspond to the normal distribution (earlier elements and later element smaller, peak in the center)
# The distribution will be centered on 0, and will have a standard devation of .3
probabilities = norm.pdf(points, 0, .3)

# Plot the points values on the x-axis and the corresponding probabilities on the y-axis
# See the bell curve?
plt.plot(points, probabilities)
plt.show()


points = np.arange(-10, 10, 0.1)
probabilities = norm.pdf(points, 0, 2)
plt.plot(points, probabilities)
plt.show()
```  

#### Results :  

see img/img26.png
see img/img27.png

---
# 10: Normal Distribution Deviation  

One cool thing about normal distributions is that for every single one, the same percentage of the data is within one standard deviation of the mean, the same percentage is within two standard deviations of the mean, and so on.  

About 68% of the data is within one standard deviation, roughly 95% is within two standard deviations, and about 99% is within three standard deviations.  

This helps us quickly understand where values fall within the data set, as well as how typical or unusual they are.    


#### Instructions :

 - For each point in wing_lengths, calculate the distance from the mean in number of standard deviations.
 - Calculate the percentage of the data that's within one standard deviation of the mean. Assign the result to within_one_percentage.
 - Calculate the percentage of the data that's within two standard deviations of the mean. Assign the result to within_two_percentage.
 - Calculate the percentage of the data that's within three standard deviations of the mean. Assign the result to within_three_percentage.
 
```python
# Housefly wing lengths in millimeters
wing_lengths = [36, 37, 38, 38, 39, 39, 40, 40, 40, 40, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 42, 42, 43, 43, 43, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 48, 48, 48, 48, 48, 48, 48, 48, 49, 49, 49, 49, 49, 49, 49, 50, 50, 50, 50, 50, 50, 51, 51, 51, 51, 52, 52, 53, 53, 54, 55]
import numpy as np
wing_mean = np.mean(wing_lengths)
wing_std = np.std(wing_lengths)
wings_len = len(wing_lengths)
print("--------------")
print("Moyenne :",wing_mean)
print("Std :",wing_std)
print("--------------")

def nb_std(p):
    distance = p - wing_mean
    std_distance = distance / wing_std
    return std_distance

wing_lengths_distance = []
for point in wing_lengths:
    wing_lengths_distance.append(nb_std(point))
    
within_one_percentage = (len([ p for p in wing_lengths_distance if abs(p) <= 1]) / wings_len)
within_two_percentage = (len([ p for p in wing_lengths_distance if abs(p) <= 2]) / wings_len)
within_three_percentage = (len([ p for p in wing_lengths_distance if abs(p) <= 3]) / wings_len) 

print("within_one_percentage :",within_one_percentage)
print("within_two_percentage :",within_two_percentage)
print("within_three_percentage :",within_three_percentage)
```  

#### Results :  

	Output
	--------------
	Moyenne : 45.5
	Std : 3.9
	--------------
	within_one_percentage : 0.68
	within_two_percentage : 0.96
	within_three_percentage : 1.0

---
# 11: Using Scatterplots To Plot Correlations  

We've spent a lot of time looking at single variables and how their distributions look. While distributions are interesting on their own, it can also be revealing to look at how two variables correlate with each other.  

Much of statistics deals with analyzing how variables impact each other, and the first step is to graph them out with a scatterplot.  

While graphing them out, we can look at correlation. If two variables change together (ie, when one goes up, the other goes up), we know that they are correlated.    


#### Instructions :

 - Make a scatterplot of the "fta" (free throws attempted) column against the "pts" column.
 - Make a scatterplot of the "stl" (steals) column against the "pf" column.
 
```python
import matplotlib.pyplot as plt

# Plot field goals attempted (number of shots someone takes in a season) vs. point scored in a season.
# Field goals attempted is on the x-axis, and points is on the y-axis.
# As you can tell, they are very strongly correlated. The plot is close to a straight line.
# The plot also slopes upward, which means that as field goal attempts go up, so do points.
# That means that the plot is positively correlated.
plt.scatter(nba_stats["fga"], nba_stats["pts"])
plt.show()

# If we make points negative (so the people who scored the most points now score the least, because 3000 becomes -3000), we can change the direction of the correlation.
# Field goals are negatively correlated with our new "negative" points column -- the more free throws you attempt, the less negative points you score.
# We can see this because the correlation line slopes downward.
plt.scatter(nba_stats["fga"], -nba_stats["pts"])
plt.show()

# Now, we can plot total rebounds (number of times someone got the ball back for their team after someone shot) vs total assists (number of times someone helped another person score).
# These are uncorrelated, so you don't see the same nice line as you see with the plot above.
plt.scatter(nba_stats["trb"], nba_stats["ast"])
plt.show()


plt.scatter(nba_stats["fta"], nba_stats["pts"])
plt.show()

plt.scatter(nba_stats["stl"], nba_stats["pf"])
plt.show()
```  

#### Results :  

	see img/img28.png
	see img/img29.png
	see img/img30.png
	see img/img31.png
	see img/img32.png


---
# 12: Measuring Correlation With Pearson's R  

Measuring correlation can be a big help when we need to analyze a lot of variables. This spares us from having to eyeball everything.  

The most common way to measure correlation is to use Pearson's r, which we also call an r-value.  

We'll explore how the calculations work later. For now, though, we'll focus on the values.  

An r-value ranges from -1 to 1, and indicates how strongly two variables are correlated.  

A 1 indicates a perfect positive correlation. This would appear as a straight, upward-sloping line on our plots.  

A 0 indicates no correlation. We'd see a scatterplot with points that appear random.  

A -1 indicates a perfect negative correlation. This would appear as a straight, downward-sloping line.  

Any correlation between -1 and 0 will show up as a scattering of points. The same is true of correlations falling between 0 and 1. The closer the value is to 0, the more random the points will appear. The closer it is to -1 or 1, the more "line-like" the points will appear.  

We can use a function from scipy to calculate Pearson's r.   


#### Instructions :

 - Find the correlation between the "fta" column and the "pts" column. Assign the result to r_fta_pts.
 - Find the correlation between the "stl" column and the "pf" column. Assign the result to r_stl_pf.
 
```python
from scipy.stats.stats import pearsonr

# The pearsonr function will find the correlation between two columns of data.
# It returns the r value and the p value.  We'll learn more about p values later on.
r, p_value = pearsonr(nba_stats["fga"], nba_stats["pts"])
# As we can see, this is a very high positive r value - it's close to 1.
print(r)

# These two columns are much less correlated.
r, p_value = pearsonr(nba_stats["trb"], nba_stats["ast"])
# We get a much lower, but still positive, r value.
print(r)

r_fta_pts, p_value = pearsonr(nba_stats["fta"], nba_stats["pts"])
print(r_fta_pts)

r_stl_pf, p_value = pearsonr(nba_stats["stl"], nba_stats["pf"])
print(r_stl_pf)
```  

#### Results :  

	Output
	0.989211400652
	0.369861731248
	0.918978538402
	0.737628216749

---
# 13: Calculate Covariance  

We looked at finding the correlation coefficient with a function. Now, let's take a brief look under the hood to see how we can do it ourselves.  

Another way to think of correlation is in terms of variance.  

Two variables are correlated when they both vary individually, but in similar ways. For example, correlation occurs when if one variable goes up, another variable also goes up.  

This is called covariance. Covariance refers to how different numbers vary jointly.  

There's a limit to how much two variables can co-vary. This is because each variable has its own variance. These individual variances set a maximum theoretical limit on the covariance between two variables. In other words, a set of variables can't co-vary more from the mean than the two variables individually vary from the mean.  

Two variables reach the maximum possible covariance when they vary in an identical way (ie, you see a straight line on the plot).  

The r-value is a ratio between the actual covariance and the maximum possible positive covariance.  

Let's look at actual covariance first. Mathematically speaking, covariance between two variables looks like this:  

	see img/img32.png
cov(x,y)=∑ni=1(xi−x¯)(yi−y¯)ncov(x,y)=∑i=1n(xi−x¯)(yi−y¯)n

For each element in the vectors x and y, we:  

 1. Take the value at each position from 1 to the length of the vectors.
 2. Subtract the mean of the vector from those values.
 3. Multiply them together at each position, and all of the resulting values together.  


#### Instructions :

 - Make a function that calculates covariance.
 - Use the function to calculate the covariance of the "stl" and "pf" columns. Assign the result to cov_stl_pf.
 - Use the function to calculate the covariance of the "fta" and "pts" columns. Assign the result to cov_fta_pts.
 
```python
# We've already loaded the nba_stats variable.
import numpy as np
def covariance(x,y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    x_len = len(x)
    sumofxy = 0
    
    for i in range(0,x_len):
        sumofxy += (x[i]-x_mean)*(y[i]-y_mean)
    
    cov = sumofxy / x_len
    return cov

cov_stl_pf = covariance(nba_stats["stl"],nba_stats["pf"])
cov_fta_pts = covariance(nba_stats["fta"],nba_stats["pts"])

#dataquest solution :

# We've already loaded the nba_stats variable.
def covariance(x, y):
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)

cov_stl_pf = covariance(nba_stats["stl"], nba_stats["pf"])
cov_fta_pts = covariance(nba_stats["fta"], nba_stats["pts"])

```  

#### Results :  

	Variables
	 cov_stl_pffloat64 (<class 'numpy.float64'>)
	1823.3548480513116
	 cov_fta_ptsfloat64 (<class 'numpy.float64'>)
	56618.413980748621


---
# 14: Calculate Correlation With The Std() Method  

Now that we know how to calculate covariance, we can get the correlation coefficient using the following formula:  

	see img/img34.png
cov(x,y)σxσycov(x,y)σxσy

For the denominator, we need to multiple the standard deviations for x and y. This is the maximum possible positive covariance, which is just both of the standard deviation values multiplied. If we divide our actual covariance by this, we get the r-value.  

We can use the std method on any pandas DataFrame or Series to calculate the standard deviation. The following code returns the standard deviation for the pf column:  

```python
nba_stats["pf"].std()
``` 

We can use the cov function from NumPy to compute covariance, returning a 2x2 matrix. The following code returns the covariance between the pf and stl columns:  

```python 
cov(nba_stats["pf"], nba_stats["stl"])[0,1]  
``` 


#### Instructions :

 - Compute the correlation coefficient for the fta and blk columns, and assign the result to r_fta_blk.
 - Compute the correlation coefficient for the ast and stl columns, and assign the result to r_ast_stl.
 
```python
from numpy import cov
# We've already loaded the nba_stats variable for you.
r_fta_blk = cov(nba_stats["fta"], nba_stats["blk"])[0,1] / (nba_stats["fta"].std() * nba_stats["blk"].std())
r_ast_stl = cov(nba_stats["ast"], nba_stats["stl"])[0,1] / (nba_stats["ast"].std() * nba_stats["stl"].std())
```  

#### Results :  

	Variables
	 r_fta_blkfloat64 (<class 'numpy.float64'>)
	0.45606282214395671
	 r_ast_stlfloat64 (<class 'numpy.float64'>)
	0.77042797946826391