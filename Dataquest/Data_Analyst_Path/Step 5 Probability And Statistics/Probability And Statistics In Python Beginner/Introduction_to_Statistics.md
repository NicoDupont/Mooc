03/2017  
Dataquest : Data Analyst Path  
Step 5: Probability and Statistics  
SubStep : Probability and Statistics in Python: Beginner / Introduction to Statistics  
lundi, 13. mars 2017 10:18 

---
# 1: Introduction To Scales  

At its core, statistics is about counting and measuring.  

In order to do both effectively, we have to define scales on which to base our counts. A scale represents the possible values that a variable can have.  


#### Instructions :

 - Compute the mean of car_speeds, and assign the result to mean_car_speed.
 - Compute the mean of earthquake_intensities, and assign the result to mean_earthquake_intensities. Note that this value will not be meaningful, because we shouldn't average values on a logarithmic scale this way.
 
```python
car_speeds = [10,20,30,50,20]
earthquake_intensities = [2,7,4,5,8]
import numpy as np
mean_car_speed = np.mean(car_speeds)
mean_earthquake_intensities = np.mean(earthquake_intensities)
print(mean_car_speed)
print("-----------")
print(mean_earthquake_intensities)
print("-----------")
```  

#### Results :  

	Output
	26.0
	-----------
	5.2
	-----------

---
# 2: Discrete And Continuous Scales 
 
Scales can be either discrete or continuous.  

Think of someone marking down the number of inches a snail crawls every day. The snail could crawl 1 inch, 2 inches, 1.5 inches, 1.51 inches, or any other number, and it would be a valid observation. This is because inches are on a continuous scale, and even fractions of an inch are possible.  

Now think of someone counting the number of cars in a parking lot each day. 1 car, 2 cars, and 10 cars are valid measurements, but 1.5 cars isn't valid.  

Half of a car isn't a meaningful quantity, because cars are discrete. You can't have 52% of a car - you either have a car, or you don't.  

You can still average items on discrete scales, though. You could say "1.75 cars use this parking lot each day, on average." Any daily value for number of cars, however, would need to be a whole number.   


#### Instructions :

 - Make a line plot with day_numbers on the x axis and snail_crawl_length on the y axis.
 - Make a line plot with day_numbers on the x axis and cars_in_parking_lot on the y axis.
 
```python
day_numbers = [1,2,3,4,5,6,7]
snail_crawl_length = [.5,2,5,10,1,.25,4]
cars_in_parking_lot = [5,6,4,2,1,7,8]

import matplotlib.pyplot as plt
plt.plot(day_numbers,snail_crawl_length)
plt.show()
plt.plot(day_numbers,cars_in_parking_lot)
plt.show()
```  

#### Results :  

see img/img1.png
see img/img2.png


---
# 3: Understanding Scale Starting Points  

Some scales use the zero value in different ways. Think of the number of cars in a parking lot.  

Zero cars in the lot means that there are absolutely no cars at all, so absolute zero is at 0 cars. You can't have negative cars.  

Now, think of degrees Fahrenheit.  

Zero degrees doesn't mean that there isn't any warmth; the degree scale can also be negative, and absolute zero (when there is no warmth at all) is at -459.67 degrees.  

Scales with absolute zero points that aren't at 0 don't enable us to take meaningful ratios. For example, if four cars parked in the lot yesterday and eight park today, I can safely say that twice as many cars are in the lot today.  

However, if it was 32 degrees Fahrenheit yesterday, and it's 64 degrees today, I can't say that it's twice as warm today as yesterday.    


#### Instructions :

 - Convert the values in fahrenheit_degrees so that absolute zero is at the value 0. If you think this is already the case, don't change anything. Assign the result to degrees_zero.
 - Convert the values in yearly_town_population so that absolute zero is at the value 0. If you think this is already the case, don't change anything. Assign the result to population_zero.
 
```python
fahrenheit_degrees = [32, 64, 78, 102]
yearly_town_population = [100,102,103,110,105,120]
degrees_zero = [f + 459.67 for f in fahrenheit_degrees]
population_zero = yearly_town_population
```  

#### Results :  

	Variables
	 population_zerolist (<class 'list'>)
	[100, 102, 103, 110, 105, 120]
	 degrees_zerolist (<class 'list'>)
	[491.67, 523.6700000000001, 537.6700000000001, 561.6700000000001]



---
# 4: Working With Ordinal Scales  

So far, we've looked at equal interval and discrete scales, where all of the values are numbers. We can also have ordinal scales, where items are ordered by rank.  

For example, we could ask people how many cigarettes they smoke per day, and the answers could be "none," "a few," "some," or "a lot." These answers don't map exactly to numbers of cigarettes, but we know that "a few" is more than "none."  

This is an ordinal rating scale. We can assign numbers to the answers in a logical order to make them easier to work with.  

For example, we could map 0 to "none," 1 to "a few," 2 to "some," and so on.    


#### Instructions :

 - In the following code block, assign a number to each survey response that corresponds with its position on the scale ("none" is 0, and so on).
 - Compute the average value of all the survey responses, and assign it to average_smoking.
 
```python
# Results from our survey on how many cigarettes people smoke per day
survey_responses = ["none", "some", "a lot", "none", "a few", "none", "none"]
survey_resp_map = ["none","some","a lot","a few"]
import numpy as np
smoking = [survey_resp_map.index(resp) for resp in survey_responses]
average_smoking = np.mean(smoking)
print(average_smoking)
```  

#### Results :  

	Output
	0.857142857143

---
# 5: Grouping Values With Categorical Scales  

We can also have categorical scales, which group values into general categories.  

One example is gender, which can be male or female.  

Unlike ordinal scales, categorical scales don't have an order. In our gender example, for instance, one category isn't greater than or less than the other.  

Categories are common in data science. You'll typically use them to split data into groups.    

#### Instructions :

 - Compute the average savings for everyone who is "male". Assign the result to male_savings.
 - Compute the average savings for everyone who is "female". Assign the result to female_savings.
 
```python
# Let's say that these lists are both columns in a matrix.  Index 0 is the first row in both, and so on.
gender = ["male", "female", "female", "male", "male", "female"]
savings = [1200, 5000, 3400, 2400, 2800, 4100]
import numpy as np
male_savings_lists = [ savings[i] for i in range(0,len(gender)) if gender[i] == "male" ]
female_savings_lists = [ savings[i] for i in range(0,len(gender)) if gender[i] == "female" ]
male_savings = np.mean(male_savings_lists)
female_savings = np.mean(female_savings_lists)
```  

#### Results :  

	Output
	2133.33333333
	4166.66666667

---
# 6: Visualizing Counts With Frequency Histograms  

Remember how statistics is all about counting? A frequency histogram is a type of plot that helps us visualize counts of data.  

These plots tally how many times each value occurs in a list, then graph the values on the x-axis and the counts on the y-axis.  

Frequency histograms give us a better understanding of where values fall within a data set.  


#### Instructions :

 - Plot a histogram of student_scores.
 
```python
# Let's say that we watch cars drive by and calculate average speed in miles per hour
average_speed = [10, 20, 25, 27, 28, 22, 15, 18, 17]
import matplotlib.pyplot as plt
plt.hist(average_speed)
plt.show()

# Let's say we measure student test scores from 0-100
student_scores = [15, 80, 95, 100, 45, 75, 65]
plt.hist(student_scores)
plt.show()
```  

#### Results :  

see img/img3.png
see img/img4.png


---
# 7: Aggregating Values With Histogram Bins  

You may have noticed that the code on the last screen plotted all of the values.  

In contrast, histograms use bins to count values. Bins aggregate values into predefined "buckets."  

Here's how they work. If the x-axis ranges from 0 to 10 and we have 10 bins, the first bin would be for values between 0-1, the second would be for values between 1-2, and so on.  

If we have five bins, the first bin would be for values between 0-2, the second would be for values between 2-4, and so on.  

Each value in the list that falls within the bin would increase the bin's count by one. The result looks like a bar chart. Bins give us a better understanding of the shape and distribution of the data than graphing each count individually.  

Now that you know about bins, we'd like to point something out about what you saw on the previous screen. matplotlib's default number of bins for a plot is 10. We had fewer values than that, so matplotlib displayed all of the values.  

Let's experiment a bit with using different numbers of bins to gain a better understanding of how they work.   


#### Instructions :

 - Plot a histogram of average_speed with only 2 bins.
 
```python
average_speed = [10, 20, 25, 27, 28, 22, 15, 18, 17]
import matplotlib.pyplot as plt
plt.hist(average_speed, bins=6)
plt.show()

# As you can see, matplotlib groups the values in the list into the nearest bins.
# If we have fewer bins, each bin will have a higher count (because there will be fewer bins to group all of the values into).
# If there are more bins, the total for each one will decrease, because each one will contain fewer values.
plt.hist(average_speed, bins=4)
plt.show()

plt.hist(average_speed, bins=2)
plt.show()
```  

#### Results :  

see img/img5.png
see img/img6.png
see img/img7.png



---
# 8: Measuring Data Skew  

Now that you know how to make histograms, did you notice how the plots have "shapes?"  

These shapes are important because they can show us the distributional characteristics of the data. The first characteristic we'll look at is skew.  

Skew refers to asymmetry in the data. When data is concentrated on the right side of the histogram, for example, we say it has a negative skew. When the data is concentrated on the left, we say it has a positive skew.  

We can measure the level of skew with the skew function. A positive value indicates a positive skew, a negative value indicates a negative skew, and a value close to zero indicates no skew.  


#### Instructions :

- Assign the skew of test_scores_positive to positive_skew.
- Assign the skew of test_scores_negative to negative_skew.
- Assign the skew of test_scores_normal to no_skew.

 
```python
# We've already loaded in some numpy arrays. We'll make some plots with them.
# The arrays contain student test scores that are on a 0-100 scale.
import matplotlib.pyplot as plt

# See how there's a long slope to the left?
# The data is concentrated in the right part of the distribution, but some people also scored poorly.
# This plot has a negative skew.
plt.hist(test_scores_negative)
plt.show()

# This plot has a long slope to the right.
# Most students did poorly, but a few did really well.
# This plot has a positive skew.
plt.hist(test_scores_positive)
plt.show()

# This plot has no skew either way. Most of the values are in the center, and there is no long slope either way.
# It is an unskewed distribution.
plt.hist(test_scores_normal)
plt.show()

# We can test how skewed a distribution is using the skew function.
# A positive value means positive skew, a negative value means negative skew, and close to zero means no skew.
from scipy.stats import skew
positive_skew = skew(test_scores_positive)
negative_skew = skew(test_scores_negative)
no_skew = skew(test_scores_normal)
print(positive_skew)
print(negative_skew)
print(no_skew)
```  

#### Results :  

	Output
	0.5376950498203763
	-0.6093247474592195
	0.0223645171350847

see img/img8.png
see img/img9.png
see img/img10.png

---
# 9: Checking For Outliers With Kurtosis  

Kurtosis is another characteristic of distributions. Kurtosis measures whether the distribution is short and flat, or tall and skinny. In other words, it assesses the shape of the peak.  

"Shorter" distributions have a lower maximum frequency, but higher subsequent frequencies. A high kurtosis may indicate problems with outliers (very large or very small values that skew the data).  


#### Instructions :

- Assign the kurtosis of test_scores_platy to kurt_platy.
- Assign the kurtosis of test_scores_lepto to kurt_lepto.
- Assign the kurtosis of test_scores_meso to kurt_meso.
 
```python
import matplotlib.pyplot as plt

# This plot is short. It is platykurtic.
# Notice how the values are distributed fairly evenly, and there isn't a large cluster in the middle.
# Student performance varied widely.
plt.hist(test_scores_platy)
plt.show()

# This plot is tall. It is leptokurtic.
# Most students performed similarly.
plt.hist(test_scores_lepto)
plt.show()

# The height of this plot neither short nor tall. It is mesokurtic.
plt.hist(test_scores_meso)
plt.show()

# We can measure kurtosis with the kurtosis function.
# Negative values indicate platykurtic distributions, positive values indicate leptokurtic distributions, and values near 0 are mesokurtic.
from scipy.stats import kurtosis

kurt_platy = kurtosis(test_scores_platy)
kurt_lepto = kurtosis(test_scores_lepto)
kurt_meso = kurtosis(test_scores_meso)
print(kurt_platy)
print(kurt_lepto)
print(kurt_meso)
```  

#### Results :  

Output
-0.9283967256161696
0.023335026722224317
-0.042791859857727044

see img/img11.png
see img/img12.png
see img/img13.png

---
# 10: Modality  

Modality is another characteristic of distributions. Modality refers to the number of modes, or peaks, in a distribution.  

Real-world data is often unimodal (it has only one mode).  


#### Instructions :

 - Plot test_scores_multi, which has four peaks.
 
```python
import matplotlib.pyplot as plt

# This plot has one mode. It is unimodal.
plt.hist(test_scores_uni)
plt.show()

# This plot has two peaks. It is bimodal.
# This could happen if one group of students learned the material and another learned something else, for example.
plt.hist(test_scores_bi)
plt.show()

# More than one peak means that the plot is multimodal.
# We can't easily measure the modality of a plot, like we can with kurtosis or skew.
# Often, the best way to detect multimodality is to examine the plot visually.
plt.hist(test_scores_multi)
plt.show()
```  

#### Results :  

see img/img14.png
see img/img15.png
see img/img16.png



---
# 11: Measures Of Central Tendency  

Now that we know how to measure the characteristics of a distribution, let's look at central tendency measures.  

Central tendency measures assess how likely the data points are to cluster around a central value.  

The first one we'll look at is the mean. We've calculated mean before, but let's explore it further.  

The mean is just the sum of all of the elements in an array divided by the number of elements.   


#### Instructions :

- Compute the mean of test_scores_normal, and assign it to mean_normal.
- Compute the mean of test_scores_negative, and assign it to mean_negative.
- Compute the mean of test_scores_positive, and assign it to mean_positive.
 
```python
import matplotlib.pyplot as plt
# Let's put a line over our plot that shows the mean.
# This is the same histogram we plotted for skew a few screens ago.
plt.hist(test_scores_normal)
# We can use the .mean() method of a numpy array to compute the mean.
mean_test_score = test_scores_normal.mean()
# The axvline function will plot a vertical line over an existing plot.
plt.axvline(mean_test_score)

# Now we can show the plot and clear the figure.
plt.show()

# When we plot test_scores_negative, which is a very negatively skewed distribution, we see that the small values on the left pull the mean in that direction.
# Very large and very small values can easily skew the mean.
# Very skewed distributions can make the mean misleading.
plt.hist(test_scores_negative)
plt.axvline(test_scores_negative.mean())
plt.show()

# We can do the same with the positive side.
# Notice how the very high values pull the mean to the right more than we would expect.
plt.hist(test_scores_positive)
plt.axvline(test_scores_positive.mean())
plt.show()

import numpy as np
mean_normal = np.mean(test_scores_normal)
mean_negative = np.mean(test_scores_negative)
mean_positive = np.mean(test_scores_positive)
print(mean_normal)
print(mean_negative)
print(mean_positive)
```  

#### Results :  

	Output
	49.232135212
	83.6276064223
	16.607018116

see img/img17.png
see img/img18.png
see img/img19.png


---
# 12: Calcultaing The Median  

Median is another measure of central tendency. This is the midpoint of an array.  

To calculate the median, we need to sort the array, then take the value in the middle. If there are two values in the middle (because there are an even number of items in the array), then we take the mean of the two middle values.  

The median is less sensitive to very large or very small values (which we call outliers), and is a more realistic center of the distribution.    


#### Instructions :

 - Plot a histogram for test_scores_positive.
 - Add a blue line for the median.
 - Add a red line for the mean.
 
```python
# Let's plot the mean and median side-by-side in a negatively skewed distribution.
# Unfortunately, arrays don't have a nice median method, so we have to use a numpy function to compute it.
import numpy
import matplotlib.pyplot as plt

# Plot the histogram
plt.hist(test_scores_negative)
# Compute the median
median = numpy.median(test_scores_negative)

# Plot the median in blue (the color argument of "b" means blue)
plt.axvline(median, color="b")

# Plot the mean in red
plt.axvline(test_scores_negative.mean(), color="r")

# Notice how the median is further to the right than the mean.
# It's less sensitive to outliers, and isn't pulled to the left.
plt.show()


plt.hist(test_scores_positive)
median = numpy.median(test_scores_positive)
mean = numpy.mean(test_scores_positive)
plt.axvline(median, color="b")
plt.axvline(mean, color="r")
plt.show()
```  

#### Results :  

see img/img20.png
see img/img21.png

---
# 13: Overview Of The Titanic Data  

On the next few screens, we'll work on cleaning up and analyzing data on passenger survival from the Titanic. Each row represents a passenger on the Titanic, complete with personal details and information on their survival.  

Here are some of the relevant columns:  

- name - The passenger's name
- sex - The passenger's gender
- age - the passenger's age

Several of the columns have missing values, such as the age and sex columns. Before we can analyze the data, we'll need to deal with these values first.   


---
# 14: Removing Missing Data  

Now that we've learned a bit about statistics, let's practice on our Titanic data.  

The data is a manifest of all the passengers on the Titanic, a ship that sunk in April 1912. It contains passenger names, ages, and other information (such as whether or not they survived).  

Unfortunately, not all of the data is available; details such as age are missing for some passengers. Before we can analyze the data, we have to do something about the missing rows.  

The easiest way to address them is to just remove all of the rows with missing data. This isn't necessarily the best solution in all cases, but we'll learn about other ways to handle these situations later on.   


#### Instructions :

 - Remove the NaN values in the "age" and "sex" columns.
 - Assign the result to new_titanic_survival.
 
```python
import pandas
f = "titanic_survival.csv"
titanic_survival = pandas.read_csv(f)

# Luckily, pandas DataFrames have a method that can drop rows that have missing data
# Let's look at how large the DataFrame is first
print(titanic_survival.shape)

# There were 1,310 passengers on the Titanic, according to our data
# Now let's drop any rows that have missing data
# The DataFrame dropna method will do this for us
# It will remove any rows with that contain missing values
new_titanic_survival = titanic_survival.dropna()

# Hmm, it looks like we were too zealous with dropping rows that contained NA values
# We now have no rows in our DataFrame
# This is because some of the later columns, which aren't immediately relevant to our analysis, contain a lot of missing values
print(new_titanic_survival.shape)

# We can use the subset keyword argument to the dropna method so that it only drops rows if there are NA values in certain columns
# This line of code will drop any row where the embarkation port (where people boarded the Titanic) or cabin number is missing
new_titanic_survival = titanic_survival.dropna(subset=["embarked", "cabin"])

# This result is much better. We've only removed the rows we needed to.
print(new_titanic_survival.shape)

f = "titanic_survival.csv"
titanic_survival = pandas.read_csv(f)
new_titanic_survival = titanic_survival.dropna(subset=["age","sex"])
```  

#### Results :  

	Output
	(1310, 14)
	(0, 14)
	(293, 14)


---
# 15: Plotting Age  

Now that we've cleaned up the data, let's analyze it.  


#### Instructions :

 - Plot a histogram of the "age" column in new_titanic_survival.
	- Add a blue line for the median.
	- Add a red line for the mean.
 
```python
# We've loaded the clean version of the data into the variable new_titanic_survival
import matplotlib.pyplot as plt
import numpy as np

median = np.median(new_titanic_survival["age"])
mean = np.mean(new_titanic_survival["age"])

plt.hist(new_titanic_survival["age"])
plt.axvline(median, color="b")
plt.axvline(mean, color="r")
plt.show()
```  

#### Results :  

see img/img22.png

---
# 16: Calculating Indexes For Age  

The age distribution is very interesting. It shows that many people in their 20s-40s were travelling without children.  

Now that we know what the distribution looks like, let's calculate its characteristics and central tendency measures.   


#### Instructions :

- Assign the mean of the "age" column of new_titanic_survival to mean_age.
- Assign the median of the "age" column of new_titanic_survival to median_age.
- Assign the skew of the "age" column of new_titanic_survival to skew_age.
- Assign the kurtosis of the "age" column of new_titanic_survival to kurtosis_age.

 
```python
import numpy as np
age = new_titanic_survival["age"]
mean_age = np.mean(age)
median_age = np.median(age)
from scipy.stats import skew
skew_age = skew(age)
from scipy.stats import kurtosis
kurtosis_age = kurtosis(age)

print("--------------------")
print(mean_age)
print("--------------------")
print(median_age)
print("--------------------")
print(skew_age)
print("--------------------")
print(kurtosis_age)
```  

#### Results :  

	Output
	--------------------
	29.8811345124
	--------------------
	28.0
	--------------------
	0.4070870379484177
	--------------------
	0.14051780299368888
